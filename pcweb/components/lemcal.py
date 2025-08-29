import reflex as rx


def lemcal_button(
    child: rx.Component | None = None,
    label: str = "Book a Demo",
    class_name: str = "",
) -> rx.Component:
    """Reusable Lemcal embed button wrapper.

    Wraps provided child (or a default button) in a div with the Lemcal
    integration class and data attributes so that the external script can
    attach the booking behavior.
    """
    content = child if child is not None else rx.el.button(label)
    return rx.el.div(
        content,
        class_name=("lemcal-embed-button " + class_name).strip(),
        custom_attrs={
            "data-user": "usr_8tiwtJ8nEJaFj2qH9",
            "data-meeting-type": "met_ToQQ9dLZDYrEBv5qz",
        },
    )
