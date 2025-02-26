import reflex as rx


@rx.memo
def h1_title(title: str) -> rx.Component:
    return rx.el.h1(
        title,
        class_name="gradient-heading font-x-large lg:font-xxx-large text-start text-transparent lg:text-center",
    )
