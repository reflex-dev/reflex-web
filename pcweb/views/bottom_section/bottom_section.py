import reflex as rx

from pcweb.views.bottom_section.get_started import get_started
from pcweb.views.bottom_section.newsletter import newsletter


@rx.memo
def bottom_section() -> rx.Component:
    return rx.box(
        newsletter(),
        get_started(),
        class_name="flex flex-col items-center gap-20 lg:gap-32 pt-8 lg:pt-[6.5rem] w-[22rem] lg:w-[25rem]",
    )
