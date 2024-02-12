---
components:
    - rx.radix.alert_dialog.root
    - rx.radix.alert_dialog.content
    - rx.radix.alert_dialog.trigger
    - rx.radix.alert_dialog.title
    - rx.radix.alert_dialog.description
    - rx.radix.alert_dialog.action
    - rx.radix.alert_dialog.cancel

only_low_level:
    - True

AlertDialogRoot: |
    lambda **props: rx.radix.themes.alert_dialog.root(
        rx.radix.themes.alert_dialog.trigger(
            rx.radix.themes.button("Revoke access"),
        ),
        rx.radix.themes.alert_dialog.content(
            rx.radix.themes.alert_dialog.title("Revoke access"),
            rx.radix.themes.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.radix.themes.flex(
                rx.radix.themes.alert_dialog.cancel(
                    rx.radix.themes.button("Cancel"),
                ),
                rx.radix.themes.alert_dialog.action(
                    rx.radix.themes.button("Revoke access"),
                ),
                gap="3",
            ),
        ),
        **props
    )

AlertDialogContent: |
    lambda **props: rx.radix.themes.alert_dialog.root(
        rx.radix.themes.alert_dialog.trigger(
            rx.radix.themes.button("Revoke access"),
        ),
        rx.radix.themes.alert_dialog.content(
            rx.radix.themes.alert_dialog.title("Revoke access"),
            rx.radix.themes.alert_dialog.description(
                "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            ),
            rx.radix.themes.flex(
                rx.radix.themes.alert_dialog.cancel(
                    rx.radix.themes.button("Cancel"),
                ),
                rx.radix.themes.alert_dialog.action(
                    rx.radix.themes.button("Revoke access"),
                ),
                gap="3",
            ),
            **props
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.

