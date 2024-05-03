import json
import httpx

import reflex as rx

from rxconfig import config

from pcweb.templates.webpage import webpage


class SideBarState(rx.State):
    """Side Bar State."""

    community_apps_list: list[dict[str, str]]
    example_apps_list: list[dict[str, str]]

    tags_list: list[str]
    chosen_tags: set[str]

    def update_tag(self, name: str):
        self.chosen_tags.symmetric_difference_update({name})

    def _filter_by_tag(self, apps_list: list[dict[str, str]]) -> list[dict[str, str]]:
        """This function iterates over all the apps we have and if the app has one of the
        tags we have selected in true_tags then it will render this app in the UI."""
        if not self.chosen_tags:
            return apps_list
        return [
            app
            for app in apps_list
            if set(app["keywords"] or []).intersection(self.chosen_tags)
        ]

    @rx.cached_var
    def example_apps_to_return(self) -> list[dict[str, str]]:
        """This function returns the examples apps filtered by selected tags."""
        return self._filter_by_tag(self.example_apps_list)

    @rx.cached_var
    def community_apps_to_return(self) -> list[dict[str, str]]:
        """This function returns the community apps filtered by selected tags."""
        return self._filter_by_tag(self.community_apps_list)

    def fetch_apps_list(self):
        try:
            response = httpx.get(f"{config.cp_backend_url}/deployments/gallery")
            response.raise_for_status()
            all_apps = response.json()
        except (httpx.HTTPError, json.JSONDecodeError) as ex:
            print(
                f"Internal error: failed to fetch the complete list of apps due to: {ex}"
            )
            return

        # Make sure all apps have a keywords field.
        for app in all_apps:
            app["keywords"] = app.get("keywords") or []
            # If the app does not have a display name, use the first part of the domain name: e.g. https://test.reflex.run -> test
            subdomain_name = app["demo_url"].replace("https://", "").split(".")[0]
            app["display_name"] = app.get("display_name") or subdomain_name
            app["image_url_dark"] = (
                app.get("image_url")
                or f"https://placehold.co/600x400/000000/FFFFFF/?text={subdomain_name}"
            )
            app["image_url_light"] = (
                app.get("image_url")
                or f"https://placehold.co/600x400/FFFFFF/000000/?text={subdomain_name}"
            )

        # Make sure reflex web is the first app in the list.
        self.example_apps_list = [
            app for app in all_apps if app.get("demo_url") == "https://reflex.dev/"
        ] + [
            app
            for app in all_apps
            if app.get("is_example_app")
            and app.get("demo_url") != "https://reflex.dev/"
        ]
        self.community_apps_list = [
            app for app in all_apps if not app.get("is_example_app")
        ]
        unique_tags = set()
        for app in all_apps:
            unique_tags.update(app["keywords"] or [])
        self.tags_list = list(unique_tags)
        self.chosen_tags_dict = {key: False for key in self.tags_list}


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
            rx.color_mode_cond(
                rx.box(
                    background_image="url(" + category["image_url_light"] + ")",
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    height="100%",
                    width="100%",
                ),
                rx.box(
                    background_image="url(" + category["image_url_dark"] + ")",
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    height="100%",
                    width="100%",
                ),
            ),
            position="relative",
            height="12rem",
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
            rx.text(category["summary"], size="2", color="#8E8EA8"),
            align_items="start",
            width="100%",
            padding_top="1em",
        ),
        rx.spacer(),
        rx.vstack(
            rx.hstack(
                rx.cond(
                    category["difficulty"],
                    rx.hstack(
                        rx.badge(category["difficulty"]),
                    ),
                    rx.spacer(),
                ),
                rx.foreach(
                    category["keywords"],
                    lambda tag: rx.badge(tag, border_radius="15px", padding_x=".5em"),
                ),
                color="#8E8EA8",
                width="100%",
                overflow_x="scroll",
                style={
                    "&::-webkit-scrollbar-thumb": {
                        "background_color": "transparent",
                    },
                    "&::-webkit-scrollbar": {
                        "background_color": "transparent",
                    },
                },
            ),
            width="100%",
            padding_top="1em",
            align_items="start",
        ),
        direction="column",
        border_radius="14px;",
        border="1px solid #3C3646;",
        background="linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%);",
        box_shadow="0px 0px 27px -4px rgba(0, 0, 0, 0.30), 0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset;",
        padding="1em",
    )


grid_layout = [1, 1, 2, 2, 3, 3]


def component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(SideBarState.example_apps_to_return, add_item),
        columns=grid_layout,
        gap=4,
        padding_x="1em",
    )


def community_component_grid():
    return rx.chakra.responsive_grid(
        rx.foreach(SideBarState.community_apps_to_return, add_item),
        columns=grid_layout,
        gap=4,
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


@webpage(path="/docs/gallery", title="Gallery · Reflex")
def gallery() -> rx.Component:
    return rx.container(
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
            community_component_grid(),
            rx.spacer(),
            align_items="center",
            padding_x="1em",
        ),
        height="100%",
        width=["90%", "90%", "90%", "90%", "90%", "90%"],
        on_mount=SideBarState.fetch_apps_list,
    )
