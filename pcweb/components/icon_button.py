from typing import Callable, Literal

import reflex as rx

LiteralButtonVariant = Literal[
    "primary", "success", "destructive", "secondary", "muted"
]

default_class_name = "rounded-full w-8 h-8 inline-flex items-center justify-center cursor-pointer relative border-t border-[rgba(255,255,255,0.21)] shrink-0"
after_class_name = "after:absolute after:inset-[1px] after:border-t after:rounded-[11px] after:border-white after:opacity-[0.22]"


def get_variant_class(variant: str) -> str:
    return (
        f"bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-9] hover:to-[--{variant}-10] text-white"
        + " "
    )


variant_styles = {
    "primary": {
        "class_name": get_variant_class("violet"),
    },
    "success": {
        "class_name": get_variant_class("green"),
    },
    "destructive": {
        "class_name": get_variant_class("red"),
    },
    "muted": {
        "class_name": "bg-slate-3 hover:bg-slate-6 text-slate-9 border-t !border-slate-5",
    },
    "secondary": {
        "class_name": "bg-slate-4 hover:bg-slate-6 text-slate-10 !border-none",
    },
}


def icon_button(
    icon: str,
    variant: LiteralButtonVariant = "primary",
    onclick: Callable | None = None,
    style: dict | None = None,
    class_name: str = "",
    *children,
    **props,
) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=16, class_name="shrink-0"),
        *children,
        onclick=onclick,
        style=style if style is not None else {},
        class_name=default_class_name
        + " "
        + variant_styles[variant]["class_name"]
        + " "
        + class_name,
        **props,
    )
