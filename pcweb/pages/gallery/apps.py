import flexdown
import reflex as rx
import re

from pcweb.components.button import button, button_with_icon
from pcweb.components.code_card import gallery_app_card
from pcweb.components.icons import get_icon
from pcweb.constants import SCREENSHOT_BUCKET
from pcweb.flexdown import xd2 as xd
from pcweb.pages.gallery import gallery
from pcweb.templates.gallery_app_page import gallery_app_page

GALLERY_APP_SOURCES = [
    ("templates/", "docs/getting-started/open-source-templates/"),
    ("reflex_build_templates/", "templates/"),
]


def load_all_gallery_apps():
    """Load markdown files from all supported paths and associate them with their base folder."""
    gallery_apps = {}
    for folder, _ in GALLERY_APP_SOURCES:
        paths = flexdown.utils.get_flexdown_files(folder)
        for path in reversed(sorted(paths)):
            document = flexdown.parse_file(path)
            clean_path = path.replace(".md", "/")
            gallery_apps[(clean_path, folder)] = document

    return gallery_apps


gallery_apps_data = load_all_gallery_apps()
gallery_apps_data_copy = {
    path: doc for (path, _), doc in gallery_apps_data.items()
}


def more_posts(current_post: dict) -> rx.Component:
    posts = []
    app_items = list(gallery_apps_data_copy.items())
    current_index = next(
        (
            i
            for i, (path, document) in enumerate(app_items)
            if document.metadata.get("title") == current_post.get("title")
        ),
        None,
    )

    if current_index is None:
        selected_posts = app_items[-3:]
    else:
        other_posts = app_items[:current_index] + app_items[current_index + 1:]
        if len(other_posts) <= 3:
            selected_posts = other_posts
        elif current_index == 0:
            selected_posts = other_posts[:3]
        elif current_index >= len(app_items) - 1:
            selected_posts = other_posts[-3:]
        else:
            if current_index < len(app_items) - 2:
                selected_posts = other_posts[current_index - 1: current_index + 2]
            else:
                selected_posts = other_posts[current_index - 2: current_index + 1]

    for path, document in selected_posts:
        posts.append(gallery_app_card(app=document.metadata))

    return rx.el.section(
        rx.box(
            rx.el.h2("More Templates", class_name="font-large text-slate-12"),
            rx.link(
                rx.box(
                    rx.text("View All", class_name="font-small text-slate-9 text-nowrap"),
                    get_icon(icon="new_tab", class_name=""),
                    class_name="flex items-center gap-1.5 border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small px-1.5 py-0.5 border rounded-md w-auto max-w-full text-slate-9 transition-bg cursor-pointer overflow-hidden border-solid",
                ),
                underline="none",
                href=gallery.path,
            ),
            class_name="flex flex-row items-center justify-between gap-4",
        ),
        rx.box(
            *posts,
            class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[300px] w-full mb-4 blog-grid",
        ),
        class_name="flex flex-col gap-10 mt-20 p-8 border-t border-slate-3",
    )


def page(document, is_reflex_template: bool) -> rx.Component:
    """Render a detailed app page based on source type."""
    meta = document.metadata

    image_component = (
        rx.image(
            src=meta["image"],
            alt=f"Image for Reflex App: {meta['title']}",
            loading="lazy",
            class_name="w-full object-cover max-w-full aspect-[1500/938] border-y border-slate-3 border-solid",
        )
        if not is_reflex_template else
        rx.el.div(
            rx.box(
                rx.el.h1(
                    meta["title"].replace("_", " ").title(),
                    class_name="font-x-large text-slate-12 text-left",
                ),
                class_name="w-full self-start pl-4",
            ),
            rx.el.iframe(
                src=meta['demo'],
                class_name="w-full h-full xl:rounded-md shadow-small",
                id="iFrame",
            ),
            class_name="w-full h-[65vh] bg-slate-2 text-center flex flex-col gap-y-4 items-center text-slate-10",
        )
    )

    back_route_origin = "/docs/getting-started/open-source-templates/" if not is_reflex_template else "/templates/"

    return rx.el.section(
        rx.el.article(
            image_component,
            rx.box(
                rx.el.header(
                    rx.link(
                        rx.box(
                            get_icon("arrow_right", class_name="rotate-180"),
                            "Back to Templates",
                            class_name="box-border flex justify-center items-center gap-2 bg-slate-1 py-0.5 font-small text-slate-9 transition-color cursor-pointer hover:text-slate-11 mb-6",
                        ),
                        underline="none",
                        class_name="flex w-fit",
                        href=back_route_origin,
                    ),
                    rx.el.h1(meta["title"], class_name="font-x-large text-slate-12") if not is_reflex_template else rx.fragment(),
                    rx.el.h2(meta["description"], class_name="font-md text-slate-11"),
                    class_name="flex flex-col gap-3 p-8",
                ),
                rx.box(
                    *(
                        [rx.box(
                                    rx.link(
                                        button_with_icon(
                                            "Book a Demo",
                                            icon="new_tab",
                                            class_name="flex-row-reverse gap-2 !w-full",
                                        ),
                                        is_external=True,
                                        href="/pricing",
                                        class_name="!w-full"
                                    ),
                                    class_name="flex justify-center items-center h-full !w-full",
                                )] if is_reflex_template else
                        (
                            [rx.link(
                                button_with_icon(
                                    "View Demo",
                                    icon="new_tab",
                                    class_name="!w-full flex-row-reverse gap-2",
                                ),
                                is_external=True,
                                href=meta["demo"],
                            )] if meta.get("demo") else []
                        )
                    ),
                    rx.link(
                        button("View Code", variant="muted", class_name="!w-full"),
                        is_external=True,
                        href=meta.get('source', "#"),
                    ) if not is_reflex_template else rx.fragment(),
                    rx.cond(
                        "Reflex" in meta["author"],
                        rx.box(
                            rx.text("Created by", class_name="text-slate-9 font-base"),
                            get_icon(icon="badge_logo"),
                            rx.text(meta["author"], class_name="text-slate-9 font-base"),
                            class_name="flex flex-row items-center gap-1 self-end",
                        ),
                        rx.text(f"by {meta['author']}", class_name="text-slate-9 font-base"),
                    ) if not is_reflex_template else rx.fragment(),
                    class_name="p-8 flex flex-col gap-4",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-slate-3 border-b border-slate-3",
            ),
            rx.box(
                xd.render(document, "blog.md"),
                class_name="flex flex-col gap-4 w-full p-8",
            ),
            more_posts(meta) if not is_reflex_template else rx.fragment(),
            class_name="flex flex-col max-w-full",
        ),
    )



gallery_apps_routes = []
for (path, source_folder), document in gallery_apps_data.items():
    is_reflex_template = source_folder.startswith("reflex_build_templates")
    base_url = "templates/" if is_reflex_template else "docs/getting-started/open-source-templates/"
    slug = re.sub(r"[\s_]+", "-", document.metadata["title"]).lower()
    route = f"/{base_url}{slug}"

    document.metadata["image"] = (
        f"/templates/{document.metadata['image']}"
        if not document.metadata.get("ai_template", False)
        else f"{SCREENSHOT_BUCKET}{document.metadata['image']}"
    )

    comp = gallery_app_page(
        path=route,
        title=document.metadata["title"],
        description=document.metadata.get("description", ""),
        image=document.metadata["image"],
        demo=document.metadata.get("demo"),
        meta=document.metadata.get("meta", []),
    )(lambda doc=document, is_reflex_template=is_reflex_template: page(doc, is_reflex_template))

    gallery_apps_routes.append(comp)
