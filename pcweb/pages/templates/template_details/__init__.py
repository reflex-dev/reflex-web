import reflex as rx

from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.templates.template_details.views import (
    about,
    faq,
    header,
    others,
    sidebar,
    social,
)
from pcweb.pages.templates.templates_state import TemplatesState
from pcweb.templates.secondary_page import secondary_page


@secondary_page(
    path="/templates/[template_name]",
    title="Template Details",
    description="Template Details",
    image="/previews/index_preview.webp",
    on_load=TemplatesState.load_templates,
)
def template_details():
    return rx.el.div(
        rx.cond(
            TemplatesState.active_template,
            rx.el.div(
                rx.el.div(
                    header(),
                    rx.cond(TemplatesState.active_template.about, about()),
                    rx.cond(TemplatesState.active_template.social, social()),
                    rx.cond(TemplatesState.active_template.faq, faq()),
                    others(),
                    class_name="flex-1 flex flex-col divide-y divide-secondary-4 border-r border-secondary-4",
                ),
                sidebar(),
                class_name="flex flex-row w-full max-w-[108rem] mx-auto min-h-screen",
            ),
        ),
        footer_index(
            class_name="max-w-[109rem]", grid_class_name="w-fit [&>div]:min-w-[9rem]"
        ),
        class_name="flex flex-col w-full relative",
    )
