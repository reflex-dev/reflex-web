import reflex as rx
import httpx
import json
from rxconfig import config

from pcweb.templates.docpage import docpage, h1_comp
from pcweb.styles.colors import c_color
from pcweb.styles.shadows import shadows
from pcweb.styles.fonts import base_semibold, small, base
from pcweb.components.icons.icons import get_icon


class CustomComponentGalleryState(rx.State):
    tags: list[str] = []

    components_list: list[dict[str, str]] = []

    selected_filter: str = ""
    original_components_list: list[dict[str, str]] = []

    def fetch_components_list(self):
        try:
            response = httpx.get(f"{config.cp_backend_url}/custom-components/gallery")
            response.raise_for_status()
            component_list = response.json()
        except (httpx.HTTPError, json.JSONDecodeError) as ex:
            print(f"Internal error: failed to fetch components list due to: {ex}")
            return

        for c in component_list:
            c["downloads_last_month"] = c["downloads"]["last_month"]
            # Filters out the keywords that says "reflex", "reflex-custom-component".
            c["keywords"] = [
                keyword
                for keyword in c["keywords"] or []
                if "reflex" not in keyword.lower()
            ]
            c["download_url"] = package_url(c["package_name"])

        self.components_list = component_list
        self.original_components_list = component_list

    def set_selected_filter(self, filter):
        if self.selected_filter == filter:
            self.selected_filter = ""
            self.components_list = self.original_components_list
        else:
            self.selected_filter = filter
            self.sort_by_filter(filter)

    def sort_by_filter(self, filter):
        if filter == "Recent":
            self.components_list = sorted(
                self.components_list, key=lambda x: x["created_at"], reverse=True
            )
        elif filter == "Downloads":
            self.components_list = sorted(
                self.components_list,
                key=lambda x: x["downloads"]["last_month"],
                reverse=True,
            )


def filter_item(
    icon: str, text: str, border: bool = False, on_click=None
) -> rx.Component:
    is_selected = CustomComponentGalleryState.selected_filter == text
    return rx.hstack(
        get_icon(icon, padding_y="2px", opacity=rx.cond(is_selected, 0.64, 1)),
        rx.text(text, opacity=rx.cond(is_selected, 0.64, 1), style=small),
        rx.spacer(),
        rx.cond(
            is_selected,
            rx.box(
                width="8px",
                height="8px",
                justify="end",
                background=c_color("violet", 9),
                border_radius="50%",
            ),
        ),
        gap="14px",
        align="center",
        justify="start",
        width="100%",
        cursor="pointer",
        _hover={"background_color": c_color("slate", 3)},
        padding="8px 14px",
        overflow="hidden",
        text_wrap="nowrap",
        border_top=f"1px solid {c_color('slate', 5)}" if border else "none",
        border_bottom=f"1px solid {c_color('slate', 5)}" if border else "none",
        on_click=CustomComponentGalleryState.set_selected_filter(text),
    )


chips_box_style = {
    "width": ["100%", "100%", "auto"],
    "box-sizing": "border-box",
    "display": "flex",
    "flex-direction": "row",
    "align_items": "center",
    "padding": "6px 12px",
    "cursor": "pointer",
    "box-shadow": shadows["large"],
    "border-radius": "1000px",
    "transition": "background 0.075s ease-out, color 0.075s ease-out, border 0.075s ease-out",
}

# Sorting
sorting_box_style = {
    "gap": "12px",
    "outline": "none",
    "_focus": {
        "outline": "none",
    },
    **chips_box_style,
}

menu_item_style = {
    "box-sizing": "border-box",
    "width": "191px",
    "height": "auto",
    "overflow": "hidden",
    "padding": "0px",
    "cursor": "default",
    "background_color": c_color("slate", 2),
    "border": f"1px solid {c_color('slate', 5)}",
    "box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.05)",
    "border-radius": "12px",
    "color": c_color("slate", 9),
    **base,
}


def sorting_filters() -> rx.Component:
    return rx.vstack(
        filter_item(
            "history",
            "Recent",
        ),
        filter_item(
            "arrow_down_big",
            "Downloads",
            border=True,
        ),
        gap="0px",
        width="100%",
    )


