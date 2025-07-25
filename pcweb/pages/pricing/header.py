import re
import urllib.parse
from typing import Any, Literal

import reflex as rx
from reflex.event import EventType
from reflex.experimental import ClientStateVar
from reflex.utils.console import log

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.new_button import button
from pcweb.constants import CAL_REQUEST_DEMO_URL
from pcweb.pages.framework.views.companies import pricing_page_companies
from pcweb.telemetry.postog_metrics import (
    DemoEvent,
    send_data_to_posthog,
    send_data_to_slack,
)

ThankYouDialogState = ClientStateVar.create("thank_you_dialog_state", False)

SelectVariant = Literal["primary", "secondary", "outline", "transparent"]
SelectSize = Literal["sm", "md", "lg"]
SelectItemVariant = Literal["selectable", "actions", "projects"]

DEFAULT_CLASS_NAME = "inline-flex transition-bg shrink-0 items-center w-auto cursor-pointer disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 outline-none focus:outline-none"

VARIANT_STYLES: dict[SelectVariant, str] = {
    "primary": "text-slate-9 font-medium border border-slate-5 bg-slate-1 hover:bg-slate-3 radix-state-open:bg-slate-3",
    "secondary": "text-slate-11 font-medium bg-slate-4 hover:bg-slate-6 radix-state-open:bg-slate-6",
    "transparent": "bg-transparent text-slate-9 font-medium hover:bg-slate-3 radix-state-open:bg-slate-3",
    "outline": "text-slate-9 font-medium border border-slate-5 hover:bg-slate-3 radix-state-open:bg-slate-3 bg-slate-1",
}

SIZE_STYLES: dict[SelectSize, str] = {
    "xs": "text-sm px-1.5 h-7 rounded-md gap-1.5",
    "sm": "text-sm px-2 h-8 rounded-lg",
    "md": "text-sm px-2.5 min-h-9 max-h-9 rounded-[10px] gap-2.5",
    "lg": "text-sm px-3 h-10 rounded-xl gap-3",
}


def select_item(
    content: tuple[str | rx.Component, EventType[()]],
    is_selected: bool = False,
    size: SelectSize = "sm",
    variant: SelectItemVariant = "actions",
    loading: bool = False,
    **props,
) -> rx.Component:
    """A select item component."""
    text, on_click_event = content
    base_classes = [
        "flex transition-bg items-center w-full max-w-32 cursor-pointer disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 outline-none focus:outline-none",
        "bg-transparent text-slate-9 font-medium hover:bg-slate-3 font-sans",
        SIZE_STYLES[size],
    ]

    common_props = {
        "class_name": " ".join(filter(None, base_classes)),
        "type": "button",
        "on_click": on_click_event,
        **props,
    }

    return rx.popover.close(
        rx.el.button(
            text,
            rx.box(class_name="flex-1"),
            **common_props,
        ),
        class_name="w-full outline-none focus:outline-none",
    )


def select(
    content: rx.Component,
    variant: SelectVariant = "primary",
    size: SelectSize = "xs",
    placeholder: str = "Select an option",
    align: Literal["start", "center", "end"] = "start",
    class_name: str = "",
    icon: rx.Component | None = None,
    show_arrow: bool = True,
    unstyled: bool = False,
    tier: str = "",
    disabled: bool = False,
    **props,
) -> rx.Component:
    """A dropdown select component."""
    classes = (
        [
            DEFAULT_CLASS_NAME,
            VARIANT_STYLES[variant],
            SIZE_STYLES[size],
            class_name,
        ]
        if not unstyled
        else [class_name]
    )

    return rx.popover.root(
        rx.popover.trigger(
            rx.el.button(
                rx.box(placeholder),
                class_name=" ".join(filter(None, classes)),
                disabled=disabled,
                type="button",
            ),
        ),
        rx.popover.content(
            content,
            class_name="bg-transparent !shadow-none !p-0 border-none overflow-visible font-sans pointer-events-auto max-w-32",
        ),
        **props,
    )


