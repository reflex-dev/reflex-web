"""The main Reflex website."""

import os
import sys

import reflex as rx
import reflex_enterprise as rxe

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
app = rxe.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    app_wraps={},
    theme=rx.theme(
        has_background=True,
        radius="large",
        accent_color="violet",
    ),
    head_components=get_pixel_website_trackers()
    + favicons_links()
    + [
        rx.el.link(
            rel="preload",
            href="/fonts/instrument-sans.woff2",
            custom_attrs={"as": "font"},
            type="font/woff2",
            cross_origin="anonymous",
        ),
        rx.el.link(
            rel="preload",
            href="/fonts/jetbrains-mono.woff2",
            custom_attrs={"as": "font"},
            type="font/woff2",
            cross_origin="anonymous",
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
                "/previews/index_preview.webp" if route.image is None else route.image
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
    ("/docs/ui", "/docs/ui/overview"),
    ("/docs/enterprise/react-flow", "/docs/enterprise/react-flow/overview"),
    ("/docs/advanced-onboarding", "/docs/advanced-onboarding/code-structure"),
    ("/docs/hosting/cli", "/docs/hosting"),
    ("/docs/enterprise/ag-grid/index", "/docs/enterprise/ag-grid"),
    ("/docs/ai-builder/integrations", "/docs/ai-builder/integrations/overview"),
    ("/docs/ai-builder/app-lifecycle", "/docs/ai-builder/app-lifecycle/general"),
    ("/docs/ai-builder/features", "/docs/ai-builder/features/ide"),
    ("/docs/ai-builder", "/docs/ai-builder/overview/best-practices"),
    ("/docs/ai-builder/overview", "/docs/ai-builder/overview/best-practices"),
    ("/framework", "/open-source"),
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
    ("/docs/enterprise", "/docs/enterprise/overview"),
    ("/docs/pages/routes", "/docs/pages/overview"),
    ("/docs/overview", "/docs/getting-started/introduction"),
    ("/docs/assets/referencing_assets", "/docs/assets/overview"),
    ("/changelog", "https://github.com/reflex-dev/reflex/releases"),
    # Blog: redirect old date-prefixed URLs to new slug-only URLs
    ("/blog/2023-06-28-rebrand-to-reflex", "/blog/rebrand-to-reflex"),
    ("/blog/2023-08-02-seed-annoucement", "/blog/seed-annoucement"),
    (
        "/blog/2023-09-28-unlocking-new-workflows-with-background-tasks",
        "/blog/unlocking-new-workflows-with-background-tasks",
    ),
    ("/blog/2023-10-11-graphing-update", "/blog/graphing-update"),
    (
        "/blog/2023-10-25-implementing-sign-in-with-google",
        "/blog/implementing-sign-in-with-google",
    ),
    ("/blog/2024-02-16-reflex-v0-4-0", "/blog/reflex-v0-4-0"),
    ("/blog/2024-03-21-reflex-architecture", "/blog/reflex-architecture"),
    ("/blog/2024-03-27-structuring-a-large-app", "/blog/structuring-a-large-app"),
    ("/blog/2024-04-16-custom-components", "/blog/custom-components"),
    ("/blog/2024-06-28-using-table-component", "/blog/using-table-component"),
    ("/blog/2024-09-21-reflex-v060", "/blog/reflex-v060"),
    ("/blog/2024-09-25-using-ag-grid-in-reflex", "/blog/using-ag-grid-in-reflex"),
    (
        "/blog/2024-10-8-self-hosting-reflex-with-docker",
        "/blog/self-hosting-reflex-with-docker",
    ),
    (
        "/blog/2024-11-19-microsoft-azure-authentication",
        "/blog/microsoft-azure-authentication",
    ),
    ("/blog/2024-12-05-reflex-cloud", "/blog/reflex-cloud"),
    ("/blog/2024-12-20-python-comparison", "/blog/python-comparison"),
    (
        "/blog/2025-01-27-top-10-data-visualization-libraries",
        "/blog/top-10-data-visualization-libraries",
    ),
    ("/blog/2025-05-16-top-5-ai-app-builders", "/blog/top-5-ai-app-builders"),
    (
        "/blog/2025-06-03-internal-tool-builders-2025",
        "/blog/internal-tool-builders",
    ),
    (
        "/blog/internal-tool-builders-2025",
        "/blog/internal-tool-builders",
    ),
    ("/blog/2025-06-20-reflex-dash", "/blog/reflex-dash"),
    (
        "/blog/2025-06-30-reflex-databricks-partnership",
        "/blog/reflex-databricks-partnership",
    ),
    ("/blog/2025-07-01-reflex-080", "/blog/reflex-080"),
    ("/blog/2025-08-20-reflex-streamlit", "/blog/reflex-streamlit"),
    ("/blog/2025-09-03-reflex-jupyter", "/blog/reflex-jupyter"),
    ("/blog/2025-12-05-on-premises-deployment", "/blog/on-premises-deployment"),
    (
        "/blog/2025-12-17-top-7-enterprise-ai-app-builders-2026",
        "/blog/top-7-enterprise-ai-app-builders",
    ),
    (
        "/blog/top-7-enterprise-ai-app-builders-2026",
        "/blog/top-7-enterprise-ai-app-builders",
    ),
    (
        "/blog/2025-10-27-top-10-data-visualization-libraries",
        "/blog/top-10-data-visualization-libraries",
    ),
    (
        "/blog/2026-01-09-top-python-web-frameworks-2026",
        "/blog/top-python-web-frameworks",
    ),
    (
        "/blog/top-python-web-frameworks-2026",
        "/blog/top-python-web-frameworks",
    ),
]


def _redirect_page():
    return rx.fragment(
        rx.el.h1("Redirecting", class_name="sr-only"),
    )


for source, target in redirects:
    if _check_whitelisted_path(target):
        app.add_page(
            _redirect_page,
            route=source,
            title="Redirecting - Reflex Web Framework",
            description="You are being redirected to the requested page.",
            on_load=rx.redirect(target),
            context={"sitemap": None},
        )

app.add_page(page404.component, route=page404.path)