def sorting_filters_dropdown_menu() -> rx.Component:
    condition = CustomComponentGalleryState.selected_filter != ""
    conditional_style = {
        "background": rx.cond(
            condition,
            c_color("violet", 9),
            c_color("slate", 1),
        ),
        "color": rx.cond(
            condition,
            "white",
            c_color("slate", 9),
        ),
        "border": rx.cond(
            condition,
            f"1px solid {c_color('violet', 9)}",
            f"1px solid {c_color('slate', 5)}",
        ),
        "&[data-state='open']": {
            "background": rx.cond(
                condition,
                c_color("violet", 9),
                c_color("slate", 3),
            ),
        },
        "_hover": {
            "background": rx.cond(
                condition,
                c_color("violet", 9),
                c_color("slate", 3),
            ),
        },
    }
    return rx.menu.root(
        rx.menu.trigger(
            rx.el.button(
                rx.text(
                    "Sort",
                    rx.cond(
                        condition,
                        rx.text(
                            f": {CustomComponentGalleryState.selected_filter}",
                            as_="span",
                            text_wrap="nowrap",
                        ),
                    ),
                    as_="span",
                    style=small,
                ),
                get_icon(
                    "select",
                ),
                justify_content="space-between",
            ),
            style=sorting_box_style | conditional_style,
        ),
        rx.menu.content(
            rx.menu.item(sorting_filters(), style=menu_item_style),
            bg="transparent",
            box_shadow="None",
            padding="0px",
            overflow="visible",
            border="none",
            align="center",
        ),
        width="100%",
    )


def package_url(package_name: str) -> str:
    return f"https://pypi.org/pypi/{package_name}/"


def demo_modal_if_present(demo_url: str) -> rx.Component:
    return rx.cond(
        demo_url,
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    rx.icon(tag="eye", width="1em", height="1em"),
                    padding_x="0.5em",
                    border_radius="15px",
                    box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14)",
                ),
            ),
            rx.dialog.content(
                rx.el.iframe(src=demo_url, width="800px", height="600px"),
                rx.dialog.close(
                    rx.button(
                        "close",
                    ),
                ),
            ),
        ),
    )


def last_update(time: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            "Last update:",
            line_height="0.5em",
            color=rx.color("mauve", 11),
            size="1",
        ),
        rx.text(
            rx.moment(
                time,
                from_now=True,
            ),
            size="1",
            line_height="0.5em",
            color=rx.color("mauve", 11),
        ),
    )


def demo(category: dict) -> rx.Component:
    return rx.cond(
        category["demo_url"],
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    get_icon(
                        icon="eye",
                    ),
                    color=c_color("slate", 9),
                    border_radius="6px",
                    box_shadow=shadows["small"],
                    border=f"1px solid {c_color('slate', 5)}",
                    _hover={
                        "background": c_color("slate", 3),
                        "transition": "background 0.075s ease-out",
                    },
                    padding="5px",
                ),
            ),
            rx.dialog.content(
                rx.vstack(
                    rx.flex(
                        install_command("pip install " + category["package_name"]),
                        rx.dialog.close(
                            rx.el.button(
                                rx.icon(
                                    tag="x",
                                    color=c_color("slate", 9),
                                    _hover={"color": c_color("slate", 10)},
                                    padding="5px",
                                ),
                                background=c_color("slate", 1),
                                border=f"1px solid {c_color('slate', 5)}",
                                _hover={
                                    "background": c_color("slate", 3),
                                    "transition": "background 0.075s ease-out",
                                },
                                outline="none",
                                border_radius="6px",
                                box_shadow=shadows["small"],
                                height="auto",
                                cursor="pointer",
                            ),
                            outline="none",
                        ),
                        flex_direction=["column-reverse", "column-reverse", "row"],
                        justify="end",
                        align_items=["flex-end", "flex-end", "center"],
                        gap="12px",
                        width="auto",
                        max_width="100%",
                    ),
                    rx.el.iframe(
                        src=category["demo_url"],
                        width="100%",
                        height="100%",
                        border_radius="var(--radius-4)",
                    ),
                    height="100%",
                    width="100%",
                    gap="16px",
                ),
                style={
                    "max_width": "calc(100vw - 20%)",
                    "height": "75vh",
                    "outline": "none",
                    "border": f"1px solid {c_color('slate', 5)}",
                    "background": c_color("slate", 1),
                    "box_shadow": shadows["large"],
                },
            ),
        ),
    )


def download(download_url: str) -> rx.Component:
    return rx.link(
        get_icon(icon="new_tab", padding="5px"),
        background=c_color("slate", 1),
        border_radius="6px",
        border=f"1px solid {c_color('slate', 5)}",
        box_shadow=shadows["small"],
        _hover={
            "background": c_color("slate", 3),
            "transition": "background 0.075s ease-out",
            "color": c_color("slate", 9),
        },
        style={
            ":hover": {
                "color": c_color("slate", 9),
            },
        },
        color=c_color("slate", 9),
        underline="none",
        href=download_url,
        is_external=True,
    )


