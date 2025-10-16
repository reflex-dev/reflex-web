import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.constants import GITHUB_URL
from pcweb.github import GithubStarState


def github() -> rx.Component:
    return ui.link(
        render_=ui.button(
            get_icon(icon="github_navbar", class_name="shrink-0 text-secondary-11"),
            GithubStarState.stars_short,
            custom_attrs={"aria-label": "Github link"},
            size="sm",
            variant="outline",
            class_name="text-secondary-11",
        ),
        to=GITHUB_URL,
    )
