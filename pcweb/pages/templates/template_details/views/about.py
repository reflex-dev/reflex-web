import reflex as rx

from pcweb.pages.templates.templates_state import TemplatesState


def about():
    return rx.el.div(
        rx.el.h2(
            "About This Template",
            class_name="text-2xl font-[575] text-secondary-12",
        ),
        rx.el.p(
            TemplatesState.active_template.about,
            class_name="text-sm text-secondary-11 font-[475]",
        ),
        class_name="pr-16 py-16 flex flex-col gap-6 w-full",
    )
