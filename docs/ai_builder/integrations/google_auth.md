---
tags: Authentication
description: Enable secure authentication using Google sign-in and OAuth 2.0 workflows.
---

# Google Auth Integration

The **Google Auth Integration** allows your app to authenticate users using their Google accounts. This provides a secure, familiar login experience and simplifies user management.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/google_light.webp",
                "/ai_builder/integrations/google_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Step 1: Create a Google OAuth Client

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **APIs & Services → Credentials**.
3. Click **Create Credentials → OAuth Client ID**.
4. Select **Web Application** as the application type.
5. Add the following **Authorized JavaScript Origin**:
   - https://3a992b51-c34a-405a-b90c-4b3320eb3b6a.fly.dev
   - The URL can be copied directly from the Google Auth integration panel.
6. Set your authorized redirect URIs to match your app environment.
7. Save the client and copy the following credentials:
   - **Client ID**: `YOUR_GOOGLE_CLIENT_ID`
   - **Client Secret**: `YOUR_GOOGLE_CLIENT_SECRET`

## Step 2: Configure the Integration in Your App

1. Go to **Integrations → Add Google Auth** in your app settings.
2. Enter your **Google Client ID** and **Google Client Secret**.
3. Save the integration. Your app is now configured to use Google Auth for login.

## Step 3: Notes

- The integration supports multiple environments (development, staging, production). Use environment-specific secrets for the client ID and secret.
- Google Auth handles token refresh automatically when users log in via OAuth.
- Users will see a standard Google login screen, ensuring familiarity and trust.
- Ensure your app domain matches the authorized JavaScript origin and redirect URIs; otherwise, authentication will fail.
