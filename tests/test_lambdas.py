import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from reflex.testing import AppHarness


@pytest.fixture
def event_argument_url() -> str:
    from pcweb.pages import docs

    return docs.events.event_arguments.path


def test_lambdas(
    reflex_web_app: AppHarness,
    page: Page,
    event_argument_url: str,
) -> None:
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + event_argument_url)

    inputs = page.get_by_role("textbox")
    inputs.nth(0).fill("rgba(4,168,152)")
    inputs.nth(0).blur()

    expect(page.locator(".rt-TextFieldRoot").nth(0)).to_have_css(
        "background-color",
        "rgb(4, 168, 152)",
    )
    inputs.nth(1).fill("DarkBlue")
    inputs.nth(1).blur()
    expect(page.locator(".rt-TextFieldRoot").nth(1)).to_have_css(
        "background-color",
        "rgb(0, 0, 139)",
    )
    inputs.nth(2).fill("#AEADE3")
    inputs.nth(2).blur()
    expect(page.locator(".rt-TextFieldRoot").nth(2)).to_have_css(
        "background-color",
        "rgb(174, 173, 227)",
    )
