"""The main Reflex website."""

import os
import sys

import reflex as rx

from pcweb import styles
from pcweb.meta.meta import favicons_links
from pcweb.pages import page404, routes
from pcweb.pages.docs import exec_blocks, outblocks
from pcweb.telemetry import get_pixel_website_trackers
from pcweb.whitelist import _check_whitelisted_path

# This number discovered by trial and error on Windows 11 w/ Node 18, any
# higher and the prod build fails with EMFILE error.
WINDOWS_MAX_ROUTES = int(os.environ.get("REFLEX_WEB_WINDOWS_MAX_ROUTES", "100"))

# Execute all the exec blocks in the documents.
for doc, href in outblocks:
    exec_blocks(doc, href)

# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    theme=rx.theme(
        has_background=True,
        radius="large",
        accent_color="violet",
    ),
    head_components=get_pixel_website_trackers()
    + favicons_links()
    + [
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&family=Source+Code+Pro:wght@400;500&display=swap&family=JetBrains+Mono:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)

# XXX: The app is TOO BIG to build on Windows, so explicitly disallow it except for testing
if sys.platform == "win32":
    if not os.environ.get("REFLEX_WEB_WINDOWS_OVERRIDE"):
        raise RuntimeError(
            "reflex-web cannot be built on Windows due to EMFILE error. To build a "
            "subset of pages for testing, set environment variable REFLEX_WEB_WINDOWS_OVERRIDE."
        )
    routes = routes[:WINDOWS_MAX_ROUTES]

# Add the pages to the app.
for route in routes:
    # print(f"Adding route: {route}")
    if _check_whitelisted_path(route.path):
        page_args = {
            "component": route.component,
            "route": route.path,
            "title": route.title,
            "image": (
                "/previews/index_preview.png" if route.image is None else route.image
            ),
            "meta": [
                {"name": "theme-color", "content": route.background_color},
            ],
        }

        # Add the description only if it is not None
        if route.description is not None:
            page_args["description"] = route.description
        # Add the extra meta data only if it is not None
        if route.meta is not None:
            page_args["meta"].extend(route.meta)

        # Call add_page with the dynamically constructed arguments
        app.add_page(**page_args)

# Add redirects
redirects = [
    ("/framework", "/open-source"),
    ("/docs", "/docs/getting-started/introduction"),
    ("/docs/getting-started", "/docs/getting-started/introduction"),
    ("/docs/state", "/docs/state/overview"),
    ("/docs/styling", "/docs/styling/overview"),
    ("/docs/database", "/docs/database/overview"),
    ("/docs/hosting", "/docs/hosting/self-hosting"),
    ("/docs/advanced-guide", "/docs/advanced-guide/custom-vars"),
    ("/docs/library/theming/theme", "/docs/library/other/theme"),
    ("/docs/library/theming/theme-panel", "/docs/library/other/theme"),
    ("/docs/library/layout/foreach", "/docs/library/dynamic-rendering/foreach"),
    ("/docs/library/layout/match", "/docs/library/dynamic-rendering/match"),
    ("/docs/library/layout/cond", "/docs/library/dynamic-rendering/cond"),
    ("/docs/components", "/docs/components/props"),
    ("/docs/pages", "/docs/pages/routes"),
    ("/docs/assets", "/docs/assets/referencing-assets"),
    ("/docs/api-reference", "/docs/api-reference/app"),
    ("/docs/wrapping-react", "/docs/wrapping-react/overview"),
    ("/docs/vars", "/docs/vars/base-vars"),
    ("/docs/events", "/docs/events/events-overview"),
    ("/docs/state-structure", "/docs/state-structure/overview"),
    ("/docs/api-routes", "/docs/api-routes/overview"),
    ("/docs/client-storage", "/docs/client-storage/overview"),
    ("/docs/authentication", "/docs/authentication/authentication-overview"),
    ("/docs/utility-methods", "/docs/utility-methods/router-attributes"),
    ("/docs/datatable-tutorial", "/docs/datatable-tutorial/simple-table"),
    ("/docs/library/graphing", "/docs/library/graphing/charts"),
    ("/docs/tutorial", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/tutorial/intro", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/tutorial/setup", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/tutorial/frontend", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/tutorial/adding-state", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/tutorial/final-app", "/docs/getting-started/chatapp-tutorial"),
    ("/docs/getting-started/configuration", "/docs/advanced-onboarding/configuration"),
    (
        "/docs/getting-started/how-reflex-works",
        "/docs/advanced-onboarding/how-reflex-works",
    ),
    # Recipes
    ("/docs/recipes/auth", "/docs/recipes"),
    ("/docs/recipes/layout", "/docs/recipes"),
    ("/docs/recipes/others", "/docs/recipes"),
    ("/docs/recipes/content", "/docs/recipes"),
    # redirect previous chakra links to the new chakra docs
    ("/docs/library/chakra/[[...splat]]", "https://chakra.reflex.run/introduction/"),
    ("/gallery", "/templates"),
    # Redirect any removed pages to their new home.
    ("/docs/components/style-props", "/docs/components/props"),
    ("/docs/components/conditional-props", "/docs/components/conditional-rendering"),
    ("/docs/pages/routes", "/docs/pages/overview"),
    ("/docs/assets/referencing_assets", "/docs/assets/overview"),
    ("/changelog", "https://github.com/reflex-dev/reflex/releases"),
    (
        "/blog/2025-10-27-top-10-data-visualization-libraries",
        "/blog/2025-01-27-top-10-data-visualization-libraries",
    ),
]

for source, target in redirects:
    if _check_whitelisted_path(target):
        app.add_page(lambda: rx.fragment(), route=source, on_load=rx.redirect(target))

app.add_page(page404.component, route=page404.path)
