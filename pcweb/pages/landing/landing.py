import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.pages.landing.views.app_build import app_build
from pcweb.pages.landing.views.companies import companies
from pcweb.pages.landing.views.hero import hero
from pcweb.pages.landing.views.integrations import integrations
from pcweb.pages.landing.views.products import products
from pcweb.pages.landing.views.social_stats import social_stats
from pcweb.pages.landing.views.video import video
from pcweb.templates.mainpage import mainpage


@mainpage(path="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def landing() -> rx.Component:
    return rx.box(
        hero(),
        app_build(),
        social_stats(),
        products(),
        integrations(),
        video(),
        companies(),
        # ai_section(),
        # framework_section(),
        # hosting_section(),
        # outcomes_section(),
        # security(),
        class_name="flex flex-col size-full justify-center items-center",
    )
