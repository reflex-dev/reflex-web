import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.constants import DISCORD_URL


def discord() -> rx.Component:
    return ui.link(
        render_=ui.button(
            get_icon(icon="discord_navbar", class_name="shrink-0 text-secondary-10"),
            custom_attrs={"aria-label": "Discord link"},
            size="icon-sm",
            variant="outline",
            class_name="text-secondary-10",
        ),
        to=DISCORD_URL,
    )
