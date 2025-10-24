import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.databricks.views.cta import final_cta
from pcweb.pages.databricks.views.hero import hero
from pcweb.pages.databricks.views.integrations import integrations
from pcweb.pages.databricks.views.middle_text import middle_text
from pcweb.pages.databricks.views.security import security
from pcweb.pages.databricks.views.video import video
from pcweb.templates.mainpage import mainpage


@mainpage(
    path="/databricks",
    title="Databricks - Reflex",
    meta=create_meta_tags(
        "Databricks - Reflex",
        "Databricks - Reflex",
        "/previews/databricks_preview.webp",
    ),
)
def databricks_page():
    return rx.el.div(
        hero(),
        video(),
        integrations(),
        middle_text(),
        security(),
        final_cta(),
        class_name="flex flex-col size-full justify-center items-center",
    )
