"""Utility functions for the component docs page."""

import inspect
import os
import re
from typing import Any, Type, get_args

import reflex as rx
from pcweb.flexdown import markdown, xd
from pcweb.templates.docpage import docpage
from reflex.base import Base
from reflex.components.component import Component


class Prop(Base):
    """Hold information about a prop."""

    # The name of the prop.
    name: str

    # The type of the prop.
    type_: Any

    # The description of the prop.
    description: str


from reflex.components.el.elements.base import BaseHTML


class Source(Base):
    """Parse the source code of a component."""

    # The component to parse.
    component: Type[Component]

    # The source code.
    code: list[str] = []

    def __init__(self, *args, **kwargs):
        """Initialize the source code parser."""
        super().__init__(*args, **kwargs)

        # Get the source code.
        self.code = [
            line
            for line in inspect.getsource(self.component).splitlines()
            if len(line) > 0
        ]

    def get_docs(self) -> str:
        """Get the docstring of the component.

        Returns:
            The docstring of the component.
        """
        return self.component.__doc__

    def get_props(self) -> list[Prop]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        props = self._get_props()

        parent_cls = self.component.__bases__[0]
        if parent_cls != rx.Component and parent_cls != BaseHTML:
            props += Source(component=parent_cls).get_props()

        return props

    def _get_props(self) -> list[Prop]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        # The output.
        out = []

        # Get the props for this component.
        props = self.component.get_props()

        comments = []
        # Loop through the source code.
        for i, line in enumerate(self.code):
            # Check if we've reached the functions.
            reached_functions = re.search("def ", line)
            if reached_functions:
                # We've reached the functions, so stop.
                break

            # Get comments for prop
            if line.strip().startswith("#"):
                comments.append(line)
                continue

            # Check if this line has a prop.
            match = re.search(r"\w+:", line)
            if match is None:
                # This line doesn't have a var, so continue.
                continue

            # Get the prop.
            prop = match.group(0).strip(":")
            if prop not in props:
                # This isn't a prop, so continue.
                continue

            # redundant check just to double-check line above prop is a comment
            comment_above = self.code[i - 1].strip()
            assert comment_above.startswith(
                "#"
            ), f"Expected comment, got {comment_above}"

            # Get the comment for this prop.
            comment = Source.get_comment(comments)
            # reset comments
            comments.clear()

            # Get the type of the prop.
            type_ = self.component.get_fields()[prop].outer_type_

            # Add the prop to the output.
            out.append(
                Prop(
                    name=prop,
                    type_=type_,
                    description=comment,
                )
            )

        # Return the output.
        return out

    @staticmethod
    def get_comment(comments: list[str]):
        return "".join([comment.strip().strip("#") for comment in comments])


# Mapping from types to colors.
TYPE_COLORS = {
    "int": "red",
    "float": "orange",
    "str": "yellow",
    "bool": "teal",
    "Component": "purple",
    "List": "blue",
    "Dict": "blue",
    "Tuple": "blue",
    "None": "gray",
    "Figure": "green",
}

count = 0

import hashlib
def get_id(s):
    global count
    count += 1
    s = str(count)
    hash_object = hashlib.sha256(s.encode())
    hex_dig = hash_object.hexdigest()
    return "a_" + hex_dig[:8]

