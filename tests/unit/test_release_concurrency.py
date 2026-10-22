"""The two-platform Zenodo draft transaction must not overlap another tag."""

from pathlib import Path

import yaml


def test_tag_releases_share_a_workflow_lock_without_cancelling_active_runs():
    root = Path(__file__).resolve().parents[2]
    workflow = yaml.safe_load((root / ".github/workflows/release.yml").read_text())
    concurrency = workflow.get("concurrency", {})
    # Every v* tag (including tag dispatches) gets the same literal group;
    # no version/ref/run id can split 1.5.0 and 1.5.1 into separate locks.
    # Ordinary branch tests use a unique run id and never hold the release lock.
    assert concurrency.get("group") == (
        "${{ startsWith(github.ref, 'refs/tags/v') && 'release-zenodo' "
        "|| format('release-test-{0}', github.run_id) }}"
    )
    assert concurrency.get("cancel-in-progress") is False
    # The lock covers both publications and all intervening builds/checks.
    assert "publish-to-zenodo" in workflow["jobs"]
    assert "publish-macos-to-zenodo" in workflow["jobs"]