class QuoteFormState(rx.State):
    """State management for the quote form."""

    num_employees: str = "500+"
    referral_source: str = "Google Search"
    banned_email: bool = False
    banned_linkedin: bool = False

    def set_select_value(self, field: str, value: str):
        """Update the selected value for a given field."""
        setattr(self, field, value)

    def is_small_company(self) -> bool:
        """Check if company has 5 or fewer employees."""
        return self.num_employees in ["1", "2-5"]

    @rx.event
    def submit(self, form_data: dict[str, Any]):
        # LinkedIn URL validation
        linkedin_url = form_data.get("linkedin_url", "").strip()
        if linkedin_url:
            # Basic LinkedIn URL validation
            linkedin_pattern = r"^https?://(www\.)?linkedin\.com/(in|company)/.+$"

            if not re.match(linkedin_pattern, linkedin_url):
                self.banned_linkedin = True
                yield rx.set_focus("linkedin_url")
                return

            self.banned_linkedin = False

        # Email domain validation
        banned_domains = [
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
        ]

        email = form_data.get("email", "").lower()
        if "@" in email:
            domain = email.split("@")[1]
            if domain in banned_domains or ".edu" in domain:
                self.banned_email = True
                yield rx.set_focus("email")
                return

            self.banned_email = False

            notes_content = f"""
Name: {form_data.get("first_name", "")} {form_data.get("last_name", "")}
Business Email: {form_data.get("email", "")}
LinkedIn URL: {form_data.get("linkedin_url", "")}
Job Title: {form_data.get("job_title", "")}
Company Name: {form_data.get("company_name", "")}
Number of Employees: {self.num_employees}
Internal Tools to Build: {form_data.get("internal_tools", "")}
How they heard about Reflex: {self.referral_source}"""

            # Send to PostHog for all submissions
            yield QuoteFormState.send_demo_event(form_data)

            yield rx.call_script(
                f"try {{ signals.identify('{email}'); }} catch(e) {{ console.warn('Signals identify failed:', e); }}"
            )

            if self.is_small_company():
                yield ThankYouDialogState.push(True)
                yield rx.redirect("https://cal.com/team/reflex/reflexdemo") 
                return

            params = {
                "email": form_data.get("email", ""),
                "name": f"{form_data.get('first_name', '')} {form_data.get('last_name', '')}",
                "notes": notes_content,
            }

            query_string = urllib.parse.urlencode(params)
            cal_url = f"{CAL_REQUEST_DEMO_URL}?{query_string}"

            return rx.redirect(cal_url)

    @rx.event(background=True)
    async def send_demo_event(self, form_data: dict[str, Any]):
        first_name = form_data.get("first_name", "")
        last_name = form_data.get("last_name", "")
        demo_event = DemoEvent(
            distinct_id=f"{first_name} {last_name}",
            first_name=first_name,
            last_name=last_name,
            company_email=form_data.get("email", ""),
            linkedin_url=form_data.get("linkedin_url", ""),
            job_title=form_data.get("job_title", ""),
            company_name=form_data.get("company_name", ""),
            num_employees=self.num_employees,
            internal_tools=form_data.get("internal_tools", ""),
            referral_source=self.referral_source,
            phone_number=form_data.get("phone_number", ""),
        )

        # Send to PostHog (existing)
        await send_data_to_posthog(demo_event)

        # Send to Slack (new)
        try:
            await send_data_to_slack(demo_event)
        except Exception as e:
            log(f"Failed to send to Slack: {e}")


def quote_input(placeholder: str, name: str, **props):
    return rx.el.input(
        placeholder=placeholder,
        name=name,
        class_name="box-border w-full border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
        **props,
    )


def form_field(
    label: str, input_component, required: bool = False, class_name: str = "mb-6"
):
    """Reusable form field component with label and input."""
    label_text = f"{label} {'*' if required else ''}"
    return rx.box(
        rx.text(label_text, class_name="text-slate-11 text-sm font-medium mb-2"),
        input_component,
        class_name=class_name,
    )


def text_input_field(
    label: str,
    name: str,
    placeholder: str,
    required: bool = False,
    input_type: str = "text",
    class_name: str = "mb-6",
):
    """Helper for creating text input fields."""
    input_component = quote_input(
        name=name,
        placeholder=placeholder,
        type=input_type,
        required=required,
    )
    return form_field(label, input_component, required, class_name)


