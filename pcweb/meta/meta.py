import reflex as rx


meta_tags = [
    # HTML Meta Tags
    {"name": "application-name", "content": "Reflex"},
    {
        "name": "keywords",
        "content": "reflex, python, web apps, framework, open source, frontend, backend, full stack",
    },
    {
        "name": "description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    # Facebook Meta Tags
    {"property": "og:url", "content": "https://reflex.dev/"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "property": "og:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"property": "og:image", "content": "/previews/index_preview.png"},
    # Twitter Meta Tags
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": "reflex.dev"},
    {"property": "twitter:url", "content": "https://reflex.dev/"},
    {"name": "twitter:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "name": "twitter:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"name": "twitter:image", "content": "/previews/index_preview.png"},
    {"name": "twitter:creator", "content": "@getreflex"},
]

hosting_meta_tags = [
    # HTML Meta Tags
    {"name": "application-name", "content": "Reflex"},
    {
        "name": "keywords",
        "content": "reflex, python, web apps, framework, open source, frontend, backend, full stack",
    },
    {
        "name": "description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    # Facebook Meta Tags
    {"property": "og:url", "content": "https://reflex.dev/"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "property": "og:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"property": "og:image", "content": "/previews/hosting_preview.png"},
    # Twitter Meta Tags
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": "reflex.dev"},
    {"property": "twitter:url", "content": "https://reflex.dev/"},
    {"name": "twitter:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "name": "twitter:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"name": "twitter:image", "content": "/previews/hosting_preview.png"},
    {"name": "twitter:creator", "content": "@getreflex"},
]


def favicons_links() -> list[rx.Component]:
    return [
        rx.el.link(rel="apple-touch-icon", sizes="180x180", href="/meta/apple-touch-icon.png"),
        rx.el.link(rel="icon", type="image/png", sizes="32x32", href="/meta/favicon-32x32.png"),
        rx.el.link(rel="icon", type="image/png", sizes="16x16", href="/meta/favicon-16x16.png"),
        rx.el.link(rel="manifest", href="/meta/site.webmanifest"),
        rx.el.link(rel="shortcut icon", href="/favicon.ico"),
    ]
