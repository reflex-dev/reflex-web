from typing import Literal

import reflex as rx


class ProgressiveBlur(rx.Component):
    """ProgressiveBlur component."""

    library = "progressive-blur"
    tag = "LinearBlur"

    steps: rx.Var[int] = rx.Var.create(8)
    strength: rx.Var[int] = rx.Var.create(64)
    falloff_percentage: rx.Var[int] = rx.Var.create(100)
    tint: rx.Var[str] = rx.Var.create("")
    side: rx.Var[Literal["top", "bottom", "left", "right"]] = rx.Var.create("bottom")


progressive_blur = ProgressiveBlur.create
