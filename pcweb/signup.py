import reflex as rx

from datetime import datetime
from sqlmodel import Field
import os
import json
import httpx
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field


class Waitlist(rx.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(rx.State):
    """Hold the state for the home page."""

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def add_contact_to_loops(self, contact_data):
        url = "https://app.loops.so/api/v1/contacts/create"
        loops_api_key = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }

        try:
            with httpx.Client() as client:
                response = client.post(url, headers=headers, json=contact_data)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.HTTPError as e:
            print(f"An error occurred: {e}")

    def signup_for_another_user(self):
        self.signed_up = False

    def signup(self, form_data: dict[str, str]):
        """Sign the user up for the waitlist."""

        email = form_data.get("input_email", None)
        if not email:
            return

        try:
            validation = validate_email(email, check_deliverability=True)
            email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return rx.toast.warning(
                str(e),
                style={
                    "border": "1px solid #3C3646",
                    "background": "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%)",
                },
            )

        # Check if the user is already on the waitlist.
        with rx.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=email))
                session.commit()
                contact_data = json.dumps({"email": email})
                self.add_contact_to_loops(contact_data)

        self.signed_up = True
