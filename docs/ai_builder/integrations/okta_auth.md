---
tags: Authentication
description: Use Okta for secure identity and access management via Single Sign-On provisioning.
---

# Okta Auth Manager Integration

The **Okta Auth Manager Integration** allows your app to authenticate users through [Okta](https://okta.com). This integration provides secure OAuth 2.0 / OIDC authentication and supports multi-tenant environments with customizable access policies.


## What You Can Do

With Okta, your app can:
- Authenticate users securely through Okta’s identity platform.  
- Enable **SSO** for enterprise users.  
- Manage user roles, groups, and access permissions.  
- Protect sensitive data and actions with **OAuth 2.0** and **OpenID Connect (OIDC)**.  
- Integrate with other identity workflows like MFA or adaptive policies.


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```



## Step 1: Set Up Okta OIDC App

Before connecting, you need to create an OIDC application in the Okta Admin Console:

1 - Go to [Okta Admin Console](https://login.okta.com) → **Applications** → **Applications**


2 - Click **Create App Integration**

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/okta_auth_1.png",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

3 - Select **OIDC – OpenID Connect** and choose **Web Application**

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/okta_auth_2.png",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

4 - Configure your app settings:
   - **Allow wildcard * in sign-in redirect URIs**
   - **Sign-in redirect URIs** found in the Okta Auth Manager integration settings in AI Builder:
     `https://{your-sandbox}/authorization-code/callback`
   - **Sign-out redirect URIs**:
     `https://{your-sandbox}`
   - Assign to the correct **Group** or **Everyone** depending on your access control

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/okta_auth_3.png",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

5 - Save the app integration.

6 - Copy your **Client ID** (`OKTA_CLIENT_ID`) and **Client Secret** (`OKTA_CLIENT_SECRET`) from the app settings.

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/okta_auth_4.png",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```


## Step 2: Finding Your Okta Issuer URI

1. In the Okta Admin Console, go to **Security** → **API** → **Authorization Servers**
2. Click on the **default** server and copy the **Issuer URI**.
3. Remove the trailing `/oauth2/default` from the URI to get your **Okta Issuer URI** (`OKTA_ISSUER_URI`).

Example:

If your Issuer URI is `https://{yourOktaDomain}.okta.com/oauth2/default`

Use `https://{yourOktaDomain}.okta.com`



```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/okta_auth_5.png",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```


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
