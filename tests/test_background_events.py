import re

import pytest
from playwright.sync_api import Page, expect
from reflex.testing import AppHarness
from utils import get_full_url


@pytest.fixture
def background_events_url() -> str:
    from pcweb.pages import docs

    return docs.events.background_events.path


def test_background_events(
    reflex_web_app: AppHarness,
    page: Page,
    background_events_url: str,
):
    assert reflex_web_app.frontend_url is not None
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    page.goto(get_full_url(reflex_web_app, background_events_url))
    expect(page).to_have_url(re.compile(background_events_url))

    start_button = page.get_by_role("button", name="Start", exact=True)
    reset_button = page.get_by_role("button", name="Reset")
    expect(start_button).to_be_visible(timeout=60000)

    demo_block = page.locator('[id="background_demo"]').nth(1)
    heading = demo_block.get_by_role("heading")
    expect(heading).to_have_text("0 /")

    start_button.click()
    expect(heading).to_have_text(re.compile(r"[4-7] /"))

    reset_button.click()
    expect(heading).to_have_text("10 /", timeout=12000)
