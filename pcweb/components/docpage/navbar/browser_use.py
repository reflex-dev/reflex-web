"""Browser Use Cloud API integration for web search functionality."""

import reflex as rx
import httpx
import os
from typing import Dict, List, Any, Optional

BROWSER_USE_CONFIG = {
    "base_url": "https://api.browser-use.com/api/v1",
    "api_key": os.getenv("BROWSER_USE_API_KEY"),
    "timeout": 30,
}


class BrowserUseSearchState(rx.State):
    """State management for Browser Use Cloud search functionality."""
    
    search_query: str = ""
    search_results: List[Dict[str, Any]] = []
    is_searching: bool = False
    show_results: bool = False
    show_modal: bool = False
    search_type: str = "simple"
    error_message: str = ""
    show_ai_chat: bool = False
    ai_messages: List[Dict[str, str]] = []
    ai_input: str = ""
    
    def open_modal(self):
        """Open the search modal."""
        self.show_modal = True
        self._reset_search_state()
    
    def close_modal(self):
        """Close the search modal and reset state."""
        self.show_modal = False
        self._reset_search_state()
    
    def _reset_search_state(self):
        """Reset search-related state variables."""
        self.show_results = False
        self.is_searching = False
        self.search_query = ""
        self.search_results = []
        self.error_message = ""
        self.show_ai_chat = False
        self.ai_messages = []
        self.ai_input = ""
    
    async def perform_search(self):
        """Perform search using Browser Use Cloud API."""
        query = self.search_query
        search_type = self.search_type
        
        if not query.strip():
            self._clear_search_results()
            return
            
        self.is_searching = True
        self.error_message = ""
        
        try:
            results = await self._call_browser_use_api(query, search_type)
            self.search_results = results
            self.show_results = True
        except Exception as e:
            self.error_message = f"Search failed: {str(e)}"
            self._clear_search_results()
        
        self.is_searching = False

    async def _call_browser_use_api(self, query: str, search_type: str) -> List[Dict[str, Any]]:
        """Call Browser Use Cloud API endpoints."""
        if not BROWSER_USE_CONFIG["api_key"]:
            raise Exception("Browser Use API key not configured")
        
        headers = {
            "Authorization": f"Bearer {BROWSER_USE_CONFIG['api_key']}",
            "Content-Type": "application/json"
        }
        
        endpoint = "/simple-search" if search_type == "simple" else "/search-url"
        url = f"{BROWSER_USE_CONFIG['base_url']}{endpoint}"
        
        payload = {
            "query": query,
            "depth": 3
        }
        
        async with httpx.AsyncClient(timeout=BROWSER_USE_CONFIG["timeout"]) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            return self._format_api_results(data)
    
    def _format_api_results(self, api_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Format Browser Use API results for display."""
        formatted_results = []
        
        results = api_data.get("results", [])
        if isinstance(results, list):
            for result in results:
                formatted_result = {
                    "title": result.get("title", "No title"),
                    "content": result.get("content", result.get("text", "")),
                    "url": result.get("url", ""),
                    "source": result.get("source", "Browser Use"),
                    "score": result.get("relevance_score", 0),
                }
                formatted_results.append(formatted_result)
        
        return formatted_results
    
    def _clear_search_results(self):
        """Clear search results and hide results display."""
        self.search_results = []
        self.show_results = False
    
    def navigate_to_result(self, url: str):
        """Navigate to a search result URL."""
        if url:
            return rx.redirect(url, external=True)
    
    def open_ai_chat(self):
        """Open AI chat interface with search results as context."""
        self.show_ai_chat = True
        context_msg = f"Based on the search results for '{self.search_query}', I can help answer follow-up questions."
        self.ai_messages = [{"role": "assistant", "content": context_msg}]
    
    def close_ai_chat(self):
        """Close AI chat interface."""
        self.show_ai_chat = False
        self.ai_messages = []
        self.ai_input = ""
    
    def handle_key_press(self, key: str):
        """Handle key press events for search input."""
        if key == "Enter":
            return BrowserUseSearchState.perform_search
    
    async def send_ai_message(self):
        """Send message to AI chat (placeholder for future AI integration)."""
        message = self.ai_input
        if not message.strip():
            return
            
        self.ai_messages.append({"role": "user", "content": message})
        
        response = f"I understand you're asking about '{message}' in relation to your search for '{self.search_query}'. This is a placeholder response that could be enhanced with actual AI integration."
        self.ai_messages.append({"role": "assistant", "content": response})
        
        self.ai_input = ""
    
    def handle_ai_key_press(self, key: str):
        """Handle key press events for AI chat input."""
        if key == "Enter":
            return BrowserUseSearchState.send_ai_message


def browser_use_search_input() -> rx.Component:
    """Render the Browser Use search input field."""
    return rx.box(
        rx.hstack(
            rx.el.input(
                placeholder="Search the web or enter a URL...",
                value=BrowserUseSearchState.search_query,
                on_change=BrowserUseSearchState.set_search_query,
                on_key_down=lambda key: BrowserUseSearchState.handle_key_press(key),
                id="browser-use-search-input",
                auto_focus=True,
                class_name="flex-1 bg-transparent border-none outline-none focus:outline-none text-base",
            ),
            rx.button(
                "Search",
                on_click=BrowserUseSearchState.perform_search,
                class_name="px-4 py-2 bg-violet-9 text-white rounded-md hover:bg-violet-10",
            ),
            spacing="2",
            align_items="center",
            width="100%",
        ),
        class_name="w-full p-4 border-b border-slate-5",
    )


def search_result_item(result: rx.Var) -> rx.Component:
    """Render a single search result item."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("external-link", class_name="size-4 shrink-0 !text-slate-9"),
                rx.text(
                    result["title"],
                    class_name="text-md font-medium !text-slate-12 truncate",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="4px",
            ),
            rx.text(
                rx.cond(
                    result["content"].length() > 200,
                    result["content"][:200] + "...",
                    result["content"]
                ),
                font_size="14px",
                line_height="1.5",
                class_name="text-slate-11",
            ),
            rx.text(
                result["url"],
                font_size="12px",
                class_name="text-violet-9 truncate",
            ),
            align_items="start",
            spacing="1",
            width="100%",
        ),
        class_name="p-3 border border-slate-4 rounded-[8px] cursor-pointer w-full hover:border-slate-5 hover:bg-slate-2 shadow-small",
        on_click=lambda: BrowserUseSearchState.navigate_to_result(result["url"]),
    )


