import reflex as rx
from reflex_ui.blocks.demo_form import demo_form_dialog

from pcweb.components.button import button


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[-1] top-[-1.25rem] pointer-events-none w-[20rem] h-[5rem] dark:[background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(58,45,118,0.207)_0%,_rgba(21,22,24,0.00)_100%)] [background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(235,228,255,0.661)_0%,_rgba(252,252,253,0.00)_100%)]",
    )


def header() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Have questions?",
            class_name="text-slate-12 text-3xl font-semibold",
        ),
        rx.el.p(
            "Check FAQ",
            class_name="text-slate-9 text-3xl font-semibold",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col pt-[5rem]",
    )


def sales_button() -> rx.Component:
    return rx.el.div(
        demo_form_dialog(
            rx.el.div(
                glow(),
                button(
                    "Need more help? Contact sales",
                    variant="secondary",
                    class_name="!text-slate-11 !font-semibold !text-sm w-fit",
                ),
            ),
        ),
        class_name="self-center relative",
    )


def accordion(title: str, content: rx.Component) -> rx.Component:
    """The accordion component.

    Args:
        title (str): The title of the accordion.
        content (rx.Component): The content of the accordion.

    Returns:
        The accordion component.

    """
    return rx.accordion.root(
        rx.accordion.item(
            rx.accordion.trigger(
                rx.el.h3(
                    title, class_name="font-semibold text-base text-slate-12 text-start"
                ),
                rx.icon(
                    tag="plus",
                    size=16,
                    class_name="!text-slate-9 group-data-[state=open]:rotate-45 transition-transform",
                ),
                class_name="hover:!bg-transparent !p-[0.5rem_0rem] !justify-between gap-4 group",
            ),
            rx.accordion.content(
                content,
                class_name="before:!h-0 after:!h-0 radix-state-open:animate-accordion-down radix-state-closed:animate-accordion-up transition-all !px-0",
            ),
        ),
        collapsible=True,
        class_name="!p-0 w-full overflow-hidden !bg-slate-1 !rounded-none !shadow-none",
    )


def accordion_text(text: str) -> rx.Component:
    return rx.el.p(text, class_name="text-slate-9 text-sm font-medium")


faq_items = [
    (
        "Can I use Reflex for free?",
        "Yes! Reflex is open source and free to use. You can self-host your apps or use our hosting platform which has a generous free tier.",
    ),
    (
        "What is the difference between Reflex and Reflex Cloud?",
        "Reflex is our open-source framework for building web apps. Reflex Cloud is our platform for hosting Reflex apps.",
    ),
    (
        "Why was I charged $1 after adding a credit card?",
        "A $1 USD transaction is performed as a credit security check to ensure your card details are correct and authorized. The charge is refunded after the transaction completes.",
    ),
    (
        "How usage based billing is calculated?",
        "Usage is calculated based on compute resources (CPU/RAM) consumed by your app. We measure this in compute units per minute.",
    ),
    (
        "What happens when I upgrade?",
        "When you upgrade your plan, you'll immediately get access to the new features and increased resource limits. Your app will continue running without interruption.",
    ),
    (
        "What are credits?",
        "Credits can be used for both hosting and building. In hosting, credits are used for compute resources. In building, credits are consumed per message sent.",
    ),
    (
        "If I upgrade my tier, do I get the extra credits immediately?",
        "Yes! When you upgrade your tier (for example, from Tier 25 to Tier 50), the additional credits (e.g., 1,000) are added to your balance right away, and you're charged the corresponding amount for the higher plan.",
    ),
    (
        "Do credits ever expire?",
        "Credits only reset if you're on the Free tier. As long as you maintain any Pro subscription, your credits will continue to roll over each month.",
    ),
    (
        "What happens if I cancel the plan?",
        "If you cancel, you'll maintain access until the end of your current billing period. After that, your app will be downgraded to the free tier limits.",
    ),
    (
        "How to cancel subscription?",
        "You can cancel your subscription anytime from your account dashboard. No long-term commitments required.",
    ),
    (
        "Can I add members to my project?",
        "Yes! You can add unlimited members to your project on the Enterprise tier with a per seat monthly charge on additional seats.",
    ),
]


def faq() -> rx.Component:
    return rx.el.section(
        header(),
        rx.box(
            *[
                accordion(title, accordion_text(content))
                for title, content in faq_items
            ],
            class_name="max-w-[40rem] flex justify-center items-center flex-col mx-auto w-full gap-2",
        ),
        sales_button(),
        class_name="flex flex-col gap-8 w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem]",
    )
