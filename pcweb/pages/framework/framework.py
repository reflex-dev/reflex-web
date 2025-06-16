import reflex as rx
from .views.hero import hero
from .views.companies import companies
from .demos.demos import demo_section
from .views.frontend_features import frontend_features
from .views.backend_features import backend_features
from .views.hosting_features import hosting_features
from pcweb.components.icons.patterns import index_patterns
from .views.stats import stats
from .views.os_newsletter import os_newsletter
from pcweb.meta.meta import meta_tags
from pcweb.templates.mainpage import mainpage


@mainpage(path="/open-source", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def framework() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        *index_patterns(),
        hero(),
        demo_section(),
        companies(),
        frontend_features(),
        backend_features(),
        hosting_features(),
        stats(),
        os_newsletter(),
        class_name="flex flex-col w-full justify-center items-center",
    )
