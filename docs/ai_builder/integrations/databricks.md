# Databricks Integration

The **Databricks Integration** allows your app to connect to a Databricks workspace, query data from warehouses, and use catalogs and schemas directly in your app. This integration supports secure authentication via tokens and can be configured per environment.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/databricks_light.png",
                "/ai_builder/integrations/databricks_dark.png",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Step 1: Gather Your Credentials

Before connecting, make sure you have the following information:

- **Hostname**: `https://adb-1234567890123456.7.azuredatabricks.net`
  *The URL of your Databricks workspace*

- **Personal Access Token**: `dapi1234567890abcdef1234567890abcd`
  *Used for secure authentication*

- **Warehouse / SQL Endpoint ID**: `wh-9876543210`
  *The warehouse ID you want to query*

- **Catalog**: `databricks_catalog_demo`
  *The catalog containing your databases*

- **Schema**: `demo_schema`
  *The schema inside the catalog to query*

> **Note:** Use environment-specific credentials for development, staging, and production.

## Step 2: Configure the Integration

1. Go to the **Integrations** section in your app settings by clicking **`@`** and then clicking the **Integrations** tab at the top.
2. Click **Add Databricks Integration**.
3. Fill in the fields using your credentials
4. Save the integration. Your app can now access Databricks data securely.
