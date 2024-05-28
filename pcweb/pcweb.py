"""The main Reflex website."""

import os
import sys 
  
import reflex as rx
from pcweb import styles
from pcweb.pages import page404, routes
from pcweb.pages.docs import outblocks, exec_blocks
from pcweb.whitelist import _check_whitelisted_path

# This number discovered by trial and error on Windows 11 w/ Node 18, any
# higher and the prod build fails with EMFILE error.
WINDOWS_MAX_ROUTES = 125
 
  
# Execute all the exec blocks in the documents.
for doc, href in outblocks:
    exec_blocks(doc, href)

# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    theme=rx.theme(
        has_background=True, radius="large", accent_color="violet"
    ),
    head_components=[
        rx.el.script(
            src="https://tag.clearbitscripts.com/v1/pk_3d711a6e26de5ddb47443d8db170d506/tags.js",
            referrer_policy="strict-origin-when-cross-origin",
        ),
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-4T7C8ZD9TR"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){window.dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-4T7C8ZD9TR');
"""
        ),
        rx.script(
            """!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('phc_JoMo0fOyi0GQAooY3UyO9k0hebGkMyFJrrCw1Gt5SGb',{api_host:'https://app.posthog.com'})"""
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
    if _check_whitelisted_path(route.path):
        app.add_page(
            route.component,
            route.path,
            route.title,
            image="/previews/index_preview.png",
            meta= [
                {"name": "theme-color", "content": route.background_color},
            ]
        )

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

app.add_custom_404_page(page404.component)
