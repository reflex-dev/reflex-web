from typing import Dict, Literal

import reflex as rx

"""Tailwind CSS class merging utility."""

from reflex import ImportVar
from reflex.vars import FunctionVar, Var
from reflex.vars.base import VarData


def cn(class_1: Var | str, class_2: Var | str = "") -> Var:
    """Merge Tailwind CSS classes.

    Args:
        class_1: First class string or Var
        class_2: Second class string or Var (optional)

    Returns:
        Var: A Var with merged classes

    Examples:
        >>> cn("bg-red-500", rx.cond(State.is_active, "bg-blue-500", "bg-red-500"))
        >>> cn("bg-red-500", "text-white bg-blue-500")
        >>> cn("base-class")

    """
    return (
        Var(
            "cn",
            _var_data=VarData(imports={"clsx-for-tailwind": ImportVar(tag="cn")}),
        )
        .to(FunctionVar)
        .call(class_1, class_2)
    )


LiteralButtonVariant = Literal[
    "primary", "secondary", "transparent", "destructive", "outline"
]
LiteralButtonSize = Literal[
    "xs", "sm", "md", "lg", "icon-xs", "icon-sm", "icon-md", "icon-lg"
]

DEFAULT_CLASS_NAME = "text-sm cursor-pointer inline-flex items-center justify-center relative transition-bg shrink-0 font-sans disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 transition-bg outline-none peer-placeholder-shown:!bg-slate-3 peer-placeholder-shown:!bg-none peer-placeholder-shown:cursor-not-allowed peer-placeholder-shown:border peer-placeholder-shown:border-slate-5 peer-placeholder-shown:!text-slate-8 text-nowrap"


def get_variant_bg_cn(variant: str) -> str:
    """Get the background color class name for a button variant.

    Args:
        variant (str): The variant of the button.

    Returns:
        str: The background color class name.

    """
    return f"enabled:bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-10] dark:to-[--{variant}-9] hover:to-[--{variant}-9] dark:hover:to-[--{variant}-10] disabled:hover:bg-[--{variant}-9]"


BUTTON_STYLES: Dict[str, Dict[str, str]] = {
    "size": {
        "xs": "px-1.5 h-7 rounded-md gap-1.5",
        "sm": "px-2 h-8 rounded-lg gap-2",
        "md": "px-2.5 h-9 rounded-[10px] gap-2.5",
        "lg": "px-3 h-10 rounded-xl gap-3",
        "icon-xs": "size-7 rounded-md",
        "icon-sm": "size-8 rounded-lg",
        "icon-md": "size-9 rounded-[10px]",
        "icon-lg": "size-10 rounded-md",
    },
    "variant": {
        "primary": f"{get_variant_bg_cn('violet')} text-[#FCFCFD] font-semibold",
        "secondary": "bg-slate-4 hover:bg-slate-5 text-slate-11 font-semibold",
        "transparent": "bg-transparent hover:bg-slate-3 text-slate-9 font-medium",
        "destructive": f"{get_variant_bg_cn('red')} text-[#FCFCFD] font-semibold",
        "outline": "bg-slate-1 hover:bg-slate-3 text-slate-9 font-medium border border-slate-5",
    },
}


def resources_button(
    *children: rx.Component | str | rx.Var,
    variant: LiteralButtonVariant = "primary",
    size: LiteralButtonSize = "sm",
    class_name: str | rx.Var[str] = "",
    **props,
) -> rx.Component:
    """Create a button component.

    Args:
        variant (LiteralButtonVariant, optional): The button variant. Defaults to "primary".
        size (LiteralButtonSize, optional): The button size. Defaults to "sm".
        class_name (str, optional): Additional CSS classes to apply to the button. Defaults to "".
        **props: Additional props to pass to the button element.

    Returns:
        rx.Component: A button component with the specified properties.

    """
    # Validate size and variant
    if size not in BUTTON_STYLES["size"]:
        raise ValueError(
            f"Invalid size: {size}. Must be one of {list(BUTTON_STYLES['size'].keys())}"
        )
    if variant not in BUTTON_STYLES["variant"]:
        raise ValueError(
            f"Invalid variant: {variant}. Must be one of {list(BUTTON_STYLES['variant'].keys())}"
        )
    variant_class = BUTTON_STYLES["variant"][variant]
    # variant_class = variant_class() if callable(variant_class) else variant_class

    internal_classes = [
        DEFAULT_CLASS_NAME,
        BUTTON_STYLES["size"][size],
        variant_class,
    ]

    return rx.el.button(
        *children,
        class_name=cn(internal_classes, class_name),
        **props,
    )
