"""Template for documentation pages."""

from typing import Callable

import reflex as rx
import flexdown
import mistletoe
from pcweb.route import Route, get_path
from .blocks import *
from .state import FeedbackState

# Docpage styles.
link_style = {
    "color": rx.color("mauve", 10),
    "font_weight": "500",
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


def feedback_content(icon, score):
    return rx.flex(
        rx.button(
            rx.icon(tag=icon, color=rx.color("mauve", 1), size=20), variant="solid"
        ),
        rx.box(
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Contact Info (Optional)",
                        _type="email",
                        name="email",
                        custom_attrs={"auto_focus": True},
                    ),
                    rx.text_area(
                        placeholder="Write a comment…",
                        name="feedback",
                        auto_height=True,
                        enter_key_submit=True,
                        min_height="0px",
                        rows="1",
                    ),
                    spacing="1",
                    direction="column",
                ),
                rx.flex(
                    rx.button(
                        "Send Feedback", size="1", width="100%", type="submit"
                    ),
                    spacing="3",
                    margin_top="12px",
                    justify="between",
                ),
                on_submit=lambda feedback: FeedbackState.handle_submit(feedback, score),
            ),
            flex_grow="1",
        ),
        spacing="3",
    )


def feedback(text, icon, score):
    return rx.popover.root(
        rx.popover.trigger(
            rx.flex(
                rx.icon(tag=icon, color=rx.color("mauve", 9), size=12),
                text,
                color=rx.color("mauve", 9),
                border=f"1px solid {rx.color('mauve', 10)}",
                align="center",
                justify="center",
                border_radius="5px",
                padding="0px 10px",
                spacing="2",
                cursor="pointer",
            )
        ),
        rx.popover.content(
            feedback_content(icon, score),
            style={"width": 360},
        ),
        on_open_change=lambda change: FeedbackState.feedback_change(change, score),
        open=FeedbackState.feedback_open[score],
    )


@rx.memo
def docpage_footer(path: str):
    from pcweb.pages.docs.gallery import gallery
    from pcweb.pages.docs import getting_started, hosting
    from pcweb.pages.changelog import changelog
    return rx.flex(
        rx.divider(size="4"),
        rx.flex(
            rx.flex(
                rx.text(
                    "Did you find this useful?",
                    color=rx.color("mauve", 10),
                    font_weight="400",
                    white_space="nowrap",
                ),
                rx.divider(size="4", orientation="vertical"),
                feedback(
                    text="No",
                    icon="thumbs_down",
                    score=0,
                ),
                feedback(
                    text="Yes",
                    icon="thumbs_up",
                    score=1,
                ),
                align_items="center",
                spacing="2",
            ),
            rx.box(
                flex_grow="1",
            ),
            rx.divider(size="4", orientation="vertical"),
            rx.flex(
                rx.desktop_only(
                    rx.link(
                        rx.flex(
                            "Raise an issue",
                            color=rx.color("mauve", 9),
                            border=f"1px solid {rx.color('mauve', 9)}",
                            align="center",
                            justify="center",
                            border_radius="5px",
                            padding="0px 10px",
                            white_space="nowrap",
                        ),
                        href=f"https://github.com/reflex-dev/reflex-web/issues/new?title=Issue with reflex.dev documentation&amp;body=Path: {path}",
                    )
                ),
                rx.desktop_only(
                    rx.link(
                        rx.flex(
                            "Edit this page",
                            color=rx.color("mauve", 9),
                            border=f"1px solid {rx.color('mauve', 9)}",
                            align="center",
                            justify="center",
                            border_radius="5px",
                            padding="0px 10px",
                            white_space="nowrap",
                        ),
                        href=f"https://github.com/reflex-dev/reflex-web/tree/main{path}.md",
                    )
                ),
                spacing="2",
            ),
            align_items="center",
            width="100%",
        ),
        rx.divider(size="4"),
        rx.flex(
            rx.flex(
                rx.link(
                    "Home", color=rx.color("mauve", 9), underline="always", href="/"
                ),
                rx.link(
                    "Gallery",
                    color=rx.color("mauve", 9),
                    underline="always",
                    href=gallery.path,
                ),
                rx.link(
                    "Changelog",
                    color=rx.color("mauve", 9),
                    underline="always",
                    href=changelog.path,
                ),
                rx.link(
                    "Introduction",
                    color=rx.color("mauve", 9),
                    underline="always",
                    href=getting_started.introduction.path,
                ),
                rx.link(
                    "Hosting",
                    color=rx.color("mauve", 9),
                    underline="always",
                    href=hosting.deploy_quick_start.path,
                ),
                spacing="2",
                flex_shrink=0,
            ),
            rx.box(
                flex_grow="1",
            ),
            rx.flex(
                rx.link(
                    rx.image(
                        src="/companies/light/github.svg",
                    ),
                    href="https://github.com/reflex-dev/reflex",
                ),
                rx.link(
                    rx.image(
                        src="/companies/light/twitter.svg",
                    ),
                    href="https://twitter.com/getreflex",
                ),
                rx.link(
                    rx.image(
                        src="/companies/light/discord.svg",
                    ),
                    href="https://discord.gg/T5WSbC2YtQ",
                ),
                rx.link(
                    rx.image(
                        src="/companies/light/linkedin.svg",
                    ),
                    href="https://www.linkedin.com/company/reflex-dev",
                ),
                spacing="2",
            ),
            align_items="center",
            width="100%",
        ),
        direction="column",
        spacing="2",
        margin_bottom="2em",
    )


