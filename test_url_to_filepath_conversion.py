#!/usr/bin/env python3
"""
Test script to verify URL-to-filepath conversion works correctly.
Tests that browser URLs (kebab-case) are converted to actual file paths (snake_case).
"""

import sys
sys.path.append('.')

def test_url_to_filepath_conversion():
    """Test that browser URLs are correctly converted to filesystem paths."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_cases = [
            ("/docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/vars/var-operations/", "docs/vars/var_operations.md"),
            ("/docs/api-reference/cli/", "docs/api_reference/cli.md"),
            ("/docs/library/forms/button/", "docs/library/forms/button.md"),
            ("/docs/hosting/deploy-quick-start/", "docs/hosting/deploy_quick_start.md"),
            ("/docs/hosting/config-file/", "docs/hosting/config_file.md"),
            ("/docs/custom-components/overview/", "docs/custom_components/overview.md"),
            ("/docs/wrapping-react/overview/", "docs/wrapping_react/overview.md"),
            
            ("docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/getting-started/introduction", "docs/getting_started/introduction.md"),
            ("docs/getting-started/introduction", "docs/getting_started/introduction.md"),
            
            ("//docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs//getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/getting-started//introduction/", "docs/getting_started/introduction.md"),
        ]
        
        print("Testing URL-to-filepath conversion:")
        print("=" * 80)
        
        all_passed = True
        
        for i, (input_url, expected_path) in enumerate(test_cases, 1):
            print(f"\nTest {i:2d}: '{input_url}'")
            
            actual_path = convert_url_path_to_github_path(input_url)
            print(f"Expected: '{expected_path}'")
            print(f"Actual:   '{actual_path}'")
            
            full_url = f"https://github.com/reflex-dev/reflex-web/blob/main/{actual_path}"
            print(f"Full URL: '{full_url}'")
            
            has_double_slash = "//" in full_url.replace("https://", "")
            matches_expected = actual_path == expected_path
            
            if matches_expected and not has_double_slash:
                print("✅ PASS")
            else:
                print("❌ FAIL")
                if not matches_expected:
                    print(f"   Expected '{expected_path}' but got '{actual_path}'")
                if has_double_slash:
                    print(f"   URL contains double slash: '{full_url}'")
                all_passed = False
            
            print("-" * 60)
        
        print("\n" + "=" * 80)
        if all_passed:
            print("🎉 SUCCESS: All URL-to-filepath conversion tests passed!")
        else:
            print("❌ FAILURE: Some tests failed. URL-to-filepath conversion needs fixing.")
            
        return all_passed
            
    except Exception as e:
        print(f"❌ Error in URL-to-filepath conversion test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_url_to_filepath_conversion()
    exit(0 if success else 1)
