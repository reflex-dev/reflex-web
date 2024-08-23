"""Template for documentation pages."""

from typing import Callable

import reflex as rx
import flexdown
import mistletoe
from pcweb.route import Route, get_path
from .blocks import *
from .state import FeedbackState
from pcweb.components.icons.icons import get_icon
from pcweb.styles.colors import c_color
from pcweb.styles.fonts import small, medium, small_semibold
from pcweb.styles.shadows import shadows
import pcweb.templates.docpage.styles as st
from reflex.components.radix.themes.base import LiteralAccentColor
from pcweb.constants import GITHUB_URL, TWITTER_URL, DISCORD_URL

# Docpage styles.
link_style = {
    "color": rx.color("mauve", 10),
    "font_weight": "500",
}

footer_h4_style = {
    "color": c_color("slate", 12),
    "font-family": "Instrument Sans",
    "font-size": "14px",
    "font-style": "normal",
    "font-weight": "600",
    "line-height": "20px",
    "letter-spacing": "-0.21px",
}


def doc_section(*contents):
    return rx.box(
        *contents,
        margin_top="1em",
        margin_left=".5em",
        border_left="1px #F4F3F6 solid",
        padding_left="1em",
        width="100%",
    )


def footer_link(text: str, href: str):
    return rx.link(
        text,
        **small,
        color=c_color("slate", 9),
        _hover={
            "color": c_color("slate", 11),
        },
        style={
            ":hover": {
                "color": c_color("slate", 11),
            }
        },
        transition="color 0.075s ease-out",
        href=href,
        underline="none",
    )


def footer_link_flex(heading: str, links):
    return rx.flex(
        rx.heading(heading, as_="h4", style=footer_h4_style),
        *links,
        gap="16px",
        flex_direction="column",
    )


def thumb_card(score: int, icon: str) -> rx.Component:
    return rx.box(
        rx.icon(
            tag=icon,
            color=rx.cond(
                FeedbackState.score == score, c_color("slate", 11), c_color("slate", 9)
            ),
            size=16,
        ),
        height="36px",
        width="36px",
        padding="8px",
        border_radius="8px",
        align_items="center",
        display="flex",
        cursor="pointer",
        justify_content="center",
        border=f"1px solid {c_color('slate', 4)}",
        background_color=rx.cond(
            FeedbackState.score == score, c_color("slate", 3), c_color("white", 1)
        ),
        _hover={
            "background_color": c_color("slate", 3),
        },
        box_shadow=shadows["medium"],
        on_click=FeedbackState.set_score(score),
    )


def thumbs_cards() -> rx.Component:
    return rx.hstack(
        thumb_card(1, "thumbs-up"),
        thumb_card(0, "thumbs-down"),
        gap="8px",
    )


def feedback_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Send feedback",
                style={
                    "font-style": "normal",
                    "font-weight": "500",
                    "font-size": "16px",
                    "line-height": "28px",
                    "letter-spacing": "-0.015em",
                    "color": c_color("slate", 11),
                },
            ),
            rx.form(
                rx.vstack(
                    rx.el.textarea(
                        name="feedback",
                        placeholder="Write a comment…",
                        type="text",
                        max_length=500,
                        enter_key_submit=True,
                        resize="vertical",
                        style=st.text_area_style,
                        required=True,
                    ),
                    thumbs_cards(),
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="Contact email (optional)",
                        style=st.input_style,
                        max_length=100,
                    ),
                    rx.hstack(
                        rx.popover.close(
                            rx.el.button(
                                rx.box(
                                    style=st.rectangle_style,
                                ),
                                "Send",
                                style=st.send_button_style,
                                type="submit",
                            ),
                        ),
                        rx.popover.close(
                            rx.el.button("Cancel", style=st.cancel_button_style)
                        ),
                        align="center",
                        justify="between",
                        width="100%",
                    ),
                    gap="16px",
                    align="start",
                    width="100%",
                ),
                width="100%",
                reset_on_submit=True,
                on_submit=FeedbackState.handle_submit,
            ),
            gap="16px",
            align="start",
            width="100%",
        ),
        style=st.feedback_box_style,
    )


