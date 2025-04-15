"""Integration tests for all titles in Reflex."""

from pathlib import Path
from collections import Counter
import sys
import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def routes_fixture():
    from pcweb.pages import routes

    yield routes


def test_unique_titles(routes_fixture):
    assert routes_fixture is not None

    titles = []
    for route in routes_fixture:
        if hasattr(route, "title"):
            titles.append(route)

    # Count occurrences of each title
    title_counts = Counter(titles)
    # Find duplicate titles
    duplicates = [title for title, count in title_counts.items() if count > 1]

    # Assert that there are no duplicates
    assert len(duplicates) == 0, f"Duplicate titles found: {duplicates}"

    print(f"Test passed. All {len(titles)} titles are unique.")
