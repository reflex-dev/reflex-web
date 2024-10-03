import contextlib
import os

import httpx
import reflex as rx
from email_validator import EmailNotValidError, ValidatedEmail, validate_email

from pcweb.constants import (
    API_BASE_URL_LOOPS,
    REFLEX_DEV_WEB_NEWSLETTER_FORM_WEBHOOK_URL,
)
from pcweb.models import Waitlist


def add_contact_to_loops(email: str, ):
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


def send_contact_to_webhook(email: str) -> None:
    with contextlib.suppress(httpx.HTTPError) and httpx.Client() as client:
        response = client.post(
            REFLEX_DEV_WEB_NEWSLETTER_FORM_WEBHOOK_URL,
            json={
                "email": email,
            },
        )
        response.raise_for_status()


def signup_for_newsletter(email: str | None = None) -> str | None:
    if email:
        try:
            validated_email: ValidatedEmail = validate_email(
                email,
                check_deliverability=True,
            )
            email = validated_email.normalized

        except EmailNotValidError as e:
            return str(e)

    send_contact_to_webhook(email)
    add_contact_to_loops(email)
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