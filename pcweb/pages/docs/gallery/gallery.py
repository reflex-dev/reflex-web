import reflex as rx

from pcweb.templates.webpage import webpage
from .state import SideBarState


border_radius = ("0.375rem",)
box_shadow = ("0px 0px 0px 1px rgba(84, 82, 95, 0.14)",)
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"


def add_item(category):
    return rx.flex(
        rx.box(
            rx.box(
                position="absolute",
                top=0,
                left=0,
                height="100%",
                width="100%",
                background_color="rgba(19, 18, 23, 0.2)",
                _hover={"background_color": "rgba(19, 18, 23, 0)"},
            ),
            rx.image(
                src=category["image_url"],
                width="100%",
            ),
            position="relative",
            height="12em",
            width="100%",
            border_radius="12px",
            overflow="hidden",
        ),
        rx.vstack(
            rx.hstack(
                rx.heading(category["display_name"], size="5", color="#D6D6ED"),
                rx.hstack(
                    rx.cond(
                        category["source"],
                        rx.link(
                            rx.icon("code", color="#8E8EA8"),
                            href=category["source"],
                            is_external=True,
                        ),
                    ),
                    rx.cond(
                        category["demo_url"],
                        rx.link(
                            rx.icon("eye", color="#8E8EA8"),
                            href=category["demo_url"],
                            is_external=True,
                        ),
                    ),
                ),
                justify="between",
                width="100%",
            ),
            #rx.text(category["summary"], size="2", color="#8E8EA8"),
            align_items="start",
            width="100%",
            padding_top="1em",
        ),
        direction="column",
        border_radius="14px;",
        border="1px solid #3C3646;",
        background="linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%);",
        box_shadow="0px 0px 27px -4px rgba(0, 0, 0, 0.30), 0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset;",
        padding="1em",
    )


grid_layout = [1, 1, 2, 2, 3, 4]


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(SideBarState.example_apps_to_return, add_item),
        columns=grid_layout,
        gap=4,
        width="100%",
    )


def community_component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(SideBarState.community_apps_to_return, add_item),
        columns=grid_layout,
        gap=4,
        width="100%",
    )


def pagination():
    return rx.hstack(
        rx.button(
            "Previous",
            on_click=SideBarState.set_page(SideBarState.page - 1),
        ),
        rx.spacer(),
        rx.button(
            "Next",
            on_click=SideBarState.set_page(SideBarState.page + 1),
        ),
        width="100%",
        padding_x="1em",
    )

def sidebar_component_grid(tags):
    return rx.chakra.wrap(
        rx.foreach(
            tags,
            lambda tag: rx.chakra.button(
                tag,
                border_radius="15px",
                padding_x=".5em",
                is_active=SideBarState.chosen_tags.contains(tag),
                on_click=SideBarState.update_tag(tag),
                color="#6C6C81",
                background="rgba(161, 157, 213, 0.05);",
                _active={
                    "color": "white",
                    "background": "#5B4BF0",
                    "border": "1px solid rgba(186, 199, 247, 0.12);",
                },
            ),
        ),
        padding_y="1em",
        padding_x=".5em",
        justify="center",
    )


def gallery_heading():
    return rx.vstack(
        rx.flex(
            rx.chakra.text(
                "Apps made in Reflex",
                background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                text_align="center",
                background_clip="text",
                padding_x="1em",
            ),
            border_radius="15px;",
            border="1px solid #4435D4;",
            background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
            box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);",
            maargin_bottom="1em",
        ),
        rx.chakra.text(
            "Reflex Gallery",
            font_size="48px;",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
            text_align="center",
            background_clip="text",
            font_weight="bold",
            letter_spacing="-1.28px;",
            line_height="1.2",
        ),
        rx.text(
            "Use the command `reflex init --template {app_url}` to run a gallery app locally.",
            color="#6C6C81",
            text_align="center",
        ),
        align_items="center",
        text_align="left",
        width="100%",
        spacing="2",
        padding_x=".5em",
        justify="center",
    )


def sort_by():
    return rx.hstack(
        rx.spacer(),
        rx.select(
            ["page_views", "updated_at", "created_at"],
            value=SideBarState.sort_by,
            on_change=SideBarState.set_sort_by,
        ),
        width="100%",  
    )

@webpage(path="/docs/gallery", title="Gallery · Reflex")
def gallery() -> rx.Component:
    return rx.vstack(
        gallery_heading(),
        rx.vstack(
            sidebar_component_grid(SideBarState.tags_list),
            component_grid(),
            rx.chakra.text(
                "Community Gallery",
                font_size="48px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
                padding_top="1em",
            ),
            sort_by(),
            community_component_grid(),
            pagination(),
            rx.spacer(),
            align_items="center",
            padding_x="1em",
            width="100%",
        ),
        height="100%",
        width=["100%", "100%", "90%", "90%", "90%", "90%"],
        on_mount=SideBarState.fetch_apps_list,
    )
