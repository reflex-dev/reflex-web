---
tags: Authentication
description: Integrate Azure for secure authentication and access management within your application.
---
# Azure Auth Manager Integration

The **Azure Auth Manager Integration** allows your app to authenticate users through Microsoft Azure Active Directory (Azure AD). This integration provides secure OAuth 2.0 authentication and supports multi-tenant applications with customizable tenant access.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/azure_auth_light.webp",
                "/ai_builder/integrations/azure_auth_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Step 1: Set Up Azure App Registration

Before connecting, you need to register your app in Azure Portal:

1. Go to [Azure Portal](https://portal.azure.com) → **App Registrations**
2. Click **New registration**
3. Configure your app settings
4. In **Authentication**, add the Web Redirect URI: `https://3a992b51-c34a-405a-b90c-4b3320eb3b6a.fly.dev/authorization-code/callback`

## Step 2: Gather Your Credentials

After registering your app, collect the following information:

- **AZURE_CLIENT_ID**: `12345678-1234-1234-1234-123456789abc`
  *Your application (client) ID from App Registration*

- **AZURE_CLIENT_SECRET**: `abcdef123456~ABCdef123456-ABCdef123456`
  *Client secret generated in Certificates & secrets*

- **AZURE_VALID_TENANT_IDS**: `87654321-4321-4321-4321-210987654321`
  *Comma-separated list of tenant IDs that can access your app*

> **Note:** Keep your client secret secure and use different registrations for development, staging, and production environments.

## Step 3: Configure the Integration

1. Go to the **Integrations** section in your app settings by clicking **`@`** and then clicking the **Integrations** tab at the top.
2. Click **Add** next to Azure Auth Manager.
3. Fill in the credential fields:
   - Enter your Azure Client ID
   - Enter your Azure Client Secret
   - Enter valid tenant IDs (comma-separated for multiple tenants)
4. Click **Connect** to save the integration.

Your app can now authenticate users through Azure AD with secure OAuth 2.0 flow.
