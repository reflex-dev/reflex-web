#!/usr/bin/env python3
"""
Test script to verify the hyphenated folder handling in convert_url_path_to_github_path function.
Tests the special cases for api-reference, api-routes, custom-components, and wrapping-react folders.
"""

import sys
sys.path.append('.')

def test_hyphenated_folders():
    """Test that hyphenated folder handling works correctly."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_cases = [
            # api-reference: folder keeps hyphens, files use underscores
            ("/docs/api-reference/browser-javascript/", "docs/api-reference/browser_javascript.md"),
            ("/docs/api-reference/event-triggers/", "docs/api-reference/event_triggers.md"),
            ("/docs/api-reference/var-system/", "docs/api-reference/var_system.md"),
            ("/docs/api-reference/cli/", "docs/api-reference/cli.md"),
            
            # api-routes: both folder and files keep hyphens
            ("/docs/api-routes/overview/", "docs/api-routes/overview.md"),
            
            # custom-components: both folder and files keep hyphens
            ("/docs/custom-components/overview/", "docs/custom-components/overview.md"),
            ("/docs/custom-components/command-reference/", "docs/custom-components/command-reference.md"),
            ("/docs/custom-components/prerequisites-for-publishing/", "docs/custom-components/prerequisites-for-publishing.md"),
            
            # wrapping-react: both folder and files keep hyphens
            ("/docs/wrapping-react/overview/", "docs/wrapping-react/overview.md"),
            ("/docs/wrapping-react/custom-code-and-hooks/", "docs/wrapping-react/custom-code-and-hooks.md"),
            ("/docs/wrapping-react/local-packages/", "docs/wrapping-react/local-packages.md"),
            ("/docs/wrapping-react/step-by-step/", "docs/wrapping-react/step-by-step.md"),
            
            # Standard folders: should convert dashes to underscores
            ("/docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/vars/var-operations/", "docs/vars/var_operations.md"),
            ("/docs/library/forms/button/", "docs/library/forms/button.md"),
            
            # Edge cases with double slashes
            ("//docs/api-reference/browser-javascript/", "docs/api-reference/browser_javascript.md"),
            ("/docs//custom-components/overview/", "docs/custom-components/overview.md"),
            ("/docs/getting-started//introduction/", "docs/getting_started/introduction.md"),
        ]
        
        print("Testing hyphenated folder handling:")
        print("=" * 80)
        
        all_passed = True
        
        for i, (input_path, expected_output) in enumerate(test_cases, 1):
            print(f"\nTest {i:2d}: '{input_path}'")
            
            actual_output = convert_url_path_to_github_path(input_path)
            print(f"Expected: '{expected_output}'")
            print(f"Actual:   '{actual_output}'")
            
            full_url = f"https://github.com/reflex-dev/reflex-web/blob/main/{actual_output}"
            print(f"Full URL: '{full_url}'")
            
            has_double_slash = "//" in full_url.replace("https://", "")
            matches_expected = actual_output == expected_output
            
            if matches_expected and not has_double_slash:
                print("✅ PASS")
            else:
                print("❌ FAIL")
                if not matches_expected:
                    print(f"   Expected '{expected_output}' but got '{actual_output}'")
                if has_double_slash:
                    print(f"   URL contains double slash: '{full_url}'")
                all_passed = False
            
            print("-" * 60)
        
        print("\n" + "=" * 80)
        if all_passed:
            print("🎉 SUCCESS: All hyphenated folder tests passed!")
        else:
            print("❌ FAILURE: Some hyphenated folder tests failed.")
            
        return all_passed
            
    except Exception as e:
        print(f"❌ Error in hyphenated folder test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_hyphenated_folders()
    exit(0 if success else 1)
