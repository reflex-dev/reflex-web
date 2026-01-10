"""Demo form component for collecting user information and scheduling enterprise calls.

This module provides a comprehensive demo form that validates company emails,
sends data to PostHog and Slack, and redirects users to appropriate Cal.com links
based on company size.
"""

import asyncio
import os
import urllib.parse
import uuid
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from typing import Any

import httpx
import reflex as rx
from reflex.experimental.client_state import ClientStateVar
from reflex.utils.console import log

import reflex_ui as ui

demo_form_error_message = ClientStateVar.create("demo_form_error_message", "")
is_sending_demo_form = ClientStateVar.create("is_sending_demo_form", False)
demo_form_open_cs = ClientStateVar.create("demo_form_open", False)

COMMONROOM_DESTINATION_ID = os.getenv("COMMONROOM_DESTINATION_ID", "")
COMMONROOM_API_TOKEN = os.getenv("COMMONROOM_API_TOKEN", "")
CAL_REQUEST_DEMO_URL = os.getenv(
    "CAL_REQUEST_DEMO_URL", "https://cal.com/team/reflex/reflex-intro-call"
)
JH_CAL_URL = os.getenv("JH_CAL_URL", "https://cal.com/team/reflex/demo-with-reflex")
INTRO_CAL_URL = os.getenv("INTRO_CAL_URL", "https://cal.com/team/reflex/reflex-intro")
CAL_ENTERPRISE_FOLLOW_UP_URL = os.getenv(
    "CAL_ENTERPRISE_FOLLOW_UP_URL",
    "https://cal.com/team/reflex/reflex-intro",
)
SLACK_DEMO_WEBHOOK_URL = os.getenv("SLACK_DEMO_WEBHOOK_URL", "")
POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY", "")


@dataclass(kw_only=True)
class PosthogEvent:
    """Base event structure."""

    distinct_id: str

    def to_dict(self) -> dict[str, Any]:
        """Convert the event instance to a dictionary representation.

        Returns:
            A dictionary containing all the event data.
        """
        return asdict(self)


@dataclass
class DemoEvent(PosthogEvent):
    """Event for demo booking."""

    first_name: str
    last_name: str
    company_email: str
    job_title: str
    company_name: str
    num_employees: str
    internal_tools: str
    technical_level: str
    referral_source: str


def input_field(
    label: str,
    placeholder: str,
    name: str,
    type: str = "text",
    required: bool = False,
) -> rx.Component:
    """Create a labeled input field component.

    Args:
        label: The label text to display above the input
        placeholder: Placeholder text for the input
        name: The name attribute for the input field
        type: The input type (text, email, tel, etc.)
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled input field
    """
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-sm font-medium text-secondary-12",
        ),
        ui.input(
            placeholder=placeholder,
            name=name,
            type=type,
            required=required,
            max_length=255,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5",
    )


def text_area_field(
    label: str, placeholder: str, name: str, required: bool = False
) -> rx.Component:
    """Create a labeled textarea field component.

    Args:
        label: The label text to display above the textarea
        placeholder: Placeholder text for the textarea
        name: The name attribute for the textarea field
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled textarea field
    """
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-secondary-12"),
        ui.textarea(
            placeholder=placeholder,
            name=name,
            required=required,
            class_name="w-full min-h-14",
            max_length=800,
        ),
        class_name="flex flex-col gap-1.5",
    )


def select_field(
    label: str,
    name: str,
    items: list[str],
    required: bool = False,
) -> rx.Component:
    """Create a labeled select field component.

    Args:
        label: The label text to display above the select
        name: The name attribute for the select field
        items: List of options to display in the select
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled select field
    """
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-xs lg:text-sm font-medium text-secondary-12 truncate min-w-0",
        ),
        ui.select(
            default_value="Select",
            name=name,
            items=items,
            required=required,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5 min-w-0",
    )


def is_small_company(num_employees: str) -> bool:
    """Check if company up to 5 employees."""
    return num_employees in ["1", "2-5"]


def check_if_company_email(email: str) -> bool:
    """Check if an email address is from a company domain (not a personal email provider).

    Args:
        email: The email address to check

    Returns:
        True if it's likely a company email, False if it's from a personal provider
    """
    if not email or "@" not in email:
        return False

    domain = email.split("@")[-1].lower()

    # List of common personal email providers
    personal_domains = {
        "gmail.com",
        "outlook.com",
        "hotmail.com",
        "yahoo.com",
        "icloud.com",
        "aol.com",
        "protonmail.com",
        "proton.me",
        "mail.com",
        "yandex.com",
        "zoho.com",
        "live.com",
        "msn.com",
        "me.com",
        "mac.com",
        "googlemail.com",
        "yahoo.co.uk",
        "yahoo.ca",
        "yahoo.co.in",
        "outlook.co.uk",
        "hotmail.co.uk",
    }

    return domain not in personal_domains and ".edu" not in domain


