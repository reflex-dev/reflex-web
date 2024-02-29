"""UI and logic for the navbar component."""
import os
from datetime import datetime
from typing import Any, Optional, Set

import requests
from sqlmodel import Field

import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import navbar_logo
from reflex.vars import ImportVar, Var


def shorten_to_k(number):
    if number >= 1000:
        return "{:.0f}k+".format(number / 1000)
    else:
        return str(number)


class Search(rx.Component):
    tag = "InkeepEmbeddedChat"

    library = "@inkeep/widgets@latest"

    special_props: Set[Var] = {Var.create_safe("{...inkeepEmbeddedChatProps}")}

    is_open: Var[bool] = False

    def _get_imports(self):
        return {"next/dynamic": {ImportVar(tag="dynamic", is_default=True)}}

    def get_event_triggers(self) -> dict[str, Any]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            **super().get_event_triggers(),
            "on_close": lambda: [],
            "on_shortcutKey_pressed": lambda: [],
        }

    def _get_custom_code(self) -> str:
        return """ 
const InkeepEmbeddedChat = dynamic(() => import("@inkeep/widgets").then((mod) => mod.InkeepEmbeddedChat), { ssr: false });

const inkeepEmbeddedChatProps = {
  baseSettings: {
    apiKey: '87b7469f79014c35a3313795088151a52de8a58a547abd16',
    integrationId: 'clkbf9e7e0001s601sa0ciax1',
    organizationId: 'org_WQKeNdnuPGEfuUhC',
    organizationDisplayName: 'Reflex',
    primaryBrandColor: '#5646ED',
    theme: {
        primaryColors: {
        textColorOnPrimary: '#11181c',
        textBold: '#141d20',
        textSubtle: '#354a51',
        lighter: '#e5feff',
        light: '#85f0ff',
        lightSubtle: '#f1f8fa',
        medium: '#26d6ff', // primaryBrandColor
        strong: '#00b5dd',
        stronger: '#006881',
        hitContentPreview: '#00b5dd',
        hitContentPreviewHover: '#006881',
        textColorOnPrimary: 'white',
        },
    },
    breadcrumbRules: {
      urlToBreadcrumbMapper: [
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/blog',
          },
          breadcrumbName: 'Blogs',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs',
          },
          breadcrumbName: 'Docs',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/api-reference',
          },
          replaceLeading: true,
          breadcrumbName: 'API Reference',
        },
        {
          matchingRule: {
            ruleType: 'PartialUrl',
            partialUrl: 'reflex.dev/docs/library',
          },
          replaceLeading: true,
          breadcrumbName: 'Components Reference',
        },
      ],
    },
    stringReplacementRules: [
      {
        matchingRule: {
          ruleType: 'Substring',
          string: 'Api',
        },
        replaceWith: 'API',
        replaceInTitles: true,
      },
      {
        matchingRule: {
          ruleType: 'Substring',
          string: 'Cli',
        },
        replaceWith: 'CLI',
        replaceInTitles: true,
      },
    ],
    theme: {
      components: {
        AIChatPageWrapper: {
          defaultProps: {
            variant: '',
            size: 'expand',
          },
        },
      }
    },
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
    botName: 'Reflex AI',
    quickQuestions: [
      'How does Reflex work?',
      'What types of apps can I build with Reflex?',
      'Where can I deploy my apps?',
    ],
  },
};
"""


inkeep = Search.create


