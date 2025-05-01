import re
import time

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness


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
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    page.goto(reflex_web_app.frontend_url + chaining_event_url)
    expect(page).to_have_url(re.compile(chaining_event_url))

    chain_heading = page.locator('[id="call-handler"] > .rt-Flex > span')
    expect(chain_heading).to_have_text("0")

    run_button = page.get_by_role("button", name="Run")
    run_button.scroll_into_view_if_needed()
    expect(run_button).to_be_visible()
    run_button.click()
    # commented this as runtime is not reliable in CI
    # expect(chain_heading).to_have_text("1")
    # expect(chain_heading).to_have_text("2")
    # expect(chain_heading).to_have_text("3")
    # expect(chain_heading).to_have_text("4")
    # expect(chain_heading).to_have_text("5")
    # expect(chain_heading).to_have_text("6")
    # expect(chain_heading).to_have_text("7")
    # expect(chain_heading).to_have_text("8")
    # expect(chain_heading).to_have_text("9")
    expect(chain_heading).to_have_text("10", timeout=10000)


def test_collatz(reflex_web_app: AppHarness, page: Page, chaining_event_url):
    assert reflex_web_app.frontend_url is not None
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    page.goto(reflex_web_app.frontend_url + chaining_event_url)
    expect(page).to_have_url(re.compile(chaining_event_url))

    collatz_box = page.locator('[id="collatz"]')

    collatz_input = collatz_box.get_by_role("textbox")
    collatz_input.fill("10", timeout=4000)
    collatz_input.blur()
    collatz_heading = page.locator('[id="collatz"] > .rt-Flex > span')
    # commented this as runtime is not reliable in CI
    # expect(collatz_heading).to_have_text("10")
    # expect(collatz_heading).to_have_text("5")
    # expect(collatz_heading).to_have_text("16")
    # expect(collatz_heading).to_have_text("8")
    # expect(collatz_heading).to_have_text("4")
    # expect(collatz_heading).to_have_text("2")
    expect(collatz_heading).to_have_text("1", timeout=10000)
    time.sleep(20)
