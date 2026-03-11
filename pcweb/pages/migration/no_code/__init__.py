import reflex as rx

from pcweb.meta.meta import create_meta_tags, faq_jsonld
from pcweb.pages.about.views.divider import divider
from pcweb.pages.migration.no_code.views import compare, explore, hero, quotes
from pcweb.templates.marketing_page import marketing_page

NO_CODE_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Why should I switch from no-code tools like Power BI or Retool to Reflex?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No-code tools get you to a first version fast, but they hit walls on custom logic, complex data flows, and performance. Reflex is built in pure Python, so there's no ceiling — if Python can do it, Reflex can do it. You own your code, deploy anywhere, and never get held hostage by a platform's pricing changes or shutdown.",
            },
        },
        {
            "@type": "Question",
            "name": "Does Reflex support vendor lock-in like Power BI and Tableau?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No. With no-code tools, your app lives on their infrastructure in a proprietary format with no way to export or migrate your work. With Reflex, it's your Python code — deploy it on any infrastructure, use full version control, and maintain complete portability.",
            },
        },
        {
            "@type": "Question",
            "name": "Can data scientists and ML engineers use Reflex directly?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Reflex gives you full access to the Python ecosystem — pandas, scikit-learn, or any pip package. Data scientists and ML engineers can build internal tools or customer-facing apps directly without learning JavaScript or being constrained by a drag-and-drop builder's integrations.",
            },
        },
        {
            "@type": "Question",
            "name": "How does Reflex handle real-time data compared to Tableau and Power BI?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Reflex is real-time by default. Unlike Tableau and Power BI, which rely on scheduled refreshes and have dataset size limits, Reflex handles CRUD operations, real-time data feeds, and complex state management natively — because it's just code.",
            },
        },
        {
            "@type": "Question",
            "name": "Can I take a Reflex app to production without rebuilding it?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Reflex fits into Git, pull requests, automated testing, and staging environments from day one. What you demo is what you ship — there's no prototype-to-production rewrite phase, which is a common failure point with no-code tools.",
            },
        },
    ],
}


@marketing_page(
    path="/migration/no-code",
    title="Switch from No-Code to Reflex | Power BI, Tableau & Retool Alternative",
    meta=create_meta_tags(
        title="Switch from No-Code to Reflex | Power BI, Tableau & Retool Alternative",
        description="Hit the ceiling with Power BI, Tableau, or Retool? Reflex gives you full Python control, no vendor lock-in, and production-ready apps from day one. No ceiling, no workarounds.",
        image="/previews/index_preview.webp",
    ),
)
def no_code_migration_page() -> rx.Component:
    return rx.el.div(
        faq_jsonld(NO_CODE_FAQ_SCHEMA),
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
