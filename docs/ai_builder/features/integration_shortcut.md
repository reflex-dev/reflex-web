# Integrations Shortcut

Reflex Build supports powerful integrations like databases, OpenAI, and Databricks, allowing you to connect external services to your app without complex setup. These integrations help you add advanced functionality—like AI-powered features, data analytics, or persistent storage—while speeding up development.

The **@** feature makes it easy to reference integrations directly while chatting with the AI Builder. By typing **@**, you can quickly insert integrations into your prompts without needing to configure them manually first.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/features/shortcut_light.webp",
                "/ai_builder/features/shortcut_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## How to Use

1. In the AI Builder chat, type **@**.
2. A **popover list** of available integrations will appear (e.g. Database, Databricks, OpenAI).
3. Select an integration from the list.
4. The integration will be inserted into your message as **@IntegrationName**.
5. Continue typing your request, and the AI Builder will use that integration context when generating.

## What It Does

- **Quick Access** – No need to remember integration names.
- **Context-Aware** – The AI Builder understands that `@Database` or `@OpenAI` refers to the actual integration.
- **Faster Building** – Jump directly into using integrations in your prompts.

## Common Use Cases

- **Query Data**
  "Show me the top 10 users from **@Database** ordered by signup date."

- **Generate with AI**
  "Use **@OpenAI** to summarize the user feedback table."