class Feedback(rx.Model, table=True):
    email: Optional[str]
    feedback: str
    score: Optional[int]
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    page: str


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_modal: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    email: str = ""

    feedback: str = ""

    page_score: int = 0

    show_form = False
    form_submitted = False

    current_category = "All"

    def handle_submit(self, form_data: dict):
        feedback = form_data["feedback"]

        # Check if the email is valid.
        if "email" in form_data:
            self.email = form_data["email"]

        if len(feedback) < 10 or len(feedback) > 500:
            return rx.window_alert(
                "Please enter your feedback. Between 10 and 500 characters."
            )

        current_page_route = self.get_current_page()

        discord_message = f"""
Contact: {self.email}
Page: {current_page_route}
Score: {"?" if  self.page_score==0 else "👍" if self.page_score > 1 else "👎"}
Feedback: {feedback}
"""

        DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
        payload = {"content": discord_message}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except:
            pass

        self.show_form = False
        self.form_submitted = True
        self.page_score = 0

    def update_score(self, score):
        if self.show_form is True:
            if self.page_score == score:
                self.show_form = not self.show_form
        else:
            self.show_form = not self.show_form

        self.page_score = score

    def display_form(self):
        self.show_form = True

    def toggle_banner(self):
        self.banner = not self.banner

    def open_search(self):
        self.search_modal = True

    def close_search(self):
        self.search_modal = False

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_ai_chat(self):
        self.ai_chat = not self.ai_chat

    def update_category(self, tag):
        self.current_category = tag

    @rx.cached_var
    def search_results(self) -> list[dict[str, dict[str, str]]]:
        """Get the search results."""
        from pcweb.tsclient import client

        if client is None or self.search_input == "":
            return []

        if self.current_category == "All":
            search_parameters = {
                "q": self.search_input,
                "query_by": "heading, description",
                "query_by_weights": "2,1",
                "sort_by": "_text_match:desc",
            }
        else:
            search_parameters = {
                "q": self.search_input,
                "query_by": "heading, description",
                "query_by_weights": "2,1",
                "sort_by": "_text_match:desc",
                "filter_by": f"category: {self.current_category}",
            }
        typesense_collection_name = os.getenv(
            "TYPESENSE_COLLECTION_NAME", "search-auto"
        )
        return client.collections[typesense_collection_name].documents.search(
            search_parameters
        )["hits"]


def search_bar():
    return rx.chakra.hstack(
        rx.fragment(
            rx.icon(tag="search", style=styles.NAV_SEARCH_STYLE),
            rx.text(
                "Search documentation...",
                style=styles.NAV_SEARCH_STYLE,
                font_weight=400,
            ),
        ),
        rx.spacer(),
        rx.text("/", style=styles.NAV_SEARCH_STYLE),
        on_click=NavbarState.open_search,
        display=["none", "flex", "flex", "flex", "flex"],
        min_width=["15em", "15em", "15em", "20em", "20em"],
        padding_x="1em",
        height="2em",
        border_radius="20px",
        bg="#FAF8FB",
    )


def search_badge(category, stateful=True):
    if stateful:
        return rx.badge(
            category,
            border_radius="8px",
            padding_x=".5em",
            on_click=NavbarState.update_category(category),
            color=rx.cond(
                NavbarState.current_category == category,
                styles.c["violet"][500],
                styles.c["gray"][500],
            ),
            bg=rx.cond(
                NavbarState.current_category == category,
                styles.c["violet"][50],
                styles.c["gray"][50],
            ),
            _hover={
                "color": styles.c["violet"][500],
            },
            transition="all 0.2s ease-in-out",
        )
    else:
        return rx.badge(
            category,
            border_radius="8px",
            color=styles.c["violet"][500],
            bg=styles.c["violet"][50],
            padding_x=".5em",
        )


def format_search_results(result):
    return rx.link(
        rx.vstack(
            rx.hstack(
                rx.text(
                    result["document"]["heading"],
                    font_weight=600,
                    color=styles.c["indigo"][700],
                ),
                rx.spacer(),
                search_badge(result["document"]["category"], stateful=False),
                width="100%",
            ),
            rx.text(
                result["document"]["description"],
                no_of_lines=1,
                font_weight=400,
                color=styles.c["indigo"][500],
            ),
            width="100%",
            _hover={
                "bg": "#F5EFFE",
            },
            bg="#f4f3f4",
            border_radius="8px",
            padding_x=".5em",
            padding_y=".25em",
            gap="0.25em",
        ),
        on_click=NavbarState.close_search,
        href=result["document"]["href"],
        style={"text_decoration": "none"},
        width="100%",
    )


def ai_button():
    return rx.center(
        rx.icon(
            tag="message-circle-question",
            color=rx.cond(
                NavbarState.ai_chat,
                "#342E5C",
                "#5646ED",
            ),
        ),
        on_click=NavbarState.toggle_ai_chat,
        _hover={
            "cursor": "pointer",
            "color": styles.ACCENT_COLOR,
        },
        height="1em",
        transition="all 0.2s ease-in-out",
    )


def search_bar_categories(categories):
    return rx.hstack(
        *[search_badge(category) for category in categories],
        padding_bottom=".25em",
    )


