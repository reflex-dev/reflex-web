import reflex as rx
from reflex.event import EventHandler, passthrough_event_spec

from pcweb.components.utils.twmerge import cn


def dialog(
    content: rx.Component,
    trigger: rx.Component,
    class_name: str = "",
    trigger_class_name: str = "",
    on_open_change: EventHandler[passthrough_event_spec(bool)] | None = None,
    **props,
) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            trigger,
            class_name=trigger_class_name,
        ),
        rx.dialog.content(
            content,
            class_name=cn(
                "!shadow-large !rounded-xl !bg-slate-1 !p-6 !font-sans",
                class_name,
            ),
            **props,
        ),
        on_open_change=on_open_change,
    )
