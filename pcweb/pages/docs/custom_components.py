import reflex as rx
import httpx
import json
from rxconfig import config

from pcweb.templates.docpage import docpage, h1_comp, text_comp


class CustomComponentGalleryState(rx.State):
    tags: list[str] = []

    components_list: list[dict[str, str]] = []

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
                rx.icon(
                    tag="eye",
                    size=17,
                    color=rx.color("mauve", 11),
                    _hover={
                        "color": rx.color("mauve", 12),
                    },
                )
            ),
            rx.dialog.content(
                rx.vstack(
                    rx.flex(
                        install_command("pip install " + category["package_name"]),
                        rx.dialog.close(
                            rx.icon_button(
                                rx.icon(
                                    tag="x",
                                    color=rx.color("mauve", 2),
                                    _hover={"color": rx.color("mauve", 3)},
                                ),
                                size="2",
                                cursor="pointer",
                            ),
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
                ),
                style={
                    "max_width": "calc(100vw - 20%)",
                    "height": "75vh",
                },
            ),
        ),
    )


def download(download_url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(
                "Source",
                color=rx.color("mauve", 11),
                font_size="14px",
                line_height="20px",
                as_="p",
            ),
            rx.icon(
                tag="arrow-right",
                size=16,
                color=rx.color("mauve", 11),
                stroke_width="1.5px",
            ),
            align="center",
            gap="4px",
            transition="all 0.2s ease",
            _hover={
                "& *": {
                    "color": rx.color("mauve", 12),
                },
            },
        ),
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
        rx.text(
            "$ " + command,
            as_="p",
            color=rx.color("accent", 11),
            weight="medium",
            overflow="hidden",
            white_space="nowrap",
            font_family="Source Code Pro",
            font_size="13px",
            text_overflow="ellipsis",
            flex_grow=1,
            flex_shrink=1,
            min_width=0,
        ),
        rx.icon(
            tag="copy",
            size=17,
            color=rx.color("mauve", 11),
            cursor="pointer",
            on_click=rx.set_clipboard(command),
            flex_shrink=0,
            _hover={
                "color": rx.color("mauve", 12),
            },
            _active={
                "transform": "scale(0.8)",
            },
        ),
        width="100%",
        padding="8px",
        align_items="center",
        background=rx.color("accent", 3),
        border_radius="6px",
        max_width="100%",
        overflow="hidden",
    )


def download_count(downloads: str) -> rx.Component:
    return rx.box(
        rx.tooltip(
            rx.badge(
                rx.hstack(
                    rx.icon(
                        tag="download",
                        size=17,
                        color=rx.color("accent", 9),
                    ),
                    downloads,
                    gap="5px",
                    align="center",
                    justify="center",
                ),
                padding="8px",
                font_size="1em",
                font_weight="400",
                bg=rx.color("mauve", 2),
                color=rx.color("accent", 9),
                border=f"1.75px solid {rx.color('accent', 9)}",
                border_radius="8px",
                justify="center",
                align_items="center",
                variant="soft",
            ),
            content="Downloads last month",
        ),
        position="absolute",
        bottom="8px",
        left="8px",
        z_index=4,
    )


def component_name(name: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            name,
            font_size="18px",
            line_height="20px",
            weight="bold",
            white_space="nowrap",
            overflow="hidden",
            text_overflow="ellipsis",
        ),
        width="100%",
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
    name = rx.Var.create(
        f"{{{category['package_name']._var_name}.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}}",
        _var_is_string=False,
    )
    return rx.flex(
        rx.box(
            download_count(category["downloads_last_month"]),
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
            height="14rem",
            border_radius="8px 8px 0 0",
            overflow="hidden",
        ),
        rx.vstack(
            rx.vstack(
                component_name(name),
                # component_description(category["summary"]),
                gap="12px",
                width="100%",
            ),
            install_command("pip install " + category["package_name"]),
            rx.hstack(
                download(category["download_url"]),
                demo(category),
                width="100%",
                justify="between",
                align="center",
            ),
            padding="16px",
            gap="12px",
            width="100%",
        ),
        background=rx.color("mauve", 2),
        direction="column",
        border_radius="8px",
        border=f"1.75px solid {rx.color('mauve', 4)}",
        _hover={
            "border": f"1.75px solid {rx.color('accent', 9)}",
            "cursor": "pointer",
        },
        overflow="hidden",
        box_sizing="border-box",
        transition="border 0.2s ease",
        width="100%",
        height="22em",
    )


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(CustomComponentGalleryState.components_list, add_item),
        columns=[1, 2, 2, 2, 3, 3],
        gap="3.5rem",
        min_child_width="20em",
        spacing_y="3.5rem",
    )


@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rx.text(text, size="3", line_height="1.7", margin_bottom="1em")


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
        text_comp(
            text="Reflex has a growing ecosystem of custom components that you can use to build your apps. Below is a list of some of the custom components available for Reflex."
        ),
        component_grid(),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
        on_mount=CustomComponentGalleryState.fetch_components_list,
    )
