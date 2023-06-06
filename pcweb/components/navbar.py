"""UI and logic for the navbar component."""

import pynecone as pc

from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.components.logo import navbar_logo
from pcweb.components.sidebar import sidebar as sb
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.resources import resources
from pcweb.pages.docs.getting_started import introduction
from pcweb.pages.index import index

try:
    from pcweb.tsclient import client
except ImportError:
    client = None


class NavbarState(State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_modal: bool = False

    search_input: str = ""

    def change_search(self):
        self.search_modal = not (self.search_modal)

    def toggle_sidebar(self):
        """Toggle the sidebar open state."""
        self.sidebar_open = not self.sidebar_open

    @pc.var
    def search_results(self) -> list[dict[str, dict[str, str]]]:
        if client is None or self.search_input == "":
            return []
        search_parameters = {
            "q": self.search_input,
            "query_by": "heading, description",
            "query_by_weights": "2,1",
            "sort_by": "_text_match:desc",
        }
        return client.collections["search-auto"].documents.search(search_parameters)[
            "hits"
        ]


def format_search_results(result):
    return pc.vstack(
        pc.link(
            pc.text(
                result["document"]["heading"],
                font_weight=600,
                color=styles.DOC_HEADER_COLOR,
            ),
            pc.divider(),
            pc.text(
                result["document"]["description"],
                font_weight=400,
                color=styles.DOC_REG_TEXT_COLOR,
            ),
            on_click=NavbarState.change_search,
            href=result["document"]["href"],
        ),
        bg="#f7f7f7",
        border_radius="0.5em",
        width="100%",
        align_items="start",
        padding="0.5em",
        _hover={"background_color": "#e3e3e3c"},
    )


# Styles to use for the navbar.
logo_style = {
    "height": "1.25em",
}
logo = navbar_logo(**logo_style)


def search_bar():
    return pc.hstack(
        pc.fragment(
            pc.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
            pc.text("Search Docs", style=styles.NAV_SEARCH_STYLE),
        ),
        pc.spacer(),
        pc.text("/", style=styles.NAV_SEARCH_STYLE),
        display=["none", "none", "none", "flex", "flex"],
        bg="#FAF8FB",
        min_width="15em",
        padding_x="1em",
        padding_y="0.5em",
        border_radius="20px",
    )


def github_button():
    return pc.hstack(
        pc.image(src="/github.png", height="1.25em"),
        pc.text("Star", style=styles.NAV_TEXT_STYLE),
        pc.text(
            "9k",
            color="#5646ED",
            bg="#F5EFFE",
            padding_x="0.5em",
            padding_y="0.25em",
            border_radius="6px",
            font_weight=600,
        ),
        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        padding_x="1em",
        padding_y="0.25em",
        border_radius="8px",
        bg="#FFFFFF",
    )


def navbar(sidebar: pc.Component = None) -> pc.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """
    # If the sidebar is not provided, create a default one.
    sidebar = sidebar or sb()

    # Create the navbar component.
    return pc.box(
        pc.hstack(
            pc.hstack(
                logo,
                pc.link(
                    "Docs",
                    href="/docs/introduction",
                    style=styles.NAV_TEXT_STYLE,
                ),
                pc.link(
                    "Gallery",
                    href="/docs/gallery",
                    style=styles.NAV_TEXT_STYLE,
                ),
                spacing="2em",
            ),
            pc.hstack(
                search_bar(),
                github_button(),
            ),
            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        bg="rgba(255,255,255, 0.9)",
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid #F4F3F6",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )
