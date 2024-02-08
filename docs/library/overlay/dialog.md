---
components:
    - rx.radix.dialog.root
    - rx.radix.dialog.trigger
    - rx.radix.dialog.title
    - rx.radix.dialog.content
    - rx.radix.dialog.description
    - rx.radix.dialog.close

only_low_level:
    - True

DialogContent: |
    lambda **props: rx.dialog.root(
        rx.dialog.trigger(rx.button("Open Dialog")),
        rx.dialog.content(
            rx.dialog.title("Welcome to Reflex!"),
            rx.dialog.description(
                "This is a dialog component. You can render anything you want in here.",
            ),
            rx.dialog.close(
                rx.button("Close Dialog"),
            ),
            **props
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