def prop_docs(prop: Prop, prop_dict, component) -> list[rx.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if rx.utils.types._issubclass(prop.type_, rx.Var):
        # For vars, get the type of the var.
        type_ = rx.utils.types.get_args(type_)[0]
    try:
        type_ = type_.__name__
    except AttributeError:
        print(type_)

    # Get the color of the prop.
    color = TYPE_COLORS.get(type_, "gray")

    # if the type if leteral show all the options
    if type_ == "Literal":
        output = get_args(prop.type_)
        prop.description = (
            str(output)
            .replace("typing.Literal[", "")
            .replace("']", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", " | ")
        )

    from typing import Literal, _GenericAlias

    def render_select(prop):
        try:
            type_ = rx.utils.types.get_args(prop.type_)[0]
        except:
            print(f"Failed to get args for {prop.type_}")
            return rx.fragment()
        if not isinstance(type_, _GenericAlias) or type_.__origin__ is not Literal:
            return rx.fragment()
        # Get the first option.
        option = type_.__args__[0]
        name = get_id(f"{component.__qualname__}_{prop.name}")
        rx.State.add_var(name, str, option)
        var = getattr(rx.State, name)
        setter = getattr(rx.State, f"set_{name}")
        prop_dict[prop.name] = var
        return rdxt.radio_group(
            list(map(str, type_.__args__)),
            value=var,
            on_value_change=setter,
        )

    # Return the docs for the prop.
    return [
        rdxt.table_cell(
            rdxt.code(prop.name, color="#333"),
            padding_left="0",
        ),
        rdxt.table_cell(
            rdxt.badge(type_, color_scheme=color, variant="solid"),
            padding_left="0",
        ),
        rdxt.table_cell(
            rx.vstack(
                markdown(prop.description),
                render_select(prop),
            ),
            padding_left="0",
        ),
    ]


EVENTS = {
    "on_focus": {
        "description": "Function or event handler called when the element (or some element inside of it) receives focus. For example, it is called when the user clicks on a text input."
    },
    "on_blur": {
        "description": "Function or event handler called when focus has left the element (or left some element inside of it). For example, it is called when the user clicks outside of a focused text input."
    },
    "on_change": {
        "description": "Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystoke triggers the on change."
    },
    "on_click": {
        "description": "Function or event handler called when the user clicks on an element. For example, it’s called when the user clicks on a button."
    },
    "on_context_menu": {
        "description": "Function or event handler called when the user right-clicks on an element. For example, it is called when the user right-clicks on a button."
    },
    "on_double_click": {
        "description": "Function or event handler called when the user double-clicks on an element. For example, it is called when the user double-clicks on a button."
    },
    "on_mouse_up": {
        "description": "Function or event handler called when the user releases a mouse button on an element. For example, it is called when the user releases the left mouse button on a button."
    },
    "on_mouse_down": {
        "description": "Function or event handler called when the user presses a mouse button on an element. For example, it is called when the user presses the left mouse button on a button."
    },
    "on_mouse_enter": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button."
    },
    "on_mouse_leave": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button."
    },
    "on_mouse_move": {
        "description": "Function or event handler called when the user moves the mouse over an element. For example, it’s called when the user moves the mouse over a button."
    },
    "on_mouse_out": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button."
    },
    "on_mouse_over": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button."
    },
    "on_scroll": {
        "description": "Function or event handler called when the user scrolls the page. For example, it is called when the user scrolls the page down."
    },
    "on_submit": {
        "description": "Function or event handler called when the user submits a form. For example, it is called when the user clicks on a submit button."
    },
    "on_cancel": {
        "description": "Function or event handler called when the user cancels a form. For example, it is called when the user clicks on a cancel button."
    },
    "on_edit": {
        "description": "Function or event handler called when the user edits a form. For example, it is called when the user clicks on a edit button."
    },
    "on_change_start": {
        "description": "Function or event handler called when the user starts selecting a new value(By dragging or clicking)."
    },
    "on_change_end": {
        "description": "Function or event handler called when the user is done selecting a new value(By dragging or clicking)."
    },
    "on_complete": {
        "description": "Called when the user completes a form. For example, it’s called when the user clicks on a complete button."
    },
    "on_error": {
        "description": "The on_error event handler is called when the user encounters an error in a form. For example, it’s called when the user clicks on a error button."
    },
    "on_load": {
        "description": "The on_load event handler is called when the user loads a form. For example, it is called when the user clicks on a load button."
    },
    "on_esc": {
        "description": "The on_esc event handler is called when the user presses the escape key. For example, it is called when the user presses the escape key."
    },
    "on_open": {
        "description": "The on_open event handler is called when the user opens a form. For example, it is called when the user clicks on a open button."
    },
    "on_close": {
        "description": "The on_close event handler is called when the user closes a form. For example, it is called when the user clicks on a close button."
    },
    "on_close_complete": {
        "description": "The on_close_complete event handler is called when the user closes a form. For example, it is called when the user clicks on a close complete button."
    },
    "on_overlay_click": {
        "description": "The on_overlay_click event handler is called when the user clicks on an overlay. For example, it is called when the user clicks on a overlay button."
    },
    "on_key_down": {
        "description": "The on_key_down event handler is called when the user presses a key."
    },
    "on_key_up": {
        "description": "The on_key_up event handler is called when the user releases a key."
    },
    "on_ready": {
        "description": "The on_ready event handler is called when the script is ready to be executed."
    },
    "on_mount": {
        "description": "The on_mount event handler is called when the component is loaded on the page."
    },
    "on_unmount": {
        "description": "The on_unmount event handler is called when the component is removed from the page. This handler is only called during navigation, not when the page is refreshed."
    },
    "on_input": {
        "description": "The on_input event handler is called when the editor receives input from the user. It receives the raw browser event as an argument.",
    },
    "on_resize_editor": {
        "description": "The on_resize_editor event handler is called when the editor is resized. It receives the height and previous height as arguments.",
    },
    "on_copy": {
        "description": "The on_copy event handler is called when the user copies text from the editor. It receives the clipboard data as an argument.",
    },
    "on_cut": {
        "description": "The on_cut event handler is called when the user cuts text from the editor. It receives the clipboard data as an argument.",
    },
    "on_paste": {
        "description": "The on_paste event handler is called when the user pastes text into the editor. It receives the clipboard data and max character count as arguments.",
    },
    "toggle_code_view": {
        "description": "The toggle_code_view event handler is called when the user toggles code view. It receives a boolean whether code view is active.",
    },
    "toggle_full_screen": {
        "description": "The toggle_full_screen event handler is called when the user toggles full screen. It receives a boolean whether full screen is active.",
    },
    "on_cell_activated": {
        "description": "The on_cell_activated event handler is called when the user activate a cell from the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_clicked": {
        "description": "The on_cell_clicked event handler is called when the user click on a cell of the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_context_menu": {
        "description": "The on_cell_context_menu event handler is called when the user right-click on a cell of the data editor. It receives the coordinates of the cell.",
    },
    "on_cell_edited": {
        "description": "The on_cell_edited event handler is called when the user modify the content of a cell. It receives the coordinates of the cell and the modified content.",
    },
    "on_group_header_clicked": {
        "description": "The on_group_header_clicked event handler is called when the user left-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_context_menu": {
        "description": "The on_group_header_context_menu event handler is called when the user right-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_renamed": {
        "description": "The on_group_header_context_menu event handler is called when the user rename a group header of the data editor. It receive the index and the modified content of the group header.",
    },
    "on_header_clicked": {
        "description": "The on_header_clicked event handler is called when the user left-click a header of the data editor. It receive the index and the content of the header.",
    },
    "on_header_context_menu": {
        "description": "The on_header_context_menu event handler is called when the user right-click a header of the data editor. It receives the index and the content of the header. ",
    },
    "on_header_menu_click": {
        "description": "The on_header_menu_click event handler is called when the user click on the menu button of the header. (menu header not implemented yet)",
    },
    "on_item_hovered": {
        "description": "The on_item_hovered event handler is called when the user hover on an item of the data editor.",
    },
    "on_delete": {
        "description": "The on_delete event handler is called when the user delete a cell of the data editor.",
    },
    "on_finished_editing": {
        "description": "The on_finished_editing event handler is called when the user finish an editing, regardless of if the value changed or not.",
    },
    "on_row_appended": {
        "description": "The on_row_appended event handler is called when the user add a row to the data editor.",
    },
    "on_selection_cleared": {
        "description": "The on_selection_cleared event handler is called when the user unselect a region of the data editor.",
    },
    "on_column_resize": {
        "description": "The on_column_resize event handler is called when the user try to resize a column from the data editor."
    },
    "on_checked_change": {
        "description": "The on_checked_change event handler is called when the checked state of the checkbox changes."
    },
    "on_open_change": {
        "description": "The on_open_change event handler is called when the open state of the component changes."
    },
    "on_focus_outside": {
        "description": "The on_focus_outside event handler is called when the user focuses outside the component."
    },
    "on_interact_outside": {
        "description": "The on_interact_outside event handler is called when the user interacts outside the component."
    },
    "on_open_auto_focus": {
        "description": "The on_open_auto_focus event handler is called when the component opens and the focus is returned to the first item."
    },
    "on_value_change": {
        "description": "The on_value_change event handler is called when the value state of the component changes."
    },
    "on_close_auto_focus": {
        "description": "The on_close_auto_focus event handler is called when focus moves to the trigger after closing. It can be prevented by calling event.preventDefault."
    },
    "on_escape_key_down": {
        "description": "The on_escape_key_down event handler is called when the escape key is down. It can be prevented by calling event.preventDefault."
    },
    "on_pointer_down_outside": {
        "description": "The on_pointer_down_outside event handler is called when a pointer event occurs outside the bounds of the component. It can be prevented by calling event.preventDefault."
    },
    "on_value_commit": {
        "description": "The on_value_commit event handler is called when the value changes at the end of an interaction. Useful when you only need to capture a final value e.g. to update a backend service."
    },
    "on_clear_server_errors": {
        "description": "The on_clear_server_errors event handler is called when the form is submitted or reset and the server errors need to be cleared."
    },
}


from reflex.components.radix import themes as rdxt

def generate_props(src, component):
    if len(src.get_props()) == 0:
        return rx.vstack(
            rx.heading("Props", font_size="1em"),
            rx.text("No component specific props"),
            width="100%",
            overflow_x="auto",
            align_items="left",
            padding_y=".5em",
        )

    prop_dict = {}
    body = rdxt.table_body(
        *[rdxt.table_row(*prop_docs(prop, prop_dict, component)) for prop in src.get_props()]
    )
    try:
        comp = component.create("Test", **prop_dict)
        if "data" in component.__name__.lower():
            raise Exception("Data components cannot be created")
    except:
        print(f"Failed to create component {component.__name__}")
        comp = rx.fragment()

    return rx.vstack(
        comp,
        rdxt.table_root(
            rdxt.table_header(
                rdxt.table_row(
                    rdxt.table_column_header_cell("Prop", padding_left="0"),
                    rdxt.table_column_header_cell("Type", padding_left="0"),
                    rdxt.table_column_header_cell("Description/Values", padding_left="0"),
                )
            ),
            body,
            width="100%",
            padding_x="0",
            size="1",
        ),
        align_items="left",
        padding_bottom="2em",
    )


# Default event triggers.
default_triggers = rx.Component.create().get_event_triggers()


import inspect


def same_trigger(t1, t2):
    if t1 is None or t2 is None:
        return False
    args1 = inspect.getfullargspec(t1).args
    args2 = inspect.getfullargspec(t2).args
    return args1 == args2


def generate_event_triggers(comp):
    triggers = comp().get_event_triggers()
    custom_events = [
        event
        for event in triggers
        if event != "on_drop"
        and not same_trigger(triggers.get(event), default_triggers.get(event))
    ]

    if not custom_events:
        return rx.vstack(
            rx.heading("Event Triggers", font_size="1em"),
            rx.text("No component specific event triggers"),
            width="100%",
            overflow_x="auto",
            align_items="left",
            padding_y=".5em",
        )

    return rx.vstack(
        rx.heading("Event Triggers", font_size="1em"),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Trigger", padding_left="0"),
                    rx.th("Description", padding_left="0"),
                )
            ),
            rx.tbody(
                *[
                    rx.tr(
                        rx.td(rx.code(event), padding_left="0"),
                        rx.td(rx.text(EVENTS[event]["description"])),
                    )
                    for event in custom_events
                ]
            ),
            width="100%",
        ),
        width="100%",
        overflow_x="auto",
        align_items="left",
    )


