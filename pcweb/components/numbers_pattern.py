import reflex as rx
import reflex_ui as ui


def _ellipses(side: str, reverse_animation: bool = False) -> rx.Component:
    """Create animated ellipses for the pattern effect."""
    direction = "right" if side == "right" else "left"
    animation_class = "[animation-direction:reverse]" if reverse_animation else ""
    common_class = (
        f"absolute bg-violet-11 dark:bg-[#534a87] blur-[10px] {animation_class}"
    )

    return rx.el.div(
        rx.el.div(
            class_name=f"w-[32px] h-[88px] {direction}-[0.5rem] {common_class} animate-ellipse-1"
        ),
        rx.el.div(
            class_name=f"w-[32px] h-[178px] {direction}-[9.5rem] {common_class} animate-ellipse-2"
        ),
        rx.el.div(
            class_name=f"w-[16px] h-[42px] {direction}-[4.19rem] {common_class} animate-ellipse-3"
        ),
        rx.el.div(
            class_name=f"w-[32px] h-[48px] {direction}-[0.44rem] {common_class} animate-ellipse-4"
        ),
    )


def numbers_pattern(
    side: str = "left", reverse: bool = False, class_name: str = ""
) -> rx.Component:
    """Numbers pattern with static background and masked animated ellipses.

    Matches Figma design structure with layered gradients.

    Args:
        side: Position side ("left" or "right")
        reverse: Reverse the ellipse animation direction
        class_name: Additional CSS classes
    """
    position_class = "left-0" if side == "left" else "right-0"
    light_dark_path = rx.color_mode_cond("light", "dark")

    src = f"landing/patterns/{light_dark_path}/numbers-pattern.webp"

    # Determine if we need to flip: right side XOR reverse
    # - right side normally flips
    # - reverse inverts the flip behavior
    is_flipped = (side == "right") != reverse

    # Background image style
    image_style = {"opacity": rx.color_mode_cond("1", "0.3")}
    if is_flipped:
        image_style |= {"transform": "scaleX(-1)"}

    # Gradient masks
    vertical_gradient = "linear-gradient(360deg, rgba(0, 0, 0, 0) 0%, #000000 12%, #000000 88%, rgba(0, 0, 0, 0) 100%)"
    # Angled gradient - angle changes based on reverse
    gradient_angle = "105deg" if reverse else "280deg"
    angled_gradient = f"linear-gradient({gradient_angle}, rgba(0, 0, 0, 0) 18.13%, rgba(0, 0, 0, 0.88) 66.72%, rgba(0, 0, 0, 0) 85.62%)"

    # Container mask combining both gradients
    container_mask_style = {
        "mask_image": f"{angled_gradient}, {vertical_gradient}",
        "webkit_mask_image": f"{angled_gradient}, {vertical_gradient}",
        "mask_composite": "intersect",
        "webkit_mask_composite": "intersect",
    }
    if is_flipped:
        container_mask_style["transform"] = "scaleX(-1)"

    # Image mask style for the ellipses layer
    ellipses_mask_style = {
        "mask_image": f"url({src})",
        "mask_size": "cover",
        "mask_repeat": "no-repeat",
        "mask_position": "center",
        "webkit_mask_image": f"url({src})",
        "webkit_mask_size": "cover",
        "webkit_mask_repeat": "no-repeat",
        "webkit_mask_position": "center",
    }
    if is_flipped:
        ellipses_mask_style["transform"] = "scaleX(-1)"

    return rx.el.div(
        # Layer 1: Background pattern image
        rx.image(
            src=src,
            class_name="pointer-events-none w-full h-full absolute inset-0 object-cover",
            style=image_style,
        ),
        # Layer 2: Masked animated ellipses
        rx.el.div(
            _ellipses(side=side, reverse_animation=reverse),
            class_name="absolute inset-0 w-full h-full",
            style=ellipses_mask_style,
        ),
        class_name=ui.cn(
            f"absolute {position_class} pointer-events-none z-[-1] lg:w-[234px] w-[180px] h-full bottom-0",
            class_name,
        ),
        style=container_mask_style,
    )
