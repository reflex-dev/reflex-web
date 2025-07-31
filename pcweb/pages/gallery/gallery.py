import flexdown
import reflex as rx
import re
from pcweb.templates.webpage import webpage
from pcweb.components.button import button
from pcweb.components.icons import get_icon

REFLEX_BUILD_TEMPLATES_PATH = "reflex_build_templates/"
REFLEX_BUILD_TEMPLATES_IMAGES = "reflex_build_template_images/"

def get_templatey_apps(paths):
    """Method to parse each markdown file and return the data from the file"""
    gallery_apps = {}
    for path in reversed(sorted(paths)):
        document = flexdown.Document.from_file(path)  # This has metadata
        key = str(path).replace(".md", "/")
        gallery_apps[key] = document
    return gallery_apps

paths = flexdown.utils.get_flexdown_files(REFLEX_BUILD_TEMPLATES_PATH)
template_apps_data = get_templatey_apps(paths)


def app_dialog_with_trigger(
    app_url: str,
    app_name: str,
    app_author: str,
    app_thread: str,
    app_inner_page: str,
    trigger_content: rx.Component,
):
    return rx.dialog.root(
        rx.dialog.trigger(trigger_content, class_name="w-full h-full"),
        rx.dialog.content(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            app_name, class_name="text-md !text-slate-11 font-bold"
                        ),
                        rx.el.p(app_author, class_name="text-sm !text-slate-9"),
                        class_name="flex flex-row gap-x-2 items-center",
                    ),
                    rx.link(
                        button(
                            "Learn More",
                            variant="secondary",
                            size="md",
                        ),
                        href=app_inner_page,
                        class_name="no-underline outline-none",
                    ),
                    class_name="flex flex-row items-center justify-between",
                ),
                rx.el.iframe(
                    src=app_url,
                    class_name="w-full h-full xl:rounded-md shadow-small",
                    id="iFrame",
                ),
                class_name="flex flex-col w-full h-full gap-y-3",
            ),
            class_name="w-full !max-w-[75em] xl:max-w-[85em] 2xl:max-w-[95em] h-[80vh]",
        ),
    )

def extended_gallery_grid_item(app_url: str, app_name: str, app_author: str, app_thread: str, app_image: str, app_inner_page: str):
    return app_dialog_with_trigger(
        app_url=app_url,
        app_author=app_author,
        app_name=app_name,
        app_thread=app_thread,
        app_inner_page=app_inner_page,
        trigger_content=rx.el.div(
            rx.el.div(
                rx.image(
                    src=app_image,
                    class_name="group-hover:scale-105 duration-200 ease-out object-center object-cover absolute inset-0 h-full w-full blur-in transition-all rounded-[12px] z-10",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.link(
                            button(
                                "Learn More",
                                variant="secondary",
                                size="md",
                                class_name="w-full",
                                on_click=rx.stop_propagation,
                            ),
                            href=app_inner_page,
                            class_name="no-underline flex-1",
                            on_click=rx.stop_propagation,
                        ),
                        button("Preview", variant="primary", size="md", class_name="flex-1"),
                        class_name="flex flex-row gap-x-2 w-full items-stretch px-4 pb-4",
                    ),
                    class_name="absolute inset-0 flex items-end justify-center z-20 opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 ease-out pointer-events-none group-hover:pointer-events-auto z-[99]",
                ),
                class_name="overflow-hidden rounded-[12px] relative w-full h-full aspect-video ease-out duration-200 transition-all outline-none border border-slate-4 group-hover:border-slate-3",
            ),
            rx.el.div(
                rx.el.div(
                    get_icon(icon="badge_logo", class_name="size-5 flex-shrink-0",),
                    rx.el.div(
                        rx.el.p(app_name, class_name="text-sm font-medium truncate"),
                        rx.el.p(app_author, class_name="text-sm font-regular text-slate-9 truncate"),
                        class_name="flex flex-col gap-y-0 min-w-0 w-full",
                    ),
                    class_name="flex flex-row gap-x-2 items-start min-w-0 w-full",
                ),
                class_name="flex flex-row items-center gap-4 justify-between !text-slate-10 group-hover:!text-slate-11 w-full",
            ),
            class_name="flex flex-col gap-2 w-full p-2 rounded-[14px] group hover:bg-slate-3 transition-all duration-200 ease-out cursor-pointer !w-full",
        ),
    )


def create_grid_with_items():
    items = []
    for path, document in template_apps_data.items():
        meta = document.metadata
        app_url = meta.get("demo", "#")
        app_name = meta.get("title", "Untitled").replace("_", " ").title()
        app_author = meta.get("author", "Team Reflex")
        app_thread = f"/gen/{app_name.lower().replace(' ', '-')}/"
        app_image = meta.get('image', "")
        slug = re.sub(r"[\s_]+", "-", meta.get("title", "")).lower()
        app_inner_page = f"/templates/{slug}"

        items.append(extended_gallery_grid_item(
            app_url=app_url,
            app_name=app_name,
            app_author=app_author,
            app_thread=app_thread,
            app_image=f"/{REFLEX_BUILD_TEMPLATES_IMAGES}{app_image}",
            app_inner_page=app_inner_page
        ))

    return rx.el.div(
        *items,
        class_name="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-2 md:px-8 lg:px-8"
    )

def create_header():
    return rx.box(
        rx.box(
            rx.el.h2(
                "Reflex Build Templates",
                class_name="text-slate-12 text-4xl font-bold mb-6",
            ),
            rx.el.p(
                "Production-ready app templates built with Reflex — explore dashboards, tools, and AI-powered apps.",
                class_name="text-slate-11 text-lg leading-relaxed mb-12 max-w-lg font-medium",
            ),
            class_name="mb-8 lg:mb-0 text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-6 w-full text-center",
    )

@webpage(path="/templates", title="Templates · Reflex")
def gallery() -> rx.Component:
    return rx.el.section(
        rx.box(
            create_header(),
            create_grid_with_items(),
            class_name="w-full !max-w-[94.5rem] mx-auto",
        ),
        id="gallery",
        class_name="w-full px-4 pt-24 lg:pt-52 mt-4 mb-20",
    )
