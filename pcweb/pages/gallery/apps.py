import reflex as rx
import flexdown
from flexdown.document import Document
from pcweb.flexdown import xd2 as xd
from pcweb.templates.gallery_app_page import gallery_app_page
from pcweb.components.icons import get_icon
from pcweb.pages.gallery import gallery
from pcweb.components.button import button, button_with_icon
from pcweb.components.code_card import gallery_app_card
import copy

GALLERY_APPS_PATH = "templates/"


def get_gallery_apps(paths):
    gallery_apps = {}
    for path in reversed(sorted(paths)):
        document = Document.from_file(path)
        path = str(path).replace(".md", "/")
        gallery_apps[path] = document
    return gallery_apps


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(GALLERY_APPS_PATH, "").replace(".md", "")


paths = flexdown.utils.get_flexdown_files(GALLERY_APPS_PATH)
gallery_apps_data = get_gallery_apps(paths)


def more_posts(current_post: dict) -> rx.Component:
    posts = []
    app_copy = copy.deepcopy(gallery_apps_data)
    app_items = list(app_copy.items())
    current_index = next(
        (
            i
            for i, (path, document) in enumerate(app_items)
            if document.metadata.get("title") == current_post.get("title")
        ),
        None,
    )

    # Always show 3 posts, excluding the current one
    if current_index is None:
        # If current post is not found, show the last 3 posts
        selected_posts = app_items[-3:]
    else:
        # Create a list of all posts except the current one
        other_posts = app_items[:current_index] + app_items[current_index + 1 :]

        if len(other_posts) <= 3:
            # If there are 3 or fewer other posts, show all of them
            selected_posts = other_posts
        elif current_index == 0:
            # If it's the first post, show the next 3
            selected_posts = other_posts[:3]
        elif current_index >= len(app_items) - 1:
            # If it's the last post, show the previous 3
            selected_posts = other_posts[-3:]
        else:
            # For all other cases, show one before and two after (or two before and one after if we're near the end)
            if current_index < len(app_items) - 2:
                selected_posts = other_posts[current_index - 1 : current_index + 2]
            else:
                selected_posts = other_posts[current_index - 2 : current_index + 1]

    for path, document in selected_posts:
        meta = document.metadata
        posts.append(gallery_app_card(app=meta))
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "More Templates",
                class_name="font-large text-slate-12",
            ),
            rx.link(
                rx.box(
                    rx.text(
                        "View All", class_name="font-small text-slate-9 text-nowrap"
                    ),
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


def page(document) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.el.section(
        rx.el.article(
            rx.image(
                src=meta["image"],
                alt=f"Image for Reflex App: {meta['title']}",
                loading="lazy",
                class_name="w-full object-cover max-w-full aspect-[1500/938] border-y border-slate-3 border-solid",
            ),
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
                        href=gallery.path,
                    ),
                    rx.el.h1(
                        meta["title"],
                        class_name="font-x-large text-slate-12",
                    ),
                    rx.el.h2(
                        meta["description"],
                        class_name="font-md text-slate-11",
                    ),
                    class_name="flex flex-col gap-3 p-8",
                ),
                rx.box(
                    *(
                        [
                            rx.link(
                                button_with_icon(
                                    "View Demo",
                                    icon="new_tab",
                                    class_name="!w-full flex-row-reverse gap-2",
                                ),
                                is_external=True,
                                href=meta["demo"],
                            )
                        ]
                        if meta.get("demo")
                        else []
                    ),
                    rx.link(
                        button("View Code", variant="muted", class_name="!w-full"),
                        is_external=True,
                        href=meta["source"],
                    ),
                    rx.cond(
                        "Reflex" in meta["author"],
                        rx.box(
                            rx.text(
                                "Created by",
                                class_name="text-slate-9 font-base",
                            ),
                            get_icon(
                                icon="badge_logo",
                            ),
                            rx.text(
                                meta["author"],
                                class_name="text-slate-9 font-base",
                            ),
                            class_name="flex flex-row items-center gap-1 self-end",
                        ),
                        rx.text(
                            f"by {meta['author']}",
                            class_name="text-slate-9 font-base",
                        ),
                    ),
                    class_name="p-8 flex flex-col gap-4",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 divide-y lg:divide-y-0 lg:divide-x divide-slate-3 border-b border-slate-3",
            ),
            rx.box(
                xd.render(document, "blog.md"),
                class_name="flex flex-col gap-4 w-full p-8",
            ),
            more_posts(meta),
            class_name="flex flex-col max-w-full",
        ),
    )


gallery_apps_routes = []
for path, document in gallery_apps_data.items():
    # Get the docpage component.
    route = f"/templates/{document.metadata['title'].replace(' ', '-').lower()}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    # Add "/gallery" to the image path
    document.metadata["image"] = f"/templates/{document.metadata['image']}"
    comp = gallery_app_page(
        path=route,
        title=document.metadata["title"],
        description=document.metadata["description"],
        image=document.metadata["image"],
        demo=document.metadata["demo"] if "demo" in document.metadata else None,
        meta=document.metadata["meta"],
    )(lambda doc=document: page(doc))

    # Add the route to the list of routes.
    gallery_apps_routes.append(comp)
