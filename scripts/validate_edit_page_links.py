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

def convert_url_to_github_path(url_path):
    """Convert URL path to GitHub file path using the same logic as the app."""
    path = str(url_path).strip("/")
    while "//" in path:
        path = path.replace("//", "/")
    
    path = path.replace("getting-started", "getting_started")
    path = path.replace("client-storage", "client_storage")
    path = path.replace("utility-methods", "utility_methods")
    path = path.replace("advanced-onboarding", "advanced_onboarding")
    path = path.replace("state-structure", "state_structure")
    path = path.replace("ai-builder", "ai_builder")
    
    path = path.replace("chatapp-tutorial", "chatapp_tutorial")
    path = path.replace("dashboard-tutorial", "dashboard_tutorial")
    
    path = path.replace("login-form", "login_form")
    path = path.replace("signup-form", "signup_form")
    path = path.replace("multi-column-row", "multi_column_row")
    path = path.replace("top-banner", "top_banner")
    path = path.replace("dark-mode-toggle", "dark_mode_toggle")
    path = path.replace("pricing-cards", "pricing_cards")
    path = path.replace("speed-dial", "speed_dial")
    
    path = path.replace("deploy-app", "deploy_app")
    path = path.replace("download-app", "download_app")
    path = path.replace("environment-variables", "environment_variables")
    path = path.replace("image-as-prompt", "image_as_prompt")
    path = path.replace("installing-external-packages", "installing_external_packages")
    path = path.replace("frequently-asked-questions", "frequently_asked_questions")
    path = path.replace("what-is-reflex-build", "what_is_reflex_build")
    path = path.replace("breaking-up-complex-prompts", "breaking_up_complex_prompts")
    path = path.replace("fixing-errors", "fixing_errors")
    
    path = path.replace("enterprise/ag-grid", "enterprise/ag_grid")
    path = path.replace("ag-chart", "ag_chart")
    
    path = path.replace("page-load-events", "page_load_events")
    path = path.replace("background-events", "background_events")
    path = path.replace("yield-events", "yield_events")
    path = path.replace("event-arguments", "event_arguments")
    path = path.replace("event-actions", "event_actions")
    path = path.replace("chaining-events", "chaining_events")
    path = path.replace("special-events", "special_events")
    path = path.replace("decentralized-event-handlers", "decentralized_event_handlers")
    path = path.replace("events-overview", "events_overview")
    path = path.replace("authentication-overview", "authentication_overview")
    path = path.replace("dynamic-routing", "dynamic_routing")
    path = path.replace("code-structure", "code_structure")
    path = path.replace("component-state", "component_state")
    
    path = path.replace("segmented-control", "segmented_control")
    path = path.replace("auto-scroll", "auto_scroll")
    path = path.replace("code-block", "code_block")
    path = path.replace("data-list", "data_list")
    path = path.replace("scroll-area", "scroll_area")
    path = path.replace("html-embed", "html_embed")
    path = path.replace("aspect-ratio", "aspect_ratio")
    path = path.replace("data-table", "data_table")
    path = path.replace("data-editor", "data_editor")
    path = path.replace("hover-card", "hover_card")
    path = path.replace("alert-dialog", "alert_dialog")
    path = path.replace("context-menu", "context_menu")
    path = path.replace("dropdown-menu", "dropdown_menu")
    path = path.replace("radio-group", "radio_group")
    path = path.replace("text-area", "text_area")
    
    path = path.replace("custom-vars", "custom_vars")
    path = path.replace("computed-vars", "computed_vars")
    path = path.replace("base-vars", "base_vars")
    
    path = path.replace("config-file", "config_file")
    
    path = path.replace("upload-and-download-files", "upload_and_download_files")
    path = path.replace("rendering-iterables", "rendering_iterables")
    path = path.replace("html-to-reflex", "html_to_reflex")
    path = path.replace("conditional-rendering", "conditional_rendering")
    path = path.replace("other-methods", "other_methods")
    path = path.replace("lifespan-tasks", "lifespan_tasks")
    path = path.replace("exception-handlers", "exception_handlers")
    path = path.replace("router-attributes", "router_attributes")
    path = path.replace("event-triggers", "event_triggers")
    path = path.replace("browser-storage", "browser_storage")
    path = path.replace("var-system", "var_system")
    path = path.replace("browser-javascript", "browser_javascript")
    
    if not path.endswith(".md"):
        path += ".md"
    return path

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
