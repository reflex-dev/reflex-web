import reflex as rx

from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.templates.template_details.views import (
    about,
    faq,
    header,
    others,
    sidebar,
    sidebar_mobile,
    social,
)
from pcweb.pages.templates.templates_state import TemplatesState
from pcweb.templates.secondary_page import secondary_page


@secondary_page(
    path="/templates/[template_id]",
    title="Template Details",
    description="Template Details",
    image="/previews/index_preview.webp",
    on_load=TemplatesState.load_template_details,
)
def template_details():
    return rx.el.div(
        rx.cond(
            TemplatesState.faq_jsonld,
            rx.el.script(TemplatesState.faq_jsonld, type="application/ld+json"),
        ),
        rx.cond(
            TemplatesState.active_template,
            rx.el.div(
                rx.el.div(
                    header(),
                    sidebar_mobile(),
                    rx.cond(TemplatesState.active_template.about, about()),
                    rx.cond(TemplatesState.active_template.quotes, social()),
                    rx.cond(TemplatesState.active_template.faq, faq()),
                    others(),
                    class_name="flex-1 flex flex-col divide-y divide-secondary-4 xl:border-r border-secondary-4 max-xl:px-4",
                ),
                sidebar(),
                class_name="flex flex-row w-full max-w-[108rem] mx-auto min-h-screen",
            ),
        ),
        rx.el.hr(
            class_name="h-[1px] w-full bg-m-slate-4 dark:bg-m-slate-10",
        ),
        footer_index(
            class_name="max-w-[109rem]",
            grid_class_name="w-fit [&>div]:min-w-[9rem]",
        ),
        class_name="flex flex-col w-full relative",
    )
