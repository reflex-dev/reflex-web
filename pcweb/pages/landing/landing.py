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
from pcweb.pages.landing.views.infra import stats, landing_infra
from pcweb.pages.landing.views.cloud import landing_animation
from pcweb.templates.mainpage import mainpage
from pcweb.pages.hosting.views.features import features
from pcweb.pages.landing.views.social_proof import landing_social_proof

@mainpage(path="/", title="Reflex · Web apps in Pure Python", meta=meta_tags)
def landing() -> rx.Component:
    return rx.box(
        hero(),
        products(),
        companies(),
        ai_section(),
        #
        framework_section(),
        #
        hosting_section(),
        #
        landing_infra(),
        stats(),
        #
        # outcomes_section(),
        # security(),
        #
        landing_animation(),
        features(),
        #
        landing_social_proof(),
        class_name="flex flex-col size-full justify-center items-center",
    )
