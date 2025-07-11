#!/usr/bin/env python3
"""
Test script to verify the simplified path preservation approach works correctly.
Tests that paths are preserved exactly as they exist in the docs folder.
"""

import sys
sys.path.append('.')

def test_simplified_path_preservation():
    """Test that the simplified path preservation works correctly."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_cases = [
            # Mixed naming in hosting folder (should preserve exactly)
            ("/docs/hosting/deploy-quick-start/", "docs/hosting/deploy-quick-start.md"),
            ("/docs/hosting/config_file/", "docs/hosting/config_file.md"),
            
            # Getting started (underscores - should preserve)
            ("/docs/getting_started/introduction/", "docs/getting_started/introduction.md"),
            ("/docs/getting_started/project-structure/", "docs/getting_started/project-structure.md"),
            
            # API reference (hyphens - should preserve)
            ("/docs/api-reference/cli/", "docs/api-reference/cli.md"),
            ("/docs/api-reference/browser-javascript/", "docs/api-reference/browser-javascript.md"),
            
            # Custom components (hyphens - should preserve)
            ("/docs/custom-components/overview/", "docs/custom-components/overview.md"),
            ("/docs/custom-components/command-reference/", "docs/custom-components/command-reference.md"),
            
            # Wrapping react (hyphens - should preserve)
            ("/docs/wrapping-react/overview/", "docs/wrapping-react/overview.md"),
            ("/docs/wrapping-react/custom-code-and-hooks/", "docs/wrapping-react/custom-code-and-hooks.md"),
            
            # Edge cases with double slashes (should clean)
            ("//docs/hosting/deploy-quick-start/", "docs/hosting/deploy-quick-start.md"),
            ("/docs//hosting/config_file/", "docs/hosting/config_file.md"),
            ("/docs/getting_started//introduction/", "docs/getting_started/introduction.md"),
        ]
        
        print("Testing simplified path preservation:")
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
            print("🎉 SUCCESS: All simplified path preservation tests passed!")
        else:
            print("❌ FAILURE: Some simplified path preservation tests failed.")
            
        return all_passed
            
    except Exception as e:
        print(f"❌ Error in simplified path preservation test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_simplified_path_preservation()
    exit(0 if success else 1)
