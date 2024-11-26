import reflex as rx

from pcweb.templates.webpage import webpage
from pcweb.components.webpage.comps import h1_title
from pcweb.components.code_card import gallery_app_card


@rx.memo
def skeleton_card() -> rx.Component:
    return rx.skeleton(
        class_name="box-border shadow-large border rounded-xl w-full h-[280px] overflow-hidden",
        loading=True,
    )


def component_grid() -> rx.Component:
    from pcweb.pages.gallery.apps import gallery_apps_data

    posts = []
    for path, document in list(gallery_apps_data.items()):
        posts.append(gallery_app_card(app=document.metadata))
    return rx.box(
        *posts,
        class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full mb-[7.5rem]",
    )


def gallery_heading() -> rx.Component:
    return rx.box(
        h1_title(title="Reflex Templates"),
        rx.el.h2(
            """Check out what the community is building with Reflex. See 2000+ more public projects on """,
            rx.link(
                "Github",
                href="https://github.com/reflex-dev/reflex/network/dependents",
                is_external=True,
            ),
            ".",
            class_name="font-md text-balance text-slate-9",
        ),
        rx.text.span(
            "Want to get your app featured? ",
            rx.text.span(
                "Submit it ",
                rx.link(
                    "here",
                    href="https://github.com/reflex-dev/templates",
                    is_external=True,
                ),
                ".",
                class_name="font-md text-balance text-slate-9",
            ),
            class_name="font-md text-balance text-slate-9 -mt-4",
        ),
        rx.text.span(
            "Copy the template command and use it during ",
            rx.code("reflex init"),
            class_name="font-sm text-balance text-slate-9",
        ),
        class_name="section-header",
    )


@webpage(path="/templates", title="Templates · Reflex")
def gallery() -> rx.Component:
    return rx.el.section(
        gallery_heading(),
        component_grid(),
        id="gallery",
        class_name="section-content",
    )