def check_if_default_value_is_selected(value: str) -> bool:
    """Check if the default value is selected."""
    return value.strip() != "Select"


class DemoFormStateUI(rx.State):
    """State for handling demo form submissions and integrations."""

    @rx.event(background=True)
    async def on_submit(self, form_data: dict[str, Any]):
        """Handle form submission with validation and routing logic.

        Validates company email, sends data to PostHog and Slack,
        then redirects to appropriate Cal.com link based on company size.

        Args:
            form_data: Form data dictionary containing user inputs
        """
        if not check_if_company_email(form_data.get("email", "")):
            yield rx.set_focus("email")
            yield rx.toast.error(
                "Please enter a valid company email - gmails, aol, me, etc are not allowed",
                position="top-center",
            )
            yield demo_form_error_message.push(
                "Please enter a valid company email - gmails, aol, me, etc are not allowed"
            )
            return
        # Check if the has selected a number of employees
        if not check_if_default_value_is_selected(
            form_data.get("number_of_employees", "")
        ):
            yield rx.toast.error(
                "Please select a number of employees",
                position="top-center",
            )
            yield demo_form_error_message.push("Please select a number of employees")
            return
        # Check if the has entered a referral source
        if not check_if_default_value_is_selected(
            form_data.get("how_did_you_hear_about_us", "")
        ):
            yield rx.toast.error(
                "Please select how did you hear about us",
                position="top-center",
            )
            yield demo_form_error_message.push(
                "Please select how did you hear about us"
            )
            return
        # Check if the has entered a technical level
        if not check_if_default_value_is_selected(form_data.get("technical_level", "")):
            yield rx.set_focus("technical_level")
            yield rx.toast.error(
                "Please select a technical level",
                position="top-center",
            )
            yield demo_form_error_message.push("Please select a technical level")
            return
        yield is_sending_demo_form.push(True)
        # Send to PostHog and Slack for all submissions
        yield DemoFormStateUI.send_demo_event(form_data)
        # Send data to Google Ads conversion tracking
        yield rx.call_script("gtag_report_conversion()")

        notes_content = f"""
Name: {form_data.get("first_name", "")} {form_data.get("last_name", "")}
Business Email: {form_data.get("email", "")}
Job Title: {form_data.get("job_title", "")}
Company Name: {form_data.get("company_name", "")}
Number of Employees: {form_data.get("number_of_employees", "")}
Internal Tools to Build: {form_data.get("internal_tools", "")}
Technical Level: {form_data.get("technical_level", "")}
How they heard about Reflex: {form_data.get("how_did_you_hear_about_us", "")}"""
        params = {
            "email": form_data.get("email", ""),
            "name": f"{form_data.get('first_name', '')} {form_data.get('last_name', '')}",
            "notes": notes_content,
        }

        query_string = urllib.parse.urlencode(params)
        technical_level = form_data.get("technical_level", "")

        # Route based on company size and technical level
        # if is_small_company(form_data.get("number_of_employees", "")):
        #     # Small companies (up to 5 employees) always go to JH_CAL_URL
        #     cal_url = JH_CAL_URL
        # else:
        #     # Large companies (more than 5 employees)
        #     if technical_level == "Non-technical":
        #         cal_url = JH_CAL_URL
        #     else:  # Neutral or Technical
        #         cal_url = INTRO_CAL_URL

        # cal_url_with_params = f"{cal_url}?{query_string}"
        yield [is_sending_demo_form.push(False), rx.redirect("/thank-you")]

    @rx.event(background=True)
    async def send_demo_event(self, form_data: dict[str, Any]):
        """Create and send demo event to PostHog and Slack.

        Converts form data into a DemoEvent and sends to both analytics
        platforms. Logs errors but doesn't raise exceptions.

        Args:
            form_data: Form data dictionary containing user inputs
        """
        first_name = form_data.get("first_name", "")
        last_name = form_data.get("last_name", "")
        demo_event = DemoEvent(
            distinct_id=f"{first_name} {last_name}",
            first_name=first_name,
            last_name=last_name,
            company_email=form_data.get("email", ""),
            job_title=form_data.get("job_title", ""),
            company_name=form_data.get("company_name", ""),
            num_employees=form_data.get("number_of_employees", ""),
            internal_tools=form_data.get("internal_tools", ""),
            technical_level=form_data.get("technical_level", ""),
            referral_source=form_data.get("how_did_you_hear_about_us", ""),
        )

        # Send data to PostHog, Common Room, and Slack
        await asyncio.gather(
            self.send_data_to_posthog(demo_event),
            self.send_data_to_common_room(demo_event),
            self.send_data_to_slack(demo_event),
        )

    async def send_data_to_posthog(self, event_instance: PosthogEvent):
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

    async def send_data_to_common_room(self, event_instance: DemoEvent):
        """Update CommonRoom with user login information."""
        tags: Sequence[str] = [
            "Requested Demo",
        ]

        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    f"https://api.commonroom.io/community/v1/source/{COMMONROOM_DESTINATION_ID}/activity",
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {COMMONROOM_API_TOKEN}",
                    },
                    json={
                        "id": "requested_demo",
                        "activityType": "requested_demo",
                        "user": {
                            "id": str(uuid.uuid4()),
                            "email": event_instance.company_email,
                        },
                        "tags": [
                            {
                                "type": "name",
                                "name": tag,
                            }
                            for tag in tags
                        ],
                    },
                )
        except Exception as ex:
            log(
                f"CommonRoom: Failed to identify user with email {event_instance.company_email}, err: {ex}"
            )

    async def send_data_to_slack(self, event_instance: DemoEvent):
        """Send demo form data to Slack webhook.

        Args:
            event_instance: An instance of DemoEvent with form data.
        """
        slack_payload = {
            "technicalLevel": event_instance.technical_level,
            "lookingToBuild": event_instance.internal_tools,
            "businessEmail": event_instance.company_email,
            "howDidYouHear": event_instance.referral_source,
            "jobTitle": event_instance.job_title,
            "numEmployees": event_instance.num_employees,
            "companyName": event_instance.company_name,
            "firstName": event_instance.first_name,
            "lastName": event_instance.last_name,
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    SLACK_DEMO_WEBHOOK_URL,
                    json=slack_payload,
                    headers={"Content-Type": "application/json"},
                )
                response.raise_for_status()
        except Exception as e:
            log(f"Error sending data to Slack webhook: {e}")


