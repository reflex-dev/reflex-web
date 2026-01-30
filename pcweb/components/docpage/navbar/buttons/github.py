import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.constants import GITHUB_STARS, GITHUB_URL


def github() -> rx.Component:
    return ui.link(
        render_=ui.button(
            get_icon(icon="github_navbar", class_name="shrink-0 text-secondary-11"),
            f"{GITHUB_STARS // 1000}K",
            custom_attrs={
                "aria-label": f"View Reflex on GitHub - {GITHUB_STARS // 1000}K stars"
            },
            size="sm",
            variant="outline",
            class_name="text-secondary-11",
        ),
        to=GITHUB_URL,
        custom_attrs={
            "aria-label": f"View Reflex on GitHub - {GITHUB_STARS // 1000}K stars"
        },
    )
