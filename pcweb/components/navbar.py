"""UI and logic for the navbar component."""

from typing import Optional

import reflex as rx
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.components.logo import navbar_logo
from pcweb.components.sidebar import sidebar as sb
from pcweb.pages.docs.gallery import gallery

try:
    from pcweb.tsclient import client
except ImportError:
    client = None


class NavMenu(rx.Component):
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

    enter: bool = False

    banner: bool = True

    def toggle_banner(self):
        self.banner = not self.banner

    def change_search(self):
        self.search_modal = not (self.search_modal)

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.var
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
    return rx.vstack(
        rx.link(
            rx.text(
                result["document"]["heading"],
                font_weight=600,
                color="#1F1944",
            ),
            rx.divider(),
            rx.text(
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
        shadow=styles.DOC_SHADOW_LIGHT,
        _hover={"background_color": "#F5EFFE", "color": "#5646ED"},
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
        "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);",
    },
}


def search_bar():
    return rx.hstack(
        rx.fragment(
            rx.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
            rx.text("Search docs", style=styles.NAV_SEARCH_STYLE, font_weight=400),
        ),
        rx.spacer(),
        rx.text("/", style=styles.NAV_SEARCH_STYLE),
        on_click=NavbarState.change_search,
        display=["none", "flex", "flex", "flex", "flex"],
        min_width=["15em", "15em", "15em", "20em", "20em"],
        padding_x="1em",
        height="2em",
        border_radius="20px",
        bg="#FAF8FB",
    )


def search_modal(state: NavbarState):
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_body(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
                            rx.input(
                                placeholder="Search the docs",
                                on_change=NavbarState.set_search_input,
                                focus_border_color="transparent",
                                border_color="transparent",
                                font_weight=400,
                                _placeholder={"color": "#342E5C"},
                            ),
                            width="100%",
                        ),
                        rx.divider(),
                        rx.vstack(
                            rx.foreach(
                                NavbarState.search_results,
                                format_search_results,
                            ),
                            spacing="1em",
                            width="100%",
                            max_height="30em",
                            align_items="start",
                            overflow_y="auto",
                        ),
                    )
                ),
                bg="radial-gradient(82.06% 100% at 50% 100%, rgba(86, 70, 237, 0.12) 0%, rgba(245, 239, 254, 0) 100%), #FFFFFF;",
            )
        ),
        is_open=NavbarState.search_modal,
        on_close=NavbarState.change_search,
        padding_top="1em",
        padding_x="1em",
    )


