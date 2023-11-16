"""UI and logic for the navbar component."""
from typing import Any, Set

import reflex as rx
from pcweb import constants, styles
from pcweb.base_state import State
from reflex.vars import ImportVar, Var
from pcweb.components.logo import navbar_logo
from pcweb.components.sidebar import sidebar as sb
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field
from datetime import datetime
from sqlalchemy import Column, JSON
from typing import Optional



def shorten_to_k(number):
    if number >= 1000:
        return "{:.0f}k+".format(number / 1000)
    else:
        return str(number)


class Search(rx.Component):
    tag = "InkeepEmbeddedChat"

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
          },
        },
      }
    },
  },
  aiChatSettings: { // optional typeof InkeepAIChatSettings
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
    meta: dict = Field(default={}, sa_column=Column(JSON))


class NavbarState(State):
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

    current_category = 'All'
    
    def handle_submit(self, form_data: dict):
        self.feedback = form_data["feedback"]

        # Check if the email is valid.
        if "email" in form_data:
            self.email = form_data["email"]
            try:
                validation = validate_email(self.email, check_deliverability=True)
                self.email = validation.email
            except EmailNotValidError as e:
                # Alert the error message.
                return rx.window_alert(str(e))

        current_page_route = self.get_current_page()
        # Check if the user is already on the waitlist.
        with rx.session() as session:
            
            # Add the feedback to database.
            session.add(Feedback(
                email=self.email,
                feedback=self.feedback,
                score=self.score,
                page=current_page_route,
                ),
            )
            session.commit()
            print("session")
            # contact_data = json.dumps({"email": self.email})
            # self.add_contact_to_loops(contact_data)


    def update_score(self, score):
        if self.show_form == True:
            if self.page_score == score:
                self.show_form = not self.show_form
        else:
            self.show_form = not self.show_form

        self.page_score = score

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

    @rx.var
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
        return client.collections["search-auto"].documents.search(search_parameters)[
            "hits"
        ]


def search_bar():
    return rx.hstack(
        rx.fragment(
            rx.icon(tag="search2", style=styles.NAV_SEARCH_STYLE),
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


def format_search_results(result):
    return rx.vstack(
            rx.link(
                rx.hstack(
                    rx.text(
                        result["document"]["heading"],
                        font_weight=600,
                        color="#1F1944",
                    ),
                    rx.spacer(),
                    rx.text(result["document"]["category"]),
                    width='100%'
                ),
                rx.divider(),
                rx.text(
                    result["document"]["description"],
                    no_of_lines=1,
                    font_weight=400,
                    color="#696287",
                ),
                on_click=NavbarState.close_search,
                href=result["document"]["href"],
                width="100%",
            ),
        bg="#FAF8FB",
        border_radius="8px",
        align_items="start",
        padding="0.5em",
        shadow=styles.DOC_SHADOW,
        _hover={"background_color": "#F5EFFE", "color": "#5646ED"},
        width="100%",
    )


def ai_button():
    return rx.center(
        rx.icon(
            tag="chat",
            color=rx.cond(
                NavbarState.ai_chat,
                "#342E5C",
                "#5646ED",      
            ),
        ),
        display=["none", "none", "none", "flex", "flex", "flex"],
        border_radius="8px",
        style=hover_button_style,
        on_click=NavbarState.toggle_ai_chat,
        height="1em",
    )


def search_bar_categories(categories):
    return rx.hstack(
        *[
            rx.button(
                category,
                border_radius="15px",
                padding_x=".5em",
                on_click=NavbarState.update_category(category),
                color="#5646ED",
                bg="#F5EFFE",
                _hover={
                    "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);",
                },
                _active={
                    "color": "white",
                    "bg": "#5646ED",
                },
            )
            for category in categories
        ],
        padding_y="1em",
        padding_x=".5em",
    )


def search_modal():
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header(
                    # add in filter tabs here categories
                    search_bar_categories(['All', 'Learn', 'Component', 'API Reference', 'Blog']),
                    rx.hstack(
                        rx.icon(tag="search2", style=styles.NAV_SEARCH_STYLE, height="1em",),
                        rx.input(
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
                rx.modal_body(
                    rx.vstack(
                        rx.cond(
                            NavbarState.ai_chat,
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
                            inkeep(),
                        ),
                    ),
                    width="100%",
                ),
                bg="#FFFFFF",
            max_width="50em",
            )
        ),
        is_open=NavbarState.search_modal,
        on_close=NavbarState.close_search,
        size="lg",
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
        rx.hstack(
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
        rx.center(
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
    return rx.form(
        rx.input(
            placeholder="Email",
            id="email",
            margin="0.25em 0.5em",
            width="24em",
            border_color="#eaeaef",
        ),
        rx.text_area(
            placeholder="Your Feedback",
            id="feedback",
            margin="0.25em 0.5em",
            width="24em",
            border_color="#eaeaef",
        ),
        rx.center(
            rx.button(
                "Send",
                type_="submit",
                style=styles.ACCENT_BUTTON,
                margin="0.5em",
            ),
            width="100%"
        ),
        on_submit=NavbarState.handle_submit,
        width="25em",
    )

def feedback_button():
    return rx.hstack(
        rx.menu(
            rx.menu_button(rx.text("Feedback", style=styles.NAV_TEXT_STYLE)),
            rx.menu_list(my_form()),
        ),
        display=["none", "none", "none", "none", "none", "flex"],
        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        padding_x=".5em",
        height="2em",
        border_radius="8px",
        bg="#FFFFFF",
        style=hover_button_style,
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
                            "✨ Reflex is in Hosting Alpha!",
                            " Learn more ",
                            rx.link(
                                "here",
                                href="https://www.notion.so/reflex-dev/Reflex-Hosting-Documentation-57a4dd55d6234858bbae0be75be79ce7?pvs=4",
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
                        tag="close",
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
                        href="/docs/getting-started/introduction",
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Blog",
                        href="/blog",
                        style=styles.NAV_TEXT_STYLE,
                        display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Gallery",
                        href="/docs/gallery",
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
                                    "flex",
                                    "flex",
                                    "flex",
                                ],
                            )
                        ),
                        rx.menu_list(
                            rx.link(
                                rx.menu_item(
                                    "Changelog", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href="/changelog",
                            ),
                            rx.link(
                                rx.menu_item(
                                    "Roadmap", style=styles.NAV_DROPDOWN_STYLE
                                ),
                                href=constants.ROADMAP_URL,
                            ),
                            rx.link(
                                rx.menu_item("FAQ", style=styles.NAV_DROPDOWN_STYLE),
                                href="/faq",
                            ),
                            rx.menu_divider(),
                            rx.link(
                                rx.menu_item(
                                    "Contribute to Open Source",
                                    style=styles.NAV_DROPDOWN_STYLE,
                                ),
                                href=constants.CONTRIBUTING_URL,
                            ),
                            rx.link(
                                rx.menu_item(
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
                    feedback_button(),
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
                justify="space-between",
                padding_x=styles.PADDING_X,
            ),
            bg="rgba(255,255,255, 0.9)",
            backdrop_filter="blur(10px)",
            padding_y=["0.8em", "0.8em", "0.5em"],
            border_bottom="1px solid #F4F3F6",
            width="100%",
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
        search_modal(),
        position="sticky",
        z_index="999",
        top="0",
        width="100%",
        spacing="0",
    )
