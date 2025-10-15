import reflex as rx

from pcweb.components.icons.icons import get_icon
from pcweb.components.webpage.comps import h1_title
from pcweb.meta.meta import create_meta_tags
from pcweb.templates.webpage import webpage

from .page import page
from .paths import blog_data


def first_post_card(meta: dict, path: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.image(
                src=meta["image"],
                loading="lazy",
                alt="Image preview for blog post: " + str(meta["title"]),
                class_name="group-hover:scale-105 w-full h-full transition-transform duration-150 ease-out object-center object-cover",
            ),
            class_name="relative flex-shrink-0 w-1/2 h-[18rem] overflow-hidden border-r border-solid border-slate-5",
        ),
        rx.box(
            rx.box(
                rx.el.h4(
                    meta["title"],
                    class_name="font-x-large text-slate-12",
                ),
                rx.moment(
                    str(meta["date"]),
                    format="MMM DD, YYYY",
                    class_name="font-normal text-slate-9 text-sm",
                ),
                class_name="flex flex-col gap-1 p-[0.625rem_0.75rem_0rem_0.75rem] w-full",
            ),
            rx.box(
                rx.text(
                    meta["description"],
                    class_name="line-clamp-2 font-base text-slate-11",
                ),
                rx.box(
                    rx.text(
                        meta["author"],
                        class_name="font-small text-slate-9 truncate overflow-hidden text-ellipsis max-w-[50%] min-w-0 flex-shrink",
                    ),
                    rx.el.button(
                        rx.text(
                            "Read more",
                            class_name="font-small text-slate-9",
                        ),
                        get_icon(icon="new_tab", class_name="p-[5px]"),
                        class_name="flex items-center border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small pl-[5px] border rounded-md w-auto max-w-full text-slate-9 transition-bg cursor-pointer overflow-hidden flex-shrink-0",
                    ),
                    class_name="flex flex-row justify-between items-center gap-1 min-w-0 w-full h-auto",
                ),
                class_name="flex flex-col justify-between p-[0rem_0.75rem_0.75rem_0.75rem] w-full h-full",
            ),
            class_name="flex flex-col gap-[10px] w-full h-auto",
        ),
        href=path,
        is_external=False,
        underline="none",
        class_name="box-border lg:flex flex-row flex-shrink-0 gap-3 border-slate-5 hidden bg-slate-1 shadow-large border border-solid rounded-xl w-full overflow-hidden group",
    )


def card_content(meta: dict, path: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.image(
                src=meta["image"],
                loading="lazy",
                alt="Image preview for blog post: " + str(meta["title"]),
                class_name="group-hover:scale-105 w-full h-full transition-transform duration-150 ease-out object-center object-cover",
            ),
            class_name="relative flex-shrink-0 border-slate-5 border-b border-solid w-full h-[13.5rem] overflow-hidden",
        ),
        rx.box(
            rx.box(
                rx.el.h4(
                    meta["title"],
                    class_name="font-smbold text-slate-12",
                ),
                rx.moment(
                    str(meta["date"]),
                    format="MMM DD, YYYY",
                    class_name="font-normal text-slate-9 text-xs",
                ),
                class_name="flex flex-col gap-1 p-[0.625rem_0.75rem_0rem_0.75rem] w-full",
            ),
            rx.box(
                rx.text(
                    meta["description"],
                    class_name="line-clamp-2 font-small text-slate-11",
                ),
                rx.box(
                    rx.text(
                        meta["author"],
                        class_name="font-small text-slate-9 truncate overflow-hidden text-ellipsis max-w-[50%] min-w-0 flex-shrink",
                    ),
                    rx.el.button(
                        rx.text(
                            "Read more",
                            class_name="font-small text-slate-9",
                        ),
                        get_icon(icon="new_tab", class_name="p-[5px]"),
                        class_name="flex items-center border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small pl-[5px] border rounded-md w-auto max-w-full text-slate-9 transition-bg cursor-pointer overflow-hidden",
                    ),
                    class_name="flex flex-row justify-between items-center gap-1 w-full h-auto",
                ),
                class_name="flex flex-col justify-between p-[0rem_0.75rem_0.75rem_0.75rem] w-full h-full",
            ),
            class_name="flex flex-col gap-[10px] w-full h-full",
        ),
        href=path,
        is_external=False,
        underline="none",
        class_name="box-border flex flex-col flex-shrink-0 border-slate-5 bg-slate-1 shadow-large border border-solid rounded-xl w-full h-[390px] overflow-hidden group",
    )


def first_post() -> rx.Component:
    for path, document in blog_data.items():
        if path == next(iter(blog_data.keys())):
            return first_post_card(meta=document.metadata, path=f"/blog/{path}")


def component_grid() -> rx.Component:
    posts = []
    for path, document in list(blog_data.items()):
        posts.append(card_content(meta=document.metadata, path=f"/blog/{path}"))
    return rx.box(
        *posts,
        class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full mb-4 lg:[&>*:first-child]:hidden",
    )


@webpage(path="/blog", title="Reflex Blog")
def blogs():
    return rx.el.section(
        rx.el.header(
            h1_title(title="Blog"),
            rx.el.h2(
                "Reflex is the open-source framework empowering Python developers to build web apps faster.",
                class_name="font-md text-balance text-slate-10",
            ),
            class_name="pb-4 section-header",
        ),
        first_post(),
        component_grid(),
        id="blog",
        class_name="section-content",
    )


blog_routes = [blogs]
for path, document in blog_data.items():
    # Get the docpage component.
    route = f"/blog/{path}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    comp = webpage(
        path=route,
        title=document.metadata["title"] + " · Reflex Blog",
        description=document.metadata["description"],
        image=document.metadata["image"],
        meta=create_meta_tags(
            title=document.metadata["title"],
            description=document.metadata["description"],
            image=document.metadata["image"],
            url=f"https://reflex.dev{route}",
        ),
    )(lambda doc=document, route=route: page(doc, route))

    # Add the route to the list of routes.
    blog_routes.append(comp)
