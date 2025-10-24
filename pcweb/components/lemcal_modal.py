"""Reusable Lemcal modal component for booking demos."""

import reflex as rx


class LemcalModalState(rx.State):
    is_open: bool = False

    @rx.event
    def open(self):
        self.is_open = True

    @rx.event
    def close(self):
        self.is_open = False


@rx.memo
def lemcal_booking_calendar():
    return rx.el.div(
        class_name="lemcal-embed-booking-calendar",
        custom_attrs={
            "data-user": "usr_8tiwtJ8nEJaFj2qH9",
            "data-meeting-type": "met_ToQQ9dLZDYrEBv5qz",
        },
        on_mount=rx.call_function("window.lemcal.refresh"),
    )


def lemcal_modal() -> rx.Component:
    """Reusable lemcal modal component that can be used anywhere in the app."""
    return rx.cond(
        LemcalModalState.is_open,
        rx.box(
            rx.el.div(
                rx.box(
                    lemcal_booking_calendar(),
                ),
                class_name="fixed inset-0 bg-black/40 backdrop-blur-sm z-[9999] flex items-center justify-center",
                on_click=LemcalModalState.close,
            ),
        ),
        rx.fragment(),
    )