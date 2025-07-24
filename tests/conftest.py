from pathlib import Path

import pytest

from reflex.testing import AppHarness


@pytest.fixture(scope="session")
def reflex_web_app():
    app_root = Path(__file__).parent.parent
    from pcweb.whitelist import WHITELISTED_PAGES

    WHITELISTED_PAGES.extend(
        [
            "/docs/events",
            "/docs/vars",
            "/docs/getting-started",
            "/docs/library/graphing",
            "/docs/api-reference/special-events",
        ]
    )

    with AppHarness.create(root=app_root) as harness:
        yield harness
