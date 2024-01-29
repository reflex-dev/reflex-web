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
    "color": "#494369",
    "font_weight": "600",
    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
    "_hover": {
        "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"
    },
    "padding_x": "0.5em",
    "border_radius": "8px",
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


def my_form():
    from pcweb.components.navbar import NavbarState

    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Email (optional)",
                id="email",
                type_="email",
                width="100%",
                font_size=".8em",
                _active={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _focus={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _placeholder={
                    "color": "#A9A7B1",
                    "font_weight": "400",
                },
                border_radius="8px",
                border="none",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
            ),
            rx.text_area(
                placeholder="Your Feedback...",
                id="feedback",
                width="100%",
                font_size=".8em",
                _active={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _focus={
                    "border": "none",
                    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
                },
                _placeholder={
                    "color": "#A9A7B1",
                    "font_weight": "400",
                },
                border_radius="8px",
                border="none",
                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    "Send",
                    type_="submit",
                    size="sm",
                    style=styles.BUTTON_LIGHT,
                ),
                width="100%",
            ),
            padding_x=".5em",
            width="100%",
        ),
        on_submit=NavbarState.handle_submit,
        padding_bottom=".2em",
        width="100%",
    )


def docpage(set_path: str | None = None, t: str | None = None) -> rx.Component:
    """A template that most pages on the pynecone.io site should use.

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
            from pcweb.components.navbar import feedback_button, navbar
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
                            width=["0", "0%", "25%"],
                        ),
                    rx.box(
                            rx.box(comp),
                            rx.hstack(
                                *links,
                                justify="space-between",
                                margin_y="3em",
                            ),
                            rx.spacer(),
                            rx.center(
                                feedback_button(),
                                width="100%",
                            ),
                            rx.box(height="2em"),
                            rx.hstack(
                                logo,
                                rx.spacer(),
                                rx.text(
                                    "Copyright © 2023 Pynecone, Inc.", color="#CDCCD1"
                                ),
                                width="100%",
                            ),
                            padding_x=styles.PADDING_X,
                            width=["100%", "100%", "100%", "75%"],
                            height="100%",
                        ),
                    rx.desktop_only(
                            rx.flex(
                                "Test",
                                "Test",
                                "Test",
                                "Test",
                                direction="column",
                                position="fixed",
                            ),
                            width=["0", "0%","0%", "0%","25%"],
                        ),
                    background = rx.color("mauve", 1),
                    max_width="110em",
                    margin_x="auto",
                    margin_top="100px",
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
            ## we need to clearly document how the on_change works as it is not obvious at all
            default_value=RadixDocState.color,
            on_change=RadixDocState.change_color,
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