def feedback_button() -> rx.Component:
    return rx.popover.root(
        rx.hstack(
            rx.popover.trigger(
                rx.hstack(
                    rx.icon(tag="thumbs-up", size=15, color=c_color("slate", 9)),
                    rx.text(
                        "Yes",
                    ),
                    style=st.thumb_pill_style,
                    border_radius="20px 0 0 20px",
                    padding="2px 12px",
                    gap="8px",
                    border_right="none",
                    width="100%",
                ),
                on_click=FeedbackState.set_score(1),
            ),
            rx.popover.trigger(
                rx.hstack(
                    rx.icon(tag="thumbs-down", size=15, color=c_color("slate", 9)),
                    rx.text(
                        "No",
                    ),
                    style=st.thumb_pill_style,
                    gap="8px",
                    padding="2px 12px",
                    border_radius="0 20px 20px 0",
                    width="100%",
                ),
                on_click=FeedbackState.set_score(0),
            ),
            align_items="center",
            gap="0px",
            width=["100%", "100%", "auto", "auto", "auto"],
        ),
        rx.popover.content(
            feedback_content(),
            bg="transparent",
            box_shadow="None",
            overflow="visible",
            left=["0px", "0px", "-255px", "-255px", "-255px"],
            padding="0px",
            border="none",
            align="start",
            transform_origin=[
                "bottom",
                "bottom",
                "bottom right",
                "bottom right",
                "bottom right",
            ],
            avoid_collisions=True,
        ),
    )


def link_pill(text, href):
    return rx.link(
        text,
        style=st.pill_style,
        href=href,
        underline="none",
        _hover={
            "background-color": c_color("slate", 3),
            "color": c_color("slate", 9),
        },
    )


def social_menu_item(
    icon: str,
    url="/",
    border: bool = False,
    border_color: list = [
        f"1px solid {c_color('slate', 1)}",
        f"1px solid {c_color('slate', 1)}",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
    ],
    **props,
) -> rx.Component:
    return rx.link(
        rx.box(
            get_icon(icon, color=c_color("slate", 9)),
            style={
                "display": "flex",
                "padding": "4px 12px",
                "justify-content": "center",
                "align-items": "center",
                "gap": "8px",
                "align-self": "stretch",
                "cursor": "pointer",
                ":hover": {"background_color": c_color("slate", 3)},
                "transition": "background 0.075s ease-out",
                "overflow": "hidden",
            },
            _hover={
                "background_color": c_color("slate", 3),
            },
            **props,
            overflow="hidden",
            border_left=border_color if border else "none",
            border_right=border_color if border else "none",
        ),
        width="100%",
        href=url,
        is_external=True,
    )


def menu_socials() -> rx.Component:
    return rx.box(
        rx.hstack(
            social_menu_item("github", GITHUB_URL),
            social_menu_item("twitter", TWITTER_URL, border=True),
            social_menu_item("discord", DISCORD_URL),
            gap="0px",
            width="auto",
            align="center",
        ),
        style={
            "border-radius": ["8px", "8px", "20px", "20px", "20px"],
            "overflow": "hidden",
            "height": "auto",
            "border": [
                "none",
                "none",
                f"1px solid {c_color('slate', 5)}",
                f"1px solid {c_color('slate', 5)}",
                f"1px solid {c_color('slate', 5)}",
            ],
            "background": [
                c_color("slate", 3),
                c_color("slate", 3),
                c_color("slate", 1),
                c_color("slate", 1),
                c_color("slate", 1),
            ],
            "box-shadow": [
                "none",
                "none",
                shadows["large"],
                shadows["large"],
                shadows["large"],
            ],
        },
        width=["100%", "100%", "auto", "auto", "auto"],
    )


