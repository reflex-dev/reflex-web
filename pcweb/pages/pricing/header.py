import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState
from pcweb.pages.framework.views.companies import pricing_page_companies
from pcweb.components.new_button import button
import reflex as rx


input_style = "w-full pl-2 py-1 bg-transparent border border-slate-6 rounded-lg focus:border-violet-8 focus:outline-none",

def custom_quote_form() -> rx.Component:
    """Custom quote form component matching the provided design with responsive grid layout."""
    return rx.box(
        # Main container with responsive grid layout
        rx.box(
            # Left column - Content
            rx.box(
                # Main heading
                rx.el.h2(
                    "Request Your Custom Quote",
                    class_name="text-slate-12 text-4xl font-bold mb-8",
                ),

                # Description text
                rx.el.p(
                    "Enterprise-ready solutions designed for scale, compliance, and support. Contact us for a tailored quote based on your infrastructure and team size.",
                    class_name="text-slate-11 text-md leading-relaxed mb-12 max-w-lg",
                ),

                # Company logos section
                rx.box(
                   pricing_page_companies(),
                    class_name="flex flex-col",
                ),
                class_name="mb-8 lg:mb-0 text-center sm:text-left",
            ),

            # Right column - Form
            rx.box(
                rx.el.form(
                    # Name fields row
                    rx.flex(
                        rx.box(
                            rx.text("First name *", class_name="text-slate-11 text-sm font-medium mb-2"),
                            rx.el.input(
                                name="first_name",
                                placeholder="John",
                                class_name=input_style,
                                required=True,
                            ),
                            class_name="flex-1",
                        ),
                        rx.box(
                            rx.text("Last name *", class_name="text-slate-11 text-sm font-medium mb-2"),
                            rx.el.input(
                                name="last_name",
                                placeholder="Smith",
                                class_name=input_style,
                                required=True,
                            ),
                            class_name="flex-1",
                        ),
                        gap="1rem",
                        class_name="mb-6 flex-col sm:flex-row",
                    ),

                    # Business email
                    rx.box(
                        rx.text("Business email *", class_name="text-slate-11 text-sm font-medium mb-2"),
                        rx.el.input(
                            name="business_email",
                            type="email",
                            placeholder="john@reflex.dev",
                            class_name=input_style,
                            required=True,
                        ),
                        class_name="mb-6",
                    ),

                    # Job title
                    rx.box(
                        rx.text("Job title", class_name="text-slate-11 text-sm font-medium mb-2"),
                        rx.el.input(
                            name="job_title",
                            placeholder="CTO",
                            class_name=input_style,
                            required=True,
                        ),
                        class_name="mb-6",
                    ),

                    # Company name and employees row
                    rx.flex(
                        rx.box(
                            rx.text("Company name *", class_name="text-slate-11 text-sm font-medium mb-2"),
                            rx.el.input(
                                name="company_name",
                                placeholder="Pynecone, Inc.",
                                class_name=input_style,
                                required=True,
                            ),
                            class_name="flex-1",
                        ),
                        gap="1rem",
                        class_name="mb-6 flex-col sm:flex-row",
                    ),

                    # Phone number
                    rx.box(
                        rx.text("Phone number *", class_name="text-slate-11 text-sm font-medium mb-2"),
                        rx.el.input(
                            name="phone_number",
                            type="tel",
                            placeholder="(555) 123-4567",
                            class_name=input_style,
                            required=True,
                        ),
                        class_name="mb-6",
                    ),

                    # What internal tools textarea
                    rx.box(
                        rx.text("What internal tools are you looking to build? *", class_name="text-slate-11 text-sm font-medium mb-2"),
                        rx.el.textarea(
                            required=True,
                            name="internal_tools",
                            placeholder="Customer service admin panel",
                            class_name="w-full pl-2 py-2 border border-slate-6 rounded-lg focus:border-violet-8 focus:outline-none bg-transparent min-h-[100px] resize-none",
                        ),
                        class_name="mb-6",
                    ),
                    rx.box(# Number of employees
                    rx.box(
                         rx.text("Number of employees *", class_name="text-slate-11 text-sm font-medium mb-2"),
                         rx.select(
                             ["1-10", "11-50", "51-100", "101-500", "500+"],
                             name="num_employees",
                             placeholder="500+",
                             class_name="w-full p-3 border border-slate-6 rounded-lg focus:border-violet-8 focus:outline-none bg-white",
                         ),
                         class_name="mb-8 flex-1",
                     ),
                    # How did you hear about us
                    rx.box(
                        rx.text("How did you hear about us? *", class_name="text-slate-11 text-sm font-medium mb-2"),
                        rx.select(
                            ["Google Search", "Social Media", "Word of Mouth", "Blog", "Conference", "Other"],
                            name="referral_source",
                            placeholder="Google Search",
                            style={"width": "100%", "min-width": "100%"},
                            class_name="!w-full p-3 border border-slate-6 rounded-lg focus:border-violet-8 focus:outline-none bg-white",
                        ),
                        class_name="mb-8 flex-1",
                    ),
                    class_name="flex flex-row w-full items-center justify-between gap-x-2",
                    ),
                    # Submit button
                    button(
                        "Submit",
                        variant="primary",
                        type="submit",
                        size="lg",
                        class_name="w-full mb-2",
                    ),
                    class_name="w-full"
                ),
                class_name="bg-slate-1 p-6 sm:p-8 rounded-2xl border border-slate-4 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0",
            ),

            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 max-w-7xl mx-auto items-start",
        ),
        class_name="py-12 sm:py-20 px-4 sm:px-8 bg-white",
    )

def header() -> rx.Component:
    return rx.box(
        custom_quote_form(),
        rx.el.h1(
            "Get a custom quote",
            class_name="gradient-heading font-semibold text-3xl lg:text-5xl text-center",
        ),
        rx.el.p(
            "The complete platform for building and deploying your apps.",
            class_name="text-slate-9 text-md lg:text-xl font-semibold text-center",
        ),
        class_name="flex flex-col gap-2 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full pb-16 "
        + rx.cond(HostingBannerState.show_banner, "pt-[11rem]", "pt-[12rem]"),
    )
