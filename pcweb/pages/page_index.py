import reflex as rx

from pcweb.templates.webpage import webpage

BLOG_POSTS = [
    # reflex.dev blogs
    (
        "How to Build a Python Web App With HubSpot in 2026",
        "/blog/build-python-web-app-hubspot",
    ),
    ("How to Build a Dashboard With Groq in 2026", "/blog/build-dashboard-with-groq"),
    (
        "How to Build a Dashboard With Twilio in 2026",
        "/blog/build-dashboard-twilio-python",
    ),
    (
        "How to Build a Dashboard With GitHub in 2026",
        "/blog/how-to-build-dashboard-with-github",
    ),
    (
        "How to Build a Python Web App With Supabase in 2026",
        "/blog/how-to-build-python-web-app-with-supabase",
    ),
    ("How to Build a Dashboard With OpenAI in 2026", "/blog/build-dashboard-openai"),
    (
        "How to Build a Dashboard With Salesforce in 2026",
        "/blog/build-dashboard-salesforce",
    ),
    (
        "How to Build a Dashboard With Intercom in 2026",
        "/blog/build-dashboard-intercom",
    ),
    (
        "How to Build a Dashboard With ServiceNow in 2026",
        "/blog/build-dashboard-servicenow",
    ),
    (
        "How to Build a Dashboard With Resend in 2026",
        "/blog/build-dashboard-resend-python",
    ),
    ("How to Build a Dashboard With MongoDB in 2026", "/blog/build-dashboard-mongodb"),
    (
        "How to Build a Python Web App With Epic EHR in 2026",
        "/blog/python-web-app-epic-ehr",
    ),
    (
        "How to Build a Python Web App With DynamoDB in 2026",
        "/blog/how-to-build-python-web-app-with-dynamodb",
    ),
    (
        "How to Build a Python Web App With Linear in 2026",
        "/blog/how-to-build-python-web-app-with-linear",
    ),
    (
        "How to Build a Python Web App With Stripe in 2026",
        "/blog/build-python-web-app-with-stripe",
    ),
    (
        "How to Build a Python Web App With Azure Auth / Microsoft Entra ID in 2026",
        "/blog/python-web-app-azure-auth-microsoft-entra-id",
    ),
    (
        "How to Build a Python Web App With Okta Auth in 2026",
        "/blog/build-python-web-app-okta-auth",
    ),
    (
        "How to Build a Python Web App With BigQuery in 2026",
        "/blog/how-to-build-python-web-app-with-bigquery",
    ),
    (
        "How to Build a Python Web App With Databricks in 2026",
        "/blog/python-web-app-databricks",
    ),
    (
        "How to Build a Python Web App With AWS (S3) in 2026",
        "/blog/build-python-web-app-aws-s3",
    ),
    (
        "How to Build a Python Web App With Hugging Face in 2026",
        "/blog/build-python-web-app-hugging-face",
    ),
    (
        "How to Build a Python Web App With Jira in 2026",
        "/blog/how-to-build-python-web-app-with-jira",
    ),
    (
        "How to Build a Python Web App With LangChain in 2026",
        "/blog/how-to-build-python-web-app-with-langchain",
    ),
    (
        "How to Build a Python Web App With Zendesk in 2026",
        "/blog/build-python-web-app-with-zendesk",
    ),
    (
        "How to Build a Python Web App With GCP in 2026",
        "/blog/how-to-build-python-web-app-with-gcp",
    ),
    (
        "How to Build a Dashboard With PostgreSQL in 2026",
        "/blog/build-dashboard-with-postgresql",
    ),
    ("How to Build a Dashboard With Slack in 2026", "/blog/build-dashboard-with-slack"),
    (
        "How to Build a Python Web App With Perplexity in 2026",
        "/blog/python-web-app-with-perplexity",
    ),
    (
        "How to Build a Dashboard With Snowflake in 2026",
        "/blog/how-to-build-dashboard-with-snowflake",
    ),
    (
        "How to Build a Dashboard With Google Auth in 2026",
        "/blog/build-dashboard-google-auth",
    ),
    ("How to Build a Dashboard With Auth0 in 2026", "/blog/build-dashboard-with-auth0"),
    (
        "How to Build a Dashboard With Plaid in 2026",
        "/blog/how-to-build-dashboard-with-plaid",
    ),
    (
        "How to Build a Dashboard With Anthropic in 2026",
        "/blog/build-dashboard-with-anthropic",
    ),
    (
        "How to Build a Dashboard With Gemini in 2026",
        "/blog/build-dashboard-with-gemini",
    ),
    (
        "How to Build a Dashboard With FHIR API in 2026",
        "/blog/build-fhir-api-dashboard-python",
    ),
    (
        "How to Build a Dashboard With a Database in 2026",
        "/blog/build-dashboard-with-database",
    ),
    (
        "How to Build a Python Web App With Ollama in 2026",
        "/blog/build-python-web-app-ollama",
    ),
    (
        "How to Build a Python Web App With Notion in 2026",
        "/blog/build-python-web-app-with-notion",
    ),
    (
        "How to Build a Python Web App With MSSQL in 2026",
        "/blog/build-python-web-app-mssql",
    ),
    (
        "How to Build a Dashboard With MySQL in 2026",
        "/blog/how-to-build-dashboard-with-mysql",
    ),
    # learn.reflex.dev blogs
    (
        "How to Build a Dashboard With GCP in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-gcp",
    ),
    (
        "How to Build a Python Web App With OpenAI in 2026",
        "https://learn.reflex.dev/blog/python-web-app-openai",
    ),
    (
        "How to Build a Python Web App With a Database in 2026",
        "https://learn.reflex.dev/blog/how-to-build-python-web-app-with-database",
    ),
    (
        "How to Build a Dashboard With Azure Auth / Microsoft Entra ID in 2026",
        "https://learn.reflex.dev/blog/azure-auth-microsoft-entra-id-dashboard",
    ),
    (
        "How to Build a Dashboard With Databricks in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-databricks",
    ),
    (
        "How to Build a Python Web App With Resend in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-with-resend",
    ),
    (
        "How to Build a Dashboard With BigQuery in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-bigquery",
    ),
    (
        "How to Build a Dashboard With Notion in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-with-notion",
    ),
    (
        "How to Build a Python Web App With Auth0 in 2026",
        "https://learn.reflex.dev/blog/python-web-app-auth0",
    ),
    (
        "How to Build a Dashboard With Zendesk in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-zendesk",
    ),
    (
        "How to Build a Python Web App With FHIR API in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-fhir-api",
    ),
    (
        "How to Build a Python Web App With Gemini in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-gemini",
    ),
    (
        "How to Build a Python Web App With Twilio in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-twilio",
    ),
    (
        "How to Build a Dashboard With Linear in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-linear",
    ),
    (
        "How to Build a Dashboard With Supabase in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-with-supabase",
    ),
    (
        "How to Build a Dashboard With LangChain in 2026",
        "https://learn.reflex.dev/blog/build-langchain-dashboard",
    ),
    (
        "How to Build a Dashboard With Okta Auth in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-okta-auth",
    ),
    (
        "How to Build a Dashboard With AWS (S3) in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-aws-s3",
    ),
    (
        "How to Build a Dashboard With Hugging Face in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-hugging-face",
    ),
    (
        "How to Build a Dashboard With Jira in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-jira",
    ),
    (
        "How to Build a Dashboard With HubSpot in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-hubspot",
    ),
    (
        "How to Build a Dashboard With DynamoDB in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-dynamodb",
    ),
    (
        "How to Build a Dashboard With Perplexity in 2026",
        "https://learn.reflex.dev/blog/how-to-build-dashboard-with-perplexity",
    ),
    (
        "How to Build a Dashboard With Ollama in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-ollama",
    ),
    (
        "How to Build a Dashboard With Epic EHR in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-epic-ehr",
    ),
    (
        "How to Build a Python Web App With Google Auth in 2026",
        "https://learn.reflex.dev/blog/python-web-app-google-auth",
    ),
    (
        "How to Build a Python Web App With PostgreSQL in 2026",
        "https://learn.reflex.dev/blog/python-web-app-with-postgresql",
    ),
    (
        "How to Build a Python Web App With Snowflake in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-snowflake",
    ),
    (
        "How to Build a Python Web App With Slack in 2026",
        "https://learn.reflex.dev/blog/python-web-app-with-slack",
    ),
    (
        "How to Build a Python Web App With Anthropic in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-anthropic",
    ),
    (
        "How to Build a Python Web App With MySQL in 2026",
        "https://learn.reflex.dev/blog/how-to-build-python-web-app-with-mysql",
    ),
    (
        "How to Build a Python Web App With MongoDB in 2026",
        "https://learn.reflex.dev/blog/python-web-app-mongodb",
    ),
    (
        "How to Build a Python Web App With Salesforce in 2026",
        "https://learn.reflex.dev/blog/python-salesforce-web-app",
    ),
    (
        "How to Build a Python Web App With ServiceNow in 2026",
        "https://learn.reflex.dev/blog/python-web-app-servicenow",
    ),
    (
        "How to Build a Python Web App With GitHub in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-github",
    ),
    (
        "How to Build a Python Web App With Plaid in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-with-plaid",
    ),
    (
        "How to Build a Python Web App With Groq in 2026",
        "https://learn.reflex.dev/blog/build-python-web-app-groq",
    ),
    (
        "How to Build a Dashboard With MSSQL in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-with-mssql",
    ),
    (
        "How to Build a Python Web App With Intercom in 2026",
        "https://learn.reflex.dev/blog/how-to-build-python-web-app-with-intercom",
    ),
    (
        "How to Build a Dashboard With Stripe in 2026",
        "https://learn.reflex.dev/blog/build-dashboard-with-stripe",
    ),
]


def link_item(title: str, path: str) -> rx.Component:
    return rx.el.li(
        rx.el.a(
            title,
            href=path,
            class_name="text-slate-11 hover:text-slate-12 underline",
        ),
        class_name="py-1",
    )


@webpage(path="/page-index", title="Page Index")
def page_index() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Page Index",
            class_name="text-3xl font-bold text-slate-12 mb-6",
        ),
        rx.el.ul(
            *[link_item(title, path) for title, path in BLOG_POSTS],
            class_name="list-disc pl-6 flex flex-col gap-1",
        ),
        class_name="max-w-2xl mx-auto px-6 py-12",
    )
