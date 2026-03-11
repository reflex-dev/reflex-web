import reflex as rx

from pcweb.components.marketing_button import button as marketing_button
from pcweb.pages.templates.templates_state import TemplatesState
from pcweb.pages.templates.views.templates_grid import template_card


def others():
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Related Templates",
                class_name="text-2xl font-[575] text-secondary-12",
            ),
            rx.el.a(
                marketing_button(
                    "Browse All",
                    variant="outline",
                    native_button=False,
                    size="sm",
                    class_name="w-fit",
                ),
                to="/templates",
                class_name="w-fit",
            ),
            class_name="flex flex-row gap-4 justify-between items-center",
        ),
        rx.el.div(
            rx.foreach(
                TemplatesState.related_templates, lambda t: template_card(template=t)
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-5",
        ),
        class_name="pr-16 py-16 flex flex-col gap-6 w-full",
    )
