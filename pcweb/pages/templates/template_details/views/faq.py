import reflex as rx
import reflex_ui as ui

from pcweb.pages.templates.templates_state import TemplatesState


def faq_item(faq: rx.Var[dict[str, str]]) -> rx.Component:
    return ui.accordion.item(
        ui.accordion.header(
            ui.accordion.trigger(
                faq.get("q", ""),
                ui.icon(
                    "PlusSignIcon",
                    class_name="lg:size-4.5 size-4 shrink-0 transition-transform ease-out group-data-[panel-open]:rotate-45",
                    data_slot="accordion-trigger-icon",
                ),
                unstyled=True,
                class_name="text-secondary-12 lg:text-lg text-base font-semibold lg:py-6 py-4 flex-row group relative flex w-full items-center justify-between gap-4 text-md transition-colors disabled:cursor-not-allowed disabled:bg-secondary-3 disabled:text-secondary-8 disabled:[&_svg]:text-secondary-8 [&_svg]:text-secondary-11 data-[panel-open]:text-primary-11 ease-out",
            ),
            unstyled=True,
        ),
        ui.accordion.panel(
            rx.el.div(faq.get("a", ""), class_name="lg:pb-6 pb-4"),
            unstyled=True,
            class_name="h-[var(--accordion-panel-height)] overflow-hidden text-sm text-secondary-11 font-medium transition-[height,opacity] ease-out data-[ending-style]:h-0 data-[starting-style]:h-0",
        ),
        unstyled=True,
    )


def faq():
    return rx.el.div(
        rx.el.h2(
            "Frequently Asked Questions",
            class_name="text-2xl font-[575] text-secondary-12",
        ),
        ui.accordion.root(
            rx.foreach(TemplatesState.active_template.faq, faq_item),
            unstyled=True,
            class_name="w-full flex flex-col justify-center divide-y divide-dashed divide-secondary-4 overflow-hidden",
            multiple=True,
        ),
        class_name="pr-16 py-16 flex flex-col gap-6 w-full",
    )