def search_results_section() -> rx.Component:
    """Render the search results section with Ask AI option."""
    return rx.box(
        rx.cond(
            BrowserUseSearchState.search_results.length() > 0,
            rx.vstack(
                rx.hstack(
                    rx.text(
                        f"Found {BrowserUseSearchState.search_results.length()} results",
                        class_name="text-sm text-slate-11 font-medium",
                    ),
                    rx.button(
                        rx.icon("message-circle", class_name="size-4"),
                        "Ask AI about these results",
                        on_click=BrowserUseSearchState.open_ai_chat,
                        class_name="ml-auto px-3 py-1 bg-violet-9 text-white rounded-md hover:bg-violet-10 text-sm",
                    ),
                    class_name="w-full justify-between items-center mb-4",
                ),
                rx.foreach(BrowserUseSearchState.search_results.to(List[Dict[str, str]]), search_result_item),
                spacing="3",
                width="100%",
            ),
            rx.cond(
                BrowserUseSearchState.error_message != "",
                rx.text(
                    BrowserUseSearchState.error_message,
                    class_name="text-red-9 text-center py-8",
                ),
                rx.text(
                    "No results found",
                    class_name="text-slate-9 text-center py-8",
                ),
            ),
        ),
        class_name="w-full flex flex-col gap-y-4 my-4 px-4",
    )


