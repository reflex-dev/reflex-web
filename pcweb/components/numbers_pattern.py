import reflex as rx
import reflex_ui as ui


def numbers_pattern(
    side: str = "left", reversed: bool = False, class_name: str = ""
) -> rx.Component:
    position_class = "left-0" if side == "left" else "right-0"

    image_sources = {
        ("left", False): "/landing/patterns/light/numbers.svg",
        ("left", True): "/landing/patterns/light/numbers-reversed.svg",
        (
            "right",
            False,
        ): "/landing/patterns/light/numbers-right.svg",
        (
            "right",
            True,
        ): "/landing/patterns/light/numbers-right-reversed.svg",
    }
    src = image_sources.get((side, reversed), "/landing/patterns/light/numbers.svg")

    return rx.el.div(
        rx.image(
            src=src,
            class_name="pointer-events-none",
        ),
        class_name=ui.cn(
            f"absolute {position_class} pointer-events-none overflow-hidden z-[-1]",
            class_name,
        ),
    )
