import reflex as rx

from pcweb.pages.templates.templates_state import TemplatesState


def social_card(social: rx.Var[dict[str, str]]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            social.get("text", ""),
            class_name="text-sm font-[525] text-secondary-12 mb-8",
        ),
        rx.el.p(
            social.get("name", "User"),
            class_name="text-sm text-secondary-12 font-[525] mb-2",
        ),
        rx.el.p(
            social.get("role", ""),
            class_name="text-sm text-secondary-11 font-[475]",
        ),
        class_name="flex flex-col bg-white-1 p-6 rounded-[0.625rem] border border-secondary-a4 shadow-small max-w-[25rem] w-full",
    )


def social():
    return rx.el.div(
        rx.el.h2(
            "What Users Say",
            class_name="text-2xl font-[575] text-secondary-12",
        ),
        rx.el.div(
            rx.foreach(TemplatesState.active_template.quotes, social_card),
            class_name="flex lg:flex-row flex-col gap-4",
        ),
        class_name="xl:pr-16 xl:py-16 py-6 flex flex-col gap-6 w-full",
    )
