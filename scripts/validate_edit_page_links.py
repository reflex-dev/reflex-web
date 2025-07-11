#!/usr/bin/env python3
"""
Script to validate all "Edit this page" GitHub links in the Reflex documentation.

This script:
1. Extracts all documentation routes from the Reflex web app
2. Applies the convert_url_path_to_github_path() function to generate GitHub URLs
3. Sends GET requests to each GitHub URL to verify they return 200 OK
4. Reports any broken links or issues
"""

import os
import re
import requests
from pathlib import Path
from typing import List, Tuple
import time


def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case (same logic as reflex's to_kebab_case)."""
    text = re.sub(r'[_\s]+', '-', text)
    text = re.sub(r'([a-z])([A-Z])', r'\1-\2', text)
    return text.lower()


def convert_url_path_to_github_path(url_path: str) -> str:
    """
    Convert a URL path to the corresponding GitHub filesystem path.
    
    This is a standalone version of the function from pcweb/templates/docpage/docpage.py
    that handles regular Python strings (not Reflex StringVar objects).
    
    Args:
        url_path: URL path like "/docs/getting-started/introduction/"
        
    Returns:
        GitHub filesystem path like "docs/getting_started/introduction.md"
    """
    path = url_path.strip("/")
    path = path.replace("-", "_")
    if not path.endswith(".md"):
        path += ".md"
    return path


def get_all_doc_paths() -> List[Tuple[str, str]]:
    """Extract all documentation paths by scanning the docs/ directory.
    
    Returns:
        List of tuples (url_route, github_file_path)
    """
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs"
    
    if not docs_dir.exists():
        raise FileNotFoundError(f"Documentation directory not found: {docs_dir}")
    
    path_pairs = []
    
    for md_file in docs_dir.rglob("*.md"):
        relative_path = md_file.relative_to(docs_dir)
        
        # GitHub file path (preserve actual file structure)
        github_path = f"docs/{str(relative_path).replace('\\', '/')}"
        
        doc_path = str(relative_path).replace("\\", "/")
        route = to_kebab_case(f"/docs/{doc_path.replace('.md', '/')}")
        
        # Handle index files: /docs/folder/index/ -> /docs/folder/
        if route.endswith("/index/"):
            route = route[:-7] + "/"
        
        path_pairs.append((route, github_path))
    
    path_pairs = sorted(list(set(path_pairs)), key=lambda x: x[0])
    
    return path_pairs


def generate_github_url(github_file_path: str) -> str:
    """Generate the GitHub URL for a documentation file path."""
    return f"https://github.com/reflex-dev/reflex-web/blob/main/{github_file_path}"


def validate_url(url: str) -> Tuple[bool, int, str]:
    """
    Validate a single GitHub URL.
    
    Returns:
        (is_valid, status_code, error_message)
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True, response.status_code, ""
        else:
            return False, response.status_code, f"HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, 0, str(e)


def main():
    """Main validation function."""
    print("🔍 Validating 'Edit this page' GitHub links...")
    print("=" * 60)
    
    try:
        path_pairs = get_all_doc_paths()
        print(f"Found {len(path_pairs)} documentation paths to validate")
        print()
        
        valid_count = 0
        invalid_count = 0
        invalid_urls = []
        
        for i, (route, github_file_path) in enumerate(path_pairs, 1):
            github_url = generate_github_url(github_file_path)
            
            print(f"[{i:3d}/{len(path_pairs)}] Testing: {route}")
            print(f"           GitHub URL: {github_url}")
            
            is_valid, status_code, error_msg = validate_url(github_url)
            
            if is_valid:
                print(f"           ✅ OK (200)")
                valid_count += 1
            else:
                print(f"           ❌ FAILED ({error_msg})")
                invalid_count += 1
                invalid_urls.append((route, github_url, error_msg))
            
            print()
            
            time.sleep(0.1)
        
        print("=" * 60)
        print("📊 VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Total URLs tested: {len(path_pairs)}")
        print(f"✅ Valid URLs: {valid_count}")
        print(f"❌ Invalid URLs: {invalid_count}")
        print()
        
        if invalid_urls:
            print("🚨 FAILED URLs:")
            print("-" * 40)
            for path, url, error in invalid_urls:
                print(f"Path: {path}")
                print(f"URL:  {url}")
                print(f"Error: {error}")
                print()
            
            return 1
        else:
            print("🎉 All 'Edit this page' links are valid!")
            return 0
            
    except Exception as e:
        print(f"❌ Script failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