def github_button():
    return rx.link(
        rx.hstack(
            rx.image(src="/github.svg", height="1.25em"),
            rx.text("Star", style=styles.NAV_TEXT_STYLE),
            rx.text(
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
        ),
        href=constants.GITHUB_URL,
        display=["none", "none", "none", "flex", "flex", "flex"],
    )


def discord_button():
    return rx.link(
        rx.center(
            rx.image(src="/icons/discord.svg", height="1.25em"),
            box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
            display=["none", "none", "none", "flex", "flex", "flex"],
            height="2em",
            width="2em",
            border_radius="8px",
            bg="#FFFFFF",
            style=hover_button_style,
        ),
        href=constants.DISCORD_URL,
    )


def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """
    # If the sidebar is not provided, create a default one.
    sidebar = sidebar or sb()

    # Create the navbar component.
    return rx.vstack(
        rx.cond(
            NavbarState.banner,
            rx.box(
                rx.hstack(
                    rx.center(
                        rx.box(
                            "✨  We have some exciting news to share: Pynecone has rebranded to Reflex!",
                            " Read more about it on our ",
                            rx.link(
                                "blog",
                                href="/blog/2023-06-28-rebrand-to-reflex",
                                style={
                                    "color": "#FFFFFF",
                                    "text_decoration": "underline",
                                    "_hover": {"color": styles.ACCENT_COLOR},
                                },
                            ),
                            "  ✨",
                            color="#FFFFFF",
                            font_weight=600,
                        ),
                        width="100%",
                    ),
                    rx.spacer(),
                    rx.icon(
                        tag="close",
                        z_index=1000,
                        style={
                                    "color": "#FFFFFF",
                                    "text_decoration": "underline",
                                    "_hover": {"color": styles.ACCENT_COLOR},
                                },
                        on_click=NavbarState.toggle_banner,
                    ),
                    width="100%",
                    padding_x=styles.PADDING_X,
                    align_items="center",
                ),
                background_color="#110F1F",
                padding_y=["0.8em", "0.8em", "0.5em"],
                width="100%",
            ),
        ),
        rx.box(
            rx.hstack(
                rx.hstack(
                    logo,
                    rx.link(
                        "Docs",
                        href="/docs/getting-started/introduction",
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "none", "flex", "flex"],
                    ),
                    rx.link(
                        "Blog",
                        href="/blog",
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "none", "flex", "flex"],
                    ),
                    rx.menu(
                        rx.menu_button(
                            rx.hstack(
                                rx.text("Resources", style=styles.NAV_TEXT_STYLE),
                                rx.icon(
                                    tag="chevron_down", style=styles.NAV_TEXT_STYLE
                                ),
                                cursor="pointer",
                                display=[
                                    "none",
                                    "none",
                                    "none",
                                    "none",
                                    "flex",
                                    "flex",
                                ],
                            )
                        ),
                        rx.menu_list(
                            rx.link(
                                rx.menu_item(
                                    "App Gallery", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href="/docs/gallery",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "Roadmap", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href="https://reflex-dev.notion.site/d1b60926ced14914bdbb42547ac84e50?v=723e0afc57294e40961d177aa691ee37",
                            ),
                            rx.menu_divider(),
                            rx.link(
                                rx.menu_item(
                                    "Contributor Program",
                                    style=styles.NAV_DROPDOWN_STYLE,
                                ),
                                href="https://reflex-dev.notion.site/2107ab2bc166497db951b8d742748284?v=f0eaff78fa984b5ab15d204af58907d7",
                            ),
                        ),
                    ),
                    spacing="2em",
                ),
                rx.hstack(
                    search_bar(),
                    github_button(),
                    discord_button(),
                    rx.icon(
                        tag="hamburger",
                        on_click=NavbarState.toggle_sidebar,
                        width="1.5em",
                        height="1.5em",
                        _hover={
                            "cursor": "pointer",
                            "color": styles.ACCENT_COLOR,
                        },
                        display=["flex", "flex", "flex", "none", "none", "none"],
                    ),
                    height="full",
                ),
                rx.drawer(
                    rx.drawer_overlay(
                        rx.drawer_content(
                            rx.hstack(
                                logo,
                                rx.icon(
                                    tag="close",
                                    on_click=NavbarState.toggle_sidebar,
                                    width="4em",
                                    _hover={
                                        "cursor": "pointer",
                                        "color": styles.ACCENT_COLOR,
                                    },
                                ),
                                justify="space-between",
                                margin_bottom="1.5em",
                            ),
                            sidebar if sidebar is not None else rx.text("Sidebar"),
                            padding_x="2em",
                            padding_top="2em",
                            bg="rgba(255,255,255, 0.97)",
                        ),
                        bg="rgba(255,255,255, 0.5)",
                    ),
                    placement="left",
                    is_open=NavbarState.sidebar_open,
                    on_close=NavbarState.toggle_sidebar,
                    bg="rgba(255,255,255, 0.5)",
                ),
                search_modal(NavbarState),
                justify="space-between",
                padding_x=styles.PADDING_X,
            ),
            bg="rgba(255,255,255, 0.9)",
            backdrop_filter="blur(10px)",
            padding_y=["0.8em", "0.8em", "0.5em"],
            border_bottom="1px solid #F4F3F6",
            width="100%",
        ),
        position="sticky",
        z_index="999",
        top="0",
        width="100%",
        spacing="0",
    )
