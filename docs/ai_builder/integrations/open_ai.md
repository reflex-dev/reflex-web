# OpenAI Integration

The **OpenAI Integration** allows your app to use OpenAI APIs for features such as text generation, embeddings, and other AI-powered functionality.



```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/open_ai_light.png",
                "/ai_builder/integrations/open_ai_dark.png",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Step 1: Obtain an OpenAI API Key

1. Go to the [OpenAI Platform](https://platform.openai.com/).
2. Navigate to **API Keys** in your account settings.
3. Click **Create new secret key**.
4. Copy the generated key.
   - Example: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`


## Step 2: Configure the Integration in Your App

1. Go to **Integrations → Add OpenAI Integration** in your app settings.
2. Enter your **OpenAI API Key** in the input field.
3. Save the integration. Your app is now ready to make OpenAI API requests.

---

## Step 3: Notes

- Keep your OpenAI key secure; do **not** hardcode it in public code repositories.
- Use environment-specific secrets if you have separate development, staging, and production environments.
- The key allows your app to interact with OpenAI endpoints securely and efficiently.
