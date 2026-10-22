"""Keep the Windows signing job from publishing unvalidated macOS artifacts."""

from fnmatch import filter as filter_names
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


def artifact_action(job, action):
    return next(
        step["with"] for step in job["steps"] if step.get("uses", "").startswith(action + "@")
    )


def artifact_name(template, context, suffix):
    return template.replace("${{ " + context + ".version }}", "1.5.0").replace(
        "${{ " + context + ".suffix }}", suffix
    )


@pytest.mark.parametrize("suffix", ["", "-bundled"])
def test_windows_signing_downloads_only_the_msix_build(suffix):
    workflow = REPO_ROOT / ".github" / "workflows" / "release.yml"
    jobs = yaml.safe_load(workflow.read_text(encoding="utf-8"))["jobs"]
    windows_upload = artifact_action(jobs["build-windows-msix"], "actions/upload-artifact")
    signing = jobs["sign-windows-msix"]
    download = artifact_action(signing, "actions/download-artifact")
    signed_upload = artifact_action(signing, "actions/upload-artifact")

    windows_name = artifact_name(windows_upload["name"], "steps.version.outputs", suffix)
    # Model both build variants, macOS outputs, and a previous signing attempt
    # being present when the signing job is re-run.
    available = [
        windows_name,
        artifact_name(
            windows_upload["name"],
            "steps.version.outputs",
            "-bundled" if not suffix else "",
        ),
        artifact_name(signed_upload["name"], "needs.build-windows-msix.outputs", suffix),
    ]
    available += [
        artifact_name(step["with"]["name"], "steps.version.outputs", "")
        for step in jobs["build-macos-dmg"]["steps"]
        if step.get("uses", "").startswith("actions/upload-artifact@")
    ]
    if "name" in download:
        name = artifact_name(download["name"], "needs.build-windows-msix.outputs", suffix)
        selected = [candidate for candidate in available if candidate == name]
    else:
        pattern = artifact_name(download["pattern"], "needs.build-windows-msix.outputs", suffix)
        selected = filter_names(available, pattern)

    assert selected == [windows_name]
