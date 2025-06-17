#!/usr/bin/env python3
import sys
sys.path.append('.')

def test_constants_import():
    try:
        from pcweb.constants import (
            MAX_FILE_SIZE_MB, MAX_IMAGES_COUNT, PROMPT_MAP, 
            CONTRIBUTION_URL, BUGS_URL, SPLINE_SCENE_URL, 
            REFLEX_DOMAIN_URL, TWITTER_CREATOR
        )
        print('✓ All new constants imported successfully')
        print(f'MAX_FILE_SIZE_MB: {MAX_FILE_SIZE_MB}')
        print(f'PROMPT_MAP keys: {list(PROMPT_MAP.keys())}')
        print(f'SPLINE_SCENE_URL: {SPLINE_SCENE_URL}')
        return True
    except ImportError as e:
        print(f'✗ Import error: {e}')
        return False

def test_updated_imports():
    try:
        from pcweb.pages.landing.views.hero import SubmitPromptState
        from pcweb.pages.framework.views.open_source import open_source
        from pcweb.styles.styles import SANS, DOC_BORDER_RADIUS
        from pcweb.styles.fonts import font_family
        from pcweb.pages.pricing.table import STYLES
        from pcweb.components.spline import Spline
        from pcweb.meta.meta import meta_tags
        print('✓ All updated imports work correctly')
        print(f'font_family: {font_family}')
        print(f'DOC_BORDER_RADIUS: {DOC_BORDER_RADIUS}')
        print(f'STYLES keys: {list(STYLES.keys())}')
        return True
    except ImportError as e:
        print(f'✗ Import error in updated files: {e}')
        return False

if __name__ == "__main__":
    success = test_constants_import() and test_updated_imports()
    sys.exit(0 if success else 1)