def breadcrumb(path):
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
        breadcrumbs.append(rx.text(segments[i], color=rx.color("mauve", 9)))

        # If it's not the last segment, add a separator
        if i < len(segments) - 1:
            breadcrumbs.append(rx.text("/", color=rx.color("mauve", 9)))

    # Return the list of breadcrumb items with separators
    return rx.flex(*breadcrumbs, spacing="2")


def get_headings(comp):
    """Get the strings from markdown component."""
    if isinstance(comp, mistletoe.block_token.Heading):
        heading_text = "".join(
            token.content for token in comp.children if hasattr(token, "content")
        )
        return [(comp.level, heading_text)]

    # Recursively get the strings from the children.
    if not hasattr(comp, "children"):
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
    for component in component_list:
        headings.append((2, component.__name__))
    return headings


def docpage(set_path: str | None = None, t: str | None = None, right_sidebar: bool = True) -> rx.Component:
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
            sidebar = sb(url=path, width="18em")

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
                        "← " + next_prev_name,
                        href=prev.link,
                        style=link_style,
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
                        next_prev_name + " →",
                        href=next.link,
                        style=link_style,
                    )
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
                navbar(sidebar=nav_sidebar),
                rx.flex(
                    rx.box(
                        sidebar,
                        margin_top="110px",
                        margin_right="2em",
                        height="100%",
                        width="24%",
                        display=["none", "none", "none", "none", "flex", "flex"],
                        flex_shrink=0,
                    ),
                    rx.box(
                        rx.box(breadcrumb(path), margin_top="110px"),
                        rx.box(comp),
                        rx.hstack(
                            *links,
                            justify="between",
                            margin_top="2em",
                            margin_bottom="4em",
                        ),
                        rx.spacer(),
                        rx.box(height="2em"),
                        docpage_footer(path=path),
                        border_left=[
                            "none",
                            "none",
                            "none",
                            "none",
                            f"1px solid {rx.color('mauve', 4)};",
                            f"1px solid {rx.color('mauve', 4)};",
                        ],
                        padding_x=styles.PADDING_X,
                        width=["100%", "97%", "94%", "90%", "70%", "60%"] if right_sidebar else "100%",
                        height="100%",
                    ),
                    rx.box(
                        rx.flex(
                            *[
                                (
                                    rx.link(
                                        rx.text(
                                            text,
                                            color=rx.color("mauve", 12),
                                            font_weight="500",
                                            font_size="1em",
                                        ),
                                        href=path
                                        + "#"
                                        + text.lower().replace(" ", "-"),
                                    )
                                    if level == 1
                                    else (
                                        rx.link(
                                            rx.text(
                                                text,
                                                color=rx.color("mauve", 11),
                                                font_weight="400",
                                                font_size="0.9em",
                                                _hover={"color": rx.color("mauve", 12)},
                                            ),
                                            href=path
                                            + "#"
                                            + text.lower().replace(" ", "-"),
                                        )
                                        if level == 2
                                        else rx.link(
                                            rx.text(
                                                text,
                                                color=rx.color("mauve", 11),
                                                _hover={"color": rx.color("mauve", 12)},
                                                font_weight="400",
                                                font_size="0.9em",
                                                padding_left="1em",
                                            ),
                                            href=path
                                            + "#"
                                            + text.lower().replace(" ", "-"),
                                        )
                                    )
                                )
                                for level, text in toc
                            ],
                            direction="column",
                            width="100%",
                            position="fixed",
                            spacing="2",
                            justify="start",
                            overflow="hidden",
                        ),
                        margin_top="110px",
                        width="18%",
                        height="100%",
                        display=["none", "none", "none", "none", "none", "flex"] if right_sidebar else "none",

                        flex_shrink=0,
                    ),
                    max_width="110em",
                    margin_left="auto",
                    margin_right="auto",
                    margin_top="0px",
                    height="100%",
                    min_height="100vh",
                    width="100%",
                ),
                background=rx.color("mauve", 1),
                width="100%",
                justify="center",
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

    color: str = "red"

    def change_color(self, color: str) -> None:
        self.color = color


def hover_item(component: rx.Component, component_str: str) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(rx.flex(component)),
        rx.hover_card.content(
            rx.code_block(f"{component_str}", can_copy=True, language="python"),
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
    return rx.vstack(
        rx.grid(
            rx.text("", size="5"),
            *[rx.text(variant, size="5") for variant in variants],
            rx.text("Accent", size="5"),
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
            rx.text("Gray", size="5"),
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
                    rx.text("Disabled", size="5"),
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
        rx.select.root(
            rx.select.trigger(
                rx.button(size="2", on_click=RadixDocState.change_color())
            ),
            rx.select.content(
                rx.select.group(
                    rx.select.label("Colors"),
                    *[
                        rx.select.item(
                            color,
                            value=color,
                            _hover={"background": f"var(--{color}-9)"},
                        )
                        for color in [
                            "tomato",
                            "red",
                            "ruby",
                            "crimson",
                            "pink",
                            "plum",
                            "purple",
                            "violet",
                            "iris",
                            "indigo",
                            "blue",
                            "cyan",
                            "teal",
                            "jade",
                            "green",
                            "grass",
                            "brown",
                            "orange",
                            "sky",
                            "mint",
                            "lime",
                            "yellow",
                            "amber",
                            "gold",
                            "bronze",
                            "gray",
                        ]
                    ],
                ),
            ),
            ## we need to clearly document how the on_change works as it is not obvious at all
            default_value=RadixDocState.color,
            on_change=RadixDocState.change_color,
        ),
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