@rx.memo
def docpage_footer(path: str):
    from pcweb.pages.docs.gallery import gallery
    from pcweb.pages.docs import getting_started, hosting
    from pcweb.pages.docs.library import library
    from pcweb.pages.changelog import changelog
    from pcweb.pages.blog import blogs
    from pcweb.pages.changelog import changelog
    from pcweb.pages.faq import faq
    from pcweb.pages.errors import errors
    from pcweb.signup import IndexState
    from pcweb.constants import ROADMAP_URL, GITHUB_DISCUSSIONS_URL

    return rx.el.footer(
        rx.flex(
            rx.flex(
                rx.text(
                    "Did you find this useful?",
                    color=[
                        c_color("slate", 11),
                        c_color("slate", 11),
                        c_color("slate", 9),
                        c_color("slate", 9),
                        c_color("slate", 9),
                    ],
                    style={**small},
                    white_space="nowrap",
                ),
                feedback_button(),
                width="100%",
                padding=["16px", "16px", "0px", "0px", "0px"],
                align_items="center",
                border_radius="8px",
                gap=["12px", "12px", "16px", "16px", "16px"],
                background_color=[
                    c_color("slate", 3),
                    c_color("slate", 3),
                    "transparent",
                    "transparent",
                    "transparent",
                ],
                flex_direction=["column", "column", "row", "row", "row"],
            ),
            rx.flex(
                rx.desktop_only(
                    link_pill(
                        "Raise an issue",
                        href=f"https://github.com/reflex-dev/reflex-web/issues/new?title=Issue with reflex.dev documentation&amp;body=Path: {path}",
                    )
                ),
                rx.desktop_only(
                    link_pill(
                        "Edit this page",
                        f"https://github.com/reflex-dev/reflex-web/tree/main{path}.md",
                    ),
                ),
                display=["none", "none", "flex", "flex", "flex"],
                gap="8px",
            ),
            padding_top=["0px", "0px", "32px", "32px"],
            padding_bottom=["24px", "24px", "32px", "32px"],
            justify_content=["center", "center", "center", "space-between"],
            align_items="center",
            width="100%",
        ),
        rx.flex(
            rx.flex(
                menu_socials(),
                gap="8px",
                width=["100%", "100%", "auto", "auto", "auto"],
                margin_bottom=["24px", "24px", "0px", "0px", "0px"],
                display=["flex", "flex", "none", "none", "none"],
            ),
            # rx.flex(
            #     link_pill("Home", "/"),
            #     link_pill("Gallery", gallery.path),
            #     link_pill("Changelog", changelog.path),
            #     link_pill("Introduction", getting_started.introduction.path),
            #     link_pill("Hosting", hosting.deploy_quick_start.path),
            #     gap="8px",
            #     flex_direction=["column", "column", "row", "row", "row"],
            #     flex_shrink=0,
            #     width=["100%", "100%", "auto", "auto", "auto"],
            #     display=["none", "none", "none", "none", "none"], # Replaced for the new footer layout
            # ),
            justify="between",
            padding_y="0px",
            align_items="center",
            width="100%",
            flex_direction=["column", "column", "row", "row", "row"],
        ),
        rx.flex(
            rx.flex(
                footer_link_flex(
                    "Links",
                    [
                        footer_link("Home", "/"),
                        footer_link("Showcase", gallery.path),
                        footer_link("Blog", blogs.path),
                        footer_link("Changelog", changelog.path),
                    ],
                ),
                footer_link_flex(
                    "Documentation",
                    [
                        footer_link("Introduction", getting_started.introduction.path),
                        footer_link("Installation", getting_started.installation.path),
                        footer_link("Components", library.path),
                        footer_link("Hosting", hosting.deploy_quick_start.path),
                    ],
                ),
                footer_link_flex(
                    "Resources",
                    [
                        footer_link("FAQ", faq.path),
                        footer_link("Common Errors", errors.path),
                        footer_link("Roadmap", ROADMAP_URL),
                        footer_link("Forum", GITHUB_DISCUSSIONS_URL),
                    ],
                ),
                flex_wrap="wrap",
                gap="48px",
                width="100%",
                justify_content="space-between",
            ),
            rx.flex(
                rx.heading("Join Newsletter", as_="h4", style=footer_h4_style),
                rx.text(
                    "Get the latest updates and news about Reflex.",
                    style=small,
                    color=c_color("slate", 9),
                ),
                rx.cond(
                    IndexState.signed_up,
                    rx.flex(
                        rx.hstack(
                            rx.icon(
                                tag="circle-check",
                                size=14,
                                color=c_color("violet", 9),
                            ),
                            rx.text(
                                "Thanks for subscribing!",
                                style=small_semibold,
                                color=c_color("slate", 11),
                            ),
                            gap="8px",
                            align_items="center",
                        ),
                        rx.el.button(
                            "Sign up for another email.",
                            style=small,
                            color=c_color("slate", 9),
                            background_color=c_color("slate", 3),
                            border_radius="10px",
                            padding="8px 14px",
                            cursor="pointer",
                            _hover={"background_color": c_color("slate", 4)},
                            on_click=IndexState.signup_for_another_user,
                        ),
                        gap="8px",
                        flex_wrap="wrap",
                        flex_direction="column",
                    ),
                    rx.form(
                        rx.flex(
                            rx.el.input(
                                placeholder="Your email",
                                name="input_email",
                                type="email",
                                padding="8px 12px",
                                color=c_color("slate", 11),
                                background_color=c_color("white", 1),
                                border_radius="10px",
                                border=f"1px solid {c_color('slate', 5)}",
                                box_sizing="border-box",
                                outline="none",
                                style={
                                    "&::placeholder": {"color": c_color("slate", 9)},
                                },
                                _focus={
                                    "outline": f"2px solid {c_color('violet', 9)}",
                                },
                                **small,
                            ),
                            rx.form.submit(
                                rx.el.button(
                                    "Subscribe",
                                    display="flex",
                                    padding="8px 14px",
                                    justify_content="center",
                                    background_color=c_color("slate", 4),
                                    border_radius="10px",
                                    align_items="center",
                                    color=c_color("slate", 9),
                                    cursor="pointer",
                                    _hover={"background_color": c_color("slate", 5)},
                                    transition="background 0.075s ease-out",
                                    **small_semibold,
                                ),
                                as_child=True,
                            ),
                            gap="8px",
                            align_items="center",
                        ),
                        on_submit=IndexState.signup,
                    ),
                ),
                flex_direction="column",
                align_items="start",
                gap="16px",
            ),
            rx.flex(
                rx.text(
                    "Copyright © 2024 Pynecone, Inc.",
                    style=small,
                    color=c_color("slate", 9),
                ),
                rx.flex(
                    menu_socials(),
                    gap="8px",
                    width=["100%", "100%", "auto", "auto", "auto"],
                    margin_bottom=["0px", "0px", "8px", "8px", "8px"],
                    display=["none", "none", "flex", "flex", "flex"],
                ),
                justify_content="space-between",
                flex_direction="row",
                align_items="center",
                width="100%",
            ),
            justify_content="space-between",
            flex_direction="column",
            width="100%",
            gap="40px",
            border_top=f"1px solid {c_color('slate', 4)}",
            padding_y=["24px", "24px", "32px", "32px", "32px"],
            display="flex",
        ),
        display="flex",
        max_width=["100%", "auto"],
        padding_bottom=["16px", "16px", "32px", "32px", "32px"],
        flex_direction="column",
    )


