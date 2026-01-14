import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.pages.use_cases.consulting.views.faq import faq
from pcweb.pages.use_cases.consulting.views.features_1 import features_1
from pcweb.pages.use_cases.consulting.views.features_2 import features_2
from pcweb.pages.use_cases.consulting.views.final_section import final_section
from pcweb.pages.use_cases.consulting.views.hero import hero
from pcweb.pages.use_cases.consulting.views.social_proof import social_proof
from pcweb.pages.use_cases.consulting.views.stats import stats
from pcweb.pages.use_cases.consulting.views.text_section_1 import text_section_1
from pcweb.pages.use_cases.consulting.views.text_section_3 import text_section_3
from pcweb.pages.use_cases.consulting.views.text_section_4 import text_section_4
from pcweb.templates.mainpage import mainpage


@mainpage(
    path="/use-cases/consulting", title="Consulting Use Case - Reflex", meta=meta_tags
)
def consulting_use_case_page() -> rx.Component:
    return rx.el.div(
        hero(),
        social_proof(),
        text_section_3(),
        features_2(),
        text_section_1(),
        features_1(),
        text_section_4(),
        stats(),
        faq(),
        final_section(),
        class_name="flex flex-col size-full justify-center items-center max-w-[calc(100vw-2rem)] mx-auto",
    )
