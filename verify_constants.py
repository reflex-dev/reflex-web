#!/usr/bin/env python3
import sys
sys.path.append('.')

def test_constants_import():
    try:
        from pcweb.constants import (
            MAX_FILE_SIZE_MB, MAX_IMAGES_COUNT, PROMPT_MAP, 
            CONTRIBUTION_URL, BUGS_URL, FONT_FAMILY, DOC_BORDER_RADIUS, 
            SPLINE_SCENE_URL, REFLEX_DOMAIN_URL, TWITTER_CREATOR, PRICING_TABLE_STYLES
        )
        print('✓ All new constants imported successfully')
        print(f'MAX_FILE_SIZE_MB: {MAX_FILE_SIZE_MB}')
        print(f'PROMPT_MAP keys: {list(PROMPT_MAP.keys())}')
        print(f'FONT_FAMILY: {FONT_FAMILY}')
        print(f'PRICING_TABLE_STYLES keys: {list(PRICING_TABLE_STYLES.keys())}')
        return True
    except ImportError as e:
        print(f'✗ Import error: {e}')
        return False

def test_updated_imports():
    try:
        from pcweb.pages.landing.views.hero import SubmitPromptState
        from pcweb.pages.framework.views.open_source import open_source
        from pcweb.styles.styles import SANS
        from pcweb.styles.fonts import font_family
        from pcweb.pages.pricing.table import STYLES
        from pcweb.components.spline import Spline
        from pcweb.meta.meta import meta_tags
        print('✓ All updated imports work correctly')
        return True
    except ImportError as e:
        print(f'✗ Import error in updated files: {e}')
        return False

if __name__ == "__main__":
    success = test_constants_import() and test_updated_imports()
    sys.exit(0 if success else 1)
