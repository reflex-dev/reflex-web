"""Template for documentation pages."""

from typing import Any, Callable

import reflex as rx
import reflex.components.radix.themes as rdxt
from pcweb import styles
from pcweb.components.logo import navbar_logo
from pcweb.route import Route, get_path
from .blocks import *

# Docpage styles.
link_style = {
    "color": rx.color("violet", 10),
    "font_weight": "600",
}

logo_style = {
    "height": "1em",
    "opacity": 0.2,
}
logo = navbar_logo(**logo_style)


def doc_section(*contents):
    return rx.box(
        *contents,
        margin_top="1em",
        margin_left=".5em",
        border_left="1px #F4F3F6 solid",
        padding_left="1em",
        width="100%",
    )




def feedback_content(icon):
    return rdxt.flex(
            rdxt.button(
                icon,
                radius="full",
                variant="soft"
            ),
            rdxt.box(
                rdxt.flex(
                    rdxt.textarea(
                        placeholder="Contact Info (Optional)",
                        style={"height": 5},
                    ),
                    rdxt.textarea(
                        placeholder="Write a comment…",
                        style={"height": 80},
                    ),
                    gap="1",
                    direction="column",
                ),
                rdxt.flex(
                    rdxt.flex(
                        rdxt.text(
                            rdxt.checkbox(),
                            rdxt.text("Follow up with me"),
                            as_="label",
                            size="2",
                        ),
                        align="center",
                        gap="2",
                        as_child=True,
                    ),
                    rdxt.popover_close(
                        rdxt.button("Send Feedback", size="1")
                    ),
                    gap="3",
                    margin_top="12px",
                    justify="between",
                ),
                flex_grow="1",
            ),
            gap="3",
        )


def feedback(text, icon):
    return rdxt.popover_root(
    rdxt.popover_trigger(
        rdxt.button(
            icon,   
            text,
            variant="outline",
        )
    ),
    rdxt.popover_content(
        feedback_content(icon),
        style={"width": 360},
    ),
)

def docpage_footer():
    return rdxt.flex(
        rdxt.separator(size="4"),
        rdxt.flex( 
            rdxt.flex(
                rdxt.text(
                    "Did you find this useful?", 
                    color = rx.color("mauve", 12),
                ),
                feedback("No", rx.lucide.icon(tag="thumbs_down"),),
                feedback("Yes", rx.lucide.icon(tag="thumbs_up"),),
                align_items="center",
                gap="2"
            ),
            rdxt.box(
                grow='1',
            ),
            rdxt.separator(size="4", orientation="vertical"),
            rdxt.flex(
                rdxt.button(
                    "Raise an issue",
                    variant="outline"
                ),
                rdxt.button(
                    "Edit this page",
                    variant="outline"
                ),
                gap="2"
            ),
            align_items="center",
            width="100%",
        ),
        rdxt.separator(size="4"),
        rdxt.flex(
            rdxt.flex(
                rdxt.text("Home"),
                rdxt.text("Gallery"),
                rdxt.text("Change Log"),
                rdxt.text("Introduction"),
                rdxt.text("Hosting"),
                gap="2",
            ),
            rdxt.box(
                grow='1',
            ),
            rdxt.flex(
                rx.image(
                    src="/companies/light/github.svg",
                ),
                rx.image(
                    src="/companies/light/twitter.svg",
                ),
                rx.image(
                    src="/companies/light/discord.svg",
                ),
                rx.image(
                    src="/companies/light/linkedin.svg",
                ),
                rx.image(
                    src="/companies/light/yc.svg",
                ),
                gap="2",
            ),
            align_items="center",
            width="100%",
        ),
        direction="column",
        gap="2",
        margin_bottom="2em",
    )


def docpage(set_path: str | None = None, t: str | None = None) -> rx.Component:
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
            from pcweb.components.navbar import navbar
            from pcweb.components.sidebar import get_prev_next
            from pcweb.components.sidebar import sidebar as sb

            # Create the docpage sidebar.
            sidebar = sb(url=path)

            # Set the sidebar path for the navbar sidebar.
            nav_sidebar = sb(url=path)

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

            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            # Return the templated page.
            return rx.box(
                navbar(sidebar=nav_sidebar),
                rx.flex(
                    rx.desktop_only(
                            sidebar,
                            margin_top="40px",
                            margin_left="1em",
                            margin_right="1em",
                            width=["none", "none", "none", "25%", "25%"],
                        ),
                    rx.box(
                            rx.box(comp, margin_top="40px"),
                            rx.hstack(
                                *links,
                                justify="space-between",
                                margin_y="3em",
                            ),
                            rx.spacer(),
                            rx.box(height="2em"),
                            docpage_footer(),
                            border_left= ["none", "none", "none", "none",f"1px solid {rx.color('mauve', 4)};"],
                            padding_x=styles.PADDING_X,
                            width=["100%", "100%", "100%", "75%"],
                            height="100%",
                        ),
                    rx.desktop_only(
                            rx.flex(
                                rdxt.heading("State", size="3"),
                                rdxt.text("Props"),
                                rdxt.text("Props"),
                                rdxt.heading("Props", size="3"),
                                rdxt.text("Props"),
                                rdxt.text("Props"),
                                rdxt.text("Props"),
                                rdxt.heading("Events", size="3"),
                                rdxt.text("Props"),
                                rdxt.text("Props"),
                                direction="column",
                                position="fixed",
                            ),
                            margin_top="40px",
                            width=["none", "none", "none", "none","25%"],
                        ),
                    background = rx.color("mauve", 1),
                    max_width="110em",
                    margin_x="auto",
                    margin_top="80px",
                    height="100%",
                )
            )

        # Return the route.
        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return docpage


class RadixDocState(rx.State):
    """The app state."""

    color: str = "red"

    def change_color(self, color: str) -> None:
        self.color = color


def hover_item(component: rx.Component, component_str: str) -> rx.Component:
    return rdxt.hovercard_root(
        rdxt.hovercard_trigger(rdxt.flex(component)),
        rdxt.hovercard_content(
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
        rdxt.grid(
            rdxt.text("", size="5"),
            *[rdxt.text(variant, size="5") for variant in variants],
            rdxt.text("Accent", size="5"),
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
            rdxt.text("", size="5"),
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
            rdxt.text("Gray", size="5"),
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
            rdxt.text("", size="5"),
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
                    rdxt.text("Disabled", size="5"),
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
            gap="3",
        ),
        rdxt.select_root(
            rdxt.select_trigger(rdxt.button(size="2", on_click=RadixDocState.change_color())),
            rdxt.select_content(
                rdxt.select_group(
                    rdxt.select_label("Colors"),
                    *[
                        rdxt.select_item(
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
            ## we need to clearly document how the on_value_change works as it is not obvious at all
            default_value=RadixDocState.color,
            on_value_change=RadixDocState.change_color,
        ),
    )


def icon_grid(
    category_name: str, icon_tags: list[str], columns: str = "4"
) -> rx.Component:
    return rdxt.flex(
        rdxt.callout_root(
            rdxt.callout_icon(
                rdxt.icon(
                    tag="check_circled",
                    width=18,
                    height=18,
                )
            ),
            rdxt.callout_text(
                f"Below is a list of all available ",
                rdxt.text(category_name, weight="bold"),
                " icons.",
                color="black",
            ),
            color="green",
        ),
        rdxt.separator(size="4"),
        rdxt.grid(
            *[
                rdxt.flex(
                    rdxt.icon(tag=icon_tag, alias="Radix" + icon_tag.title()),
                    rdxt.text(icon_tag),
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
            gap="1",
        ),
        direction="column",
        gap="2",
    )