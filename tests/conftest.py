import sys
from pathlib import Path

import pytest

from reflex.testing import AppHarness

# Add tests directory to Python path for absolute imports
sys.path.insert(0, str(Path(__file__).parent))


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


@pytest.fixture
def browser_context_args():
    """Configure browser context with video recording."""
    return {
        "record_video_dir": "test-videos/",
        "record_video_size": {"width": 1280, "height": 720},
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Create metadata mapping for video files on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = None
        if hasattr(item, "funcargs"):
            if "page" in item.funcargs:
                page = item.funcargs["page"]
            else:
                # Look for page object in other fixtures
                for fixture_name, fixture_value in item.funcargs.items():
                    if hasattr(fixture_value, "page") and hasattr(
                        fixture_value.page, "video"
                    ):
                        page = fixture_value.page
                        print(f"Found page object in fixture: {fixture_name}")
                        break

        if page and hasattr(page, "video") and page.video:
            try:
                import time

                video_path = None
                for _ in range(3):
                    try:
                        video_path = page.video.path()
                        if video_path and Path(video_path).exists():
                            break
                    except Exception:
                        time.sleep(0.5)

                if not video_path:
                    print(f"Failed to get video path for test: {item.name}")
                    return

                test_name = item.name
                print(f"Video recorded for {test_name}: {video_path}")

                import fcntl
                import json
                import os

                split_index = os.environ.get("PYTEST_SPLIT_INDEX", "1")
                metadata_file = (
                    Path("test-videos") / f"video_metadata_{split_index}.json"
                )
                metadata_file.parent.mkdir(exist_ok=True)

                with metadata_file.open("a+") as f:
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                    f.seek(0)
                    try:
                        content = f.read()
                        metadata = json.loads(content) if content.strip() else {}
                    except (json.JSONDecodeError, ValueError):
                        metadata = {}

                    video_filename = Path(video_path).name
                    metadata[video_filename] = test_name

                    f.seek(0)
                    f.truncate()
                    json.dump(metadata, f, indent=2)

                print(f"Added metadata mapping: {video_filename} -> {test_name}")

            except Exception as e:
                print(f"Failed to create video metadata: {e}")
                import traceback

                traceback.print_exc()
        else:
            print(f"No video available for failed test: {item.name}")
            video_dir = Path("test-videos")
            if video_dir.exists():
                import time

                recent_videos = [
                    f
                    for f in video_dir.glob("*.webm")
                    if f.stat().st_mtime > (time.time() - 60)
                ]
                print(f"Recent video files found: {[f.name for f in recent_videos]}")
