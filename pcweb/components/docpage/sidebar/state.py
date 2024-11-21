"""The state of the sidebar component."""


from __future__ import annotations

import reflex as rx
from reflex.base import Base


class SideBarBase(Base):
    """Base class for the Side bar."""

    # The name to display in the sidebar.
    names: str = ""

    alt_name_for_next_prev: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SideBarItem] = []

    # Whether the item is a category. Occurs if a single item is at the top level of the sidebar for asthetics.
    outer = False


class SideBarItem(SideBarBase):
    """A single item in the sidebar."""
    ...


class SideBarSection(SideBarBase):
    """A section in the sidebar."""
    ...


class SidebarState(rx.State):
    _sidebar_index: int = -1

    def set_sidebar_index(self, num) -> int:
        self._sidebar_index = num

    @rx.var(cache=True, initial_value=-1)
    def sidebar_index(self) -> int:
        if self._sidebar_index < 0:
            route = self.router.page.path
            if "library" in route or "api-reference" in route or "recipe" in route:
                return 1
            else:
                return 0
        return self._sidebar_index