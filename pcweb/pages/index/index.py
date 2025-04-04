import reflex as rx
from .views.hero import hero
from .views.companies import companies
from .demos.demos import demo_section
from .views.frontend_features import frontend_features
from .views.backend_features import backend_features
from .views.hosting_features import hosting_features
from pcweb.components.icons.patterns import index_patterns
from .views.stats import stats
from pcweb.components.docpage.navbar import navbar
from .views.os_newsletter import os_newsletter
from .views.get_started import get_started
from .views.footer_index import footer_index
from pcweb.components.webpage.badge import badge
from .index_colors import index_colors
from pcweb.meta.meta import meta_tags


@rx.page(route="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        index_colors(),
        *index_patterns(),
        navbar(),
        rx.el.main(
            hero(),
            demo_section(),
            companies(),
            frontend_features(),
            backend_features(),
            hosting_features(),
            stats(),
            os_newsletter(),
            get_started(),
            class_name="flex flex-col w-full justify-center items-center",
        ),
        footer_index(),
        badge(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
