"""The state for the navbar component."""

import contextlib
import os
from datetime import datetime
from typing import Any, Optional, Set

import httpx
import reflex as rx
import requests
from sqlmodel import Field

from pcweb.constants import REFLEX_DEV_WEB_GENERAL_FORM_FEEDBACK_WEBHOOK_URL


class Feedback(rx.Model, table=True):
    email: Optional[str]
    feedback: str
    score: Optional[int]
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    page: str


class FeedbackState(rx.State):
    """The state for feedback components"""

    score: Optional[int] = None

    def handle_submit(self, form_data: dict):
        feedback = form_data["feedback"]

        # Check if the email is valid.
        if "email" in form_data:
            email = form_data["email"]

        if len(feedback) < 10 or len(feedback) > 500:
            return rx.toast.warning(
                "Please enter your feedback. Between 10 and 500 characters.",
                close_button=True,
            )

        current_page_route: str = self.router.page.raw_path
        with contextlib.suppress(httpx.HTTPError) and httpx.Client() as client:
            client.post(
                REFLEX_DEV_WEB_GENERAL_FORM_FEEDBACK_WEBHOOK_URL,
                json=form_data,
            )

        discord_message = f"""
Contact: {email}
Page: {current_page_route}
Score: {"👍" if self.score == 1 else "👎"}
Feedback: {feedback}
"""

        DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
        payload = {"content": discord_message}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)

        except Exception:
            return rx.toast.error(
                """An error occurred while submitting your feedback. If the issue persists,
please file a Github issue or stop by our Discord.""",
                close_button=True,
            )

        else:
            yield rx.toast.success(
                "Thank you for your feedback!",
                close_button=True,
            )