def ai_chat_interface() -> rx.Component:
    """Render AI chat interface for follow-up questions."""
    return rx.cond(
        BrowserUseSearchState.show_ai_chat,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.text("Ask AI", class_name="text-lg font-semibold text-slate-12"),
                    rx.button(
                        rx.icon("x", class_name="size-4"),
                        on_click=BrowserUseSearchState.close_ai_chat,
                        class_name="ml-auto p-1 hover:bg-slate-3 rounded",
                    ),
                    class_name="w-full justify-between items-center p-4 border-b border-slate-5",
                ),
                rx.scroll_area(
                    rx.foreach(
                        BrowserUseSearchState.ai_messages,
                        lambda msg: rx.box(
                            rx.text(
                                msg["content"],
                                class_name=rx.cond(
                                    msg["role"] == "user",
                                    "bg-violet-3 text-violet-12 p-3 rounded-lg ml-8",
                                    "bg-slate-3 text-slate-12 p-3 rounded-lg mr-8",
                                ),
                            ),
                            class_name="mb-3",
                        ),
                    ),
                    class_name="h-64 p-4",
                ),
                rx.hstack(
                    rx.el.input(
                        placeholder="Ask a follow-up question...",
                        value=BrowserUseSearchState.ai_input,
                        on_change=BrowserUseSearchState.set_ai_input,
                        on_key_down=lambda key: BrowserUseSearchState.handle_ai_key_press(key),
                        class_name="flex-1 p-2 border border-slate-5 rounded-l-md",
                    ),
                    rx.button(
                        "Send",
                        on_click=BrowserUseSearchState.send_ai_message,
                        class_name="px-4 py-2 bg-violet-9 text-white rounded-r-md hover:bg-violet-10",
                    ),
                    spacing="0",
                    class_name="p-4 border-t border-slate-5",
                ),
                class_name="bg-white border border-slate-5 rounded-lg shadow-lg",
            ),
            class_name="absolute top-0 right-0 w-96 h-full z-10",
        ),
        rx.fragment(),
    )


def browser_use_search_modal() -> rx.Component:
    """Create the Browser Use search modal dialog."""
    return rx.box(
        browser_use_search_input(),
        rx.cond(
            BrowserUseSearchState.is_searching,
            rx.box(
                rx.hstack(
                    rx.spinner(class_name="size-6"),
                    rx.text("Searching the web...", class_name="text-slate-11 ml-2"),
                    spacing="2",
                    align_items="center",
                ),
                class_name="flex items-center justify-center py-8",
            ),
            rx.cond(
                (BrowserUseSearchState.show_results) | (BrowserUseSearchState.error_message != ""),
                search_results_section(),
                rx.box(
                    rx.text(
                        "Search the web or enter a specific URL to extract content",
                        class_name="text-slate-9 text-center py-8",
                    ),
                ),
            ),
        ),
        ai_chat_interface(),
        class_name="w-full flex flex-col relative",
    )


def browser_use_search_trigger() -> rx.Component:
    """Render the Browser Use search trigger button."""
    return rx.button(
        rx.icon("globe", class_name="size-4"),
        "Web Search",
        on_click=BrowserUseSearchState.open_modal,
        class_name="flex items-center gap-2 px-3 py-2 bg-slate-1 border border-slate-5 rounded-md hover:bg-slate-3 text-slate-11 hover:text-slate-12 transition-colors",
    )


def browser_use_search() -> rx.Component:
    """Create the main Browser Use search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(browser_use_search_trigger()),
            rx.dialog.content(
                browser_use_search_modal(),
                class_name="w-full max-w-[800px] mx-auto bg-slate-1 border-none outline-none p-0 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
                on_interact_outside=BrowserUseSearchState.close_modal,
                on_escape_key_down=BrowserUseSearchState.close_modal,
            ),
            open=BrowserUseSearchState.show_modal,
        ),
    )
