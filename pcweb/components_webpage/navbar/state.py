"""The state for the navbar component."""
import os
from datetime import datetime
from typing import Any, Optional, Set

import reflex as rx
import requests
from sqlmodel import Field


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    current_category = "All"

    def toggle_banner(self):
        self.banner = not self.banner

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_ai_chat(self):
        self.ai_chat = not self.ai_chat

    def update_category(self, tag):
        self.current_category = tag

    @rx.cached_var
    def search_results(self) -> list[dict[str, dict[str, str]]]:
        """Get the search results."""
        from pcweb.tsclient import client

        if client is None or self.search_input == "":
            return []

        if self.current_category == "All":
            search_parameters = {
                "q": self.search_input,
                "query_by": "heading, description",
                "query_by_weights": "2,1",
                "sort_by": "_text_match:desc",
            }
        else:
            search_parameters = {
                "q": self.search_input,
                "query_by": "heading, description",
                "query_by_weights": "2,1",
                "sort_by": "_text_match:desc",
                "filter_by": f"category: {self.current_category}",
            }
        typesense_collection_name = os.getenv(
            "TYPESENSE_COLLECTION_NAME", "search-auto"
        )
        return client.collections[typesense_collection_name].documents.search(
            search_parameters
        )["hits"]
