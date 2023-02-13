"""UI and logic for the navbar component."""

import pynecone as pc

from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.components.logo import logo
from pcweb.components.sidebar import sidebar as sb
from pcweb.pages.docs.gallery import gallery
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
    "width": "3.21em",
    "height": "3em",
}
logo = logo(**logo_style)

button_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "_hover": {"color": styles.ACCENT_COLOR, "text_decoration": "none"},
}


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
            pc.link(
                pc.hstack(
                    logo,
                    pc.tablet_and_desktop(
                        pc.text(
                            "Pynecone",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=600,
                        ),
                    ),
                    spacing="0.25em",
                ),
                href=index.path,
                _hover={"text_decoration": "none"},
            ),
            pc.box(
                pc.hstack(
                    pc.input_group(
                        pc.input_left_addon(
                            pc.icon(tag="SearchIcon", color=styles.DOC_REG_TEXT_COLOR),
                            bg="white",
                        ),
                        pc.input(
                            placeholder="Search the docs",
                            on_click=NavbarState.change_search,
                            _focus={
                                "border": f"2px solid {styles.ACCENT_COLOR}",
                            },
                        ),
                        bg="white",
                    ),
                ),
                pc.modal(
                    pc.modal_overlay(
                        pc.modal_content(
                            pc.modal_body(
                                pc.vstack(
                                    pc.input(
                                        placeholder="Search",
                                        on_change=NavbarState.set_search_input,
                                    ),
                                    pc.vstack(
                                        pc.foreach(
                                            NavbarState.search_results,
                                            format_search_results,
                                        ),
                                        spacing="0.5em",
                                        width="100%",
                                        max_height="30em",
                                        align_items="start",
                                        overflow="auto",
                                    ),
                                ),
                                opacity=0.8,
                            ),
                            opacity=0.1,
                        )
                    ),
                    is_open=NavbarState.search_modal,
                    on_close=NavbarState.change_search,
                    padding="1em",
                ),
                display=["none", "none", "none", "none", "flex"],
            ),
            pc.hstack(
                pc.tablet_and_desktop(
                    pc.link(
                        pc.text(
                            "Docs",
                        ),
                        href=introduction.path,
                        **button_style,
                    ),
                ),
                pc.tablet_and_desktop(
                    pc.link(
                        pc.text(
                            "Gallery",
                        ),
                        href=gallery.path,
                        **button_style,
                    ),
                ),
                pc.desktop_only(
                    pc.menu(
                        pc.hstack(
                            pc.menu_button(
                                "Reference",
                                pc.icon(tag="ChevronDownIcon"),
                                color=styles.DOC_REG_TEXT_COLOR,
                                _hover={"color": styles.ACCENT_COLOR},
                            ),
                        ),
                        pc.menu_list(
                            pc.link(
                                pc.menu_item(
                                    "Components",
                                    _hover={"background_color": "white"},
                                    _focus={},
                                ),
                                _hover={"color": styles.ACCENT_COLOR},
                                href="/docs/library",
                            ),
                            pc.link(
                                pc.menu_item(
                                    "Hosting", _hover={"background_color": "white"}
                                ),
                                _hover={"color": styles.ACCENT_COLOR},
                                href="/docs/hosting/deploy",
                            ),
                        ),
                    )
                ),
                pc.desktop_only(
                    pc.link(
                        pc.image(src="/github.png", height="1.25em"),
                        href=constants.GITHUB_URL,
                    ),
                ),
                pc.mobile_and_tablet(
                    pc.icon(
                        tag="HamburgerIcon",
                        on_click=NavbarState.toggle_sidebar,
                        width="1.5em",
                        height="1.5em",
                        _hover={
                            "cursor": "pointer",
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                ),
                spacing="1em",
            ),
            pc.drawer(
                pc.drawer_overlay(
                    pc.drawer_content(
                        pc.hstack(
                            logo,
                            pc.icon(
                                tag="CloseIcon",
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
                        sidebar if sidebar is not None else pc.text("Sidebar"),
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
            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        bg="rgba(255,255,255, 0.8)",
        backdrop_filter="blur(6px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid rgba(100, 116, 139, .1)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )
