#!/usr/bin/env python3
"""
Debug script to understand the complete URL construction flow and identify
where the double slash is coming from in the GitHub edit page URLs.
"""

import sys
sys.path.append('.')

def debug_url_construction():
    """Debug the complete URL construction flow."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_cases = [
            "/docs/getting-started/introduction/",
            "/docs/getting-started/introduction",
            "docs/getting-started/introduction/",
            "docs/getting-started/introduction",
            "/docs/vars/var-operations/",
            "/docs/api-reference/cli/",
            "//docs/getting-started/introduction/",  # Edge case: double leading slash
            "/docs//getting-started/introduction/",  # Edge case: double slash in middle
        ]
        
        print("Debugging URL construction flow:")
        print("=" * 80)
        
        for test_path in test_cases:
            print(f"\nTesting path: '{test_path}'")
            
            stripped_path = test_path.rstrip("/")
            print(f"After rstrip('/'): '{stripped_path}'")
            
            github_path = convert_url_path_to_github_path(stripped_path)
            print(f"GitHub path: '{github_path}'")
            
            full_url_before = f"https://github.com/reflex-dev/reflex-web/blob/main/{github_path}"
            print(f"Full URL before replace: '{full_url_before}'")
            
            full_url_after = full_url_before.replace("main//", "main/")
            print(f"Full URL after replace: '{full_url_after}'")
            
            has_double_slash_before = "main//" in full_url_before
            has_double_slash_after = "//" in full_url_after.replace("https://", "")
            fix_was_applied = full_url_before != full_url_after
            
            print(f"Had double slash before fix: {has_double_slash_before}")
            print(f"Fix was applied: {fix_was_applied}")
            print(f"Still has double slash after fix: {has_double_slash_after}")
            
            if has_double_slash_after:
                print("❌ ERROR: Double slash still present after fix!")
            elif has_double_slash_before and fix_was_applied:
                print("✅ SUCCESS: Double slash was fixed")
            elif not has_double_slash_before:
                print("✅ OK: No double slash to begin with")
            else:
                print("⚠️  WARNING: Unexpected state")
            
            print("-" * 60)
            
    except Exception as e:
        print(f"❌ Error in debug script: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_url_construction()
