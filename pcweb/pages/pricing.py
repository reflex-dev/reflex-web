import reflex as rx
import httpx
from pcweb.templates.webpage import webpage
from pcweb.components.webpage.comps import h1_title
from pcweb.components.button import button, variant_styles, default_class_name
from pcweb.pages.docs import getting_started, hosting


class FormState(rx.State):
    is_loading: bool = False

    async def submit(self, form_data: dict):
        self.is_loading = True
        yield
        webhook_url = "https://hkdk.events/fl9kcr4bf5pn7w"

        try:
            with httpx.Client() as client:
                response = client.post(webhook_url, json=form_data)
                response.raise_for_status()
            self.is_loading = False
            yield rx.toast.success("Demo request submitted successfully!")
        except httpx.HTTPError as e:
            self.is_loading = False
            yield rx.toast.error("Failed to submit request. Please try again later.")


def form() -> rx.Component:
    input_class_name = "box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-slate-1 p-[0.5rem_0.75rem] border rounded-[10px] w-full font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none"
    return rx.box(
        rx.form(
            rx.box(
                rx.text(
                    "Get an Enterprise Quote",
                    class_name="text-2xl text-slate-12 font-bold leading-6 scroll-m-[7rem]",
                    id="form-title",
                ),
                rx.text(
                    "Get a custom demo and discover the value of Reflex for your enterprise. Explore our custom plans and pricing.",
                    class_name="font-base text-slate-9",
                ),
                class_name="flex flex-col gap-2 mb-4 items-start",
            ),
            rx.box(
                rx.hstack(
                    rx.el.input(
                        name="first_name",
                        type="text",
                        placeholder="First Name *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    rx.el.input(
                        name="last_name",
                        type="text",
                        placeholder="Last Name *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    spacing="2",
                    width="100%",
                    class_name="mb-2.5 gap-2",
                ),
                rx.hstack(
                    rx.el.input(
                        name="business_email",
                        type="email",
                        placeholder="Business Email *",
                        required=True,
                        class_name=input_class_name,
                    ),
                    rx.el.input(
                        name="linkedin_profile",
                        type="text",
                        placeholder="LinkedIn Profile",
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
                        placeholder="Company Name *",
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
                rx.el.button(
                    rx.spinner(class_name="w-4 h-4"),
                    class_name=default_class_name
                    + " "
                    + variant_styles["primary"]["class_name"]
                    + " "
                    + "w-full bg-slate-5 text-slate-12 hover:bg-slate-6 rounded",
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
                "If you have any questions, please contact us.",
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


def features(text: str, included: bool) -> rx.Component:
    if included:
        return rx.hstack(
            rx.icon("circle-check", color=rx.color("green", 9), stroke_width=1.2, size=22),
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
                "Everything you need to kickstart your project.",
                class_name="text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Community Support", True),
                features("Single developer workspace", True),
                features("1 Deployed App", True),
                features("1024 MB Machine Size", True),
                features("1 CPU", True),
                features("1-day Log Retention", True),
                features("Multi Region", False),
                features("Custom Domain", False),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            rx.link(
                button(
                    "Get Started",
                    # class_name="w-full bg-slate-5 text-slate-12 hover:bg-slate-6 rounded py-2 cursor-pointer",
                    variant="secondary",
                    class_name="!w-full !text-slate-12"
                ),
                href=hosting.deploy_quick_start.path,
                width="100%",
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
                "Professional developers and smallteams shipping to production.",
                class_name="text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Priority Support", True),
                features("5 Team Members", True),
                features("5 Deployed Apps", True),
                features("2048 MB Machine Size", True),
                features("2 CPU", True),
                features("30-day Log Retention", True),
                features("Multi Region", True),
                features("Custom Domain", True),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            rx.link(
                button(
                    "Join Waitlist",
                    variant="secondary",
                    class_name="!w-full !text-slate-12"
                ),
                href="mailto:contact@reflex.dev",
                width="100%",
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
                "A plan based on your specific needs.",
                class_name="text-m text-slate-10 mb-4",
            ),
            rx.vstack(
                features("Dedicated Support Channel", True),
                features("Support SLAs available", True),
                features("Unlimited Team Members", True),
                features("Unlimited Apps", True),
                features("Customized Machine Size", True),
                features("90-day Log Retention", True),
                features("Multi Region", True),
                features("Custom Domain", True),
                align_items="start",
                spacing="3",
                class_name="mb-6",
            ),
            rx.link(
                button(
                    "Contact",
                    class_name="!w-full"
                ),
                href="#form-title",
                width="100%",
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
                form(),
                class_name="mt-12 w-full",
            ),
            class_name="flex flex-col justify-center items-center w-full max-w-[84.5rem]",
        ),
        id="pricing",
        class_name="section-content",
    )
