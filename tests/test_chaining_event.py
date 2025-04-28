import re

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness
import time


@pytest.fixture
def chaining_event_url() -> str:
    from pcweb.pages import docs

    return docs.events.chaining_events.path


def test_handler_from_handler(
    reflex_web_app: AppHarness,
    page: Page,
    chaining_event_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + chaining_event_url)
    expect(page).to_have_url(re.compile(chaining_event_url))

    chain_heading = page.locator('[id="call-handler"] > .rt-Flex > span')
    expect(chain_heading).to_have_text("0")

    run_button = page.get_by_role("button", name="Run")
    run_button.scroll_into_view_if_needed()
    expect(run_button).to_be_visible()
    
    run_button.click(force=True)
    
    expect(chain_heading).to_have_text("10")


def test_collatz(reflex_web_app: AppHarness, page: Page, chaining_event_url):
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + chaining_event_url)
    expect(page).to_have_url(re.compile(chaining_event_url))

    collatz_box = page.locator('[id="collatz"]')

    collatz_input = collatz_box.get_by_role("textbox")
    collatz_input.fill("10")
    
    collatz_input.blur(force=True)
    
    collatz_heading = page.locator('[id="collatz"] > .rt-Flex > span')
    
    expect(collatz_heading).to_have_text("1")
