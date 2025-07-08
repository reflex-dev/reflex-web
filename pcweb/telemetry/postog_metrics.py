from dataclasses import asdict, dataclass
from typing import Any

import httpx
from posthog import Posthog
from reflex.utils.console import log
from pcweb.constants import POSTHOG_API_KEY

try:
    posthog = Posthog(POSTHOG_API_KEY, host="https://us.i.posthog.com")
except Exception:
    pass


@dataclass(kw_only=True)
class PosthogEvent:
    """Base event structure."""

    distinct_id: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class DemoEvent(PosthogEvent):
    """Event for demo booking."""

    first_name: str
    last_name: str
    company_email: str
    linkedin_url: str
    job_title: str
    company_name: str
    num_employees: str
    internal_tools: str
    referral_source: str


async def send_data_to_posthog(event_instance: PosthogEvent):
    """Send data to PostHog using class introspection.

    Args:
        event_instance: An instance of a PosthogEvent subclass.

    Raises:
        httpx.HTTPError: When there is an error sending data to PostHog.
    """
    event_data = {
        "api_key": POSTHOG_API_KEY,
        "event": event_instance.__class__.__name__,
        "properties": event_instance.to_dict(),
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://app.posthog.com/capture/", json=event_data
            )
            response.raise_for_status()
    except Exception:
        log("Error sending data to PostHog")