def select_field(
    label: str,
    name: str,
    options: list,
    placeholder: str,
    required: bool = False,
    state_var: str = "",
):
    """Helper for creating custom select fields."""

    def create_select_item(option, state_var):
        return select_item(
            content=(
                option,
                lambda: QuoteFormState.set_select_value(state_var, option),
            ),
            size="sm",
            variant="selectable",
            class_name="w-full justify-start px-4 py-2 hover:bg-slate-2 rounded-md",
        )

    # Create scroll area with selectable options
    scroll_content = rx.box(
        *[create_select_item(option, state_var) for option in options],
        class_name="!pt-0 !mt-0 !max-h-[15rem] bg-slate-1 border border-slate-5 rounded-lg shadow-lg py-0 overflow-y-scroll w-full",
    )

    # Get the current selected value for this field
    current_value = getattr(QuoteFormState, state_var, placeholder)

    select_component = select(
        content=scroll_content,
        placeholder=current_value,
        variant="primary",
        size="md",
        class_name="w-full justify-between flex-1",
        show_arrow=True,
    )
    return form_field(label, select_component, required)


def textarea_field(label: str, name: str, placeholder: str, required: bool = False):
    """Helper for creating textarea fields."""
    textarea_component = rx.el.textarea(
        name=name,
        placeholder=placeholder,
        required=required,
        class_name="w-full px-3 py-2 font-medium text-slate-12 text-sm placeholder:text-slate-9 border border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] rounded-lg focus:border-violet-8 focus:outline-none bg-transparent min-h-[100px] resize-y transition-colors",
    )
    return form_field(label, textarea_component, required)


def thank_you_modal() -> rx.Component:
    """Thank you modal for small companies."""

    return rx.dialog.root(
        rx.dialog.content(
            rx.box(
                rx.box(
                    rx.text(
                        "Thank You for Your Interest!",
                        class_name="text-2xl font-semibold text-slate-12 font-sans",
                    ),
                    rx.dialog.close(
                        button(
                            rx.icon("x", class_name="!text-slate-9"),
                            variant="transparent",
                            size="icon-sm",
                            type="button",
                            class_name="focus:outline-none",
                            on_click=ThankYouDialogState.set_value(False),
                        ),
                    ),
                    class_name="flex flex-row items-center gap-2 justify-between w-full",
                ),
                rx.text(
                    "We've received your submission and our team will get back to you soon. We appreciate your interest in Reflex!",
                    class_name="text-slate-9 font-medium text-sm",
                ),
                class_name="flex flex-col w-full gap-y-4",
            ),
            class_name="w-full",
            on_interact_outside=ThankYouDialogState.set_value(False),
            on_escape_key_down=ThankYouDialogState.set_value(False),
        ),
        open=ThankYouDialogState.value,
    )


