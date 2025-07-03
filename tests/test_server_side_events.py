import re

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness

from utils import get_full_url


@pytest.fixture
def server_side_events_url() -> str:
    from pcweb.pages import docs

    return docs.api_reference.special_events.path


def _predicate_console_message(msg):
    return msg.text == "Hello World!"


def _predicate_download(download):
    return download.suggested_filename == "different_name_logo.png"


def test_server_side_events(
    reflex_web_app: AppHarness,
    page: Page,
    server_side_events_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(get_full_url(reflex_web_app, server_side_events_url))
    expect(page).to_have_url(re.compile(server_side_events_url))

    with page.expect_console_message(_predicate_console_message):
        page.get_by_role("button", name="Log", exact=True).click()

    page.get_by_role("button", name="Scroll").click()

    with page.expect_download(_predicate_download):
        page.get_by_role("button", name="Download", exact=True).click()
