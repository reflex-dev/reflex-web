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
from typing import Optional

try:
    from pcweb.tsclient import client
except ImportError:
    client = None


class NavMenu(pc.Component):
    library = "@radix-ui/react-navigation-menu"
    tag = "NavigationMenu"

    @classmethod
    def get_alias(cls) -> Optional[str]:
        return "*"


class NavbarState(State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_modal: bool = False

    search_input: str = ""

    def change_search(self):
        self.search_modal = not (self.search_modal)

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @pc.var
    def search_results(self) -> list[dict[str, dict[str, str]]]:
        """Get the search results."""
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
                    color="#1F1944",
                ),
                pc.divider(),
                pc.text(
                    result["document"]["description"],
                    font_weight=400,
                    color="#696287",
                    
                ),
            on_click=NavbarState.change_search,
            href=result["document"]["href"],
            ),
            bg="#FAF8FB",
            border_radius="8px",
            align_items="start",
            padding="0.5em",
            shadow = styles.DOC_SHADOW_LIGHT,
            _hover={
                "background_color": "#F5EFFE",
                "color":"#5646ED"
            },
            width="100%",
    )



# Styles to use for the navbar.
logo_style = {
    "height": "1.25em",
}
logo = navbar_logo(**logo_style)


hover_button_style = {
    "_hover": {
        "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
        "box-shadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"
    },
}

def search_bar():
    return pc.hstack(
        pc.fragment(
            pc.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
            pc.text("Search Docs", style=styles.NAV_SEARCH_STYLE, font_weight=400),
        ),
        pc.spacer(),
        pc.text("/", style=styles.NAV_SEARCH_STYLE),
        on_click=NavbarState.change_search,
        display=["none", "none", "none", "flex", "flex"],
        bg="#FAF8FB",
        min_width="15em",
        padding_x="1em",
        height="2em",
        border_radius="20px",
    )

def search_modal(state: NavbarState):
    return pc.modal(
        pc.modal_overlay(
            pc.modal_content(
                pc.modal_body(
                    pc.vstack(
                        pc.hstack(
                            pc.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
                            pc.input(
                                placeholder="Search the docs",
                                on_change=NavbarState.set_search_input,
                                focus_border_color="transparent",
                                border_color="transparent",
                            ),
                            width="100%",
                        ),
                        pc.divider(),
                        pc.vstack(
                            pc.foreach(
                                NavbarState.search_results,
                                format_search_results,
                            ),
                            spacing="1em",
                            width="100%",
                            max_height="30em",
                            align_items="start",
                            overflow_y="auto",
                        )
                    )
                ),
                bg= "radial-gradient(82.06% 100% at 50% 100%, rgba(86, 70, 237, 0.12) 0%, rgba(245, 239, 254, 0) 100%), #FFFFFF;",
            )
        ),
        is_open=NavbarState.search_modal,
        on_close=NavbarState.change_search,
        padding_top="1em",
        padding_x="1em",
    )


def github_button():
    return pc.hstack(
        pc.image(src="/github.png", height="1.25em"),
        pc.text("Star", style=styles.NAV_TEXT_STYLE),
        pc.text(
            "9k+", 
            color="#5646ED",
            bg="#F5EFFE",
            padding_x="0.5em",
            border_radius="6px",
            font_weight=600,
        ),
        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        padding_x=".5em",
        height="2em",
        border_radius="8px",
        bg="#FFFFFF",
        style=hover_button_style,
    )

def discord_button():
    return pc.center(
        pc.image(src="/icons/discord.svg", height="1.25em"),
        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        height="2em",
        width="2em",
        border_radius="8px",
        bg="#FFFFFF",
        style=hover_button_style,
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
                    href="/docs/getting-started/introduction",
                    style=styles.NAV_TEXT_STYLE,
                ),
                pc.link(
                    "Gallery",
                    href="/docs/gallery",
                    style=styles.NAV_TEXT_STYLE,
                ),
                pc.menu(
                    pc.menu_button("Resources", style=styles.NAV_TEXT_STYLE),
                    pc.menu_list(
                        pc.hstack(
                            pc.link(pc.vstack(
                                pc.text("Contributor Program", style=styles.NAV_TEXT_STYLE),
                                pc.text("Become a contributor", style=styles.NAV_TEXT_STYLE),
                            ), href="/docs/gallery"),
                            pc.vstack(
                                pc.text("Community", style=styles.NAV_TEXT_STYLE),
                                pc.text("Join the community", style=styles.NAV_TEXT_STYLE),
                            )
                        ),
                    ),
                    background="radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
                ),
                spacing="2em",
            ),
            pc.hstack(
                search_bar(),
                github_button(),
                discord_button(),
                height="full",
            ),
            search_modal(NavbarState),
            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        bg="rgba(255,255,255, 0.9)",
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="2px solid #F4F3F6",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )
