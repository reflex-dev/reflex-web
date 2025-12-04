import reflex as rx
import reflex_ui as ui
from reflex.components.lucide.icon import LUCIDE_ICON_LIST
from reflex.experimental.client_state import ClientStateVar

icon_search_cs = ClientStateVar.create("icon_search", default="")


@rx.memo
def lucide_icons():
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(
                    tag="search",
                    size=20,
                    class_name="shrink-0 !text-slate-11",
                ),
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 z-[1] shrink-0 flex items-center justify-center pb-2",
            ),
            rx.el.input(
                placeholder="Search icons...",
                on_change=icon_search_cs.set_value,
                class_name="relative box-border border-slate-4 focus:border-violet-9 focus:border-1 bg-slate-2 p-[0.5rem_0.75rem] border rounded-xl font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full mb-2 pl-10",
            ),
            class_name="relative flex items-center",
        ),
        rx.el.div(
            rx.box(
                rx.foreach(
                    LUCIDE_ICON_LIST,
                    lambda icon: rx.cond(
                        icon.startswith(icon_search_cs.value),
                        ui.tooltip(
                            content=icon,
                            trigger=rx.box(
                                rx.icon(tag=icon),
                                class_name="flex items-center justify-center rounded-md hover:bg-slate-3 transition-bg p-2 cursor-pointer",
                                on_click=[
                                    rx.set_clipboard(icon),
                                    rx.toast.success(f"Copied {icon} to clipboard"),
                                ],
                                key=icon,
                            ),
                        ),
                        None,
                    ),
                ),
                class_name="flex flex-wrap justify-start gap-4 mb-4",
            ),
            class_name="overflow-y-auto max-h-[500px]",
        ),
        class_name="flex flex-col gap-4",
    )
