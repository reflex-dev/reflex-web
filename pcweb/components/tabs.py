"""Interactive tab components for Base UI."""

from __future__ import annotations

from typing import Any, Literal

from reflex import Component
from reflex.components.component import ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars import Var

from pcweb.components.utils.twmerge import cn


class BaseUIComponent(Component):
    """Set of content sections to be displayed one at a time."""

    lib_dependencies: list[str] = ["@base-ui-components/react@^1.0.0-alpha.8"]


# Default class names for each component
TABS_LIST_CLASS_NAME = "bg-slate-3 inline-flex gap-1 p-1 items-center justify-start rounded-[10px] relative z-0"

TABS_TAB_CLASS_NAME = "h-7 px-1.5 rounded-md justify-center items-center gap-1.5 inline-flex text-sm font-medium text-slate-9 cursor-pointer z-[1] hover:text-slate-12 transition-color text-nowrap data-[selected]:text-slate-12"

TABS_INDICATOR_CLASS_NAME = "absolute top-1/2 left-0 -z-1 h-7 w-[var(--active-tab-width)] -translate-y-1/2 translate-x-[var(--active-tab-left)] rounded-md bg-slate-1 shadow-small transition-all duration-200 ease-in-out"


class TabsBaseUIComponent(BaseUIComponent):
    library = "@base-ui-components/react/tabs"

    @property
    def import_var(self):
        return ImportVar(
            tag="Tabs",
            package_path="",
            install=False,
        )


class TabsRoot(TabsBaseUIComponent):
    """Groups the tabs and the corresponding panels."""

    tag = "Tabs.Root"

    # The value of the tab that should be active when initially rendered
    default_value: Var[Any] = 0

    # The controlled value of the tab that should be active
    value: Var[Any]

    # Event handler called when the value changes
    on_value_change: EventHandler[passthrough_event_spec(str)]

    # The orientation of the component
    orientation: Var[Literal["horizontal", "vertical"]] = "horizontal"

    # Class name
    class_name: Var[str] | str | None


class TabsList(TabsBaseUIComponent):
    """Groups the individual tab buttons."""

    tag = "Tabs.List"

    # Whether to activate tabs on focus
    activate_on_focus: Var[bool] = True

    # Whether to loop through tabs
    loop: Var[bool] = True

    # Class name
    class_name: Var[str] | str | None = TABS_LIST_CLASS_NAME

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the tabs list component."""
        if "class_name" in props:
            props["class_name"] = cn(TABS_LIST_CLASS_NAME, props["class_name"])
        return super().create(*children, **props)


class TabsTab(TabsBaseUIComponent):
    """An individual interactive tab button."""

    tag = "Tabs.Tab"

    # The value of the tab
    value: Var[Any]

    # Optional icon component
    icon: Component | None = None

    # Class name
    class_name: Var[str] | str | None = TABS_TAB_CLASS_NAME

    @classmethod
    def create(cls, *children, icon: Component | None = None, **props) -> Component:
        """Create the tab component with optional icon."""
        if "class_name" in props:
            props["class_name"] = cn(TABS_TAB_CLASS_NAME, props["class_name"])
        if icon is not None:
            children = (icon, *children)
        return super().create(*children, **props)


class TabsIndicator(TabsBaseUIComponent):
    """Visual indicator for the active tab."""

    tag = "Tabs.Indicator"

    # Whether to render before hydration
    render_before_hydration: Var[bool] = False

    # Class name
    class_name: Var[str] | str | None = TABS_INDICATOR_CLASS_NAME

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the tabs indicator component."""
        if "class_name" in props:
            props["class_name"] = cn(TABS_INDICATOR_CLASS_NAME, props["class_name"])
        return super().create(*children, **props)


class TabsPanel(TabsBaseUIComponent):
    """Content panel associated with a tab."""

    tag = "Tabs.Panel"

    # The value that associates the panel with a tab
    value: Var[Any]

    # Whether to keep the panel mounted when inactive
    keep_mounted: Var[bool] = False

    # Class name
    class_name: Var[str] | str | None


class Tabs(ComponentNamespace):
    """Namespace for Tab components."""

    root = __call__ = staticmethod(TabsRoot.create)
    list = staticmethod(TabsList.create)
    tab = staticmethod(TabsTab.create)
    panel = staticmethod(TabsPanel.create)
    indicator = staticmethod(TabsIndicator.create)


tabs = Tabs()
