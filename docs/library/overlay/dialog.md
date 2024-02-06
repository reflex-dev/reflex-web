---
components:
    # - rx.radix.themes.DialogRoot
    - rx.radix.themes.DialogTrigger
    - rx.radix.themes.DialogTitle
    - rx.radix.themes.DialogContent
    - rx.radix.themes.DialogDescription
    - rx.radix.themes.DialogClose

only_low_level:
    - True

DialogContent: |
    lambda **props: rx.radix.themes.dialog_root(
        rx.radix.themes.dialog_trigger(rx.radix.themes.button("Open Dialog")),
        rx.radix.themes.dialog_content(
            rx.radix.themes.dialog_title("Welcome to Reflex!"),
            rx.radix.themes.dialog_description(
                "This is a dialog component. You can render anything you want in here.",
            ),
            rx.radix.themes.dialog_close(
                rx.radix.themes.button("Close Dialog"),
            ),
            **props
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

