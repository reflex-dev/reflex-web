"""The main Reflex website."""

import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.component_list import component_list
from pcweb.middleware import CloseSidebarMiddleware
from pcweb.pages import blog_routes, doc_routes, routes, faq_routes, changelog_routes
from pcweb.pages.docs.component import multi_docs

from pcweb.pages import page404

# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-4T7C8ZD9TR"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){window.dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-4T7C8ZD9TR');
"""
        ),
    ],
)

# Add the pages to the app.
for route in routes:
    app.add_page(
        route.component,
        route.path,
        "Reflex",
        description="Performant, customizable web apps in pure Python. Deploy in seconds.",
        image="/previews/index_preview.png",
    )

# Add the pages to the app.
for route in blog_routes:
    app.add_page(
        route.component,
        route.path,
        "Reflex | Blog",
        description="Keep up to date with the latest Reflex news.",
        image="/previews/blog_preview.png",
    )

# Add the pages to the app.
for route in doc_routes:
    app.add_page(
        route.component,
        route.path,
        "Reflex | Docs",
        description="Learn how to build web apps in pure Python.",
        image="/previews/docs_preview.png",
    )

# # Add the pages to the app.
for route in changelog_routes:
    app.add_page(
        route.component,
        route.path,
        "Reflex | Changelog",
        description="Keep up to date with the latest Reflex news.",
        image="/previews/changelog_preview.png",
    )

# Add the pages to the app.
for route in faq_routes:
    app.add_page(
        route.component,
        route.path,
        "Reflex | FAQ",
        description="Frequently asked questions about Reflex.",
        image="/previews/faq_preview.png",
    )


for key in component_list:
    for component_group in component_list[key]:
        if isinstance(component_group[0], str):
            continue
        else:
            path = f"/docs/library/{key.lower()}/{component_group[0].__name__.lower()}"
            app.add_page(
                multi_docs(path=path, component_list=component_group).component,
                route=path,
                title=f"Reflex | {component_group[0].__name__}",
                description=f"Reflex | Docs for {component_group[0].__name__} component.",
                image="/previews/index_preview.png",
            )

# Add the middleware.
app.add_middleware(CloseSidebarMiddleware(), index=0)

# Add redirects
redirects = [
    ("/docs", "/docs/getting-started/introduction"),
    ("/docs/getting-started", "/docs/getting-started/introduction"),
    ("/docs/components", "/docs/components/overview"),
    ("/docs/state", "/docs/state/overview"),
    ("/docs/styling", "/docs/styling/overview"),
    ("/docs/database", "/docs/database/overview"),
    ("/docs/hosting", "/docs/hosting/self-hosting"),
    ("/docs/advanced-guide", "/docs/advanced-guide/custom-vars"),
    ("/docs/library/typography", "/docs/library/typography/text"),
    ("/docs/library/forms", "/docs/library/forms/form"),
    ("/docs/library/layout", "/docs/library/layout/box"),
    ("/docs/library/navigation", "/docs/library/navigation/link"),
    ("/docs/library/datadisplay", "/docs/library/datadisplay/badge"),
    ("/docs/library/graphing", "/docs/library/graphing/chart"),
    ("/docs/library/disclosure", "/docs/library/disclosure/accordion"),
    ("/docs/library/feedback", "/docs/library/feedback/alert"),
    ("/docs/library/media", "/docs/library/media/image"),
    ("/docs/library/overlay", "/docs/library/overlay/alertdialog"),
    ("/docs/library/other", "/docs/library/other/html"),
]

for source, target in redirects:
    app.add_page(lambda: rx.fragment(), route=source, on_load=rx.redirect(target))

app.add_custom_404_page(page404.index)
# Run the app.
app.compile() 
 