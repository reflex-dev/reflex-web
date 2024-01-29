"""The state for the navbar component."""
import os
from datetime import datetime
from typing import Any, Optional, Set

import reflex as rx
import requests
from sqlmodel import Field



class Feedback(rx.Model, table=True):
    email: Optional[str]
    feedback: str
    score: Optional[int]
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    page: str


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_modal: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    email: str = ""

    feedback: str = ""

    page_score: int = 0

    show_form = False
    form_submitted = False

    current_category = "All"

    def handle_submit(self, form_data: dict):
        feedback = form_data["feedback"]

        # Check if the email is valid.
        if "email" in form_data:
            self.email = form_data["email"]

        if len(feedback) < 10 or len(feedback) > 500:
            return rx.window_alert(
                "Please enter your feedback. Between 10 and 500 characters."
            )

        current_page_route = self.get_current_page()

        discord_message = f"""
Contact: {self.email}
Page: {current_page_route}
Score: {"?" if  self.page_score==0 else "👍" if self.page_score > 1 else "👎"}
Feedback: {feedback}
"""

        DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
        payload = {"content": discord_message}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except:
            pass

        self.show_form = False
        self.form_submitted = True
        self.page_score = 0

    def update_score(self, score):
        if self.show_form is True:
            if self.page_score == score:
                self.show_form = not self.show_form
        else:
            self.show_form = not self.show_form

        self.page_score = score

    def display_form(self):
        self.show_form = True

    def toggle_banner(self):
        self.banner = not self.banner

    def open_search(self):
        self.search_modal = True

    def close_search(self):
        self.search_modal = False

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
