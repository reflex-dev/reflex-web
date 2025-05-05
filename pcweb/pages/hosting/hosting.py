import reflex as rx

from .views.hero import hero
from .views.preview import preview
from .views.deploy_animation import deploy_animation
from .views.pricing_cards import pricing_cards
from .views.templates import templates
from .views.features import features
from pcweb.components.icons.patterns import hosting_patterns
from pcweb.meta.meta import hosting_meta_tags
from pcweb.templates.mainpage import mainpage


@mainpage(path="/hosting", title="Reflex · Hosting", meta=hosting_meta_tags)
def hosting_landing() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        *hosting_patterns(),
        hero(),
        preview(),
        deploy_animation(),
        features(),
        pricing_cards(),
        templates(),
        class_name="flex flex-col size-full justify-center items-center",
    )
