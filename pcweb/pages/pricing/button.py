from typing import Any, Dict, Literal, Optional

import reflex as rx

LiteralButtonVariant = Literal[
    "primary", "secondary", "transparent", "destructive", "outline"
]
LiteralButtonSize = Literal["sm", "md", "lg", "icon-sm", "icon-md", "icon-lg"]

DEFAULT_CLASS_NAME = "text-sm cursor-pointer inline-flex items-center justify-center relative transition-bg shrink-0 font-sans disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 transition-bg"


def get_variant_bg_cn(variant: str) -> str:
    """Get the background color class name for a button variant.

    Args:
        variant (str): The variant of the button.

    Returns:
        str: The background color class name.

    """
    return f"enabled:bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-10] hover:to-[--{variant}-9] disabled:hover:bg-[--{variant}-9]"


BUTTON_STYLES: Dict[str, Dict[str, Dict[str, str]]] = {
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
        "primary": lambda: f"{get_variant_bg_cn('violet')} text-[#FCFCFD] font-semibold",
        "secondary": "bg-slate-4 hover:bg-slate-5 text-slate-11 font-semibold",
        "transparent": "bg-transparent hover:bg-slate-3 text-slate-9 font-medium",
        "destructive": lambda: f"{get_variant_bg_cn('red')} text-[#FCFCFD] font-semibold",
        "outline": "bg-slate-1 hover:bg-slate-3 text-slate-9 font-medium border border-slate-5",
    },
}


def button(
    text: str = "",
    variant: LiteralButtonVariant = "primary",
    size: LiteralButtonSize = "sm",
    style: Dict[str, Any] | None = None,
    class_name: str = "",
    icon: Optional[rx.Component] = None,
    **props,
) -> rx.Component:
    """Create a button component.

    Args:
        text (str): The text to display on the button.
        variant (LiteralButtonVariant, optional): The button variant. Defaults to "primary".
        size (LiteralButtonSize, optional): The button size. Defaults to "sm".
        style (Dict[str, Any], optional): Additional styles to apply to the button. Defaults to {}.
        class_name (str, optional): Additional CSS classes to apply to the button. Defaults to "".
        icon (Optional[rx.Component], optional): An optional icon component to display before the text. Defaults to None.
        **props: Additional props to pass to the button element.

    Returns:
        rx.Component: A button component with the specified properties.

    """
    if style is None:
        style = {}
    variant_class = BUTTON_STYLES["variant"][variant]
    variant_class = variant_class() if callable(variant_class) else variant_class

    classes = [
        DEFAULT_CLASS_NAME,
        BUTTON_STYLES["size"][size],
        variant_class,
        class_name,
    ]

    content = [icon, text] if icon else [text]

    return rx.el.button(
        *content,
        style=style,
        class_name=" ".join(filter(None, classes)),
        **props,
    )
