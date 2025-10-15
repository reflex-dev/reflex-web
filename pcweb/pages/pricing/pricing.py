import reflex as rx

from pcweb.meta.meta import hosting_meta_tags
from pcweb.pages.framework.index_colors import index_colors
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.pricing.calculator import calculator_section
from pcweb.pages.pricing.faq import faq
from pcweb.pages.pricing.plan_cards import plan_cards
from pcweb.pages.pricing.slider_calculator import MachineState, slider_calculator
from pcweb.pages.pricing.table import tiers_tables

pricing_path = "/pricing"


@rx.page(
    route=pricing_path,
    title="Reflex · Pricing",
    meta=hosting_meta_tags,
    on_load=MachineState.reset_machines,
)
def pricing() -> rx.Component:
    """Get the Pricing landing page."""
    from pcweb.components.docpage.navbar import navbar

    return rx.box(
        index_colors(),
        navbar(),
        rx.el.main(
            rx.box(
                plan_cards(),
                tiers_tables(),
                slider_calculator(),
                calculator_section(),
                faq(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        footer_index(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative",
    )
