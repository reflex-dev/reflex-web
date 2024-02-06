---
components:
    - rx.radix.themes.TabsRoot
    - rx.radix.themes.TabsList
    - rx.radix.themes.TabsTrigger
    - rx.radix.themes.TabsContent

only_low_level:
    - True

TabsRoot: |
    lambda **props: rx.radix.themes.tabs_root(
        rx.radix.themes.tabs_list(
            rx.radix.themes.tabs_trigger("Account", value="account"),
            rx.radix.themes.tabs_trigger("Documents", value="documents"),
            rx.radix.themes.tabs_trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
        **props,
    )

TabsList: |
    lambda **props: rx.radix.themes.tabs_root(
        rx.radix.themes.tabs_list(
            rx.radix.themes.tabs_trigger("Account", value="account"),
            rx.radix.themes.tabs_trigger("Documents", value="documents"),
            rx.radix.themes.tabs_trigger("Settings", value="settings"),
            **props,
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
    )

TabsTrigger: |
    lambda **props: rx.radix.themes.tabs_root(
        rx.radix.themes.tabs_list(
            rx.radix.themes.tabs_trigger("Account", value="account", **props,),
            rx.radix.themes.tabs_trigger("Documents", value="documents"),
            rx.radix.themes.tabs_trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
            ),
        ),
    )

TabsContent: |
    lambda **props: rx.radix.themes.tabs_root(
        rx.radix.themes.tabs_list(
            rx.radix.themes.tabs_trigger("Account", value="account"),
            rx.radix.themes.tabs_trigger("Documents", value="documents"),
            rx.radix.themes.tabs_trigger("Settings", value="settings"),
        ),
        rx.radix.themes.box(
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Make changes to your account"),
                value="account",
                **props,
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Update your documents"),
                value="documents",
                **props,
            ),
            rx.radix.themes.tabs_content(
                rx.radix.themes.text("Edit your personal profile"),
                value="settings",
                **props,
            ),
        ),
    )
---


# Check Out Low Level Docs! High Level API Coming Soon.
