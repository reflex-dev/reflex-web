from __future__ import annotations

import contextlib
from typing import Any

import httpx
import reflex as rx
from email_validator import EmailNotValidError, validate_email

from pcweb.components.button import button
from pcweb.components.icons import get_icon
from pcweb.constants import REFLEX_DEV_WEB_LANDING_FORM_DEMO_FORM_WEBHOOK_URL


class FormState(rx.State):
    @rx.event
    def submit(
        self,
        form_data: dict[str, Any],
    ):
        def submit_form() -> None:
            nonlocal form_data
            email: str | None
            if email := form_data.get("input_email"):
                validated_email: str | None = None
                with contextlib.suppress(EmailNotValidError):
                    validated_email = validate_email(
                        email,
                        check_deliverability=True,
                    )

                if validated_email is None:
                    return

                with contextlib.suppress(httpx.HTTPError) and httpx.Client() as client:
                    response = client.post(
                        REFLEX_DEV_WEB_LANDING_FORM_DEMO_FORM_WEBHOOK_URL,
                        json=form_data,
                    )
                    response.raise_for_status()

                return

        submit_form()
        return rx.toast(form_data)


def form() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.box(
                    get_icon("message_form", class_name="text-slate-9"),
                    class_name="size-14 rounded-full bg-slate-5 flex items-center justify-center shrink-0",
                ),
                rx.box(
                    rx.text(
                        "Send us a message",
                        class_name="font-md-smbold text-slate-12 leading-6",
                    ),
                    rx.text(
                        "Fill the form and we’ll back to you shortly.",
                        class_name="font-small text-slate-9",
                    ),
                    class_name="flex flex-col gap-1",
                ),
                class_name="flex flex-row gap-5 items-center",
            ),
            rx.box(
                rx.text(
                    "Name ",
                    rx.text.span("*", class_name="text-red-10 font-smbold"),
                    class_name="font-smbold text-slate-12",
                ),
                rx.el.input(
                    name="name",
                    type="text",
                    required=True,
                    custom_attrs={"aria-label": "Name"},
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 dark:bg-[#27282B] bg-slate-1 p-[0.5rem_0.75rem] border rounded-[10px] w-full font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.box(
                rx.text(
                    "Email ",
                    rx.text.span("*", class_name="text-red-10 font-smbold"),
                    class_name="font-smbold text-slate-12",
                ),
                rx.el.input(
                    # placeholder="Enter your password",
                    name="input_email",
                    type="email",
                    required=True,
                    custom_attrs={"aria-label": "Email"},
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 dark:bg-[#27282B] bg-slate-1 p-[0.5rem_0.75rem] border rounded-[0.625rem] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.box(
                rx.text(
                    "Message ",
                    class_name="font-smbold text-slate-12",
                ),
                rx.el.textarea(
                    name="message",
                    type="text",
                    custom_attrs={"aria-label": "Message"},
                    class_name="h-[4.75rem] box-border border-slate-5 focus:border-violet-9 focus:border-1 dark:bg-[#27282B] bg-slate-1 p-[0.5rem_0.75rem] border rounded-[10px] w-full font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none resize-none",
                ),
                class_name="flex flex-col gap-2",
            ),
            button(
                "Send",
                variant="muted",
                type="submit",
                class_name="!w-full !bg-slate-5 !border-t-[rgba(255,255,255,0.05)] !rounded-[0.625rem] hover:!bg-slate-6 !text-slate-9",
            ),
            on_submit=FormState.submit,
            class_name="flex flex-col gap-4 border-slate-4 bg-[#F9F9FB] dark:bg-[#222326] p-6 border rounded-[1rem] w-full lg:shadow-large",
        ),
        class_name="flex items-center p-4 lg:px-10 lg:py-12 h-full overflow-hidden",
    )


form_code = """import reflex as rx

class FormState(rx.State):

    @rx.event
    def submit(self, form_data):
        return rx.toast(form_data)

def form() -> rx.Component:
    return rx.card(
        rx.form(
            rx.hstack(
                rx.image(src="/envelope.png"),
                rx.vstack(
                    rx.heading("Send us a message"),
                    rx.text(
                        "Fill the form and we’ll back to you shortly.",
                    ),
                ),
            ),
            rx.vstack(
                rx.text(
                    "Name ",
                    rx.text.span("*", color="red"),
                ),
                rx.input(
                    name="name",
                    required=True,
                ),
            ),
            rx.vstack(
                rx.text(
                    "Email ",
                    rx.text.span("*", color="red"),
                ),
                rx.input(
                    name="email",
                    type="email",
                    required=True,
                ),
            ),
            rx.vstack(
                rx.text("Message"),
                rx.textarea(
                    name="message",
                ),
            ),
            rx.button("Send", type="submit"),
            on_submit=FormState.submit,
        )
    )
"""
