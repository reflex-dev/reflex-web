import reflex as rx
from pcweb.components.hosting_banner import HostingBannerState
from pcweb.pages.framework.views.companies import pricing_page_companies
from pcweb.components.new_button import button
from typing import Literal

from reflex.event import EventType

# Import your custom select components
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
    "sm": "text-sm px-2 h-8 rounded-lg gap-2",
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
        "inline-flex transition-bg shrink-0 items-center w-full cursor-pointer disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 outline-none focus:outline-none",
        "bg-transparent text-slate-9 font-medium hover:bg-slate-3 font-sans",
        SIZE_STYLES[size],
    ]

    common_props = {
        "class_name": " ".join(filter(None, base_classes)),
        "type": "button",
        "on_click": on_click_event,
        **props,
    }

    return rx.el.button(text, **common_props)

def select(
    content: rx.Component,
    variant: SelectVariant = "primary",
    size: SelectSize = "sm",
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
            class_name="items-center bg-transparent !shadow-none !p-0 border-none overflow-visible font-sans pointer-events-auto",
        ),
        **props,
    )

class QuoteFormState(rx.State):
    """State management for the quote form."""
    num_employees: str = "500+"
    referral_source: str = "Google Search"

    def set_select_value(self, field: str, value: str):
        """Update the selected value for a given field."""
        setattr(self, field, value)

def quote_input(placeholder: str, name: str, **props):
    return rx.el.input(
        placeholder=placeholder,
        name=name,
        class_name="box-border w-full border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
        **props,
    )

def form_field(label: str, input_component, required: bool = False, class_name: str = "mb-6"):
    """Reusable form field component with label and input."""
    label_text = f"{label} {'*' if required else ''}"
    return rx.box(
        rx.text(label_text, class_name="text-slate-11 text-sm font-medium mb-2"),
        input_component,
        class_name=class_name,
    )

def text_input_field(label: str, name: str, placeholder: str, required: bool = False, input_type: str = "text", class_name: str = "mb-6"):
    """Helper for creating text input fields."""
    input_component = quote_input(
        name=name,
        placeholder=placeholder,
        type=input_type,
        required=required,
    )
    return form_field(label, input_component, required, class_name)

def select_field(label: str, name: str, options: list, placeholder: str, required: bool = False, state_var: str = ""):
    """Helper for creating custom select fields."""
    # Create scroll area with selectable options
    scroll_content = rx.scroll_area(
        *[
            select_item(
                content=(option, lambda opt=option, var=state_var: QuoteFormState.set_select_value(var, opt)),
                size="md",
                class_name="w-full justify-start px-4 py-2 hover:bg-slate-2 rounded-md",
            )
            for option in options
        ],
        class_name="max-h-48 bg-slate-1 border border-slate-5 rounded-lg shadow-lg",
    )

    # Get the current selected value for this field
    current_value = getattr(QuoteFormState, state_var, placeholder)

    select_component = select(
        content=scroll_content,
        placeholder=current_value,
        variant="primary",
        size="md",
        class_name="w-full",
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

def custom_quote_form() -> rx.Component:
    """Custom quote form component with clean, maintainable structure."""
    return rx.box(
        rx.box(
            # Left column - Content
            rx.box(
                rx.el.h2(
                    "Request Your Custom Quote",
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
                        text_input_field("First name", "first_name", "John", required=True, class_name="mb-0"),
                        text_input_field("Last name", "last_name", "Smith", required=True, class_name="mb-0"),
                        class_name="flex-row flex gap-x-2 mb-6",
                    ),

                    text_input_field("Business email", "business_email", "john@reflex.dev", required=True, input_type="email"),

                    rx.el.div(
                        text_input_field("Job title", "job_title", "CTO", required=True, class_name="mb-0"),
                        text_input_field("Company name", "company_name", "Pynecone, Inc.", required=True, class_name="mb-0"),
                        class_name="flex-row flex gap-x-2 mb-6",
                    ),

                    text_input_field("Phone number", "phone_number", "(555) 123-4567", required=True, input_type="tel"),

                    # Project Details
                    textarea_field("What internal tools are you looking to build?", "internal_tools", "Customer service admin panel", required=True),

                    # Company Size and Referral
                    select_field("Number of employees", "num_employees", ["1-10", "11-50", "51-100", "101-500", "500+"], "500+", required=True, state_var="num_employees"),
                    select_field("How did you hear about us?", "referral_source", ["Google Search", "Social Media", "Word of Mouth", "Blog", "Conference", "Other"], "Google Search", required=True, state_var="referral_source"),

                    # Submit button
                    button(
                        "Submit",
                        variant="primary",
                        type="submit",
                        size="lg",
                        class_name="w-full mt-2",
                    ),
                    class_name="w-full space-y-6",
                ),
                rx.box(
                    "1 Month Free Trial",
                    class_name="absolute top-[-0.75rem] left-8 rounded-md bg-[--violet-9] h-[1.5rem] text-sm font-medium text-center px-2 flex items-center justify-center text-[#FCFCFD] z-[10]",
                ),
                class_name="relative bg-slate-1 p-6 sm:p-8 rounded-2xl border-2 border-[--violet-9] shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 max-w-7xl mx-auto items-start",
        ),
        class_name="py-12 sm:py-20 px-4 sm:px-8",
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
