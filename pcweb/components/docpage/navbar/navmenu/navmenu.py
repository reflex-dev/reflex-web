"""Reflex custom component NavMenu."""

import reflex as rx

from reflex.style import Style
from pcweb.styles.shadows import shadows
from pcweb.styles.colors import c_color

from typing import Any, Dict, List, Literal, Optional, Union
from reflex.vars import Var


LiteralMenuComponentDir = Literal["ltr", "rtl"]
LiteralMenuComponentOrientation = Literal["vertical", "horizontal"]


class NavMenu(rx.Component):
    """NavMenu component."""

    library = "@radix-ui/react-navigation-menu@^1.2.0"


class NavMenuRoot(NavMenu):
    """Navigation menu root component"""

    tag = "Root"
    alias = "RadixNavigationMenuRoot"

    value: Var[str]
    default_value: Var[str]
    delay_duration: Var[int] = 200
    skip_delay_duration: Var[int] = 300
    orientation: Var[LiteralMenuComponentOrientation] = "horizontal"
    dir: Var[LiteralMenuComponentDir]

    class_name: Var[str] = (
        "relative flex w-full items-center h-full justify-between gap-6 mx-auto z-[9999] flex-row max-w-[94.5rem]"
    )

    def get_event_triggers(self) -> Dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_value_change": lambda e0: [e0],
        }


class NavMenuSub(NavMenu):
    """Navigation menu sub component"""

    tag = "Sub"
    alias = "RadixNavigationMenuSub"

    value: Var[str]
    default_value: Var[str]
    orientation: Var[LiteralMenuComponentOrientation] = "horizontal"

    def get_event_triggers(self) -> Dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_value_change": lambda e0: [e0],
        }


class NavMenuList(NavMenu):
    """Contains the top level menu items."""

    tag = "List"
    alias = "RadixNavigationMenuList"

    as_child: Var[bool] = False


class NavMenuItem(NavMenu):
    """A top level menu item, contains a link or trigger with content combination."""

    tag = "Item"
    alias = "RadixNavigationMenuItem"

    as_child: Var[bool] = False
    value: Var[str]


class NavMenuTrigger(NavMenu):
    """The button that toggles the content."""

    tag = "Trigger"
    alias = "RadixNavigationMenuTrigger"

    as_child: Var[bool] = False

    class_name: Var[str] = "outline-none user-select-none"

class NavMenuContent(NavMenu):
    """Contains the content associated with each trigger."""

    tag = "Content"
    alias = "RadixNavigationMenuContent"

    as_child: Var[bool] = False
    force_mount: Var[bool]

    on_escape_key_down: rx.EventHandler[lambda e: [e]] = None
    on_pointer_down_outside: rx.EventHandler[lambda e: [e]] = None
    on_focus_outside: rx.EventHandler[lambda e: [e]] = None
    on_interact_outside: rx.EventHandler[lambda e: [e]] = None
    class_name: Var[str] = (
        "data-[motion=from-start]:animate-enterFromLeft data-[motion=from-end]:animate-enterFromRight data-[motion=to-start]:animate-exitToLeft data-[motion=to-end]:animate-exitToRight absolute top-0 left-0 w-full sm:w-auto",
    )


class NavMenuLink(NavMenu):
    """A navigational link."""

    tag = "Link"
    alias = "RadixNavigationMenuLink"

    as_child: Var[bool] = False
    active: Var[bool] = False
    on_select: rx.EventHandler[lambda e: [e]] = None

    def add_style(self) -> Style:
        return {
            "display": "block",
            "text_decoration": "none",
            "font_size": "15px",
            "line_height": "1",
            "padding": "8px 12px",
            "outline": "none",
            "user_select": "none",
            "font_weight": "500",
            "border_radius": "4px",
            "color": "var(--accent-11)",
            "_focus": {
                "box_shadow": "0 0 0 2px var(--accent-7)",
            },
            "_hover": {
                "background_color": "var(--accent-3)",
                "color": "var(--accent-11)",
            },
        }


class NavMenuIndicator(NavMenu):
    """An optional indicator element that renders below the list."""

    tag = "Indicator"
    alias = "RadixNavigationMenuIndicator"

    as_child: Var[bool] = False
    force_mount: Var[bool]

    def add_style(self) -> Style:
        return {
            "display": "flex",
            "align_items": "flex-end",
            "justify_content": "center",
            "height": "10px",
            "top": "100%",
            "overflow": "hidden",
            "z_index": "1",
            "transition": "width, transform 250ms ease",
            "&[data-state='visible']": {
                "animation": "fadeIn 100ms ease",
            },
            "&[data-state='hidden']": {
                "animation": "fadeOut 100ms ease",
            },
            "@keyframes fadeIn": {
                "from": {
                    "opacity": "0",
                },
                "to": {
                    "opacity": "1",
                },
            },
            "@keyframes fadeOut": {
                "from": {
                    "opacity": "1",
                },
                "to": {
                    "opacity": "0",
                },
            },
        }


class NavMenuViewport(NavMenu):
    """An optional viewport element that is used to render active content outside of the list."""

    tag = "Viewport"
    alias = "RadixNavigationMenuViewport"

    as_child: Var[bool] = False
    force_mount: Var[bool]

    class_name: Var[str] = (
        "data-[state=open]:animate-scaleIn data-[state=closed]:animate-scaleOut relative h-[var(--radix-navigation-menu-viewport-height)] w-full origin-[top_left] overflow-hidden bg-slate-2 transition-[width,_height] duration-300 sm:w-[var(--radix-navigation-menu-viewport-width)] border border-slate-5 shadow-large rounded-xl"
    )


class NavMenu(rx.Component):
    """NavMenu component."""

    root = staticmethod(NavMenuRoot.create)
    # sub = staticmethod(NavMenuSub.create)
    list = staticmethod(NavMenuList.create)
    item = staticmethod(NavMenuItem.create)
    trigger = staticmethod(NavMenuTrigger.create)
    content = staticmethod(NavMenuContent.create)
    # link = staticmethod(NavMenuLink.create)
    # indicator = staticmethod(NavMenuIndicator.create)
    viewport = staticmethod(NavMenuViewport.create)


nav_menu = NavMenu()
