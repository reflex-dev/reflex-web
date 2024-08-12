import re

from playwright.sync_api import Page, expect

import pytest
from reflex.testing import AppHarness


@pytest.fixture
def intro_page_url() -> str:
    from pcweb.pages import docs

    return docs.charts.introduction.path


def tests_recharts(
    reflex_web_app: AppHarness,
    page: Page,
    intro_page_url: str,
):
    assert reflex_web_app.frontend_url is not None
    page.goto(intro_page_url)

    page.get_by_placeholder("Enter a number")
