import reflex as rx
from pcweb.constants import REFLEX_DOMAIN_URL, REFLEX_DOMAIN, TWITTER_CREATOR


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
    {"property": "og:url", "content": REFLEX_DOMAIN_URL},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "property": "og:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"property": "og:image", "content": "/previews/index_preview.png"},
    # Twitter Meta Tags
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": REFLEX_DOMAIN},
    {"property": "twitter:url", "content": REFLEX_DOMAIN_URL},
    {"name": "twitter:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "name": "twitter:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"name": "twitter:image", "content": "/previews/index_preview.png"},
    {"name": "twitter:creator", "content": TWITTER_CREATOR},
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
    {"property": "og:url", "content": REFLEX_DOMAIN_URL},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "property": "og:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"property": "og:image", "content": "/previews/hosting_preview.png"},
    # Twitter Meta Tags
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": REFLEX_DOMAIN},
    {"property": "twitter:url", "content": REFLEX_DOMAIN_URL},
    {"name": "twitter:title", "content": "Reflex · Web apps in Pure Python"},
    {
        "name": "twitter:description",
        "content": "The open-source framework to build and deploy web apps using Python.",
    },
    {"name": "twitter:image", "content": "/previews/hosting_preview.png"},
    {"name": "twitter:creator", "content": TWITTER_CREATOR},
]


def favicons_links() -> list[rx.Component]:
    return [
        rx.el.link(
            rel="apple-touch-icon", sizes="180x180", href="/meta/apple-touch-icon.png"
        ),
        rx.el.link(
            rel="icon", type="image/png", sizes="32x32", href="/meta/favicon-32x32.png"
        ),
        rx.el.link(
            rel="icon", type="image/png", sizes="16x16", href="/meta/favicon-16x16.png"
        ),
        rx.el.link(rel="manifest", href="/meta/site.webmanifest"),
        rx.el.link(rel="shortcut icon", href="/favicon.ico"),
    ]


def create_meta_tags(title: str, description: str, image: str, url: str = None) -> list[rx.Component]:
    page_url = url if url else REFLEX_DOMAIN_URL
    
    if image and not image.startswith(('http://', 'https://')):
        image_url = f"https://reflex.dev{'' if image.startswith('/') else '/'}{image}"
    else:
        image_url = image
    
    return [
        # HTML Meta Tags
        {"name": "application-name", "content": "Reflex"},
        {
            "name": "keywords",
            "content": "reflex, python, web apps, framework, open source, frontend, backend, full stack",
        },
        {
            "name": "description",
            "content": description,
        },
        # Facebook Meta Tags
        {"property": "og:url", "content": page_url},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": title},
        {
            "property": "og:description",
            "content": description,
        },
        {"property": "og:image", "content": image_url},
        # Twitter Meta Tags
        {"name": "twitter:card", "content": "summary_large_image"},
        {"property": "twitter:domain", "content": REFLEX_DOMAIN},
        {"property": "twitter:url", "content": page_url},
        {"name": "twitter:title", "content": title},
        {
            "name": "twitter:description",
            "content": description,
        },
        {"name": "twitter:image", "content": image_url},
        {"name": "twitter:creator", "content": TWITTER_CREATOR},
    ]