def search_modal():
    return rx.chakra.modal(
        rx.chakra.modal_overlay(
            rx.chakra.modal_content(
                rx.chakra.modal_header(
                    # add in filter tabs here categories
                    search_bar_categories(
                        ["All", "Learn", "Component", "API Reference", "Blog"]
                    ),
                    rx.hstack(
                        rx.icon(
                            tag="search",
                            style=styles.NAV_SEARCH_STYLE,
                            height="1em",
                        ),
                        rx.chakra.input(
                            placeholder="Search the docs...",
                            on_change=NavbarState.set_search_input,
                            focus_border_color="transparent",
                            border_color="transparent",
                            font_weight=400,
                            _placeholder={"color": "#342E5C"},
                            _hover={"border_color": "transparent"},
                        ),
                        ai_button(),
                        border_bottom="1px solid #F4F3F6",
                    ),
                ),
                rx.chakra.modal_body(
                    rx.vstack(
                        rx.cond(
                            NavbarState.ai_chat,
                            rx.vstack(
                                rx.foreach(
                                    NavbarState.search_results,
                                    format_search_results,
                                ),
                                gap="1em",
                                width="100%",
                                max_height="30em",
                                align_items="start",
                                overflow_y="auto",
                                padding_top="0em",
                            ),
                            inkeep(
                                width="100%",
                            ),
                        ),
                        max_height="40em",
                        overflow="auto",
                        scrollbar_width="none",
                    ),
                    width="100%",
                ),
                bg="#FFFFFF",
                max_width="50em",
            )
        ),
        is_open=NavbarState.search_modal,
        on_close=NavbarState.close_search,
        size="xl",
        padding_top="1em",
        padding_x="1em",
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


def github_button():
    return rx.link(
        rx.chakra.hstack(
            rx.image(src="/companies/dark/github.svg", height="1.25em"),
            # rx.text("Star", style=styles.NAV_TEXT_STYLE),
            rx.text(
                shorten_to_k(constants.GITHUB_STARS),
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
        rx.chakra.center(
            rx.image(src="/companies/dark/discord.svg", height="1.25em"),
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


def my_form():
    # Define common styles
    border_none = {"border": "none"}
    common_shadow_style = {
        "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;"
    }
    placeholder_style = {"color": "#A9A7B1", "font_weight": "400"}
    common_input_style = {
        "width": "100%",
        "font_size": ".8em",
        "border_radius": "8px",
        "border": "none",
        "box_shadow": common_shadow_style["box_shadow"],
        "_active": border_none | common_shadow_style,
        "_focus": border_none | common_shadow_style,
        "_placeholder": placeholder_style,
    }

    # Create input and text area elements
    email_input = rx.chakra.input(
        placeholder="Email (optional)", id="email", type_="email", **common_input_style
    )
    feedback_text_area = rx.text_area(
        placeholder="Your Feedback...", id="feedback", **common_input_style
    )

    # Create button element
    submit_button = rx.hstack(
        rx.spacer(),
        rx.chakra.button("Send", type_="submit", size="sm", style=styles.BUTTON_LIGHT),
        width="100%",
    )

    # Form container with vertical stack
    form_container = rx.vstack(
        email_input, feedback_text_area, submit_button, padding_x=".5em", width="100%"
    )

    # Return the complete form
    return rx.form.root(
        form_container,
        on_submit=NavbarState.handle_submit,
        padding_bottom=".2em",
        width="100%",
    )


def feedback_indicator(icon, score):
    return rx.hstack(
        rx.image(src=icon, height="1em"),
        on_click=NavbarState.update_score(score),
        box_shadow=rx.cond(
            NavbarState.page_score == score,
            "0px 4px 10px -2px rgba(3, 3, 11, 0.12), 0px 4px 8px 0px rgba(3, 3, 11, 0.12), 0px 2px 3px 0px rgba(3, 3, 11, 0.10), 0px 0px 0px 2px rgba(149, 128, 247, 0.60), 0px -20px 12px -4px rgba(126, 105, 224, 0.60) inset, 0px 12px 12px -2px rgba(86, 70, 237, 0.12) inset, 0px 0px 0px 1px rgba(32, 17, 126, 0.40) inset;",
            "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        ),
        padding_x=".5em",
        height="2em",
        border_radius="8px",
        bg="#FFFFFF",
    )


def feedback_button():
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Was this page useful?",
                style=styles.NAV_TEXT_STYLE,
                font_size="1em",
            ),
            feedback_indicator("/icons/thumbs-down.svg", 1),
            feedback_indicator("/icons/thumbs-up.svg", 2),
            padding_x=".5em",
            padding_y=".25em",
        ),
        rx.cond(
            NavbarState.show_form,
            my_form(),
        ),
        transition="all 2s",
        border="2px solid #F4F3F6",
        border_radius="8px",
        padding="0.2em",
    )


def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """
    from pcweb import constants
    from pcweb.components.sidebar import sb
    from pcweb.pages.blog import blg
    from pcweb.pages.changelog import changelog
    from pcweb.pages.docs import getting_started
    from pcweb.pages.docs.gallery import gallery
    from pcweb.pages.faq import faq

    # If the sidebar is not provided, create a default one.
    sidebar = sidebar or sb

    # Create the navbar component.
    return rx.vstack(
        rx.cond(
            NavbarState.banner,
            rx.box(
                rx.hstack(
                    rx.center(
                        rx.box(
                            "✨ Reflex is in Hosting Alpha!",
                            " Learn more ",
                            rx.link(
                                "here",
                                href=constants.NOTION_HOSTING_URL,
                                style={
                                    "color": "#FFFFFF",
                                    "text_decoration": "underline",
                                    "_hover": {"color": "#AD9BF8"},
                                },
                                is_external=True,
                            ),
                            ". ✨",
                            color="#FFFFFF",
                            font_weight=600,
                        ),
                        width="100%",
                    ),
                    rx.spacer(),
                    rx.icon(
                        tag="x-square",
                        z_index=1000,
                        style={
                            "color": "#FFFFFF",
                            "text_decoration": "underline",
                            "_hover": {"color": "#AD9BF8"},
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
                        href=getting_started.introduction.path,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Blog",
                        href=blg.path,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Gallery",
                        href=gallery.path,
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "none", "flex", "flex"],
                    ),
                    rx.chakra.menu(
                        rx.chakra.menu_button(
                            rx.chakra.hstack(
                                rx.text("Resources", style=styles.NAV_TEXT_STYLE),
                                rx.icon(
                                    tag="chevron_down", style=styles.NAV_TEXT_STYLE
                                ),
                                cursor="pointer",
                                display=[
                                    "none",
                                    "none",
                                    "none",
                                    "flex",
                                    "flex",
                                    "flex",
                                ],
                            )
                        ),
                        rx.chakra.menu_list(
                            rx.link(
                                rx.chakra.menu_item(
                                    "Changelog", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href=changelog.path,
                            ),
                            rx.link(
                                rx.chakra.menu_item(
                                    "Roadmap", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href=constants.ROADMAP_URL,
                            ),
                            rx.link(
                                rx.chakra.menu_item(
                                    "FAQ", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href=faq.path,
                            ),
                            rx.chakra.menu_divider(),
                            rx.link(
                                rx.chakra.menu_item(
                                    "Contribute to Open Source",
                                    style=styles.NAV_DROPDOWN_STYLE,
                                ),
                                href=constants.CONTRIBUTING_URL,
                            ),
                            rx.link(
                                rx.chakra.menu_item(
                                    "Report A Bug",
                                    style=styles.NAV_DROPDOWN_STYLE,
                                ),
                                href=constants.REPORT_A_BUG_URL,
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
                        tag="menu",
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
                justify="between",
                padding_x=styles.PADDING_X,
            ),
            bg="rgba(255,255,255, 0.8)",
            backdrop_filter="blur(10px)",
            padding_y=["0.8em", "0.8em", "0.5em"],
            border_bottom="1px solid #F4F3F6",
            width="100%",
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    rx.hstack(
                        logo,
                        rx.icon(
                            tag="x-square",
                            on_click=NavbarState.set_sidebar_open(False),
                            width="4em",
                            _hover={
                                "cursor": "pointer",
                                "color": styles.ACCENT_COLOR,
                            },
                        ),
                        justify="between",
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
            on_close=NavbarState.set_sidebar_open(False),
            bg="rgba(255,255,255, 0.5)",
        ),
        search_modal(),
        position="sticky",
        z_index="999",
        top="0",
        width="100%",
        spacing="0",
    )
