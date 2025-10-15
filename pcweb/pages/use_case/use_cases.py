import reflex as rx
from flexdown.document import Document

from pcweb.components.docpage.navbar import navbar
from pcweb.flexdown import xd2 as xd
from pcweb.meta.meta import meta_tags
from pcweb.pages.customers.views.footer import footer_customer
from pcweb.pages.framework.index_colors import index_colors
from pcweb.views.bottom_section.bottom_section import bottom_section

document = Document.from_file("pcweb/pages/use_case/use_cases.md")


def use_case_content():
    return rx.box(xd.render(document, document.filename))


@rx.page(route="/use-cases", title="Use Cases - Reflex", meta=meta_tags)
def use_case():
    return rx.box(
        rx.box(
            index_colors(),
            navbar(),
            rx.el.main(
                use_case_content(),
                rx.box(class_name="flex-grow"),
                class_name="w-full z-[1] relative flex flex-col justify-center mx-auto max-w-[640px] lg:px-0 px-4 pb-20",
            ),
            rx.box(class_name="h-[1px] bg-slate-3 w-full"),
            bottom_section(),
            footer_customer(),
            class_name="relative flex flex-col justify-start items-center w-full h-full min-h-screen font-instrument-sans gap-4 mx-auto max-w-[64.19rem] lg:border-x border-slate-3 pt-24 lg:pt-48",
        ),
        class_name="relative overflow-hidden",
    )
