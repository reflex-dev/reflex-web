import reflex as rx

from pcweb.constants import REFLEX_DOMAIN, REFLEX_DOMAIN_URL, TWITTER_CREATOR

TITLE = "The unified platform to build and scale enterprise apps."
ONE_LINE_DESCRIPTION = "Build with AI, iterate in Python, deploy to any cloud. The unified platform to build and scale enterprise apps."

# Common constants
APPLICATION_NAME = "Reflex"
KEYWORDS = (
    "reflex, python, web apps, framework, open source, frontend, backend, full stack"
)
TWITTER_CARD_TYPE = "summary_large_image"
OG_TYPE = "website"


def _build_meta_tags(
    title: str,
    description: str,
    image: str,
    url: str = REFLEX_DOMAIN_URL,
) -> list[dict[str, str]]:
    """Build a list of meta tags with the given parameters.

    Args:
        title: The page title.
        description: The page description.
        image: The image path for social media previews.
        url: The page URL (defaults to REFLEX_DOMAIN_URL).

    Returns:
        A list of meta tag dictionaries.
    """
    return [
        # HTML Meta Tags
        {"name": "application-name", "content": APPLICATION_NAME},
        {"name": "keywords", "content": KEYWORDS},
        {"name": "description", "content": description},
        # Facebook Meta Tags
        {"property": "og:url", "content": url},
        {"property": "og:type", "content": OG_TYPE},
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:image", "content": image},
        # Twitter Meta Tags
        {"name": "twitter:card", "content": TWITTER_CARD_TYPE},
        {"property": "twitter:domain", "content": REFLEX_DOMAIN},
        {"property": "twitter:url", "content": url},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": image},
        {"name": "twitter:creator", "content": TWITTER_CREATOR},
    ]


meta_tags = _build_meta_tags(
    title=TITLE,
    description=ONE_LINE_DESCRIPTION,
    image="/previews/index_preview.webp",
)

hosting_meta_tags = _build_meta_tags(
    title=TITLE,
    description=ONE_LINE_DESCRIPTION,
    image="/previews/hosting_preview.webp",
)


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


def create_meta_tags(
    title: str, description: str, image: str, url: str | None = None
) -> list[rx.Component]:
    """Create meta tags for a page.

    Args:
        title: The page title.
        description: The page description.
        image: The image path for social media previews.
        url: The page URL (optional, defaults to REFLEX_DOMAIN_URL).

    Returns:
        A list of meta tag dictionaries.
    """
    page_url = url if url else REFLEX_DOMAIN_URL

    if image and not image.startswith(("http://", "https://")):
        image_url = f"https://reflex.dev{'' if image.startswith('/') else '/'}{image}"
    else:
        image_url = image

    return _build_meta_tags(
        title=title,
        description=description,
        image=image_url,
        url=page_url,
    )
