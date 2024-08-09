import pytest
from pathlib import Path
from reflex.testing import AppHarness


@pytest.fixture(scope="session")
def reflex_web_app():
    with AppHarness.create(root=Path(__file__).parent.parent) as harness:
        yield harness
