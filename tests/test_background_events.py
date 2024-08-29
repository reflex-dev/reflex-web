import os
import re

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness
import time


@pytest.fixture
def background_events_url() -> str:
    from pcweb.pages import docs

    return docs.events.background_events.path


@pytest.mark.skipif(os.environ.get("GITHUB_ACTIONS") is not None, reason="Consistently fails in CI")
def test_background_events(
    reflex_web_app: AppHarness,
    page: Page,
    background_events_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + background_events_url)
    expect(page).to_have_url(re.compile(background_events_url))

    start_button = page.get_by_role("button", name="Start", exact=True)
    reset_button = page.get_by_role("button", name="Reset")
    expect(start_button).to_be_visible()

    demo_block = page.locator('[id="background_demo"]').nth(1)
    heading = demo_block.get_by_role("heading")
    expect(heading).to_have_text("0 /")

    start_button.click()
    expect(heading).to_have_text("4 /")
    reset_button.click()
    expect(heading).to_have_text("0 /")
    expect(heading).to_have_text("10 /")
