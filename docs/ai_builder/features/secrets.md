# Secrets

The **Secrets** feature allows you to securely store environment-specific values that your app can use, such as API keys, tokens, or other sensitive information.


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom

def render_image():
    return rx.el.div(
        image_zoom(
            rx.image(
                src=rx.color_mode_cond(
                    "/ai_builder/features/secrets_light.png",
                    "/ai_builder/features/secrets_dark.png",
                ),
                class_name="p-2 rounded-md h-auto",
                border=f"0.81px solid {rx.color('slate', 5)}",
            ),
            class_name="rounded-md overflow-hidden",
        ),
        class_name="w-full flex flex-col rounded-md cursor-pointer",
    )
```

```python eval

rx.el.div(render_image())

```

## Adding Secrets

### 1. Add Individually
- **Description:** Set a single secret by providing a key and value.
- **Example:**
  - Key: `OPENAI_API_KEY`
  - Value: `sk-xxxxxx`
- **Behavior:** The secret is encrypted and accessible to your app at runtime.

### 2. Add in Bulk
- **Description:** Upload multiple secrets at once using a simple `VAR=VALUE` format.
- **Example:**

```text
DATABASE_URL=postgresql://user:pass@host:5432/db
STRIPE_SECRET_KEY=sk_test_xxxxx
OPENAI_API_KEY=sk-xxxxxx
```
- **Behavior:** Each secret is securely stored and immediately available in the app environment.
