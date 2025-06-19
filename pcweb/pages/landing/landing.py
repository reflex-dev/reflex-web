import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.pages.landing.views.ai_section import ai_section
from pcweb.pages.landing.views.companies import companies
from pcweb.pages.landing.views.framework_section import framework_section
from pcweb.pages.landing.views.hero import hero
from pcweb.pages.landing.views.hosting_section import hosting_section
from pcweb.pages.landing.views.outcomes_section import outcomes_section
from pcweb.pages.landing.views.products import products
from pcweb.pages.landing.views.security import security
from pcweb.pages.landing.views.start_building import start_building
from pcweb.pages.landing.views.video_demo import video_demo
from pcweb.templates.mainpage import mainpage


@mainpage(path="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def landing() -> rx.Component:
    return rx.box(
        hero(),
        # video_demo(),
        products(),
        companies(),
        ai_section(),
        framework_section(),
        hosting_section(),
        outcomes_section(),
        security(),
        start_building(),
        class_name="flex flex-col size-full justify-center items-center",
    )
