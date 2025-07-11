#!/usr/bin/env python3
"""
Comprehensive test script to verify the double slash fix works correctly
for all possible edge cases and path formats.
"""

import sys
sys.path.append('.')

def test_comprehensive_double_slash_fix():
    """Test that the double slash fix works for all edge cases."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_cases = [
            ("/docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/vars/var-operations/", "docs/vars/var_operations.md"),
            ("/docs/api-reference/cli/", "docs/api_reference/cli.md"),
            ("/docs/library/forms/button/", "docs/library/forms/button.md"),
            
            ("docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("docs/vars/var-operations/", "docs/vars/var_operations.md"),
            
            ("/docs/getting-started/introduction", "docs/getting_started/introduction.md"),
            ("docs/getting-started/introduction", "docs/getting_started/introduction.md"),
            
            ("//docs/getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs//getting-started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/getting-started//introduction/", "docs/getting_started/introduction.md"),
            ("docs//getting-started/introduction/", "docs/getting_started/introduction.md"),
            
            ("///docs/getting-started/introduction///", "docs/getting_started/introduction.md"),
            ("docs///getting-started///introduction", "docs/getting_started/introduction.md"),
            
            ("/docs/getting-started/introduction.md", "docs/getting_started/introduction.md"),
            ("docs/getting-started/introduction.md", "docs/getting_started/introduction.md"),
        ]
        
        print("Testing comprehensive double slash fix:")
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
            print("🎉 SUCCESS: All tests passed! Double slash fix is working correctly.")
        else:
            print("❌ FAILURE: Some tests failed. Double slash issue not fully resolved.")
            
        return all_passed
            
    except Exception as e:
        print(f"❌ Error in comprehensive test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_comprehensive_double_slash_fix()
    exit(0 if success else 1)
