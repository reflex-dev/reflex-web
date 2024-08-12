import re

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness
import time


@pytest.fixture
def server_side_events_url() -> str:
    from pcweb.pages import docs

    return docs.api_reference.special_events.path


def test_server_side_events(
    reflex_web_app: AppHarness,
    page: Page,
    server_side_events_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + server_side_events_url)
    expect(page).to_have_url(re.compile(server_side_events_url))

    with page.expect_console_message() as msg_info:
        page.get_by_role("button", name="Log", exact=True).click()
        assert msg_info.value.text == "Hello World!"

    page.get_by_role("button", name="Scroll").click()

    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download", exact=True).click()
        assert download_info.value.suggested_filename == "different_name_logo.png"
