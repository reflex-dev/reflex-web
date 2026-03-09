import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.databricks.views.cta import final_cta
from pcweb.pages.databricks.views.hero import hero
from pcweb.pages.databricks.views.integrations import integrations
from pcweb.pages.databricks.views.security import security
from pcweb.pages.databricks.views.video import video
from pcweb.templates.mainpage import mainpage


@mainpage(
    path="/databricks",
    title="Reflex on Databricks - Deploy Python Apps",
    description="Deploy Reflex apps on Databricks and Snowflake. Build Python web apps in your data platform.",
    meta=create_meta_tags(
        "Reflex on Databricks - Deploy Python Apps",
        "Deploy Reflex apps on Databricks and Snowflake. Build Python web apps in your data platform.",
        "/previews/databricks_preview.png",
    ),
)
def databricks_page():
    return rx.el.div(
        hero(),
        video(),
        integrations(),
        security(),
        final_cta(),
        class_name="flex flex-col size-full justify-center items-center",
    )