def drawer_item(text: str, href: str):
    return rx.link(
        text,
        href=href,
        display="flex",
        underline="none",
        justify_content="center",
        align_items="center",
        padding="14px 16px",
        width="100%",
        color=c_color("slate", 9),
        _hover={
            "color": c_color("slate", 9),
        },
        style={
            ":hover": {
                "color": c_color("slate", 9),
            },
            **small,
        },
        border_bottom=f"1px solid {c_color('slate', 4)}",
    )


def drawer_socials():
    return rx.hstack(
        social_menu_item("github", GITHUB_URL, height="47px"),
        social_menu_item(
            "twitter",
            TWITTER_URL,
            border=True,
            border_color=[f"1px solid {c_color('slate', 4)}"],
            height="47px",
        ),
        social_menu_item("discord", DISCORD_URL, height="47px"),
        border_bottom=f"1px solid {c_color('slate', 4)}",
        gap="0px",
        width="100%",
        align="center",
    )


def breadcrumb(path, nav_sidebar):
    from pcweb.components.docpage.navbar.buttons.sidebar import docs_sidebar_drawer

    overflow_style = {
        "overflow": "hidden",
        "text_overflow": "ellipsis",
        "white_space": "nowrap",
    }
    # Split the path into segments, removing 'docs' and capitalizing each segment
    segments = [
        segment.capitalize()
        for segment in path.split("/")
        if segment and segment != "docs"
    ]

    # Initialize an empty list to store the breadcrumbs and their separators
    breadcrumbs = []

    # Iteratively build the href for each segment
    for i in range(len(segments)):
        # Add the breadcrumb item to the list
        breadcrumbs.append(
            rx.text(
                segments[i],
                color=c_color("slate", 9),
                style=small,
                **(overflow_style if i == len(segments) - 1 else {}),
            )
        )

        # If it's not the last segment, add a separator
        if i < len(segments) - 1:
            breadcrumbs.append(
                rx.icon(
                    tag="chevron-right",
                    size=14,
                    color=c_color("slate", 8),
                    display=["none", "none", "none", "flex", "flex"],
                ),
            )
            breadcrumbs.append(
                rx.text(
                    "/",
                    display=["flex", "flex", "flex", "none", "none"],
                    style=small,
                    color=c_color("slate", 8),
                )
            )

    # Return the list of breadcrumb items with separators
    return rx.flex(
        rx.hstack(
            *breadcrumbs,
            align_items="center",
            gap=["5px", "16px"],
            overflow="hidden",
        ),
        docs_sidebar_drawer(
            nav_sidebar,
            trigger=rx.el.button(
                rx.icon(tag="chevron-down", size=14, color=c_color("slate", 9)),
                padding="9px",
                display=["flex", "flex", "flex", "flex", "none", "none"],
            ),
        ),
        padding=[
            "8px 12px 8px 16px",
            "8px 19.5px 8px 24px",
            "8px 19.5px 8px 24px",
            "0px",
            "0px",
        ],
        gap=["16px", "0px"],
        align_items="center",
        margin_bottom=["24px", "24px", "24px", "48px"],
        margin_top=["48px", "64px", "64px", "119px"],
        border_bottom=[
            f"1px solid {c_color('slate', 4)}",
            f"1px solid {c_color('slate', 4)}",
            f"1px solid {c_color('slate', 4)}",
            f"1px solid {c_color('slate', 4)}",
            "none",
            "none",
        ],
        justify_content="space-between",
        width="100%",
        z_index="10",
        position="relative",
        background_color=c_color("slate", 1),
    )


