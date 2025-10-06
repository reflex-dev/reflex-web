---
tags: Communication
description: Send transactional and automated emails directly from your AI-generated applications using Resend.
---
# Resend Integration

The **Resend Integration** allows your AI-generated apps to send emails directly from workflows, user actions, or automated triggers — perfect for notifications, confirmations, or any email-based communication your app needs.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/resend_light.webp",
                "/ai_builder/integrations/resend_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## What You Can Do

With the Resend Integration, your app can:
- Send automated transactional emails
- Notify users of important events (signups, job completions, etc.)
- Integrate email sending into AI workflows
- Use dynamic variables in your message body (e.g. user name, order ID)

## Step 1: Get Your Resend API Key

1. Go to [Resend](https://resend.com/).
2. Log in or create a free account.
3. Navigate to **API Keys** from the dashboard sidebar.
4. Click **Create API Key**, give it a name (e.g. “AI Builder”), and copy it.
   - Example: `re_1234567890abcdefghijklmn`

## Step 2: Configure the Integration in Your App

1. Open your app in the **AI Builder**.
2. Click the **Settings** gear icon and navigate to the **Integrations** tab.
3. Find and enable the **Resend** integration.
4. Paste your **API Key** in the input field.
5. Click **Connect** to confirm the connection.
