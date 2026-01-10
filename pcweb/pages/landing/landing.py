import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.pages.landing.views.ai_bento import ai_bento
from pcweb.pages.landing.views.app_build import app_build
from pcweb.pages.landing.views.companies import companies
from pcweb.pages.landing.views.connect_section import connect_section
from pcweb.pages.landing.views.deploy_section import deploy_section
from pcweb.pages.landing.views.enterprise_social import enterprise_social
from pcweb.pages.landing.views.final_cta import final_cta
from pcweb.pages.landing.views.hero import hero
from pcweb.pages.landing.views.integrations import integrations
from pcweb.pages.landing.views.os_bento import os_bento
from pcweb.pages.landing.views.os_stats import os_stats
from pcweb.pages.landing.views.products import products
from pcweb.pages.landing.views.social_marquee import social_marquee
from pcweb.pages.landing.views.social_stats import social_stats
from pcweb.pages.landing.views.use_cases import use_cases_section
from pcweb.pages.landing.views.video import video
from pcweb.templates.mainpage import mainpage


@mainpage(
    path="/",
    title="Reflex · The platform to build and scale enterprise apps",
    meta=meta_tags,
)
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
        social_marquee(),
        use_cases_section(),
        os_bento(),
        os_stats(),
        deploy_section(),
        final_cta(),
        class_name="flex flex-col size-full justify-center items-center max-w-[calc(100vw-2rem)] mx-auto",
    )
