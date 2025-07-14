"""
URL-to-filepath mapping utilities for documentation pages.

This module provides dynamic mapping between browser URLs and filesystem paths
for the "Edit this page" GitHub links functionality. It's separated from the
main docpage module to avoid circular import issues.
"""

_URL_TO_FILEPATH_MAP = None

def _get_url_to_filepath_mapping():
    """Get the URL-to-filepath mapping, building it lazily on first access.
    
    Uses lazy loading to avoid circular imports during module initialization.
    """
    global _URL_TO_FILEPATH_MAP
    
    if _URL_TO_FILEPATH_MAP is not None:
        return _URL_TO_FILEPATH_MAP
    
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
    
    _URL_TO_FILEPATH_MAP = url_to_filepath
    return _URL_TO_FILEPATH_MAP

def convert_url_path_to_github_path(url_path) -> str:
    """Convert a URL path to the corresponding GitHub filesystem path.
    
    Uses dynamic mapping built from the actual docs folder structure,
    eliminating hardcoded path conversions while preserving exact file paths.
    
    Args:
        url_path: URL path like "/docs/getting-started/introduction/" (can be str or rx.Var[str])

    Returns:
        GitHub filesystem path like "docs/getting_started/introduction.md"
    """
    if hasattr(url_path, '_js_expr'):  # This is a Reflex Var
        from reflex.vars.sequence import string_replace_operation

        path_no_slashes = string_replace_operation(url_path, r"^/+|/+$", "")
        path_clean = string_replace_operation(path_no_slashes, r"/+", "/")
        path_without_docs = string_replace_operation(path_clean, "^docs/", "")
        
        path_converted = string_replace_operation(path_without_docs, "-", "_")
        
        final_path = path_converted
        if not path_converted._js_expr.endswith(".md"):
            final_path = path_converted + ".md"
        
        return "docs/" + final_path
    else:
        path = str(url_path).strip("/")
        while "//" in path:
            path = path.replace("//", "/")
        
        if path.startswith("docs/"):
            path = path[5:]
        
        url_to_filepath_map = _get_url_to_filepath_mapping()
        if path in url_to_filepath_map:
            return url_to_filepath_map[path]
        
        if not path.endswith(".md"):
            path += ".md"
        return f"docs/{path}"
