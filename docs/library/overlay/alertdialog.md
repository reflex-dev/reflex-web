---
components:
    - rx.radix.themes.AlertDialogRoot
    - rx.radix.themes.AlertDialogContent
    - rx.radix.themes.AlertDialogTrigger
    - rx.radix.themes.AlertDialogTitle
    - rx.radix.themes.AlertDialogDescription
    - rx.radix.themes.AlertDialogAction
    - rx.radix.themes.AlertDialogCancel

only_low_level:
    - True

AlertDialogRoot: |
    lambda **props: rx.radix.themes.alertdialog_root(
        rx.radix.themes.alertdialog_trigger(
            rx.radix.themes.button("Revoke access"),
        ),
        rx.radix.themes.alertdialog_content(
            rx.radix.themes.alertdialog_title("Revoke access"),
            rx.radix.themes.alertdialog_description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.radix.themes.flex(
                rx.radix.themes.alertdialog_cancel(
                    rx.radix.themes.button("Cancel"),
                ),
                rx.radix.themes.alertdialog_action(
                    rx.radix.themes.button("Revoke access"),
                ),
                gap="3",
            ),
        ),
        **props
    )

AlertDialogContent: |
    lambda **props: rx.radix.themes.alertdialog_root(
        rx.radix.themes.alertdialog_trigger(
            rx.radix.themes.button("Revoke access"),
        ),
        rx.radix.themes.alertdialog_content(
            rx.radix.themes.alertdialog_title("Revoke access"),
            rx.radix.themes.alertdialog_description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.radix.themes.flex(
                rx.radix.themes.alertdialog_cancel(
                    rx.radix.themes.button("Cancel"),
                ),
                rx.radix.themes.alertdialog_action(
                    rx.radix.themes.button("Revoke access"),
                ),
                gap="3",
            ),
            **props
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

