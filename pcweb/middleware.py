"""Application middleware."""

import reflex as rx

from pcweb.components.navbar import NavbarState
from pcweb.pages.index import IndexState


class CloseSidebarMiddleware(rx.Middleware):
    """Middleware to make sure the sidebar closes when the page changes."""

    def preprocess(self, app, state, event):
        """Preprocess the event.

        Args:
            app: The app to apply the middleware to.
            state: The client state.
            event: The event to preprocess.
        """
        if event.name == rx.event.get_hydrate_event(state):
            state.get_substate(NavbarState.get_full_name().split(".")).sidebar_open = False
            state.get_substate(IndexState.get_full_name().split(".")).show_c2a = True
