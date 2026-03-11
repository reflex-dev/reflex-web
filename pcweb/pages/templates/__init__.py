import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.templates.templates_state import TemplatesState
from pcweb.pages.templates.views import templates_grid, templates_sidebar
from pcweb.templates.secondary_page import secondary_page


@secondary_page(
    path="/templates",
    title="Reflex Templates - Python Dashboards & Tools",
    description="Reflex templates: dashboards, chatbots, data tools, and AI apps. Start from a template and customize in Python.",
    meta=create_meta_tags(
        title="Reflex Templates - Python Dashboards & Tools",
        description="Reflex templates: dashboards, chatbots, data tools, and AI apps. Start from a template and customize in Python.",
        image="/previews/index_preview.webp",
    ),
    on_load=TemplatesState.load_templates,
)
def templates_landing() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            templates_sidebar(),
            rx.el.div(
                templates_grid(),
                footer_index(
                    class_name="max-w-[109rem]",
                    grid_class_name="w-fit [&>div]:min-w-[9rem]",
                ),
                class_name="flex flex-col flex-1 min-w-0",
            ),
            class_name="flex flex-row w-full max-w-[108rem] mx-auto min-h-screen",
        ),
        class_name="flex flex-col w-full relative overflow-x-clip",
    )