def source_if_present(source: str) -> rx.Component:
    return rx.cond(
        source,
        rx.link(
            info_icon(tag="github"),
            href=source,
            is_external=True,
        ),
    )


def pypi_keywords(keywords: rx.Var[list[str]]) -> rx.Component:
    return rx.chakra.wrap(
        rx.foreach(
            keywords,
            lambda tag: rx.badge(tag, border_radius="15px", padding_x=".5em"),
        ),
        padding_bottom=".5em",
    )


def install_command(command: str) -> rx.Component:
    return rx.hstack(
        get_icon(icon="copy", padding="5px"),
        rx.text(
            "$" + command,
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
        on_click=rx.set_clipboard(command),
        max_width="100%",
        cursor="pointer",
        _hover={
            "transition": "background 0.075s ease-out",
            "background": c_color("slate", 3),
        },
        border=f"1px solid {c_color('slate', 5)}",
        overflow="hidden",
    )


def download_count(downloads: str) -> rx.Component:
    return rx.hstack(
        get_icon(icon="arrow_down", padding="3px"),
        rx.text(
            downloads,
            overflow="hidden",
            white_space="nowrap",
            text_overflow="ellipsis",
            style=small,
        ),
        gap="6px",
        color=c_color("slate", 9),
        align_items="center",
        justify_content="center",
    )


def component_name(name: str) -> rx.Component:
    return rx.heading(
        name,
        color=c_color("slate", 12),
        style=base_semibold,
        white_space="nowrap",
        overflow="hidden",
        text_overflow="ellipsis",
        as_="h4",
    )


def component_description(summary: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            summary,
            color=rx.color("mauve", 11),
            font_size="14px",
            line_height="20px",
        ),
        width="100%",
    )


def add_item(category: dict) -> rx.Component:
    # Format the package name to be more human readable
    name = rx.ivars.ImmutableVar.create(
        f"{str(category['package_name'])}.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')",
    )
    return rx.flex(
        rx.box(
            rx.cond(
                category["demo_url"],
                rx.link(
                    rx.box(
                        background_image="url(" + category["image_url"] + ")",
                        background_size="cover",
                        background_position="center",
                        background_repeat="no-repeat",
                        height="100%",
                        width="100%",
                    ),
                    href=category["demo_url"],
                    is_external=True,
                ),
                rx.box(
                    background_image="url(" + category["image_url"] + ")",
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    height="100%",
                    width="100%",
                ),
            ),
            position="relative",
            width="100%",
            height="100%",
            overflow="hidden",
        ),
        rx.vstack(
            rx.hstack(
                component_name(name),
                download_count(category["downloads_last_month"]),
                gap="12px",
                align_items="center",
                justify_content="space-between",
                width="100%",
                padding="10px 12px 0px 12px",
            ),
            rx.hstack(
                install_command("pip install " + category["package_name"]),
                download(category["download_url"]),
                demo(category),
                gap="6px",
                align_items="center",
                padding="0px 6px 6px 6px",
                width="100%",
            ),
            gap="10px",
            width="100%",
        ),
        background=c_color("slate", 2),
        direction="column",
        border_radius="12px",
        border=f"1px solid {c_color('slate', 5)}",
        cursor="pointer",
        box_shadow=shadows["large"],
        overflow="hidden",
        box_sizing="border-box",
        width="100%",
        flex_shrink=0,
        height="280px",
    )


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(CustomComponentGalleryState.components_list, add_item),
        columns=[1, 2, 2, 2, 3, 3],
        gap="24px",
        min_child_width="320px",
        spacing_y="24px",
    )


def info_icon(
    tag: str,
    **kwargs,
) -> rx.Component:
    return rx.badge(
        rx.icon(tag=tag, width="1.4em", height="1.4em"),
        padding_x="0.5em",
        border_radius="15px",
    )


@docpage(right_sidebar=False)
def custom_components() -> rx.Component:
    return rx.flex(
        h1_comp(text="Custom Components"),
        rx.hstack(
            rx.text(
                "Reflex has a growing ecosystem of custom components that you can use to build your apps. Below is a list of some of the custom components available for Reflex.",
                as_="p",
                style={
                    "color": c_color("slate", 11),
                    "font-size": "16px",
                    "font-style": "normal",
                    "font-weight": "500",
                    "line-height": "24px",
                    "letter-spacing": "-0.24px",
                    "max-width": "75%",
                },
            ),
            sorting_filters_dropdown_menu(),
            align_items="center",
            justify_content="space-between",
            gap="48px",
        ),
        component_grid(),
        flex_direction="column",
        height="100%",
        gap="24px",
        margin_bottom="4em",
        on_mount=CustomComponentGalleryState.fetch_components_list,
    )
