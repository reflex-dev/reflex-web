import reflex as rx

from pcweb.meta.meta import create_meta_tags, faq_jsonld
from pcweb.pages.about.views.divider import divider
from pcweb.pages.migration.low_code.views import compare, explore, hero, quotes
from pcweb.templates.marketing_page import marketing_page

LOW_CODE_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What are the main limitations of Streamlit that Reflex solves?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Streamlit reruns your entire script every time a user interacts with the app, which leads to memory leaks and slowdowns that make it unreliable for long-term use. It also can't push updates to the user — nothing happens in the browser until the user clicks something. Reflex uses an event-driven model with WebSocket sync, so only affected components update and server changes appear instantly in the browser.",
            },
        },
        {
            "@type": "Question",
            "name": "How does Reflex compare to Dash for building Python web apps?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Dash scatters logic across many separate callback functions that become harder to trace as your app grows. It also has no built-in auth, background tasks, or database layer. Reflex uses a Python class-based state model that keeps code organized, and real projects typically use roughly half the code compared to an equivalent Dash app.",
            },
        },
        {
            "@type": "Question",
            "name": "Is Gradio a good alternative to Reflex for building apps?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Gradio is purpose-built for ML model demos — it's not a general-purpose app framework. It only handles simple input-in, output-out interactions and can't support complex multi-page app structures, real-time features, or production deployment requirements.",
            },
        },
        {
            "@type": "Question",
            "name": "Does Reflex support real-time features without extra setup?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Reflex uses WebSocket sync, so server changes show up instantly in the browser with no refresh and no extra infrastructure. Live dashboards, real-time data feeds, and collaborative features work out of the box — something Streamlit and Dash can't do natively.",
            },
        },
        {
            "@type": "Question",
            "name": "Can I deploy a Reflex app to production without rewriting it?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Reflex compiles to a FastAPI backend with a React frontend on an async web server — production-ready and container-friendly from day one. It fits into Git, pull requests, automated testing, and CI/CD from the start. Low-code tools like Streamlit and Dash are widely seen as prototyping tools that require a separate production rewrite.",
            },
        },
    ],
}


@marketing_page(
    path="/migration/low-code",
    title="Switch from Streamlit, Dash & Gradio to Reflex | Python App Framework",
    meta=create_meta_tags(
        title="Switch from Streamlit, Dash & Gradio to Reflex | Python App Framework",
        description="Outgrown Streamlit's rerun model or Dash's callback spaghetti? Reflex gives you declarative state, real-time updates, and production-ready output — in pure Python, from day one.",
        image="/previews/index_preview.webp",
    ),
)
def low_code_migration_page() -> rx.Component:
    return rx.el.div(
        faq_jsonld(LOW_CODE_FAQ_SCHEMA),
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
