import reflex as rx

from pcweb.meta.meta import meta_tags
from pcweb.templates.mainpage import mainpage

from .integration_header import integration_header
from .integration_gallery import integration_filters, integration_gallery, integration_request_form

@mainpage(path="/integrations", title="Reflex · Integrations", meta=meta_tags)
def integration_page():
    return rx.el.div(
        integration_header(),
        integration_filters(),
        integration_gallery(),
        integration_request_form(),
        class_name="flex flex-col size-full justify-center items-center",
    )
