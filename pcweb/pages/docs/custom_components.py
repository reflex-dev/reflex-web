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

def demo(demo_url: str) -> rx.Component:
    return rx.cond(
        demo_url,
        rx.link(
            info_icon(tag="eye"), 
            href=demo_url, 
            is_external=True,
        ),
    )

def download(download_url: str) -> rx.Component:
    return rx.link(info_icon(tag="chevrons-left-right"), href=download_url, is_external=True)


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

        # rx.button(
        #     rx.icon(tag="copy", size=18, color=rx.color("mauve", 9)),
        #     on_click=rx.set_clipboard(code),

def install_command(command: str) -> rx.Component:
    return rx.hstack(
        rx.button(
            rx.icon(tag="copy", size=15, color=rx.color("mauve", 9)),
            on_click=rx.set_clipboard(command),
            background="transparent",
            _hover={
                "opacity": 0.5,
                "cursor": "pointer",
                "background": "transparent",
            },
            _active={
                "size": "0.8em",
                "transform": "scale(0.8)",
            },
        ),
        rx.code_block(
            command, 
            custom_style={"fontSize": "0.8em"}, 
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
        ),
        width="100%",
        align="center",
        justify="center",
    )


def download_count(downloads: str) -> rx.Component:
    return rx.box(
        rx.tooltip(
            rx.chakra.badge(
                rx.hstack(
                    downloads,
                    rx.icon(tag="arrow-down-to-line", size=15),
                    align="center",
                    justify="center",
                ),
                padding_x=".5em",
                font_size="1em",
                bg=rx.color("accent", 3),
                color=rx.color("accent", 9),
                border=f"2px solid {rx.color('accent', 9)}",
                border_radius="8px",
                justify="center",
                align_items="center",
                variant="solid",
            ),
            content="PyPI downloads last month",
        ),
        padding_right="0.175em",
        padding_top="0.175em",
        position= 'absolute',
        right= 0,
        z_index=4
    )

def component_name(name: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            name,
            size="3",
            weight="bold",
            line_height="1em",
        ),
        width="100%",
    )

def component_description(summary: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            summary,
            color=rx.color("mauve", 11),
            size="1",
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
                        background_image='url('+category["image_url"]+')',
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
                    background_image='url('+category["image_url"]+')',
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    height="100%",
                    width="100%",
                ),
            ),
            position="relative",
            height="16rem",
            width="100%",
            border_radius="8px 8px 0 0",
            overflow="hidden",
        ),
        rx.vstack(
            rx.vstack(
                component_name(name),
                component_description(category["summary"]),
                width="100%",
                padding_left="0.4em",
            ),
            install_command("pip install " + category["package_name"]),
            rx.hstack(
                demo(category["demo_url"]),
                download(category["download_url"]),
                rx.spacer(),
                last_update(category["updated_at"]),
                width="100%",
                padding_left="0.25em",
                padding_right="0.25em",
                justify="center",
                align="center",
            ),
            spacing="1",
            width="100%",
            height="10em",
            padding=".25em",
        ),
        direction="column",
        border_radius="8px",
        border=f"2px solid {rx.color('mauve', 4)}",
        _hover={
            "border": f"4px solid {rx.color('mauve', 4)}",
            "cursor": "pointer",
        },
        width="100%",
        height="23em",
    )


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(CustomComponentGalleryState.components_list, add_item),
        columns=[1,2,2,2,3,3],
        gap="4",
        min_child_width="20em",
        spacing_y="2em",
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
