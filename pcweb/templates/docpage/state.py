"""The state for the navbar component."""

import os
from datetime import datetime

import reflex as rx
import requests
from sqlmodel import Field


class Feedback(rx.Model, table=True):
    email: str | None
    feedback: str
    score: int | None
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    page: str


class FeedbackState(rx.State):
    """The state for feedback components."""

    score: int | None = None

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

        current_page_route = self.router.page.raw_path

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
                "An error occurred while submitting your feedback. If the issue persists, "
                "please file a Github issue or stop by our discord.",
                close_button=True,
            )
        else:
            yield rx.toast.success(
                "Thank you for your feedback!",
                close_button=True,
            )
