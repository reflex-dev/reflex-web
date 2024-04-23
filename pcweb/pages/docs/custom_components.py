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


def package_url(package_name: str) -> str:
    return f"https://pypi.org/pypi/{package_name}/"


def author_card_if_present(author: str) -> rx.Component:
    return rx.cond(
        author,
        info_icon(tag="user"),
    )


def updated_on_pypi_if_present(updated_on_pypi: str) -> rx.Component:
    return rx.cond(
        updated_on_pypi,
        info_icon(tag="pencil-line"),
    )


def demo_url_if_present(demo_url: str) -> rx.Component:
    return rx.cond(
        demo_url,
        rx.link(info_icon(tag="eye"), href=demo_url, is_external=True),
    )


def download_url(download_url: str) -> rx.Component:
    return rx.link(info_icon(tag="external-link"), href=download_url, is_external=True)


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


def pypi_summary(summary: str) -> rx.Component:
    return rx.text(
        summary,
        color=rx.color("mauve", 11),
        size="1",
    )


def pip_install_command_copy_button(package_name: str) -> rx.Component:
    return rx.code_block(
        "pip install " + package_name, 
        custom_style={"fontSize": "0.7em"}, 
        border_radius="4px",
        overflow_x="scroll",
        width="100%",
        style={
            "&::-webkit-scrollbar-thumb": {
                "background_color": "transparent",
            },
            "&::-webkit-scrollbar": {
                "background_color": "transparent",
                "height": "0px",
            },
            
        },
    )


def pypi_download_box(name: str, downloads: str) -> rx.Component:
    return rx.hstack(
        rx.heading(
            name,
            size="2",
        ),
        rx.box(
            flex_grow=1,
        ),
        rx.tooltip(
            rx.badge(
                downloads,
                rx.icon(tag="external-link", size=12),
                padding_x=".5em",
                font_size="0.75em",
                border_radius="6px",
                justify="center",
                align_items="center",
            ),
            content="PyPI downloads last month",
        ),
        width="100%",
        justify_content="center",
    )


def add_item(category: dict) -> rx.Component:
    # Format the package name to be more human readable
    name = rx.Var.create(
        f"{{{category['package_name']._var_name}.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}}"
    )
    return rx.flex(
        rx.box(
            rx.box(
                position= 'absolute',
                top= 0,
                left= 0,
                height= '100%',
                width= '100%',
                background_color= 'rgba(19, 18, 23, 0.2)',
                _hover= {
                    "background_color": "rgba(19, 18, 23, 0)"
                },
            ),
            rx.box(
                background_image='url('+category["image_url"]+')',
                background_size="cover",
                background_position="center",
                background_repeat="no-repeat",
                height="100%",
                width="100%",
                border="2px solid gold",
            ),
            position="relative",
            height="12rem",
            width="100%",
            border_radius="8px 8px 0 0",
            overflow="hidden",
            border="1px solid blue",
        ),
        rx.vstack(
            rx.vstack(
                pypi_download_box(
                    name,
                    category["downloads_last_month"],
                ),
                pypi_summary(category["summary"]),
                align_items="start",
                width="100%",
            ),
            rx.spacer(),
            pip_install_command_copy_button(category["package_name"]),
            rx.hstack(
                rx.spacer(),
                author_card_if_present(category["author"]),
                source_if_present(category["source"]),
                demo_url_if_present(category["demo_url"]),
                download_url(category["download_url"]),
                width="100%",
                justify="center",
            ),
            spacing="1",
            width="100%",
            height="11em",
            padding=".25em",
            border="1px solid red"
        ),
        direction="column",
        border_radius="8px",
        # border=f"1px solid {rx.color('mauve', 4)}",
        border="1px solid red",
        width="16em",
        height="20em",
    )


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(CustomComponentGalleryState.components_list, add_item),
        columns=[1,1,2,2,3,3],
        spacing_x="4em",
    )


@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rx.text(text, size="3", line_height="1.7", margin_bottom="1em")


def info_icon(
    tag: str,
    **kwargs,
) -> rx.Component:
    return rx.badge(
        rx.icon(tag=tag, width="1em", height="1em"),
        padding_x="0.5em",
        border_radius="15px",
    )


@docpage()
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