def demo_form(**props) -> rx.Component:
    """Create and return the demo form component.

    Builds a complete form with all required fields, validation,
    and styling. The form includes personal info, company details,
    and preferences.

    Args:
        **props: Additional properties to pass to the form component

    Returns:
        A Reflex form component with all demo form fields
    """
    return rx.el.form(
        rx.el.div(
            input_field("First name", "John", "first_name", "text", True),
            input_field("Last name", "Smith", "last_name", "text", True),
            class_name="grid grid-cols-2 gap-4",
        ),
        input_field("Business Email", "john@company.com", "email", "email", True),
        rx.el.div(
            input_field("Job title", "CTO", "job_title", "text", True),
            input_field("Company name", "Pynecone, Inc.", "company_name", "text", True),
            class_name="grid grid-cols-2 gap-4",
        ),
        text_area_field(
            "What are you looking to build? *",
            "Please list any apps, requirements, or data sources you plan on using",
            "internal_tools",
            True,
        ),
        rx.el.div(
            select_field(
                "Number of employees?",
                "number_of_employees",
                ["1", "2-5", "6-10", "11-50", "51-100", "101-500", "500+"],
            ),
            select_field(
                "How did you hear about us?",
                "how_did_you_hear_about_us",
                [
                    "Google Search",
                    "Social Media",
                    "Word of Mouth",
                    "Blog",
                    "Conference",
                    "Other",
                ],
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
        ),
        select_field(
            "How technical are you?",
            "technical_level",
            ["Non-technical", "Neutral", "Technical"],
            True,
        ),
        rx.cond(
            demo_form_error_message.value,
            rx.el.span(
                demo_form_error_message.value,
                class_name="text-destructive-10 text-sm font-medium px-2 py-1 rounded-md bg-destructive-3 border border-destructive-4",
            ),
        ),
        ui.button(
            "Submit",
            type="submit",
            class_name="w-full",
            loading=is_sending_demo_form.value,
        ),
        on_submit=DemoFormStateUI.on_submit,
        class_name=ui.cn(
            "@container flex flex-col lg:gap-6 gap-2 p-6",
            props.pop("class_name", ""),
        ),
        **props,
    )


def demo_form_dialog(trigger: rx.Component | None, **props) -> rx.Component:
    """Return a demo form dialog container element.

    Args:
        trigger: The component that triggers the dialog
        **props: Additional properties to pass to the dialog root

    Returns:
        A Reflex dialog component containing the demo form
    """
    class_name = ui.cn("w-auto", props.pop("class_name", ""))
    return ui.dialog.root(
        ui.dialog.trigger(render_=trigger),
        ui.dialog.portal(
            ui.dialog.backdrop(),
            ui.dialog.popup(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Book a Demo",
                            class_name="text-xl font-bold text-secondary-12",
                        ),
                        ui.dialog.close(
                            render_=ui.button(
                                ui.hi("Cancel01Icon"),
                                variant="ghost",
                                size="icon-sm",
                                class_name="text-secondary-11",
                            ),
                        ),
                        class_name="flex flex-row justify-between items-center gap-1 px-6 pt-4 -mb-4",
                    ),
                    demo_form(class_name="w-full max-w-md"),
                    class_name="relative isolate overflow-hidden -m-px w-full max-w-md",
                ),
                class_name="h-fit mt-1 overflow-hidden w-full max-w-md",
            ),
        ),
        open=demo_form_open_cs.value,
        on_open_change=demo_form_open_cs.set_value,
        class_name=class_name,
        **props,
    )
