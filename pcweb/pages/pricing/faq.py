import reflex as rx
from pcweb.components.button import button
from pcweb.constants import HOSTING_URL


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[-1] top-[-1.25rem] pointer-events-none w-[20rem] h-[5rem]",
        background_image=rx.color_mode_cond(
            "radial-gradient(50% 50% at 50% 50%, rgba(235, 228, 255, 0.661) 0%, rgba(252, 252, 253, 0.00) 100%) !important",
            "radial-gradient(50% 50% at 50% 50%, rgba(58, 45, 118, 0.207) 0%, rgba(21, 22, 24, 0.00) 100%) !important",
        ),
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
        class_name="flex items-center justify-between text-slate-11 flex-col pt-[5rem] pb-82xl:border-x border-slate-4",
    )


def sales_button() -> rx.Component:
    return rx.link(
        glow(),
        button(
            "Need more help? Contact sales",
            variant="secondary",
            class_name="!text-slate-11 !font-semibold !text-sm",
        ),
        href=HOSTING_URL,  # TODO: Change to sales page when we have it
        is_external=True,
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
        "How usage based billing is calculated?",
        "Usage is calculated based on compute resources (CPU/RAM) consumed by your app. We measure this in compute units per hour.",
    ),
    (
        "What is your privacy and security policy?",
        "We take security seriously. All apps are deployed with SSL certificates, DDoS protection, and web application firewall. Your code and data remain private and secure.",
    ),
    (
        "What happens when I upgrade?",
        "When you upgrade your plan, you'll immediately get access to the new features and increased resource limits. Your app will continue running without interruption.",
    ),
    (
        "How are prorations calculated?",
        "If you upgrade mid-billing cycle, we'll prorate the new charges for the remainder of the billing period. You'll only pay for what you use.",
    ),
    (
        "What happens if I cancel the plan?",
        "If you cancel, you'll maintain access until the end of your current billing period. After that, your app will be downgraded to the free tier limits.",
    ),
    (
        "How can I influence Reflex roadmap?",
        "We welcome feedback and feature requests from our community. You can submit ideas through GitHub issues or discuss them in our Discord community.",
    ),
    (
        "What determines the total amount billed?",
        "Your bill is determined by your base plan plus any usage-based charges for compute resources that exceed the plan limits.",
    ),
    (
        "How to cancel subscription?",
        "You can cancel your subscription anytime from your account dashboard. No long-term commitments required.",
    ),
    (
        "Can I add members to my project?",
        "Yes! Pro plan allows up to 5 team members, Team plan up to 25 members, and Enterprise plan has unlimited team members.",
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