def custom_quote_form() -> rx.Component:
    """Custom quote form component with clean, maintainable structure."""
    return rx.box(
        rx.box(
            # Left column - Content
            rx.box(
                rx.el.h2(
                    "Book a Demo",
                    class_name="text-slate-12 text-4xl font-bold mb-8",
                ),
                rx.el.p(
                    "Enterprise-ready solutions designed for scale, compliance, and support. Contact us for a tailored quote based on your infrastructure and team size.",
                    class_name="text-slate-11 text-md leading-relaxed mb-12 max-w-lg",
                ),
                rx.box(
                    pricing_page_companies(),
                    class_name="flex flex-col",
                ),
                class_name="mb-8 lg:mb-0 text-center sm:text-left",
            ),
            # Right column - Form
            rx.box(
                rx.el.form(
                    # Personal Information
                    rx.el.div(
                        text_input_field(
                            "First name",
                            "first_name",
                            "John",
                            required=True,
                            class_name="mb-0",
                        ),
                        text_input_field(
                            "Last name",
                            "last_name",
                            "Smith",
                            required=True,
                            class_name="mb-0",
                        ),
                        class_name="flex-row flex gap-x-2 mb-6",
                    ),
                    rx.cond(
                        QuoteFormState.banned_email,
                        rx.box(
                            rx.el.div(
                                rx.text(
                                    "Business email",
                                    class_name="text-slate-11 text-sm font-medium mb-2",
                                ),
                                rx.text(
                                    "Personal emails not allowed!",
                                    class_name="text-red-8 text-sm font-medium mb-2",
                                ),
                                class_name="flex flex-row items-center justify-between w-full",
                            ),
                            rx.el.input(
                                placeholder="Personal emails not allowed!",
                                name="email",
                                class_name="box-border w-full border-2 border-red-5 bg-slate-1 px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
                            ),
                        ),
                        text_input_field(
                            "Business email",
                            "email",
                            "john@reflex.dev",
                            required=True,
                            input_type="email",
                        ),
                    ),
                    rx.el.div(
                        text_input_field(
                            "Job title",
                            "job_title",
                            "CTO",
                            required=True,
                            class_name="mb-0",
                        ),
                        text_input_field(
                            "Company name",
                            "company_name",
                            "Pynecone, Inc.",
                            required=True,
                            class_name="mb-0",
                        ),
                        class_name="flex-row flex gap-x-2 mb-6",
                    ),
                    # LinkedIn field (replacing phone number)
                    rx.cond(
                        QuoteFormState.banned_linkedin,
                        rx.box(
                            rx.el.div(
                                rx.text(
                                    "LinkedIn profile URL",
                                    class_name="text-slate-11 text-sm font-medium mb-2",
                                ),
                                rx.text(
                                    "Invalid LinkedIn URL format!",
                                    class_name="text-red-8 text-sm font-medium mb-2",
                                ),
                                class_name="flex flex-row items-center justify-between w-full",
                            ),
                            rx.el.input(
                                placeholder="Please enter a valid LinkedIn URL",
                                name="linkedin_url",
                                type="url",
                                required=True,
                                class_name="box-border w-full border-2 border-red-5 bg-slate-1 px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
                            ),
                            class_name="mb-6",
                        ),
                        text_input_field(
                            "LinkedIn profile URL",
                            "linkedin_url",
                            "https://linkedin.com/in/your-profile",
                            required=True,
                            input_type="url",
                        ),
                    ),
                    text_input_field(
                        "Phone number (optional)",
                        "phone_number",
                        "+1 (555) 123-4567",
                        required=False,
                        input_type="tel",
                    ),
                    # Project Details
                    textarea_field(
                        "What are you looking to build?",
                        "internal_tools",
                        "Please list any apps, requirements, or data sources you plan on using",
                        required=True,
                    ),
                    # Company Size and Referral
                    rx.el.div(
                        select_field(
                            "Number of employees",
                            "num_employees",
                            [
                                "1",
                                "2-5",
                                "6-10",
                                "11-50",
                                "51-100",
                                "101-500",
                                "500+",
                            ],  # Updated options
                            "500+",
                            required=True,
                            state_var="num_employees",
                        ),
                        select_field(
                            "How did you hear about us?",
                            "referral_source",
                            [
                                "Google Search",
                                "Social Media",
                                "Word of Mouth",
                                "Blog",
                                "Conference",
                                "Other",
                            ],
                            "Google Search",
                            required=True,
                            state_var="referral_source",
                        ),
                        class_name="w-full flex-row flex flex-wrap justify-between mb-6",
                    ),
                    # Submit button
                    button(
                        "Submit",
                        variant="primary",
                        type="submit",
                        size="lg",
                        class_name="w-full mt-2",
                    ),
                    class_name="w-full space-y-6",
                    on_submit=QuoteFormState.submit,
                    reset_on_submit=True,
                ),
                class_name="relative bg-slate-1 p-6 sm:p-8 rounded-2xl border-2 border-violet-9 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 max-w-7xl mx-auto items-start",
        ),
        # Thank you modal
        thank_you_modal(),
        class_name="py-12 sm:py-20 px-4 sm:px-8",
    )


def header() -> rx.Component:
    return rx.box(
        custom_quote_form(),
        class_name="flex flex-col gap-2 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full -mb-10 "
        + rx.cond(HostingBannerState.show_banner, "pt-[11rem]", "pt-[12rem]"),
    )
