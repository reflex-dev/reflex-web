---
tags: Authentication
description: Add Descope’s identity and authentication platform to your apps to manage user sign-in, onboarding, MFA, SSO, and flows with ease.
---
# Descope Integration

The **Descope Integration** enables your app to leverage Descope’s full Customer Identity & Access Management (CIAM) features—visual authentication flows, identity management, SSO, MFA, tenant isolation, and more. Once set up, you can orchestrate secure user journeys across your application with minimal coding.


```md alert warning
# You must open your app in a new tab from the builder to test the Descope integration.

![Open new tab to test Descope](/ai_builder/integrations/descope_new_tab.webp)
```

## What You Can Do

With Descope Integration, your app can:
- Handle user sign-up, login, and passwordless flows seamlessly  
- Enable multifactor authentication (MFA), passkeys, and social login  
- Support single sign-on (SSO) via OIDC/SAML  
- Manage users, roles, tenants, and permissions via management APIs  
- Orchestrate onboarding, branding, and multi-tenant flows via drag-and-drop workflows  
- Sync user data with tools like HubSpot or Segment via built-in connectors


## Step 1: Obtain Descope Credentials

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/descope.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

1. Log in to the **Descope Console** (or sign up).
2. Create your first Project. 
3. Go to the Project page under Settings.
4. Copy the `Project ID`.


## Step 2: Configure the Integration in Your App

1. In your app’s settings or integration dashboard, select **Add Descope**.  
2. Enter your **PROJECT_ID**.  
3. (Optional) Pick a **DESCOPE_FLOW_ID** (e.g. “sign-up-or-login”) and **SESSION_SECRET_KEY** or press the Clipboard Copy to use default values.  
4. Click **Connect** to validate credentials and enable Descope features.

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/descope_2.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```


