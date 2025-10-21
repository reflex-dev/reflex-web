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


## Step 1: Set Up Azure App Registration

Before connecting, you need to register your app in Azure Portal:

1 - Go to [Azure Portal](https://portal.azure.com) → **App Registrations**

2 - Click **New registration** as shown in the image below:

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/azure_auth_1.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

3 - Register your app. Ensure that for the Redirect URI you select **Web** and enter the following URI that you find in the Azure Auth Manager integration settings in AI Builder:
   ```
   https://{your-sandbox}/authorization-code/callback
   ```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/azure_auth_2.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

4 - On the next page get your `client_id` (`AZURE_CLIENT_ID`) and `tenant_id` (`AZURE_VALID_TENANT_IDS`) from the **Overview** tab.

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/azure_auth_3.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

5 - Next click `Add a certificate or secret` and copy the generated secret value (`AZURE_CLIENT_SECRET`).

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/azure_auth_4.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```



## Step 2: Configure the Integration

1. Go to the **Integrations** section in your app settings by clicking **`@`** and then clicking the **Integrations** tab at the top.
2. Click **Add** next to Azure Auth Manager.
3. Fill in the credential fields:
   - Enter your Azure Client ID
   - Enter your Azure Client Secret
   - Enter valid tenant IDs (comma-separated for multiple tenants)
4. Click **Connect** to save the integration.

Your app can now authenticate users through Azure AD with secure OAuth 2.0 flow.
