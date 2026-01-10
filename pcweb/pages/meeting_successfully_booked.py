import reflex as rx
import reflex_ui as ui
from pcweb.templates.webpage import webpage


@webpage(
    path="/meeting-successfully-booked",
    title="Meeting Successfully Booked · Reflex.dev",
    add_as_page=True,
)
def page_meeting_successfully_booked():
    return rx.box(
        rx.heading(
            "Meeting Successfully Booked!",
            class_name="gradient-heading font-x-large lg:font-xxx-large text-center text-transparent",
        ),
        rx.text(
            "We have sent you a confirmation email with all the details.",
            class_name="font-md text-balance text-slate-9 text-center mt-4",
        ),
        rx.box(
            ui.button(
                "Home", variant="primary", size="lg", on_click=rx.redirect("/")
            ),
            class_name="flex flex-row items-center gap-x-4 mt-8",
        ),
        class_name="h-[60vh] w-full flex flex-col items-center justify-center p-4",
    )
