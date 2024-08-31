import re

import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from reflex.testing import AppHarness


@pytest.fixture
def scatterchart_page_url() -> str:
    from pcweb.pages import docs

    return docs.library.graphing.charts.scatterchart.path


def tests_recharts(
    reflex_web_app: AppHarness,
    page: Page,
    scatterchart_page_url: str,
) -> None:
    assert reflex_web_app.frontend_url is not None
    page.goto(reflex_web_app.frontend_url + scatterchart_page_url)
    expect(page).to_have_url(re.compile(scatterchart_page_url))

    input = page.get_by_placeholder("Enter a number")
    symbols = page.locator(".recharts-symbols")
    page.get_by_role("button", name="Compute")

    expect(input).to_be_visible()

    expect(symbols).to_have_count(45)
