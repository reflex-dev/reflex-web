import httpx
import reflex as rx

from pcweb.components.button import button
from pcweb.constants import REFLEX_DEV_WEB_LANDING_FORM_SALES_CALL_WEBHOOK_URL
from pcweb.templates.webpage import webpage


class FormState(rx.State):
    is_loading: bool = False
    email_sent: bool = False

    @rx.event
    async def submit(self, form_data: dict):
        self.is_loading = True
        yield

        try:
            with httpx.Client() as client:
                response = client.post(
                    REFLEX_DEV_WEB_LANDING_FORM_SALES_CALL_WEBHOOK_URL,
                    json=form_data,
                )
                response.raise_for_status()

            self.is_loading = False
            self.email_sent = True
            yield rx.toast.success("Demo request submitted successfully!")

        except httpx.HTTPError:
            self.is_loading = False
            self.email_sent = False
            yield rx.toast.error("Failed to submit request. Please try again later.")


def dialog(trigger: rx.Component, content: rx.Component) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            trigger,
        ),
        rx.dialog.content(
            content,
            class_name="bg-white-1 p-4 rounded-[1.625rem] w-[26rem]",
        ),
    )


def form() -> rx.Component:
    input_class_name = "box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-slate-1 p-[0.5rem_0.75rem] border rounded-[10px] w-full font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none"
    return rx.box(
        rx.form(
            rx.box(
                rx.text(
                    "Contact the Sales Team",
                    class_name="text-2xl text-slate-12 font-bold leading-6 scroll-m-[7rem]",
                    id="form-title",
                ),
                rx.text(
                    "Explore custom plans and pricing",
                    class_name="font-base text-slate-9",
                ),
                class_name="flex flex-col gap-2 mb-4 items-start",
            ),
            rx.box(
                rx.hstack(
                    rx.el.input(
                        name="first_name",
                        type="text",
                        placeholder="First name *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    rx.el.input(
                        name="last_name",
                        type="text",
                        placeholder="Last name *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    spacing="2",
                    width="100%",
                    class_name="mb-2.5 gap-2",
                ),
                rx.hstack(
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="Business email *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    rx.el.input(
                        name="linkedin_profile",
                        type="text",
                        placeholder="LinkedIn profile",
                        required=False,
                        class_name=input_class_name,
                    ),
                    spacing="2",
                    width="100%",
                    class_name="mb-2.5 gap-2",
                ),
                rx.hstack(
                    rx.el.input(
                        name="company_name",
                        type="text",
                        placeholder="Company name *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    rx.el.input(
                        name="title",
                        type="text",
                        placeholder="Title *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    spacing="2",
                    width="100%",
                    class_name="mb-2.5 gap-2",
                ),
                rx.el.textarea(
                    name="project_description",
                    placeholder="Your company needs",
                    class_name=input_class_name + " h-24 mb-4 resize-none",
                ),
                class_name="flex flex-col",
            ),
            rx.cond(
                FormState.is_loading,
                button(
                    "Sending...",
                    variant="secondary",
                    type="submit",
                    class_name="opacity-80 !cursor-not-allowed pointer-events-none !w-min",
                ),
                button(
                    "Submit",
                    type="submit",
                    class_name="!w-min",
                ),
            ),
            on_submit=FormState.submit,
            class_name="flex flex-col",
        ),
        rx.box(
            rx.text(
                "If you have any questions, feel free to contact us",
                class_name="font-small text-slate-9",
            ),
            rx.link(
                "sales@reflex.dev",
                href="mailto:sales@reflex.dev",
                underline="always",
                class_name="text-slate-9 font-small",
            ),
            class_name="flex flex-row justify-between items-center gap-2 mt-4",
        ),
        class_name="relative flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large p-8 border rounded-[1.125rem] self-stretch scroll-[3rem]",
    )


@webpage(path="/sales", title="Pricing · Reflex")
def sales():
    return rx.el.section(
        rx.box(
            rx.box(
                rx.cond(
                    FormState.email_sent,
                    rx.box(
                        rx.box(
                            rx.text(
                                """Thanks for your interest in Reflex!
You'll get a reply from us soon.""",
                                class_name="font-large text-slate-12 whitespace-pre text-center",
                            ),
                            class_name="flex flex-row items-center gap-2",
                        ),
                        button(
                            "Back",
                            on_click=FormState.setvar("email_sent", False),
                            class_name="mt-4",
                        ),
                        class_name="flex flex-col items-center gap-2",
                    ),
                    form(),
                ),
                class_name="mt-12 w-full",
            ),
            class_name="flex flex-col justify-center items-center w-full max-w-[84.5rem]",
        ),
        id="pricing",
        class_name="section-content",
    )
