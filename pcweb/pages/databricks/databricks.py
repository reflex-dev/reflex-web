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
    description="Build and deploy production-ready Databricks apps in pure Python. Integrate with SQL Warehouse, Unity Catalog, and Genie AI.",
    meta=create_meta_tags(
        "Reflex on Databricks - Deploy Python Apps",
        "Build and deploy production-ready Databricks apps in pure Python. Integrate with SQL Warehouse, Unity Catalog, and Genie AI.",
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
