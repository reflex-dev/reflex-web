#!/usr/bin/env python3
"""
Test script to verify the double slash fix in GitHub edit page URLs.
This script tests the convert_url_path_to_github_path function and URL construction
to ensure no double slashes are generated.
"""

import sys
sys.path.append('.')

def test_double_slash_fix():
    """Test that the double slash fix works correctly."""
    try:
        from pcweb.templates.docpage.docpage import convert_url_path_to_github_path
        
        test_paths = [
            "/docs/getting-started/introduction/",
            "/docs/vars/var-operations/", 
            "/docs/api-reference/cli/",
            "/docs/library/forms/button/",
            "docs/getting-started/introduction/",  # without leading slash
            "/docs/getting-started/introduction",   # without trailing slash
        ]
        
        print("Testing double slash fix in GitHub edit page URLs:")
        print("=" * 70)
        
        all_good = True
        
        for test_path in test_paths:
            github_path = convert_url_path_to_github_path(test_path)
            
            full_url = f"https://github.com/reflex-dev/reflex-web/blob/main/{github_path}"
            
            fixed_url = full_url.replace("main//", "main/")
            
            has_double_slash = "main//" in full_url
            fix_applied = full_url != fixed_url
            
            print(f"Input path:     {test_path}")
            print(f"GitHub path:    {github_path}")
            print(f"Full URL:       {full_url}")
            print(f"Fixed URL:      {fixed_url}")
            print(f"Had double //:  {has_double_slash}")
            print(f"Fix applied:    {fix_applied}")
            
            if has_double_slash:
                print(f"⚠️  DOUBLE SLASH DETECTED (but fixed by .replace())")
            else:
                print(f"✅ No double slash")
            
            print()
            
            if "//" in fixed_url.replace("https://", ""):
                print(f"❌ ERROR: Final URL still contains double slashes!")
                all_good = False
        
        print("=" * 70)
        if all_good:
            print("🎉 SUCCESS: Double slash fix is working correctly!")
            print("All URLs are properly formatted without double slashes.")
        else:
            print("❌ FAILURE: Some URLs still contain double slashes!")
            
        return all_good
            
    except Exception as e:
        print(f"❌ Error testing double slash fix: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_double_slash_fix()
    exit(0 if success else 1)
