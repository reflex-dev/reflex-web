import contextlib
import json
import os
from datetime import datetime

import httpx
import reflex as rx
from email_validator import EmailNotValidError, ValidatedEmail, validate_email
from sqlmodel import Field

from pcweb.constants import API_BASE_URL_LOOPS

REFLEX_DEV_WEB_NEWSLETTER_FORM_URL: str = "https://hkdk.events/t0qopjbznnp2fr"


class Waitlist(rx.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(rx.State):
    """Hold the state for the home page."""

    # Whether the user signed up for the newsletter.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def send_contact_to_webhook(
        self,
        email: str,
    ) -> None:
        with contextlib.suppress(httpx.HTTPError) and httpx.Client() as client:
            response = client.post(
                REFLEX_DEV_WEB_NEWSLETTER_FORM_URL,
                json={
                        "email": email,
                    },
            )
            response.raise_for_status()


    def add_contact_to_loops(
        self,
        email: str,
    ):
        url: str = f"{API_BASE_URL_LOOPS}/contacts/create"
        loops_api_key: str | None = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
            return

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }
        try:
            with httpx.Client() as client:
                response = client.post(
                    url,
                    headers=headers,
                    json={
                            "email": email,
                        },
                )
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.HTTPError as e:
            print(f"An error occurred: {e}")

    def signup_for_another_user(self):
        self.signed_up = False

    def signup(
        self,
        form_data: dict[str, str],
    ):
        """Sign the user up for the newsletter."""
        email: str | None = None
        if email_to_validate := form_data.get("input_email"):
            try:
                validated_email: ValidatedEmail = validate_email(
                    email_to_validate,
                    check_deliverability=True,
                )
                email = validated_email.normalized

            except EmailNotValidError as e:
                # Alert the error message.
                return rx.toast.warning(
                    str(e),
                    style={
                        "border": "1px solid #3C3646",
                        "background": "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%)",
                    },
                )

        self.send_contact_to_webhook(email)
        self.add_contact_to_loops(email)
        # Check if the user is already on the newsletter
        with rx.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == email).first()
            if user is None:
                # Add the user to the newsletter
                session.add(
                    Waitlist(
                        email=email,
                    ),
                )
                session.commit()

        self.signed_up = True
        return None
