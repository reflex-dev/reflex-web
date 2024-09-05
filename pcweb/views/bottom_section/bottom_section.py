import reflex as rx
from pcweb.views.bottom_section.newsletter import newsletter
from pcweb.views.bottom_section.get_started import get_started


@rx.memo
def bottom_section() -> rx.Component:
    return rx.box(
        newsletter(),
        get_started(),
        class_name="flex flex-col items-center gap-32 pt-[6.5rem] pb-32 w-[22rem] lg:w-[25rem]",
    )
