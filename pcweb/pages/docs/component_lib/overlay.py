import reflex as rx
from pcweb.templates.docpage import docdemo, doctext

# Overlay
code85 = """
rx.box(rx.button("Show Alert Dialog", on_click=AlertDialogState.change),
    rx.alert_dialog(
        rx.alert_dialog_overlay(
            rx.alert_dialog_content(
                rx.alert_dialog_header("Confirm"),
                rx.alert_dialog_body("Do you want to confirm example?"),
                rx.alert_dialog_footer(
                    rx.button("Close", on_click=AlertDialogState.change)
                ),
            )
        ),
        is_open=AlertDialogState.show,
    )
)
"""
code86 = """class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)
"""
exec(code86)


def render_alertdialog():
    return rx.vstack(
        doctext(
            "AlertDialog component is used to interrupt the user with a mandatory confirmation or event. When used a alertdialog component will appear in front of the page prompting the user to conplete an event."
        ),
        docdemo(code85, state=code86, comp=eval(code85)),
        align_items="start",
    )


code88 = """class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)
"""
exec(code88)
code87 = """
rx.box(rx.button("Show Right Drawer", on_click=DrawerState.right),
    rx.drawer(
        rx.drawer_overlay(
            rx.drawer_content(
                rx.drawer_header("Confirm"),
                rx.drawer_body("Do you want to confirm example?"),
                rx.drawer_footer(
                    rx.button("Close", on_click=DrawerState.right)
                ),
                bg = "rgba(0, 0, 0, 0.3)"
            )
        ),
        is_open=DrawerState.show_right,
    )
)
"""
code89 = """
rx.box(rx.button("Show Top Drawer", on_click=DrawerState.top),
    rx.drawer(
        rx.drawer_overlay(
            rx.drawer_content(
                rx.drawer_header("Confirm"),
                rx.drawer_body("Do you want to confirm example?"),
                rx.drawer_footer(
                    rx.button("Close", on_click=DrawerState.top)
                ),
            )
        ),
        placement="top",
        is_open=DrawerState.show_top,
    )
)
"""


def render_drawer():
    return rx.vstack(
        rx.text(
            "The Drawer component is a panel that slides out from the edge of the screen. It can be useful when you need users to complete a task or view some details without leaving the current page."
        ),
        rx.text("For purpose of these example we will be using this same state."),
        docdemo(code87, state=code88, comp=eval(code87)),
        doctext(
            "Drawer can display from the top, bottom, left, or right. By defualt it displays to the right as seen above."
        ),
        docdemo(code89, comp=eval(code89)),
        align_items="start",
    )


code90 = """rx.menu(
    rx.menu_button("Menu"),
    rx.menu_list(
        rx.menu_item("Example"),
        rx.menu_divider(),
        rx.menu_item("Example"),
        rx.menu_item("Example"),
    ),
)
"""


def render_menu():
    return rx.vstack(
        doctext(
            "An accessible dropdown menu for the common dropdown menu button design pattern."
        ),
        docdemo(code90),
        align_items="start",
    )


code91 = """rx.box(
    rx.button("Confirm", on_click=ModalState.change),
    rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Confirm"),
                rx.modal_body("Do you want to confirm example?"),
                rx.modal_footer(rx.button("Close", on_click=ModalState.change)),
            )
        ),
        is_open=ModalState.show,
    ),
)
"""
code92 = """class ModalState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)
"""
exec(code92)


def render_modal():
    return rx.vstack(
        doctext(
            "A modal dialog is a window overlaid on either the primary window or another dialog window. Content behind a modal dialog is inert, meaning that users cannot interact with it."
        ),
        docdemo(code91, state=code92, comp=eval(code91)),
        align_items="start",
    )


code93 = """rx.popover(
    rx.popover_trigger(rx.button("Popover Example")),
    rx.popover_content(
        rx.popover_header("Confirm"),
        rx.popover_body("Do you want to confirm example?"),
        rx.popover_footer(rx.text("Footer text.")),
        rx.popover_close_button(),
    ),
)
"""


def render_popover():
    return rx.vstack(
        doctext(
            "Popover is a non-modal dialog that floats around a trigger. It is used to display contextual information to the user, and should be paired with a clickable trigger element."
        ),
        docdemo(code93),
        align_items="start",
    )


code94 = """rx.tooltip(
    rx.text("Example", font_size=30),
    label="Tooltip helper.",
)
"""


def render_tooltip():
    return rx.vstack(
        doctext(
            "A tooltip is a brief, informative message that appears when a user interacts with an element. Tooltips are usually initiated in one of two ways: through a mouse-hover gesture or through a keyboard-hover gesture."
        ),
        docdemo(code94),
        align_items="start",
    )
