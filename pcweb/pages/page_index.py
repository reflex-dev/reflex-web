import reflex as rx

from pcweb.templates.webpage import webpage

BLOG_POSTS = [
    (
        "Build Python Admin Panels and Internal Tools: A Complete Guide",
        "/blog/build-python-admin-panels-internal-tools-guide",
    ),
    ("Reflex vs Plotly Dash", "/blog/reflex-dash"),
    (
        "Top Python Web Development Frameworks in 2026",
        "/blog/top-python-web-frameworks",
    ),
    ("Designing a Pure Python Web Framework", "/blog/reflex-architecture"),
    ("Reflex vs Streamlit", "/blog/reflex-streamlit"),
]


def link_item(title: str, path: str) -> rx.Component:
    return rx.el.li(
        rx.el.a(
            title,
            href=path,
            class_name="text-slate-11 hover:text-slate-12 underline",
        ),
        class_name="py-1",
    )


@webpage(path="/page-index", title="Page Index")
def page_index() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Page Index",
            class_name="text-3xl font-bold text-slate-12 mb-6",
        ),
        rx.el.ul(
            *[link_item(title, path) for title, path in BLOG_POSTS],
            class_name="list-disc pl-6 flex flex-col gap-1",
        ),
        class_name="max-w-2xl mx-auto px-6 py-12",
    )