def get_headings(comp):
    """Get the strings from markdown component."""
    if isinstance(comp, mistletoe.block_token.Heading):
        heading_text = "".join(
            token.content for token in comp.children if hasattr(token, "content")
        )
        return [(comp.level, heading_text)]

    # Recursively get the strings from the children.
    if not hasattr(comp, "children") or comp.children is None:
        return []

    headings = []
    for child in comp.children:
        headings.extend(get_headings(child))
    return headings


def get_toc(source, href, component_list=None):
    from pcweb.flexdown import xd

    component_list = component_list or []
    component_list = component_list[1:]

    # Generate the TOC
    # The environment used for execing and evaling code.
    env = source.metadata
    env["__xd"] = xd

    # Get the content of the document.
    source = source.content

    # Get the blocks in the source code.
    # Note: we must use reflex-web's special flexdown instance xd here - it knows about all custom block types (like DemoBlock)
    blocks = xd.get_blocks(source, href)

    content_pieces = []
    for block in blocks:
        if (
            not isinstance(block, flexdown.blocks.MarkdownBlock)
            or len(block.lines) == 0
            or not block.lines[0].startswith("#")
        ):
            continue
        # Now we should have all the env entries we need
        content = block.get_content(env)
        content_pieces.append(content)

    content = "\n".join(content_pieces)
    doc = mistletoe.Document(content)

    # Parse the markdown headers.
    headings = get_headings(doc)

    if len(component_list):
        headings.append((1, "API Reference"))
    for component_tuple in component_list:
        headings.append((2, component_tuple[1]))
    return headings


