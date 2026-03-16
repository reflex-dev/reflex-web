import json

import reflex as rx

from pcweb.constants import (
    DISCORD_URL,
    FORUM_URL,
    GITHUB_URL,
    LINKEDIN_URL,
    REFLEX_DOMAIN,
    REFLEX_DOMAIN_URL,
    TWITTER_CREATOR,
    TWITTER_URL,
)

TITLE = "The unified platform to build and scale enterprise apps."
ONE_LINE_DESCRIPTION = "Build with AI, iterate in Python, deploy to any cloud. Reflex is the platform for full-stack web apps and internal tools."

# Common constants
APPLICATION_NAME = "Reflex"
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


def _normalize_image_url(image: str) -> str:
    """Ensure image path is a full URL."""
    if image and not image.startswith(("http://", "https://")):
        return f"https://reflex.dev{'' if image.startswith('/') else '/'}{image}"
    return image


def blog_jsonld(
    title: str,
    description: str,
    author: str,
    date: str,
    image: str,
    url: str,
    faq: list[dict[str, str]] | None = None,
    author_bio: str | None = None,
    updated_at: str | None = None,
) -> rx.Component:
    """Create a single JSON-LD script tag with @graph for a blog post.

    Always includes a BlogPosting entry. If faq items are provided,
    a FAQPage entry is also added to the graph.
    """
    author_node: dict = {"@type": "Person", "name": author}
    if author_bio:
        author_node["description"] = author_bio

    posting: dict = {
        "@type": "BlogPosting",
        "headline": title,
        "description": description,
        "image": _normalize_image_url(image),
        "datePublished": str(date),
        "author": author_node,
    }
    if updated_at:
        posting["dateModified"] = str(updated_at)

    graph: list[dict] = [
        {
            **posting,
            "publisher": {
                "@type": "Organization",
                "name": "Reflex",
                "url": REFLEX_DOMAIN_URL,
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": url,
            },
        },
    ]
    if faq:
        graph.append(
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["question"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item["answer"],
                        },
                    }
                    for item in faq
                ],
            }
        )
    data = {
        "@context": "https://schema.org",
        "@graph": graph,
    }
    return rx.el.script(json.dumps(data), type="application/ld+json")


def website_organization_jsonld(url: str = REFLEX_DOMAIN_URL) -> rx.Component:
    """Create Organization + WebSite JSON-LD for the homepage."""
    org_url = REFLEX_DOMAIN_URL.rstrip("/")
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{org_url}/#organization",
                "name": "Reflex",
                "url": REFLEX_DOMAIN_URL,
                "logo": f"{org_url}/meta/apple-touch-icon.png",
                "description": "Open-source Python framework for building full-stack web applications. Deploy to any cloud with AI-powered code generation.",
                "sameAs": [
                    GITHUB_URL,
                    TWITTER_URL,
                    DISCORD_URL,
                    LINKEDIN_URL,
                    FORUM_URL,
                ],
            },
            {
                "@type": "WebSite",
                "name": "Reflex",
                "url": url,
                "description": ONE_LINE_DESCRIPTION,
                "publisher": {"@id": f"{org_url}/#organization"},
            },
        ],
    }
    return rx.el.script(json.dumps(data), type="application/ld+json")


def blog_index_jsonld(posts: list[tuple[str, dict]], url: str) -> rx.Component:
    """Create Blog JSON-LD with ItemList of posts for the blog index page."""
    items = [
        {
            "@type": "ListItem",
            "position": i + 1,
            "url": f"{REFLEX_DOMAIN_URL.rstrip('/')}/blog/{path}",
            "name": meta.get("title_tag") or meta.get("title", ""),
            "datePublished": str(meta.get("date", "")),
        }
        for i, (path, meta) in enumerate(posts[:20])
    ]
    blog_posts = [
        {
            "@type": "BlogPosting",
            "headline": meta.get("title_tag") or meta.get("title", ""),
            "url": f"{REFLEX_DOMAIN_URL.rstrip('/')}/blog/{path}",
            "datePublished": str(meta.get("date", "")),
        }
        for path, meta in posts[:20]
    ]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Blog",
                "name": "Reflex Blog",
                "description": "Python web app tutorials, framework comparisons, and tips for building with Reflex.",
                "url": url,
                "publisher": {
                    "@type": "Organization",
                    "name": "Reflex",
                    "url": REFLEX_DOMAIN_URL,
                },
                "blogPost": blog_posts,
            },
            {
                "@type": "ItemList",
                "itemListElement": items,
                "numberOfItems": len(items),
            },
        ],
    }
    return rx.el.script(json.dumps(data), type="application/ld+json")


def faq_jsonld(faq_schema: dict) -> rx.Component:
    """Create a FAQPage JSON-LD script tag from a pre-built schema dict."""
    return rx.el.script(json.dumps(faq_schema), type="application/ld+json")


def pricing_jsonld(url: str) -> rx.Component:
    """Create SoftwareApplication + Product JSON-LD for the pricing page."""
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": "Reflex",
                "applicationCategory": "DeveloperApplication",
                "description": "The platform to build and scale enterprise apps. Python full-stack framework for web apps and internal tools.",
                "url": url,
            },
            {
                "@type": "Product",
                "name": "Reflex Enterprise Platform",
                "brand": {"@type": "Brand", "name": "Reflex"},
                "description": "Enterprise-grade fullstack app building platform with AI-powered code generation in pure Python. Includes dedicated support, SSO, on-prem deployment, and custom SLAs.",
                "offers": [
                    {
                        "@type": "Offer",
                        "price": "0",
                        "priceCurrency": "USD",
                        "name": "Free",
                        "availability": "https://schema.org/InStock",
                    },
                    {
                        "@type": "Offer",
                        "name": "Enterprise",
                        "description": "Custom enterprise pricing",
                        "availability": "https://schema.org/PreOrder",
                    },
                ],
            },
        ],
    }
    return rx.el.script(json.dumps(data), type="application/ld+json")
