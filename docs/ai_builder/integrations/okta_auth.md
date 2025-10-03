---
tags: Authentication
description: Use Okta for secure identity and access management via Single Sign-On provisioning.
---

# Okta Auth Manager Integration

The **Okta Auth Manager Integration** allows your app to authenticate users through [Okta](https://okta.com). This integration provides secure OAuth 2.0 / OIDC authentication and supports multi-tenant environments with customizable access policies.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/okta_light.webp",
                "/ai_builder/integrations/okta_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Step 1: Set Up Okta OIDC App

Before connecting, you need to create an OIDC application in the Okta Admin Console:

1. Go to [Okta Admin Console](https://login.okta.com) → **Applications**
2. Click **Create App Integration**
3. Select **OIDC – OpenID Connect** and choose **Web Application**
4. Configure your app settings:
   - **Sign-in redirect URIs**:
     `https://sb-39b61a39-c9bb-4877-8926-b309598edc58.fly.dev/authorization-code/callback`
   - Assign to the correct **Group** or **Everyone** depending on your access control
5. Save the app integration.

## Step 2: Gather Your Credentials

After creating your Okta app, collect the following information:

- **OKTA_CLIENT_ID**: `0oa1abcdXYZ2efGhI5d7`
  *Your app’s Client ID from the Okta Admin Console*

- **OKTA_CLIENT_SECRET**: `xYzABC1234567DefghIJKLmnopQrstuVW`
  *Your app’s Client Secret (keep this secure)*

- **OKTA_ISSUER_URI**: `https://dev-12345678.okta.com/oauth2/default`
  *The Issuer URL from your app’s settings*

> **Note:** Always use separate Okta apps for dev, staging, and production environments to avoid mixing credentials.

## Step 3: Configure the Integration

1. Go to the **Integrations** section in your app settings by clicking **`@`** and then selecting the **Integrations** tab.
2. Click **Add** next to **Okta Auth Manager**.
3. Fill in the credential fields:
   - Enter your Okta Client ID
   - Enter your Okta Client Secret
   - Enter your Okta Issuer URI
4. Click **Connect** to save the integration.

Your app can now authenticate users through Okta using the secure OAuth 2.0 / OIDC flow.