def docpage(
    set_path: str | None = None, t: str | None = None, right_sidebar: bool = True
) -> rx.Component:
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        prop: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """

    def docpage(contents: Callable[[], Route]) -> Route:
        """Wrap a component in a docpage template.

        Args:
            contents: A function that returns a page route.

        Returns:
            The final route with the template applied.
        """
        # Get the path to set for the sidebar.
        path = get_path(contents) if set_path is None else set_path
        # Set the page title.
        title = contents.__name__.replace("_", " ").title() if t is None else t

        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.docpage.navbar import navbar
            from pcweb.components.docpage.sidebar import get_prev_next
            from pcweb.components.docpage.sidebar import sidebar as sb

            # Create the docpage sidebar.
            sidebar = sb(url=path, width="280px")

            # Set the sidebar path for the navbar sidebar.
            nav_sidebar = sb(url=path, width="100%")

            # Get the previous and next sidebar links.
            prev, next = get_prev_next(path)
            links = []

            # Create the previous component link.
            if prev:
                next_prev_name = (
                    prev.alt_name_for_next_prev
                    if prev.alt_name_for_next_prev
                    else prev.names
                )
                links.append(
                    rx.link(
                        rx.hstack(
                            get_icon(icon="arrow_right", transform="rotate(180deg)"),
                            next_prev_name,
                            align_items="center",
                            gap="8px",
                            width="100%",
                            justify_content=[
                                "center",
                                "center",
                                "flex-start",
                                "flex-start",
                                "flex-start",
                            ],
                            border_radius="8px",
                        ),
                        underline="none",
                        href=prev.link,
                        _hover={"color": c_color("slate", 11)},
                        transition="color 0.035s ease-out",
                        background_color=[
                            c_color("slate", 3),
                            c_color("slate", 3),
                            "transparent",
                            "transparent",
                            "transparent",
                        ],
                        border_radius="8px",
                        padding=["2px 6px", "2px 6px", "0px", "0px", "0px"],
                        style={
                            "color": c_color("slate", 9),
                            **small,
                            ":hover": {"color": c_color("slate", 11)},
                        },
                        width=["100%", "100%", "auto", "auto", "auto"],
                    )
                )
            else:
                links.append(rx.box())

            # Create the next component link.
            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.link(
                        rx.hstack(
                            next_prev_name,
                            get_icon(icon="arrow_right"),
                            align_items="center",
                            gap="8px",
                            width="100%",
                            justify_content=[
                                "center",
                                "center",
                                "flex-end",
                                "flex-end",
                                "flex-end",
                            ],
                            background_color=[
                                c_color("slate", 3),
                                c_color("slate", 3),
                                "transparent",
                                "transparent",
                                "transparent",
                            ],
                            padding=["2px 6px", "2px 6px", "0px", "0px", "0px"],
                            border_radius="8px",
                        ),
                        underline="none",
                        href=next.link,
                        _hover={"color": c_color("slate", 11)},
                        transition="color 0.035s ease-out",
                        style={
                            "color": c_color("slate", 9),
                            **small,
                            ":hover": {"color": c_color("slate", 11)},
                        },
                        width=["100%", "100%", "auto", "auto", "auto"],
                    ),
                )
            else:
                links.append(rx.box())

            toc = []
            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            if isinstance(comp, tuple):
                toc, comp = comp

            # Return the templated page.
            return rx.flex(
                navbar(),
                rx.el.main(
                    rx.box(
                        sidebar,
                        margin_top="105px",
                        height="100%",
                        width="24%",
                        display=["none", "none", "none", "none", "flex", "flex"],
                        flex_shrink=0,
                    ),
                    rx.box(
                        rx.box(
                            breadcrumb(path, nav_sidebar),
                            padding_x=[
                                "0px",
                                "0px",
                                "0px",
                                "48px",
                                "96px",
                            ],
                        ),
                        rx.box(
                            rx.el.article(comp),
                            rx.el.nav(
                                *links,
                                justify="between",
                                margin_top=["32px", "32px", "40px", "40px", "40px"],
                                margin_bottom=[
                                    "24px",
                                    "24px",
                                    "24px",
                                    "48px",
                                    "48px",
                                ],
                                gap="8px",
                                display="flex",
                                flex_direction="row",
                                justify_content="space-between",
                            ),
                            docpage_footer(path=path),
                            padding_x=["16px", "24px", "24px", "48px", "96px"],
                            margin_top=["105px", "145px", "0px", "0px", "0px"],
                        ),
                        width=(
                            ["100%", "100%", "100%", "100%", "70%", "60%"]
                            if right_sidebar
                            else "100%"
                        ),
                        height="100%",
                    ),
                    rx.el.nav(
                        rx.flex(
                            rx.heading(
                                "On this page",
                                as_="h5",
                                style={
                                    "color": c_color("slate", 12),
                                    "font-family": "Instrument Sans",
                                    "font-size": "14px",
                                    "font-style": "normal",
                                    "font-weight": "600",
                                    "line-height": "20px",
                                    "letter-spacing": "-0.21px",
                                },
                            ),
                            rx.unordered_list(
                                *[
                                    (
                                        rx.list_item(
                                            rx.link(
                                                text,
                                                style={
                                                    "transition": "color 0.035s ease-out",
                                                    "color": c_color("slate", 9),
                                                    "overflow": "hidden",
                                                    "text-overflow": "ellipsis",
                                                    "white-space": "nowrap",
                                                    **small,
                                                    ":hover": {
                                                        "color": c_color("slate", 11),
                                                    },
                                                },
                                                _hover={
                                                    "color": c_color("slate", 11),
                                                },
                                                underline="none",
                                                href=path
                                                + "#"
                                                + text.lower().replace(" ", "-"),
                                            )
                                        )
                                        if level == 1
                                        else (
                                            rx.list_item(
                                                rx.link(
                                                    text,
                                                    style={
                                                        "transition": "color 0.035s ease-out",
                                                        "overflow": "hidden",
                                                        "text-overflow": "ellipsis",
                                                        "white-space": "nowrap",
                                                        "color": c_color("slate", 9),
                                                        **small,
                                                        ":hover": {
                                                            "color": c_color(
                                                                "slate", 11
                                                            ),
                                                        },
                                                    },
                                                    _hover={
                                                        "color": c_color("slate", 11),
                                                    },
                                                    underline="none",
                                                    href=path
                                                    + "#"
                                                    + text.lower().replace(" ", "-"),
                                                )
                                            )
                                            if level == 2
                                            else rx.list_item(
                                                rx.link(
                                                    text,
                                                    style={
                                                        "transition": "color 0.035s ease-out",
                                                        "overflow": "hidden",
                                                        "text-overflow": "ellipsis",
                                                        "white-space": "nowrap",
                                                        "color": c_color("slate", 9),
                                                        **small,
                                                        ":hover": {
                                                            "color": c_color(
                                                                "slate", 11
                                                            ),
                                                        },
                                                    },
                                                    _hover={
                                                        "color": c_color("slate", 11),
                                                    },
                                                    underline="none",
                                                    padding_left="24px",
                                                    href=path
                                                    + "#"
                                                    + text.lower().replace(" ", "-"),
                                                )
                                            )
                                        )
                                    )
                                    for level, text in toc
                                ],
                                list_style_type="none",
                                display="flex",
                                gap="16px",
                                flex_direction="column",
                                margin_left="0px !important",
                            ),
                            direction="column",
                            width="100%",
                            position="fixed",
                            gap="16px",
                            padding="14px 8px 0px 8px",
                            max_width="280px",
                            justify="start",
                            overflow="hidden",
                            max_height="80vh",
                            overflow_y="scroll",
                        ),
                        margin_top="105px",
                        width="18%",
                        height="100%",
                        display=(
                            ["none", "none", "none", "none", "none", "flex"]
                            if right_sidebar
                            else "none"
                        ),
                        flex_shrink=0,
                    ),
                    max_width="110em",
                    margin_left="auto",
                    margin_right="auto",
                    margin_top="0px",
                    height="100%",
                    min_height="100vh",
                    width="100%",
                    display="flex",
                    flex_direction="row",
                ),
                background=c_color("slate", 1),
                width="100%",
                justify="center",
                flex_direction="column",
            )

        # Return the route.
        components = path.split("/")
        category = (
            " ".join(
                word.capitalize() for word in components[2].replace("-", " ").split()
            )
            if len(components) > 2
            else None
        )
        return Route(
            path=path,
            title=f"{title} · Reflex Docs" if category is None else title,
            component=wrapper,
        )

    return docpage


class RadixDocState(rx.State):
    """The app state."""

    color: str = "tomato"


def hover_item(component: rx.Component, component_str: str) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(rx.flex(component)),
        rx.hover_card.content(
            # rx.code_block(f"{component_str}", can_copy=True, language="python"),
            rx.el.button(
                get_icon(icon="copy", padding="5px"),
                rx.text(
                    component_str,
                    as_="p",
                    overflow="hidden",
                    white_space="nowrap",
                    style=small,
                    text_overflow="ellipsis",
                    flex_grow=1,
                    flex_shrink=1,
                    min_width=0,
                ),
                gap="6px",
                color=c_color("slate", 9),
                width="100%",
                padding_right="6px",
                align_items="center",
                background=c_color("slate", 1),
                border_radius="6px",
                box_shadow=shadows["small"],
                on_click=rx.set_clipboard(component_str),
                cursor="pointer",
                _hover={
                    "transition": "background 0.075s ease-out",
                    "background": c_color("slate", 3),
                },
                border=f"1px solid {c_color('slate', 5)}",
                display="flex",
                flex_direction="row",
                max_width="300px",
            ),
        ),
    )


def dict_to_formatted_string(input_dict):
    # List to hold formatted string parts
    formatted_parts = []

    # Iterate over dictionary items
    for key, value in input_dict.items():
        # Format each key-value pair
        if isinstance(value, str):
            formatted_part = f'{key}="{value}"'  # Enclose string values in quotes
        else:
            formatted_part = f"{key}={value}"  # Non-string values as is

        # Append the formatted part to the list
        formatted_parts.append(formatted_part)

    # Join all parts with a comma and a space
    return ", ".join(formatted_parts)


def used_component(
    component_used: rx.Component,
    components_passed: rx.Component | str | None,
    color_scheme: str,
    variant: str,
    high_contrast: bool,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    if components_passed is None and disabled is False:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is not None and disabled is False:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is None and disabled is True:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )

    else:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )


def style_grid(
    component_used: rx.Component,
    component_used_str: str,
    variants: list,
    components_passed: rx.Component | str | None = None,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    text_style = {"color": c_color("slate", 11), "text-wrap": "nowrap", **medium}
    return rx.vstack(
        rx.grid(
            rx.text("", size="5"),
            *[
                rx.text(variant, style=text_style, color=c_color("slate", 11))
                for variant in variants
            ],
            rx.text(
                "Accent", style=text_style, color=f"var(--{RadixDocState.color}-10)"
            ),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("Gray", style=text_style, color=c_color("slate", 11)),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            (
                rx.fragment(
                    rx.text("Disabled", style=text_style, color=c_color("slate", 11)),
                    *[
                        hover_item(
                            component=used_component(
                                component_used=component_used,
                                components_passed=components_passed,
                                color_scheme="gray",
                                variant=variant,
                                high_contrast=True,
                                disabled=disabled,
                                **kwargs,
                            ),
                            component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, disabled=True, {dict_to_formatted_string(kwargs)})",
                        )
                        for variant in variants
                    ],
                )
                if disabled
                else ""
            ),
            flow="column",
            columns="5",
            rows=str(len(variants) + 1),
            spacing="3",
        ),
        rx.popover.root(
            rx.popover.trigger(
                rx.box(
                    rx.button(
                        rx.text(RadixDocState.color, style=small),
                        # Match the select.trigger svg icon
                        rx.html(
                            """<svg width="9" height="9" viewBox="0 0 9 9" fill="currentcolor" xmlns="http://www.w3.org/2000/svg" class="rt-SelectIcon" aria-hidden="true"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg>"""
                        ),
                        color_scheme=RadixDocState.color,
                        width="8em",
                        variant="surface",
                        justify_content="space-between",
                    ),
                    margin_top="18px",
                ),
            ),
            rx.popover.content(
                rx.grid(
                    *[
                        rx.box(
                            rx.icon(
                                "check",
                                color=rx.color("gray", 12),
                                size=15,
                                position="absolute",
                                top="50%",
                                left="50%",
                                transform="translate(-50%, -50%)",
                                display=rx.cond(
                                    RadixDocState.color == color, "block", "none"
                                ),
                            ),
                            width="30px",
                            height="30px",
                            border_radius="max(var(--radius-2), var(--radius-full))",
                            bg=f"var(--{color}-9)",
                            cursor="pointer",
                            position="relative",
                            flex_shrink=0,
                            on_click=RadixDocState.setvar("color", color),
                            border=rx.cond(
                                RadixDocState.color == color,
                                "2px solid var(--gray-12)",
                                "",
                            ),
                        )
                        for color in list(map(str, LiteralAccentColor.__args__))
                    ],
                    columns="6",
                    spacing="3",
                ),
            ),
        ),
        padding="24px",
        border_radius="12px",
        border=f"1px solid {c_color('slate', 4)}",
        background=c_color("slate", 2),
    )


def icon_grid(
    category_name: str, icon_tags: list[str], columns: str = "4"
) -> rx.Component:
    return rx.flex(
        rx.callout.root(
            rx.callout.icon(
                rx.icon(
                    tag="circle_check_big",
                    width=18,
                    height=18,
                )
            ),
            rx.callout.text(
                f"Below is a list of all available ",
                rx.text(category_name, weight="bold"),
                " icons.",
                color="black",
            ),
            color="green",
        ),
        rx.divider(size="4"),
        rx.grid(
            *[
                rx.flex(
                    rx.icon(tag=icon_tag, alias="Radix" + icon_tag.title()),
                    rx.text(icon_tag),
                    direction="column",
                    align="center",
                    bg="white",
                    border="1px solid #EAEAEA",
                    border_radius="0.5em",
                    padding=".75em",
                )
                for icon_tag in icon_tags
            ],
            columns=columns,
            spacing="1",
        ),
        direction="column",
        spacing="2",
    )
