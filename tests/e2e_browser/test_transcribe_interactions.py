"""Real-browser interaction smokes for the transcribe page.

Sister to `test_pages_render.py` (pure render/presence). These drive
actual clicks and assert reactive JS-side state - visibility toggles
and dialog open/close - that the in-process NiceGUI User fixture
can't observe (it inspects Python-side element state, not the DOM
Quasar produces).
"""

import pytest
from playwright.sync_api import Page, expect


def test_speaker_detection_toggle_reveals_speaker_count(atrain_server: str, page: Page) -> None:
    """Speaker-count column is bound to the `speaker_detection` flag
    (speaker_count.py::input_speaker_count → bind_visibility). Toggling
    the switch must show/hide the column in the actual DOM."""
    page.goto(atrain_server)
    speaker_count = page.get_by_text("Number of Speakers")
    expect(speaker_count).to_be_hidden()

    # Two "Speaker Detection" strings render (section header + switch label).
    # The switch label is the second occurrence; .last targets it.
    switch_label = page.get_by_text("Speaker Detection").last
    switch_label.click()
    expect(speaker_count).to_be_visible()

    switch_label.click()
    expect(speaker_count).to_be_hidden()


def test_advanced_settings_button_opens_dialog(atrain_server: str, page: Page) -> None:
    """The Advanced Settings dialog is embedded closed on the transcribe
    page and re-created on button click. `GPU acceleration` lives only
    inside the dialog, so its visibility is a clean proxy for open-state."""
    page.goto(atrain_server)
    gpu_label = page.get_by_text("GPU acceleration").last
    expect(gpu_label).to_be_hidden()

    page.get_by_role("button", name="Advanced Settings").click()
    expect(gpu_label).to_be_visible()


def test_selecting_a_model_fills_the_language_list(atrain_server: str, page: Page) -> None:
    """Choosing a model is a round trip: the server stores it and fills the
    language options from the model's config (language.py). In the frozen
    macOS app neither happened (#307). Needs a model on disk; the macOS
    job places an empty `large-v3-turbo/model.bin`, enough for the list."""
    page.goto(atrain_server)
    # Model is the first select on the page, language the second.
    model_select, language_select = (
        page.locator(".q-select").nth(0),
        page.locator(".q-select").nth(1),
    )
    expect(model_select).to_be_visible(timeout=120_000)  # splash imports torch first

    if "No models yet" in model_select.inner_text():
        pytest.skip("no model on disk")

    model_select.click()
    option = page.locator(".q-menu .q-item").first
    expect(option).to_be_visible()
    name = option.inner_text().strip()
    option.click()
    expect(model_select).to_contain_text(name)

    language_select.click()
    expect(page.locator(".q-menu .q-item").first).to_be_visible()
