import reflex as rx
from typing import Literal, Callable

LiteralButtonVariant = Literal["primary", "success", "destructive", "secondary", "muted"]

default_button_style = {
    # "input:placeholder-shown + &": {
    #     "opacity": "0.80",
    #     "cursor": "not-allowed",
    #     "_hover": {
    #         "background": "linear-gradient(180deg, var(--c-violet-9) 0%, var(--c-violet-10) 100%)"
    #     },
    # },
}

default_class_name = "rounded-full w-8 h-8 inline-flex items-center justify-center cursor-pointer relative border-t border-[rgba(255,255,255,0.21)] shrink-0"
after_class_name = "after:absolute after:inset-[1px] after:border-t after:rounded-[11px] after:border-white after:opacity-[0.22]"


def get_variant_class(variant: str) -> str:
    return (
        f"bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-9] hover:to-[--{variant}-10] text-white"
        + " "
        # + after_class_name
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
    onclick: Callable = None,
    style: dict = {},
    class_name: str = "",
    *children,
    **props,
) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=16, class_name="shrink-0"),
        onclick=onclick,
        style=default_button_style | style,
        class_name=default_class_name
        + " "
        + variant_styles[variant]["class_name"]
        + " "
        + class_name,
        *children,
        **props,
    )
