---
components:
    - rx.radix.tabs.root
    - rx.radix.tabs.list
    - rx.radix.tabs.trigger
    - rx.radix.tabs.content

only_low_level:
    - True

TabsRoot: |
    lambda **props: rx.radix.themes.tabs.root(
        rx.radix.themes.tabs.list(
            rx.radix.themes.tabs.trigger("Account", value="account"),
            rx.radix.themes.tabs.trigger("Documents", value="documents"),
            rx.radix.themes.tabs.trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
        **props,
    )

TabsList: |
    lambda **props: rx.radix.themes.tabs.root(
        rx.radix.themes.tabs.list(
            rx.radix.themes.tabs.trigger("Account", value="account"),
            rx.radix.themes.tabs.trigger("Documents", value="documents"),
            rx.radix.themes.tabs.trigger("Settings", value="settings"),
            **props,
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
    )

TabsTrigger: |
    lambda **props: rx.radix.themes.tabs.root(
        rx.radix.themes.tabs.list(
            rx.radix.themes.tabs.trigger("Account", value="account", **props,),
            rx.radix.themes.tabs.trigger("Documents", value="documents"),
            rx.radix.themes.tabs.trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
    )

TabsContent: |
    lambda **props: rx.radix.themes.tabs.root(
        rx.radix.themes.tabs.list(
            rx.radix.themes.tabs.trigger("Account", value="account"),
            rx.radix.themes.tabs.trigger("Documents", value="documents"),
            rx.radix.themes.tabs.trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
                **props,
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
                **props,
            ),
            rx.radix.themes.tabs.content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
                **props,
            ),
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.