def generate_valid_children(comp):
    if not comp._valid_children:
        return rx.text("")

    valid_children = [rx.wrap_item(rx.code(child)) for child in comp._valid_children]
    return rx.vstack(
        rx.heading("Valid Children", font_size="1em"),
        rx.wrap(*valid_children),
        width="100%",
        align_items="left",
        padding_y=".5em",
    )


def component_docs(component):
    """Generates documentation for a given component."""
    src = Source(component=component)
    props = generate_props(src, component)
    triggers = generate_event_triggers(component)
    children = generate_valid_children(component)

    return rx.box(
        rx.heading(component.__name__, font_size="2em"),
        rx.divider(),
        rx.box(markdown(src.get_docs()), padding_bottom="1em"),
        props,
        children,
        triggers,
        text_align="left",
        width="100%",
        padding_bottom="2em",
    )


tab_style = {
    "font_size": "1em",
    "font_weight": "500",
    "padding_x": ".5em",
    "color": "#696287",
}
tab_selected_style = {
    "color": "#5646ED",
    "bg": "#F5EFFE",
    "font_size": "1em",
    "font_weight": "500",
    "padding_x": ".5em",
    "padding_y": ".10em",
    "border_radius": "8px",
}


def multi_docs(path, comp, component_list, title):
    @docpage(set_path=path, t=title)
    def out():
        components = [component_docs(component) for component in component_list[1:]]
        fname = path.strip("/") + ".md"
        style_doc_exists = os.path.exists(fname.replace(".md", "-style.md"))
        ll_doc_exists = os.path.exists(
            fname.replace("radix/", "").replace(".md", "-ll.md")
        )

        return rx.box(
            rx.box(
                rx.box(
                    rx.tabs(
                        rx.tab_list(
                            rx.spacer(),
                            rx.tab(
                                "High Level API",
                                _selected=tab_selected_style,
                                style=tab_style,
                            ),
                            rx.tab(
                                "Low Level API",
                                _selected=tab_selected_style,
                                style=tab_style,
                            )
                            if ll_doc_exists
                            else "",
                            rx.tab(
                                "Styling", _selected=tab_selected_style, style=tab_style
                            )
                            if style_doc_exists
                            else "",
                            rx.tab(
                                "Props", _selected=tab_selected_style, style=tab_style
                            ),
                            width="100%",
                            padding_bottom="1em",
                        ),
                        rx.tab_panels(
                            rx.tab_panel(xd.render(comp, filename=fname)),
                            rx.tab_panel(
                                xd.render_file(
                                    fname.replace("radix/", "").replace(".md", "-ll.md")
                                )
                            )
                            if ll_doc_exists
                            else "",
                            rx.tab_panel(
                                xd.render_file(fname.replace(".md", "-style.md"))
                            )
                            if style_doc_exists
                            else "",
                            rx.tab_panel(rx.vstack(*components)),
                        ),
                        variant="unstyled",
                        default_index=1 if "only_low_level" in comp.metadata else 0,
                    ),
                    padding_y="1em",
                ),
            ),
        )

    return out
