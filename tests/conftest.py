from pathlib import Path

import pytest
from reflex.testing import AppHarness


@pytest.fixture(scope="session")
def reflex_web_app():
    app_root = Path(__file__).parent.parent
    with AppHarness.create(root=app_root) as harness:
        yield harness
