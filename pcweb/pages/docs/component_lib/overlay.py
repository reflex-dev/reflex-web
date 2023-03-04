import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

# Overlay
code85 = """
pc.box(pc.button("Show Alert Dialog", on_click=AlertDialogState.change),
    pc.alert_dialog(
        pc.alert_dialog_overlay(
            pc.alert_dialog_content(
                pc.alert_dialog_header("Confirm"),
                pc.alert_dialog_body("Do you want to confirm example?"),
                pc.alert_dialog_footer(
                    pc.button("Close", on_click=AlertDialogState.change)
                ),
            )
        ),
        is_open=AlertDialogState.show,
    )
)
"""
code86 = """class AlertDialogState(State):
    show: bool = False

    def change(self):
        self.show = not (self.show)
"""
exec(code86)


def render_alertdialog():
    return pc.vstack(
        doctext(
            "AlertDialog component is used to interrupt the user with a mandatory confirmation or event. When used a alertdialog component will appear in front of the page prompting the user to conplete an event."
        ),
        docdemo(code85, state=code86, comp=eval(code85)),
        align_items="start",
    )


code88 = """class DrawerState(State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)
"""
exec(code88)
code87 = """
pc.box(pc.button("Show Right Drawer", on_click=DrawerState.right),
    pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.drawer_header("Confirm"),
                pc.drawer_body("Do you want to confirm example?"),
                pc.drawer_footer(
                    pc.button("Close", on_click=DrawerState.right)
                ),
                bg = "rgba(0, 0, 0, 0.3)"
            )
        ),
        is_open=DrawerState.show_right,
    )
)
"""
code89 = """
pc.box(pc.button("Show Top Drawer", on_click=DrawerState.top),
    pc.drawer(
        pc.drawer_overlay(
            pc.drawer_content(
                pc.drawer_header("Confirm"),
                pc.drawer_body("Do you want to confirm example?"),
                pc.drawer_footer(
                    pc.button("Close", on_click=DrawerState.top)
                ),
            )
        ),
        placement="top",
        is_open=DrawerState.show_top,
    )
)
"""


def render_drawer():
    return pc.vstack(
        pc.text(
            "The Drawer component is a panel that slides out from the edge of the screen. It can be useful when you need users to complete a task or view some details without leaving the current page."
        ),
        pc.text("For purpose of these example we will be using this same state."),
        docdemo(code87, state=code88, comp=eval(code87)),
        doctext(
            "Drawer can display from the top, bottom, left, or right. By defualt it displays to the right as seen above."
        ),
        docdemo(code89, comp=eval(code89)),
        align_items="start",
    )


code90 = """pc.menu(
    pc.menu_button("Menu"),
    pc.menu_list(
        pc.menu_item("Example"),
        pc.menu_divider(),
        pc.menu_item("Example"),
        pc.menu_item("Example"),
    ),
)
"""


def render_menu():
    return pc.vstack(
        doctext(
            "An accessible dropdown menu for the common dropdown menu button design pattern."
        ),
        docdemo(code90),
        align_items="start",
    )


code91 = """pc.box(
    pc.button("Confirm", on_click=ModalState.change),
    pc.modal(
        pc.modal_overlay(
            pc.modal_content(
                pc.modal_header("Confirm"),
                pc.modal_body("Do you want to confirm example?"),
                pc.modal_footer(pc.button("Close", on_click=ModalState.change)),
            )
        ),
        is_open=ModalState.show,
    ),
)
"""
code92 = """class ModalState(State):
    show: bool = False

    def change(self):
        self.show = not (self.show)
"""
exec(code92)


def render_modal():
    return pc.vstack(
        doctext(
            "A modal dialog is a window overlaid on either the primary window or another dialog window. Content behind a modal dialog is inert, meaning that users cannot interact with it."
        ),
        docdemo(code91, state=code92, comp=eval(code91)),
        align_items="start",
    )


code93 = """pc.popover(
    pc.popover_trigger(pc.button("Popover Example")),
    pc.popover_content(
        pc.popover_header("Confirm"),
        pc.popover_body("Do you want to confirm example?"),
        pc.popover_footer(pc.text("Footer text.")),
        pc.popover_close_button(),
    ),
)
"""


def render_popover():
    return pc.vstack(
        doctext(
            "Popover is a non-modal dialog that floats around a trigger. It is used to display contextual information to the user, and should be paired with a clickable trigger element."
        ),
        docdemo(code93),
        align_items="start",
    )


code94 = """pc.tooltip(
    pc.text("Example", font_size=30),
    label="Tooltip helper.",
)
"""


def render_tooltip():
    return pc.vstack(
        doctext(
            "A tooltip is a brief, informative message that appears when a user interacts with an element. Tooltips are usually initiated in one of two ways: through a mouse-hover gesture or through a keyboard-hover gesture."
        ),
        docdemo(code94),
        align_items="start",
    )
