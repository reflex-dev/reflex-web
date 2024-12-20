import reflex as rx

from .views.hero import hero
from .views.preview import preview
from .views.deploy_animation import deploy_animation
from .views.pricing_cards import pricing_cards
from .views.templates import templates
from .views.features import features
from pcweb.pages.index.views.companies import companies
from pcweb.components.icons.patterns import hosting_patterns
from pcweb.components.docpage.navbar import navbar
from pcweb.pages.index.views.get_started import get_started
from pcweb.pages.index.views.footer_index import footer_index
from pcweb.components.webpage.badge import badge
from pcweb.pages.index.index_colors import index_colors
from pcweb.meta.meta import hosting_meta_tags


@rx.page(route="/hosting", title="Reflex · Hosting", meta=hosting_meta_tags)
def hosting_landing() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        index_colors(),
        *hosting_patterns(),
        navbar(),
        rx.el.main(
            hero(),
            preview(),
            # companies(),
            deploy_animation(),
            features(),
            pricing_cards(),
            templates(),
            get_started(),
            class_name="flex flex-col w-full justify-center items-center",
        ),
        footer_index(),
        badge(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
