#!/usr/bin/env python3
"""
Validation script to test all "Edit this page" URLs by gathering documentation routes
and testing GitHub links return 200 OK status.
"""

import requests
import sys
import os
from pathlib import Path

def get_all_doc_files():
    """Get all markdown files in docs folder."""
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("docs/ directory not found")
        return []
    
    doc_files = []
    for md_file in docs_dir.rglob("*.md"):
        rel_path = md_file.relative_to(docs_dir)
        doc_files.append(str(rel_path))
    
    return sorted(doc_files)

def convert_file_to_url(file_path):
    """Convert a file path to browser URL format."""
    url_path = file_path.replace(".md", "")
    
    url_parts = []
    for part in url_path.split("/"):
        kebab_part = part.replace("_", "-")
        url_parts.append(kebab_part)
    
    return "/docs/" + "/".join(url_parts) + "/"

def build_url_to_filepath_mapping():
    """Build dynamic mapping from browser URLs to filesystem paths.
    
    Uses the same logic as the main docpage.py function.
    """
    import flexdown
    import reflex as rx
    
    url_to_filepath = {}
    
    flexdown_docs = [
        str(doc).replace("\\", "/") for doc in flexdown.utils.get_flexdown_files("docs/")
    ]
    
    for doc_path in flexdown_docs:
        browser_url = rx.utils.format.to_kebab_case(f"/{doc_path.replace('.md', '/')}")
        
        if browser_url.endswith("/index/"):
            folder_url = browser_url[:-7] + "/"
            index_url = browser_url[:-1]  # Remove trailing slash but keep /index
            
            folder_key = folder_url.strip("/")
            index_key = index_url.strip("/")
            
            if folder_key.startswith("docs/"):
                folder_key = folder_key[5:]
            if index_key.startswith("docs/"):
                index_key = index_key[5:]
            
            url_to_filepath[folder_key] = doc_path
            url_to_filepath[index_key] = doc_path
        else:
            url_key = browser_url.strip("/")
            if url_key.startswith("docs/"):
                url_key = url_key[5:]
            
            url_to_filepath[url_key] = doc_path
    
    return url_to_filepath

def convert_url_to_github_path(url_path):
    """Convert URL path to GitHub file path using dynamic mapping."""
    url_to_filepath_map = build_url_to_filepath_mapping()
    
    path = str(url_path).strip("/")
    while "//" in path:
        path = path.replace("//", "/")
    
    if path.startswith("docs/"):
        path = path[5:]
    
    if path in url_to_filepath_map:
        return url_to_filepath_map[path]
    
    if not path.endswith(".md"):
        path += ".md"
    return f"docs/{path}"

def validate_edit_page_links():
    """Validate all edit page GitHub links return 200 OK."""
    doc_files = get_all_doc_files()
    print(f"Found {len(doc_files)} documentation files")
    
    success_count = 0
    failure_count = 0
    failures = []
    
    for doc_file in doc_files:
        browser_url = convert_file_to_url(doc_file)
        
        github_path = convert_url_to_github_path(browser_url)
        
        github_url = f"https://github.com/reflex-dev/reflex-web/blob/main/{github_path}"
        
        try:
            response = requests.get(github_url, timeout=10)
            if response.status_code == 200:
                success_count += 1
                print(f"✅ {browser_url:50} -> {github_path}")
            else:
                failure_count += 1
                failures.append((browser_url, github_path, github_url, response.status_code))
                print(f"❌ {browser_url:50} -> {github_path} (HTTP {response.status_code})")
        except Exception as e:
            failure_count += 1
            failures.append((browser_url, github_path, github_url, str(e)))
            print(f"❌ {browser_url:50} -> {github_path} (Error: {e})")
    
    print(f"\n{'='*80}")
    print(f"Validation Results:")
    print(f"✅ Success: {success_count}")
    print(f"❌ Failures: {failure_count}")
    print(f"📊 Total: {len(doc_files)}")
    
    if failures:
        print(f"\nFailure Details:")
        for browser_url, github_path, github_url, error in failures:
            print(f"  URL: {browser_url}")
            print(f"  Path: {github_path}")
            print(f"  GitHub: {github_url}")
            print(f"  Error: {error}")
            print()
    
    return failure_count == 0

if __name__ == "__main__":
    success = validate_edit_page_links()
    sys.exit(0 if success else 1)
