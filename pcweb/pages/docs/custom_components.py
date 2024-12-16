import reflex as rx
import httpx
import json
import os
from rxconfig import config
import reflex_chakra as rc
from pcweb.templates.docpage import docpage, h1_comp, text_comp_2
from pcweb.styles.colors import c_color
from pcweb.styles.shadows import shadows
from pcweb.styles.fonts import base
from pcweb.components.icons.icons import get_icon


class CustomComponentGalleryState(rx.State):
    tags: list[str] = []

    components_list: list[dict[str, str]] = []

    selected_filter: str = ""
    original_components_list: list[dict[str, str]] = []

    @rx.event
    def fetch_components_list(self):
        try:
            response = httpx.get(
                f"{os.getenv('RCC_ENDPOINT')}/custom-components/gallery"
            )
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

    @rx.event
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
    return rx.box(
        get_icon(icon, class_name="py-[2px]", opacity=rx.cond(is_selected, 0.64, 1)),
        rx.text(text, opacity=rx.cond(is_selected, 0.64, 1), class_name="font-small"),
        rx.spacer(),
        rx.cond(
            is_selected,
            rx.box(
                class_name="size-2 justify-end bg-violet-9 rounded-full",
            ),
        ),
        class_name="flex flex-row gap-[14px] items-center justify-start w-full cursor-pointer hover:bg-slate-3 transition-bg text-nowrap overflow-hidden p-[8px_14px]",
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
                            class_name="text-nowrap",
                        ),
                    ),
                    as_="span",
                    class_name="font-small",
                ),
                get_icon(
                    icon="select",
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
                    class_name="text-slate-9 rounded-[6px] hover:bg-slate-3 transition-bg cursor-pointer border border-slate-5 bg-slate-1 shadow-small p-[5px]",
                ),
            ),
            rx.dialog.content(
                rx.box(
                    rx.box(
                        install_command("pip install " + category["package_name"]),
                        rx.dialog.close(
                            rx.el.button(
                                rx.icon(
                                    tag="x",
                                    class_name="p-[5px] !text-slate-9",
                                ),
                                class_name="cursor-pointer h-auto shadow-small rounded-[6px] outline-none bg-slate-1 border border-slate-5 hover:bg-slate-3 transition-bg",
                            ),
                            outline="none",
                        ),
                        class_name="flex flex-col-reverse gap-3 w-auto max-w-full lg:flex-row items-end lg:items-center justify-end lg:justify-center",
                    ),
                    rx.el.iframe(
                        src=category["demo_url"],
                        class_name="w-full h-full rounded-xl",
                    ),
                    class_name="flex flex-col gap-4 w-full h-full",
                ),
                class_name="h-[75vh] border border-slate-5 bg-slate-1 shadow-large max-w-[calc(100vw-20%)]",
            ),
        ),
    )


def download(download_url: str) -> rx.Component:
    return rx.link(
        get_icon(icon="new_tab", class_name="p-[5px]"),
        underline="none",
        href=download_url,
        is_external=True,
        class_name="text-slate-9 hover:!text-slate-9 border border-slate-5 bg-slate-1 hover:bg-slate-3 transition-bg cursor-pointer max-w-full shadow-small rounded-[6px] border-solid",
    )


def install_command(command: str) -> rx.Component:
    return rx.box(
        get_icon(icon="copy", class_name="p-[5px]"),
        rx.text(
            "$" + command,
            as_="p",
            class_name="font-small truncate flex-1 min-w-0",
        ),
        on_click=rx.set_clipboard(command),
        class_name="flex flex-row gap-1.5 text-slate-9 w-full items-center overflow-hidden border border-slate-5 bg-slate-1 hover:bg-slate-3 transition-bg cursor-pointer shadow-small rounded-[6px] pr-1.5 max-w-[20rem]",
    )


def download_count(downloads: str) -> rx.Component:
    return rx.box(
        get_icon(icon="arrow_down", class_name="p-[3px]"),
        rx.text(
            downloads,
            class_name="font-small truncate",
        ),
        class_name="flex flex-row gap-1 text-slate-9 justify-center items-center",
    )


def component_name(name: str) -> rx.Component:
    return rx.heading(
        name,
        class_name="font-base truncate text-slate-12 font-semibold",
        as_="h4",
    )


def add_item(category: dict) -> rx.Component:
    # Format the package name to be more human readable
    name = rx.Var(
        f"{str(category['package_name'])}.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')",
    )
    return rx.flex(
        rx.box(
            rx.cond(
                category["demo_url"],
                rx.box(
                    rx.link(
                        rx.cond(
                            category["image_url"],
                            rx.image(
                                src=category["image_url"],
                                loading="lazy",
                                alt="Image preview for app: " + category["name"],
                                class_name="w-full h-full duration-150 object-top object-cover hover:scale-105 transition-transform ease-out",
                            ),
                            rx.fragment(),
                        ),
                        href=category["demo_url"],
                        is_external=True,
                    ),
                    class_name="relative w-full h-full overflow-hidden",
                ),
            ),
            class_name="flex w-full h-full relative overflow-hidden border-slate-5 border-b border-solid",
        ),
        rx.box(
            rx.box(
                component_name(name),
                download_count(category["downloads_last_month"]),
                class_name="flex flex-row justify-between items-center w-full gap-3 p-[10px_12px_0px_12px]",
            ),
            rx.box(
                install_command("pip install " + category["package_name"]),
                download(category["download_url"]),
                demo(category),
                title="pip install " + category["package_name"],
                class_name="flex flex-row justify-between items-center w-full gap-1.5 p-[0px_6px_6px_6px]",
            ),
            class_name="flex flex-col gap-[10px] w-full",
        ),
        class_name="bg-slate-2 flex flex-col rounded-xl border border-slate-5 shadow-large overflow-hidden w-full h-[300px] cursor-pointer",
    )


def component_grid():
    return rc.box(
        rx.foreach(CustomComponentGalleryState.components_list, add_item),
        class_name="gap-6 grid grid-cols-1 lg:grid-cols-1 2xl:grid-cols-3 [&>*]:min-w-[260px] w-full",
    )


@docpage(right_sidebar=False)
def custom_components() -> rx.Component:
    return rx.box(
        rx.box(
            h1_comp(text="Custom Components"),
            rx.box(
                text_comp_2(
                    text="Reflex has a growing ecosystem of custom components that you can use to build your apps. Below is a list of some of the custom components available for Reflex.",
                ),
                sorting_filters_dropdown_menu(),
                class_name="flex flex-row w-full gap-12 justify-between items-center",
            ),
            class_name="flex flex-col w-full",
        ),
        component_grid(),
        class_name="flex flex-col h-full w-full gap-6 mb-16",
        on_mount=CustomComponentGalleryState.fetch_components_list,
    )
