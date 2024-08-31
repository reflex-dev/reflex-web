"""Reflex custom component NavMenu."""

from typing import Any
from typing import Literal

import reflex as rx
from pcweb.styles.colors import c_color
from pcweb.styles.shadows import shadows
from reflex.style import Style
from reflex.vars import Var

LiteralMenuComponentDir = Literal["ltr", "rtl"]
LiteralMenuComponentOrientation = Literal["vertical", "horizontal"]


class NavMenu(rx.Component):
    """NavMenu component."""

    library = "@radix-ui/react-navigation-menu@^1.2.0"


class NavMenuRoot(NavMenu):
    """Navigation menu root component."""

    tag = "Root"
    alias = "RadixNavigationMenuRoot"

    value: Var[str]
    default_value: Var[str]
    delay_duration: Var[int] = 200
    skip_delay_duration: Var[int] = 300
    orientation: Var[LiteralMenuComponentOrientation] = "horizontal"
    dir: Var[LiteralMenuComponentDir]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_value_change": lambda e0: [e0],
        }

    def add_style(self) -> Style:
        return {
            "position": "relative",
            "z_index": "10",
            "flex": "1 1 0%",
            "margin_x": "auto",
            "display": "flex",
            "height": "100%",
            "padding_x": ["16px", "24px", "24px", "24px", "24px"],
            "align_items": "center",
            "gap": "24px",
            "justify_content": "space-between",
        }


class NavMenuSub(NavMenu):
    """Navigation menu sub component."""

    tag = "Sub"
    alias = "RadixNavigationMenuSub"

    value: Var[str]
    default_value: Var[str]
    orientation: Var[LiteralMenuComponentOrientation] = "horizontal"

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_value_change": lambda e0: [e0],
        }


class NavMenuList(NavMenu):
    """Contains the top level menu items."""

    tag = "List"
    alias = "RadixNavigationMenuList"

    as_child: Var[bool] = False

    def add_style(self) -> Style:
        return {
            "list-style-type": "none",
            "flex": "1 1 0%",
            "display": "flex",
            "list_style": "none",
            "align_items": "stretch",
            "justify_content": "center",
            "height": "100%",
        }


class NavMenuItem(NavMenu):
    """A top level menu item, contains a link or trigger with content combination."""

    tag = "Item"
    alias = "RadixNavigationMenuItem"

    as_child: Var[bool] = False
    value: Var[str]

    def add_style(self) -> Style:
        return {
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
        }


class NavMenuTrigger(NavMenu):
    """The button that toggles the content."""

    tag = "Trigger"
    alias = "RadixNavigationMenuTrigger"

    as_child: Var[bool] = False

    def add_style(self) -> Style:
        return {
            "outline": "none",
            "user_select": "none",
        }


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

    def add_style(self) -> Style:
        return {
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "animation_duration": "250ms",
            "animation_timing_function": "ease",
            "@media (min-width: 600px)": {
                "width": "auto",
            },
            "&[data-motion='from-start']": {
                "animation_name": "enterFromLeft",
            },
            "&[data-motion='from-end']": {
                "animation_name": "enterFromRight",
            },
            "&[data-motion='to-start']": {
                "animation_name": "exitToLeft",
            },
            "&[data-motion='to-end']": {
                "animation_name": "exitToRight",
            },
            "@keyframes enterFromRight": {
                "from": {
                    "opacity": "0",
                    "transform": "translateX(200px)",
                },
                "to": {
                    "opacity": "1",
                    "transform": "translateX(0)",
                },
            },
            "@keyframes enterFromLeft": {
                "from": {
                    "opacity": "0",
                    "transform": "translateX(-200px)",
                },
                "to": {
                    "opacity": "1",
                    "transform": "translateX(0)",
                },
            },
            "@keyframes exitToRight": {
                "from": {
                    "opacity": "1",
                    "transform": "translateX(0)",
                },
                "to": {
                    "opacity": "0",
                    "transform": "translateX(200px)",
                },
            },
            "@keyframes exitToLeft": {
                "from": {
                    "opacity": "1",
                    "transform": "translateX(0)",
                },
                "to": {
                    "opacity": "0",
                    "transform": "translateX(-200px)",
                },
            },
        }


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

    def add_style(self) -> Style:
        return {
            "position": "relative",
            "transform_origin": "top left",
            "width": "100%",
            "border-radius": "12px",
            "border": f"1px solid {c_color('slate', 5)}",
            "background": f"{c_color('slate', 2)}",
            "box-shadow": shadows["large"],
            "overflow": "hidden",
            "will-change": "width, height",
            "height": "var(--radix-navigation-menu-viewport-height)",
            "transition": "width, height 300ms ease",
            "@media (min-width: 600px)": {
                "width": "var(--radix-navigation-menu-viewport-width)",
            },
            "@keyframes scaleIn": {
                "from": {
                    "transform": "rotateX(-30deg) scale(0.9)",
                    "opacity": "0",
                },
                "to": {
                    "transform": "rotateX(0deg) scale(1)",
                    "opacity": "1",
                },
            },
            "@keyframes scaleOut": {
                "from": {
                    "opacity": "1",
                    "transform": "rotateX(0deg) scale(1)",
                },
                "to": {
                    "opacity": "0",
                    "transform": "rotateX(-10deg) scale(0.95)",
                },
            },
            "&[data-state='open']": {
                "animation": "scaleIn 200ms ease",
            },
            "&[data-state='closed']": {
                "animation": "scaleOut 200ms ease",
            },
        }


class NavMenu(rx.Component):
    """NavMenu component."""

    root = staticmethod(NavMenuRoot.create)
    sub = staticmethod(NavMenuSub.create)
    list = staticmethod(NavMenuList.create)
    item = staticmethod(NavMenuItem.create)
    trigger = staticmethod(NavMenuTrigger.create)
    content = staticmethod(NavMenuContent.create)
    link = staticmethod(NavMenuLink.create)
    indicator = staticmethod(NavMenuIndicator.create)
    viewport = staticmethod(NavMenuViewport.create)


nav_menu = NavMenu()
