# What Is Reflex Build

<div class="p-1 my-4 rounded-lg bg-slate-5">
  <iframe
    width="100%"
    height="400"
    src="https://www.youtube.com/embed/s-kr8v7827g "
    title="Reflex Build"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>


Reflex Build is an AI-powered platform that empowers users of all skill levels to create full-stack web applications
without writing any code—just by describing their ideas in plain English. Instead of hiring developers, users can
instantly generate web apps or websites, turning ideas into functional apps as quickly as possible.


Reflex Build provides everything you need to create stunning websites, front-end interfaces, and full-stack web
applications—all from a single browser tab, with no installation required. It includes AI-powered coding tools,
real-time collaboration (currently in beta), and easy project sharing to give you a head start on your app development
journey.



```python exec
from typing import List, TypedDict

import reflex as rx
from reflex_image_zoom import image_zoom


class Feature(TypedDict):
    title: str
    description: str
    icon: str


class LandingState(rx.State):
    features: List[Feature] = [
        {
            "title": "Database Integration",
            "description": "Automatically integrate your database\ninto your application with ease",
            "icon": "database",
        },
        {
            "title": "Secure Secrets",
            "description": "Safely manage your API keys and tokens\nwith a built in secrets manager",
            "icon": "shield",
        },
        {
            "title": "Live Preview",
            "description": "See all application changes in real-time\nwith our interactive preview tab",
            "icon": "eye",
        },
        {
            "title": "Quick Download",
            "description": "Download your complete project files\nwith just a single click operation",
            "icon": "download",
        },
        {
            "title": "Easy Deployment",
            "description": "Deploy your application to production\nwith just a single click process",
            "icon": "rocket",
        },
        {
            "title": "Manual File Editing",
            "description": "Edit your project files directly\nwith our intuitive code editor",
            "icon": "code",
        },
        {
            "title": "AI Package Manager",
            "description": "Let AI handle your package installations\nvia natural prompting",
            "icon": "sparkles",
        },
        {
            "title": "Smart Prompting",
            "description": "Get better development results\nwith AI-optimized prompt templates",
            "icon": "message-circle",
        },
    ]


class BuildDocState(rx.State):
    current_feature: dict[str, str] = {
        "light": "/ai_builder/what_is_reflex_build/project_bar_light.png",
        "dark": "/ai_builder/what_is_reflex_build/project_bar_dark.png",
    }

    image_opacity: float = 1.0  # Use float instead of string for opacity
    transition_in_progress: bool = False

    features: list[dict[str, str | dict[str, str]]] = [
        {
            "title": "Project Menu Bar",
            "subtitle": "Browse previously built applications, create new sessions, store database variables, and much more!",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/project_bar_light.png",
                "dark": "/ai_builder/what_is_reflex_build/project_bar_dark.png",
            },
            "selected": True,
        },
        {
            "title": "Chat Area",
            "subtitle": "See your prompts in action with visual cues, editing notifications, and file generations every step of the way.",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/chat_light.png",
                "dark": "/ai_builder/what_is_reflex_build/chat_dark.png",
            },
            "selected": False,
        },
        {
            "title": "Application Workspace",
            "subtitle": "Your workspace contains all the folders and files of your application. You can add new files and folders as well!",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/file_tree_light.png",
                "dark": "/ai_builder/what_is_reflex_build/file_tree_dark.png",
            },
            "selected": False,
        },
        {
            "title": "Code Editor",
            "subtitle": "The code editor displays the current selected file. You can edit the code directly and save it instantly.",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/code_light.png",
                "dark": "/ai_builder/what_is_reflex_build/code_dark.png",
            },
            "selected": False,
        },
        {
            "title": "Bottom Menu Bar",
            "subtitle": "This menu contains important actions such as deploying, downloading, and sharing your application.",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/bottom_light.png",
                "dark": "/ai_builder/what_is_reflex_build/bottom_dark.png",
            },
            "selected": False,
        },
        {
            "title": "Preview Tab",
            "subtitle": "The preview tab showcases a live application. You can navigate to other applications directly from this tab, refresh the app, and even view it in full screen.",
            "img": {
                "light": "/ai_builder/what_is_reflex_build/preview_light.png",
                "dark": "/ai_builder/what_is_reflex_build/preview_dark.png",
            },
            "selected": False,
        },
    ]

    @rx.event(background=True)
    async def select_feature(self, index: int):
        import asyncio

        # Prevent multiple transitions at once
        if self.transition_in_progress:
            return

        # Update the selected feature and image
        async with self:
            for i, feature in enumerate(self.features):
                feature["selected"] = i == index

            self.transition_in_progress = True

            # Fade out
            self.image_opacity = 0.0
            yield
            await asyncio.sleep(0.1)

            self.current_feature = self.features[index]["img"]
            await asyncio.sleep(0.2)

            # # Fade in
            self.image_opacity = 1.0
            self.transition_in_progress = False


feature_images = [
    [
        "/ai_builder/what_is_reflex_build/project_bar_light.png",
        "/ai_builder/what_is_reflex_build/project_bar_dark.png",
        "Project Menu Bar",
        "Browse previously built applications, create new sessions, store database variables, and much more!",
    ],
    [
        "/ai_builder/what_is_reflex_build/chat_light.png",
        "/ai_builder/what_is_reflex_build/chat_dark.png",
        "Chat Area",
        "See your prompts in action with visual cues, editing notifications, and file generations every step of the way.",
    ],
    [
        "/ai_builder/what_is_reflex_build/file_tree_light.png",
        "/ai_builder/what_is_reflex_build/file_tree_dark.png",
        "Application Workspace",
        "Your workspace contains all the folders and files of your application. You can add new files and folders as well!",
    ],
    [
        "/ai_builder/what_is_reflex_build/code_light.png",
        "/ai_builder/what_is_reflex_build/code_dark.png",
        "Code Editor",
        "The code editor displays the current selected file. You can edit the code directly and save it instantly.",
    ],
    [
        "/ai_builder/what_is_reflex_build/bottom_light.png",
        "/ai_builder/what_is_reflex_build/bottom_dark.png",
        "Bottom Menu Bar",
        "This menu contains important actions such as deploying, downloading, and sharing your application.",
    ],
    [
        "/ai_builder/what_is_reflex_build/preview_light.png",
        "/ai_builder/what_is_reflex_build/preview_dark.png",
        "Preview Tab",
        "The preview tab showcases a live application. You can navigate to other applications directly from this tab, refresh the app, and even view it in full screen.",
    ],
]


def feature_card(feature: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                rx.icon(
                    tag=feature["icon"],
                    size=15,
                    class_name="inline-block pr-2 "
                    + rx.color_mode_cond(
                        "stroke-purple-8",
                        "stroke-purple-9",
                    ),
                ),
                rx.el.span(f"{feature['title']} ", class_name="text-sm font-bold"),
                class_name="text-sm font-medium block align-center pt-5 px-2",
            ),
            rx.el.span(
                feature["description"],
                class_name="text-sm font-regular block align-center px-2",
            ),
            class_name="flex flex-col",
        ),
        class_name="w-full rounded-md",
    )


def _docs_features() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(LandingState.features, feature_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 gap-4",
        ),
        class_name="flex flex-col w-full h-full justify-start align-start items-start py-4 gap-x-4 z-[99]",
    )


def _docs_app_section_features_small_screen(feature: list[str]):
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(feature[0], feature[1]),
                class_name="p-2 rounded-md h-auto",
                border=f"0.81px solid {rx.color('slate', 5)}",
            ),
            class_name="rounded-md overflow-hidden",
        ),
        rx.el.div(
            rx.el.label(feature[2], class_name="text-sm font-bold cursor-pointer"),
            rx.el.label(feature[3], class_name="text-sm font-light cursor-pointer"),
            class_name="flex flex-col px-1 py-2",
        ),
        class_name="w-full flex flex-col rounded-md cursor-pointer",
    )


def _docs_app_section_toggles(feature: dict, index: int):
    return rx.el.div(
        rx.el.label(feature["title"], class_name="text-sm font-bold cursor-pointer"),
        rx.el.label(
            feature["subtitle"], class_name="text-sm font-light cursor-pointer"
        ),
        on_click=BuildDocState.select_feature(index),
        class_name="w-full flex flex-col max-w-md rounded-md p-4 cursor-pointer "
        + rx.cond(
            feature["selected"],
            "",
            rx.color_mode_cond("hover:bg-slate-5", "hover:bg-slate-3"),
        ),
        border=rx.cond(
            feature["selected"],
            f"0.81px solid {rx.color('purple', 7)}",
            "",
        ),
        box_shadow=rx.cond(
            feature["selected"],
            rx.color_mode_cond(
                "5px 5px oklch(0.946 0.033 307.174 / 0.5)",
                "",
            ),
            "",
        ),
    )


def _docs_app_sections():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Small details, big impact", class_name="text-sm font-light"
                ),
                rx.el.label(
                    "Made With Exceptional Care", class_name="text-3xl font-bold"
                ),
                rx.el.label(
                    "Every feature in Reflex Build is carefully crafted to set new standards. Mediocre isn't an option.",
                    class_name="text-md font-regular",
                ),
                class_name="flex flex-col w-full max-w-lg gap-y-1",
            ),
            rx.foreach(
                BuildDocState.features[:5],
                lambda feature, index: _docs_app_section_toggles(feature, index),
            ),
            class_name="flex flex-col gap-y-4 justify-start max-w-sm",
        ),
        rx.el.div(
            image_zoom(
                rx.image(
                    src=rx.color_mode_cond(
                        BuildDocState.current_feature["light"],
                        BuildDocState.current_feature["dark"],
                    ),
                    class_name="p-2 rounded-md h-auto",
                    border=f"0.81px solid {rx.color('slate', 5)}",
                ),
                class_name="rounded-md overflow-hidden",
            ),
            style={
                "opacity": f"{BuildDocState.image_opacity}",
                "transition": "opacity 300ms ease-in-out",
            },
            class_name="w-full max-w-4xl",
        ),
        class_name="flex flex-row w-full h-full justify-between align-center items-center py-4 gap-x-4 z-[99]",
        display=["none" if i <= 4 else "flex" for i in range(6)],
    )


def _docs_app_sections_small_screen():
    return rx.el.div(
        rx.el.div(
            rx.grid(
                rx.foreach(
                    feature_images,
                    lambda feature: _docs_app_section_features_small_screen(feature),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-10 w-full",
            ),
            class_name="flex flex-col gap-y-4 justify-start py-4",
        ),
    )






screen_normalization = (
        "z-[99] w-full"
    )
```


## Feature Overview

Reflex Build provides a streamlined interface for building AI applications. The **Project Menu Bar** helps you manage sessions and stored variables, while the **Chat Area** displays real-time prompts, edits, and file generations. The **Application Workspace** organizes your project structure, and the **Code Editor** allows direct, instant code editing. Key actions like deploy and share are accessible via the **Bottom Menu Bar**, and the **Preview Tab** lets you view and interact with your live app at any time.

```python eval
rx.el.div(
    _docs_app_sections_small_screen(),
)
```

## Interface Highlights

Reflex Build’s interface is designed for clarity and efficiency. The **Project Menu Bar** helps you manage sessions, apps, and variables. The **Chat Area** shows prompts in action with visual feedback and file generation. In the **Application Workspace**, you can view and organize your project files. The **Code Editor** allows quick, direct edits with instant saving. Use the **Bottom Menu Bar** for key actions like deploy and download. The **Preview Tab** lets you interact with a live version of your app, including refresh and full-screen options.

```python eval
rx.el.div(
    rx.el.div(_docs_features(), class_name=screen_normalization),
)
```
