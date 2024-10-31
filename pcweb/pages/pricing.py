import httpx
import reflex as rx
from httpx import Response

from pcweb.components.button import button
from pcweb.components.webpage.comps import h1_title
from pcweb.constants import (
    REFLEX_DEV_WEB_LANDING_FORM_SALES_CALL_WEBHOOK_URL,
    REFLEX_DEV_WEB_PRICING_FORM_PRO_PLAN_WAITLIST_WEBHOOK_URL,
)
from pcweb.pages.docs import getting_started, hosting
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

    @rx.event
    async def submit_pro_waitlist(self, form_data: dict):
        try:
            with httpx.Client() as client:
                response: Response = client.post(
                    REFLEX_DEV_WEB_PRICING_FORM_PRO_PLAN_WAITLIST_WEBHOOK_URL,
                    json=form_data,
                )
                response.raise_for_status()

            yield rx.toast.success("Thank you for joining the waitlist!")

        except httpx.HTTPError:
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
                    "Get an enterprise quote",
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
                    variant="muted",
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


# TODO(elvis): refactor the boolean logic to use enums
# https://linear.app/reflex-dev/issue/ENG-3837/refactor-the-included-variable-param-on-our-pricing-page-to-use-enums
def features(text: str, included: bool) -> rx.Component:
    if included:
        return rx.hstack(
            rx.icon(
                "circle-check", color=rx.color("green", 9), stroke_width=1.2, size=22
            ),
            rx.text(text, class_name="font-base font-normal"),
            align_items="center",
            spacing="2",
        )
    else:
        return rx.hstack(
            rx.icon("circle-x", color=rx.color("mauve", 9), stroke_width=1.2, size=22),
            rx.text(text, class_name="font-base"),
            align_items="center",
            spacing="2",
        )


def hobby_tier() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Hobby", class_name="text-2xl font-bold"),
                rx.badge(
                    "Free",
                    color_scheme="gray",
                    size="3",
                    variant="surface",
                    radius="full",
                ),
                width="100%",
                justify_content="space-between",
                class_name="mb-2",
            ),
            rx.text(
                "Everything you need to kickstart your project",
                class_name="text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Community support", True),
                features("Single developer workspace", True),
                features("A single deployed app", True),
                features("1024 MB Machine Size", True),
                features("A single CPU", True),
                features("1 day log retention", True),
                features("Multi-region", False),
                features("Custom domain", False),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            rx.link(
                button(
                    "Start building",
                    variant="secondary",
                    class_name="!w-full !text-slate-12",
                ),
                href=hosting.deploy_quick_start.path,
                width="100%",
                underline="none",
            ),
            align_items="start",
            class_name="h-full z-10 p-8",
        ),
        class_name="relative flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large p-4 border rounded-[1.125rem] self-stretch",
    )


def pro_tier() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Pro", class_name="text-2xl font-bold"),
                rx.badge(
                    "Coming Soon",
                    color_scheme="gray",
                    size="3",
                    variant="surface",
                    radius="full",
                ),
                width="100%",
                justify_content="space-between",
                class_name="mb-2",
            ),
            rx.text(
                "Professional devs and small teams shipping quickly",
                class_name="text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Priority support", True),
                features("5 Team members", True),
                features("5 Deployed apps", True),
                features("2048 MB machine size", True),
                features("2 CPU", True),
                features("30 days log retention", True),
                features("Multi-region", True),
                features("Custom domain", True),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            dialog(
                trigger=button(
                    "Join waitlist",
                    variant="secondary",
                    class_name="!w-full !text-slate-12",
                ),
                content=rx.form(
                    rx.box(
                        rx.text(
                            "Join waitlist",
                            class_name="text-slate-12 font-large",
                        ),
                        rx.text(
                            "Be the first to know when the Pro hosting plan is ready",
                            class_name="font-medium text-slate-11",
                        ),
                        class_name="flex flex-col gap-2 w-full font-instrument-sans",
                    ),
                    rx.box(
                        rx.el.input(
                            placeholder="Your email",
                            name="email",
                            type="email",
                            class_name="relative box-border border-slate-4 focus:border-violet-9 focus:border-1 bg-slate-2 p-[0.5rem_0.75rem] border rounded-xl font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                        ),
                        rx.dialog.close(
                            button(
                                "Submit",
                                type="submit",
                            ),
                        ),
                        class_name="flex flex-row justify-between items-center gap-4 w-full",
                    ),
                    rx.dialog.close(
                        rx.icon(
                            "x",
                            class_name="absolute top-2 right-2 !text-slate-9 hover:!text-slate-11 cursor-pointer transition-color",
                        ),
                    ),
                    on_submit=FormState.submit_pro_waitlist,
                    class_name="flex flex-col gap-5 relative p-1",
                ),
            ),
            align_items="start",
            class_name="h-full z-10 p-8",
        ),
        class_name="relative flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large p-4 border rounded-[1.125rem] self-stretch",
    )


def enterprise_tier() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Enterprise", class_name="text-2xl font-bold"),
                rx.badge(
                    "Custom",
                    color_scheme="violet",
                    size="3",
                    variant="surface",
                    radius="full",
                ),
                width="100%",
                justify_content="space-between",
                class_name="mb-2",
            ),
            rx.text(
                "A plan based on your specific needs",
                class_name="text-m text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Dedicated support", True),
                features("Support SLAs", True),
                features("Unlimited team members", True),
                features("Unlimited apps", True),
                features("Customized machine size", True),
                features("90 day log Retention", True),
                features("Multi-region", True),
                features("Custom domain", True),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            rx.text(
                "* With enterprise, you can deploy on-prem or host your app with us.",
                class_name="text-sm text-slate-10",
            ),
            align_items="start",
            class_name="h-full z-10 p-8",
        ),
        class_name="relative flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large p-4 border rounded-[1.125rem] self-stretch",
    )


@webpage(path="/pricing", title="Pricing · Reflex")
def pricing():
    return rx.el.section(
        rx.box(
            rx.box(
                h1_title(title="Find a plan that's right for you", class_name="mb-4"),
                rx.el.h2(
                    "Start for free using the open-source and scale as you grow.",
                    class_name="font-md text-balance text-slate-10 mb-10",
                ),
                class_name="section-header",
            ),
            rx.grid(
                rx.box(
                    hobby_tier(),
                    class_name="w-full",
                ),
                rx.box(
                    pro_tier(),
                    class_name="w-full",
                ),
                rx.box(
                    enterprise_tier(),
                    class_name="w-full",
                ),
                columns=rx.breakpoints(
                    xs="1",
                    sm="1",
                    md="3",
                    lg="3",
                    xl="3",
                ),
                spacing="4",
                width="100%",
            ),
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
