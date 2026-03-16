import reflex as rx

from pcweb.meta.meta import create_meta_tags, faq_jsonld
from pcweb.pages.about.views.divider import divider
from pcweb.pages.migration.other_frameworks.views import compare, explore, hero, quotes
from pcweb.templates.marketing_page import marketing_page

OTHER_FRAMEWORKS_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "How does Reflex compare to using React with a Python backend like FastAPI or Django?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Traditional stacks require maintaining two codebases in two languages — Python for the backend and JavaScript or TypeScript for the frontend. Every new feature touches both. Reflex lets you build your entire app in pure Python with one codebase to maintain, version control, test, and deploy — no REST glue code, no CORS configuration, no context switching.",
            },
        },
        {
            "@type": "Question",
            "name": "Do I need to know JavaScript to build a modern frontend with Reflex?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No. Reflex compiles your Python code into a React frontend automatically. You get a modern, interactive UI without writing any JavaScript. When you need something custom, you can wrap any existing React component directly from Python.",
            },
        },
        {
            "@type": "Question",
            "name": "How much faster is building with Reflex compared to a traditional Python and React stack?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Building with Reflex is roughly 5x faster than assembling the same app from a traditional Python and React stack. There's no time spent wiring API endpoints, configuring CORS, setting up build pipelines, or debugging mismatches between the frontend and backend.",
            },
        },
        {
            "@type": "Question",
            "name": "Does Reflex include auth, a database ORM, and other production essentials?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Authentication, ORM, database migrations, real-time sync, background jobs, and file uploads all come out of the box. FastAPI and Flask give you almost nothing built in, and Django's HTML templating isn't suited for modern interactive interfaces.",
            },
        },
        {
            "@type": "Question",
            "name": "How does Reflex handle real-time features compared to Django or Flask?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Reflex runs on an async web server with WebSocket sync, handling real-time updates, live data feeds, and high-concurrency traffic natively. Flask is synchronous by default and Django's monolithic architecture creates scaling challenges — neither framework includes built-in real-time capabilities.",
            },
        },
    ],
}


@marketing_page(
    path="/migration/other-frameworks",
    title="Switch from React, Django & FastAPI to Reflex | Full-Stack Python Framework",
    meta=create_meta_tags(
        title="Switch from React, Django & FastAPI to Reflex | Full-Stack Python Framework",
        description="Tired of maintaining two codebases in two languages? Reflex replaces React + Django/FastAPI with a single pure Python stack — full-stack, production-ready, ~5x faster to build.",
        image="/previews/index_preview.webp",
    ),
)
def other_frameworks_migration_page() -> rx.Component:
    return rx.el.div(
        faq_jsonld(OTHER_FRAMEWORKS_FAQ_SCHEMA),
        rx.el.div(
            hero(),
            quotes(),
            divider(),
            compare(),
            divider(),
            explore(),
            class_name="flex flex-col relative justify-center items-center w-full",
        ),
        class_name="flex flex-col w-full relative h-full justify-center items-center",
    )
