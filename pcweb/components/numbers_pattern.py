import reflex as rx
import reflex_ui as ui


def ellipses(side: str = "left"):
    direction = "right" if side == "right" else "left"
    common_class = "absolute bg-violet-11 dark:bg-[#534a87] blur-[10px]"
    return rx.el.div(
        # Ellipse 1
        rx.el.div(
            class_name=f"w-[32px] h-[88px] {direction}-[0.5rem] {common_class} animate-ellipse-1"
        ),
        # Ellipse 2
        rx.el.div(
            class_name=f"w-[32px] h-[178px] {direction}-[9.5rem] {common_class} animate-ellipse-2"
        ),
        # Ellipse 3
        rx.el.div(
            class_name=f"w-[16px] h-[42px] {direction}-[4.19rem] {common_class} animate-ellipse-3"
        ),
        # Ellipse 4
        rx.el.div(
            class_name=f"w-[32px] h-[48px] {direction}-[0.44rem] {common_class} animate-ellipse-4"
        ),
    )


def ellipses_reversed(side: str = "left"):
    direction = "right" if side == "right" else "left"
    common_class = f"absolute bg-violet-11 dark:bg-[#534a87] blur-[10px] [animation-direction:reverse] {direction}"
    return rx.el.div(
        # Ellipse 1
        rx.el.div(
            class_name=f"w-[32px] h-[88px] {direction}-[0.5rem] {common_class} animate-ellipse-1"
        ),
        # Ellipse 2
        rx.el.div(
            class_name=f"w-[32px] h-[178px] {direction}-[9.5rem] {common_class} animate-ellipse-2"
        ),
        # Ellipse 3
        rx.el.div(
            class_name=f"w-[16px] h-[42px] {direction}-[4.19rem] {common_class} animate-ellipse-3"
        ),
        # Ellipse 4
        rx.el.div(
            class_name=f"w-[32px] h-[48px] {direction}-[0.44rem] {common_class} animate-ellipse-4"
        ),
    )


def numbers_pattern(
    side: str = "left", reversed: bool = False, class_name: str = ""
) -> rx.Component:
    """Numbers pattern with static background and masked animated ellipses."""
    position_class = "left-0" if side == "left" else "right-0"

    light_dark_path = rx.color_mode_cond("light", "dark")

    image_sources = {
        ("left", False): f"/landing/patterns/{light_dark_path}/numbers-img.webp",
        (
            "left",
            True,
        ): f"/landing/patterns/{light_dark_path}/numbers-reversed-img.webp",
        ("right", False): f"/landing/patterns/{light_dark_path}/numbers-right-img.webp",
        (
            "right",
            True,
        ): f"/landing/patterns/{light_dark_path}/numbers-right-reversed-img.webp",
    }
    src = image_sources.get(
        (side, reversed), f"/landing/patterns/{light_dark_path}/numbers-img.webp"
    )

    mask_style = {
        "mask_image": f"url({src})",
        "mask_size": "100% 100%",
        "mask_repeat": "no-repeat",
        "webkit_mask_image": f"url({src})",
        "webkit_mask_size": "100% 100%",
        "webkit_mask_repeat": "no-repeat",
    }

    return rx.el.div(
        rx.el.div(
            # Static background pattern (always visible)
            rx.image(src=src, class_name="pointer-events-none"),
            # Masked layer with ellipses
            rx.el.div(
                ellipses(side=side) if not reversed else ellipses_reversed(side=side),
                class_name="absolute inset-0 w-full h-full",
                style=mask_style,
            ),
            class_name="relative size-full",
        ),
        class_name=ui.cn(
            f"absolute {position_class} pointer-events-none overflow-hidden z-[-1] lg:w-[234px] w-[180px] h-auto",
            class_name,
        ),
    )
