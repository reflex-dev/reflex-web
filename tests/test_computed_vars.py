import re

import pytest
from playwright.sync_api import Page, expect
from reflex.testing import AppHarness
from utils import get_full_url


@pytest.fixture
def computed_vars_url() -> str:
    from pcweb.pages import docs

    return docs.vars.computed_vars.path


def test_computed_vars(
    reflex_web_app: AppHarness,
    page: Page,
    computed_vars_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(get_full_url(reflex_web_app, computed_vars_url))
    expect(page).to_have_url(re.compile(computed_vars_url))

    upper_box = page.locator('[id="upper"]')

    input = upper_box.get_by_role("textbox")
    input.fill("upper")
    input.blur()
    expect(upper_box.get_by_role("heading")).to_have_text("UPPER")
