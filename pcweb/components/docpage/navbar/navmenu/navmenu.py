"""Reflex custom component NavMenu."""

from types import SimpleNamespace
from typing import Any, Dict, Literal

import reflex as rx
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

    class_name: Var[str] | str = (
        "relative flex w-full items-center h-full justify-between gap-6 mx-auto z-[9999] flex-row max-w-[94.5rem]"
    )

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

    class_name: Var[str] | str = "outline-none user-select-none"


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
    class_name: Var[str] | str = (
        "data-[motion=from-start]:animate-enterFromLeft data-[motion=from-end]:animate-enterFromRight data-[motion=to-start]:animate-exitToLeft data-[motion=to-end]:animate-exitToRight absolute top-0 left-0 w-full sm:w-auto",
    )


class NavMenuViewport(NavMenu):
    """An optional viewport element that is used to render active content outside of the list."""

    tag = "Viewport"
    alias = "RadixNavigationMenuViewport"

    as_child: Var[bool] = False
    force_mount: Var[bool]

    class_name: Var[str] | str = (
        "data-[state=open]:animate-scaleIn data-[state=closed]:animate-scaleOut relative h-[var(--radix-navigation-menu-viewport-height)] w-full origin-[top_left] overflow-hidden bg-slate-2 transition-[width,_height] duration-300 sm:w-[var(--radix-navigation-menu-viewport-width)] border border-slate-5 shadow-large rounded-xl"
    )


class NavMenu(SimpleNamespace):
    """NavMenu component."""

    root = __call__ = staticmethod(NavMenuRoot.create)
    list = staticmethod(NavMenuList.create)
    item = staticmethod(NavMenuItem.create)
    trigger = staticmethod(NavMenuTrigger.create)
    content = staticmethod(NavMenuContent.create)
    viewport = staticmethod(NavMenuViewport.create)


nav_menu = NavMenu()
