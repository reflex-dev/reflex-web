import reflex as rx
from pcweb.templates.mainpage import mainpage
from pcweb.pages.landing.views.hero import hero
from pcweb.pages.landing.views.products import products
from pcweb.pages.landing.views.ai_section import ai_section
from pcweb.pages.landing.views.framework_section import framework_section
from pcweb.pages.landing.views.hosting_section import hosting_section
from pcweb.pages.index.views.stats import stats
from pcweb.pages.index.views.os_newsletter import os_newsletter
from pcweb.pages.landing.views.start_building import start_building
from pcweb.pages.landing.views.companies import companies
from pcweb.components.icons.patterns import landing_patterns
from pcweb.meta.meta import meta_tags


@mainpage(path="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def landing() -> rx.Component:
    return rx.box(
        *landing_patterns(),
        hero(),
        products(),
        companies(),
        ai_section(),
        framework_section(),
        hosting_section(),
        start_building(),
        stats(),
        os_newsletter(),
        class_name="flex flex-col size-full justify-center items-center",
    )
