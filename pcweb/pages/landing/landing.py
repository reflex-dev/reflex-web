import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.pages.landing.views.ai_bento import ai_bento
from pcweb.pages.landing.views.app_build import app_build
from pcweb.pages.landing.views.companies import companies
from pcweb.pages.landing.views.connect_section import connect_section
from pcweb.pages.landing.views.enterprise_social import enterprise_social
from pcweb.pages.landing.views.hero import hero
from pcweb.pages.landing.views.integrations import integrations
from pcweb.pages.landing.views.products import products
from pcweb.pages.landing.views.social_stats import social_stats
from pcweb.pages.landing.views.use_cases import use_cases_section
from pcweb.pages.landing.views.video import video
from pcweb.templates.mainpage import mainpage


@mainpage(path="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def landing() -> rx.Component:
    return rx.el.div(
        hero(),
        app_build(),
        social_stats(),
        products(),
        integrations(),
        video(),
        companies(),
        ai_bento(),
        connect_section(),
        enterprise_social(),
        use_cases_section(),
        class_name="flex flex-col size-full justify-center items-center",
    )
