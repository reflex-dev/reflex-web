---
tags: Data Infrastructure
description: Connect with Databricks to run data pipelines and advanced analytics seamlessly.
---


# Databricks Integration

The **Databricks Integration** allows your app to connect to [Databricks](https://www.databricks.com/) for secure data access, querying, and analytics. Once connected, you can run SQL queries, retrieve results, and power data-driven workflows directly from your app.

## What You Can Do

With Databricks, your app can:
- Connect securely to your Databricks workspace.  
- Run **SQL queries** or fetch data programmatically.  
- Build **dashboards and data visualizations** on top of your Databricks tables.  
- Automate workflows triggered by new or updated data.  
- Combine Databricks with AI models for advanced analytics.


```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```


## Step 1: Get Your Databricks Credentials

1 - Log in to your [Databricks Workspace](https://databricks.com/).

2 - Get your **DATABRICKS_HOST** and **DATABRICKS_WAREHOUSE_ID**:
   - Go to `SQL Warehouses` from the sidebar.
   - Select your desired warehouse.
   - Click `Connection details`.
   - Copy the Server hostname (this is your **DATABRICKS_HOST**).
   - Copy the HTTP path removing the `/sql/1.0/warehouses/` prefix (this is your **DATABRICKS_WAREHOUSE_ID**).


```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/databricks_integration_1.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

3 - Generate a **Personal Access Token** (**DATABRICKS_TOKEN**):
   - Click on your profile icon → **Settings**.
   - Click **Developer**.
   - Click **Manage** in Access Tokens.
   - Click **Generate New Token**, provide a name and expiration, then copy it (**DATABRICKS_TOKEN**).

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/databricks_integration_2.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```



```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/databricks_integration_3.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

4 - Get your **DATABRICKS_CATALOG** and **DATABRICKS_SCHEMA**:
   - Click the SQL Editor from the sidebar.
   - Choose the **DATABRICKS_CATALOG** and **DATABRICKS_SCHEMA** from the dropdowns as shown below.


```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/ai_builder/integrations/databricks_integration_4.webp",
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```



## Step 2: Configure the Integration in Your App

1. In your app, go to **Integrations** and **Add Databricks**.  
2. Paste your 
   1. **DATABRICKS_TOKEN**
   2. **DATABRICKS_HOST**
   3. **DATABRICKS_WAREHOUSE_ID**
   4. **DATABRICKS_CATALOG**
   5. **DATABRICKS_SCHEMA**  
3. Click **Connect** to validate and save your integration.

Once connected, the AI Builder can execute queries directly against your Databricks environment.


## Step 3: Notes

* **Secure your token:** Never expose tokens in public code.  
* **Permissions:** Ensure your token or service account has the required workspace and table permissions.
* **Combine with AI:** Use query outputs to power models, summaries, or alerts in real time.

