"""Utility functions for the component docs page."""

import inspect
import os
import re
from typing import Any, Type, get_args, Literal, _GenericAlias

import reflex as rx
import flexdown
import textwrap

from pcweb.flexdown import markdown, xd
from pcweb.templates.docpage import docpage, get_toc, h1_comp, h2_comp, docdemobox
from reflex.base import Base
from reflex.components.component import Component
from reflex.components.radix.primitives.base import RadixPrimitiveComponent
from reflex.components.radix.themes.base import RadixThemesComponent
from reflex.components.base.fragment import Fragment


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
    "Literal": "ruby",
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


class PropDocsState(rx.State):
    """Container for dynamic vars used by the prop docs."""

EXCLUDED_COMPONENTS = [
    "Theme",
    "ThemePanel",
    "DrawerRoot",
    "DrawerTrigger",
    "DrawerOverlay",
    "DrawerPortal",
    "DrawerContent",
    "DrawerClose",
]

def render_select(prop, component, prop_dict):
    if not rx.utils.types._issubclass(
        component, (RadixThemesComponent, RadixPrimitiveComponent)
    ) or component.__name__ in EXCLUDED_COMPONENTS:
        return rx.fragment()
    try:
        type_ = rx.utils.types.get_args(prop.type_)[0]
    except:
        return rx.fragment()

    try:
        if issubclass(type_, bool) and prop.name not in [
            "open",
            "checked",
            "as_child",
            "default_open",
            "default_checked",
        ]:
            name = get_id(f"{component.__qualname__}_{prop.name}")
            PropDocsState.add_var(name, bool, False)
            var = getattr(PropDocsState, name)
            setter = getattr(PropDocsState, f"set_{name}")
            prop_dict[prop.name] = var
            return rx.checkbox(
                var,
                on_change=setter,
            )
    except TypeError:
        pass

    if not isinstance(type_, _GenericAlias) or type_.__origin__ is not Literal:
        return rx.fragment()
    # Get the first option.
    option = type_.__args__[0]
    name = get_id(f"{component.__qualname__}_{prop.name}")
    PropDocsState.add_var(name, str, option)
    var = getattr(PropDocsState, name)
    setter = getattr(PropDocsState, f"set_{name}")
    prop_dict[prop.name] = var

    return rx.select.root(
        rx.select.trigger(width="8em"),
        rx.select.content(
            rx.select.group(
                *[
                    rx.select.item(
                        item,
                        value=item,
                        _hover={"background": f"var(--{item}-9)"}
                        if prop.name == "color_scheme"
                        else None,
                    )
                    for item in list(map(str, type_.__args__))
                ]
            ),
        ),
        value=var,
        on_change=setter,
    )


def prop_docs(prop: Prop, prop_dict, component) -> list[rx.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if rx.utils.types._issubclass(prop.type_, rx.Var):
        # For vars, get the type of the var.
        type_ = rx.utils.types.get_args(type_)[0]
    type_ = type_.__name__

    # Get the color of the prop.
    color = TYPE_COLORS.get(type_, "gray")

    # Return the docs for the prop.
    return [
        rx.table.cell(rx.code(prop.name), padding_left="1em", justify="start"),
        rx.table.cell(
            rx.badge(type_, color_scheme=color, variant="solid"),
            padding_left="1em",
            justify="start",
        ),
        rx.table.cell(markdown(prop.description), padding_left="1em", justify="start"),
        rx.table.cell(render_select(prop, component, prop_dict), padding_left="1em", justify="start"),
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
    "on_change": {
        "description": "The on_change event handler is called when the value or checked state of the component changes."
    },
    "on_value_change": {
        "description": "The on_change event handler is called when the value state of the component changes."
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
    "on_select": {
        "description": "The on_select event handler is called when the user selects an item."
    },
    "on_drop": {
        "description": "The on_drop event handler is called when the user drops an item."
    },
}


from reflex.components.radix import themes as rdxt


def generate_props(src, component, comp):
    if len(src.get_props()) == 0:
        return rx.vstack(
            rx.heading("Props", font_size="1em"),
            rx.text("No component specific props"),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )

    padding_left = "1em"

    prop_dict = {}
    body = rx.table.body(
        *[
            rx.table.row(*prop_docs(prop, prop_dict, component), align="center")
            for prop in src.get_props()
            if not prop.name.startswith("on_")  # ignore event trigger props
        ]
    )
    try:
        if f"{component.__name__}" in comp.metadata:
            comp = eval(comp.metadata[component.__name__])(**prop_dict)

        elif not rx.utils.types._issubclass(
            component, (RadixThemesComponent, RadixPrimitiveComponent)
        ) or component.__name__ in [
            "Theme",
            "ThemePanel",
            "DrawerRoot",
            "DrawerTrigger",
            "DrawerOverlay",
            "DrawerPortal",
            "DrawerContent",
            "DrawerClose",
        ]:
            comp = rx.fragment()

        else:
            try:
                comp = rx.vstack(component.create("Test", **prop_dict))
            except:
                comp = rx.fragment()
            if "data" in component.__name__.lower():
                raise Exception("Data components cannot be created")
    except Exception as e:
        print(f"Failed to create component {component.__name__}, error: {e}")
        comp = rx.fragment()

    return rx.vstack(
        docdemobox(comp) if not isinstance(comp, Fragment) else "",
        rx.scroll_area(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(
                            "Prop", padding_left=padding_left, justify="start"
                        ),
                        rx.table.column_header_cell(
                            "Type", padding_left=padding_left, justify="start"
                        ),
                        rx.table.column_header_cell(
                            "Description",
                            padding_left=padding_left,
                            justify="start",
                            width="40%",
                        ),
                        rx.table.column_header_cell(
                            "Values", padding_left=padding_left, justify="start"
                        ),
                    )
                ),
                body,
                width="100%",
                padding_x="0",
                size="1",
            ),
            max_height="20em",
        ),
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


def generate_event_triggers(comp, src):
    prop_name_to_description = {
        prop.name: prop.description for prop in src.get_props()
        if prop.name.startswith("on_")
    }
    triggers = comp().get_event_triggers()
    custom_events = [
        event
        for event in triggers
        if not same_trigger(triggers.get(event), default_triggers.get(event))
    ]

    if not custom_events:
        return rx.vstack(
            rx.heading("Event Triggers", font_size="1em"),
            rx.link(
                "See the full list of default event triggers",
                href="https://reflex.dev/docs/api-reference/event-triggers/",
                underline="hover",
                is_external=True,
            ),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )

    padding_left = "1em"

    return rx.vstack(
        rx.heading("Event Triggers", font_size="1em"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(
                        "Trigger", padding_left=padding_left, justify="start"
                    ),
                    rx.table.column_header_cell(
                        "Description", padding_left=padding_left, justify="start"
                    ),
                ),
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(
                            rx.code(event), padding_left=padding_left, justify="start"
                        ),
                        rx.table.cell(
                            rx.text(prop_name_to_description.get(event) or EVENTS[event]["description"]),
                            padding_left=padding_left,
                            justify="start",
                        ),
                    )
                    for event in custom_events
                ]
            ),
            width="100%",
        ),
        width="100%",
        overflow_x="auto",
        align_items="start",
        padding_top="2em",
    )


def generate_valid_children(comp):
    if not comp._valid_children:
        return rx.text("")

    valid_children = [
        rx.chakra.wrap_item(rx.code(child)) for child in comp._valid_children
    ]
    return rx.vstack(
        rx.heading("Valid Children", font_size="1em"),
        rx.chakra.wrap(*valid_children),
        width="100%",
        align_items="start",
        padding_y=".5em",
    )


def component_docs(component, comp):
    """Generates documentation for a given component."""
    src = Source(component=component)
    props = generate_props(src, component, comp)
    triggers = generate_event_triggers(component, src)
    children = generate_valid_children(component)

    return rx.box(
        h2_comp(text=component.__name__),
        rx.box(markdown(textwrap.dedent(src.get_docs())), padding_bottom=".5em"),
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
    components = [component_docs(component, comp) for component in component_list[1:]]

    fname = path.strip("/") + ".md"
    ll_doc_exists = os.path.exists(fname.replace(".md", "-ll.md"))

    non_active_style = {
        "padding": ".5em",
        "color": rx.color("mauve", 9),
        "width": "7em",
    }

    active_style = {
        "padding": ".5em",
        "background": rx.color("mauve", 1),
        "color": rx.color("mauve", 12),
        "box_shadow": "0px 4px 4px -4px rgba(194, 198, 215, 0.30), 0px 1px 4px -1px rgba(135, 144, 181, 0.40);",
        "border_radius": "8px",
        "width": "7em",
    }

    def links(current_page, ll_doc_exists, path):
        if ll_doc_exists:
            if current_page == "hl":
                return rx.flex(
                    rx.box(flex_grow="1"),
                    rx.flex(
                        rx.link(rx.center(rx.text("High Level"), style=active_style)),
                        rx.link(
                            rx.center(rx.text("Low Level"), style=non_active_style),
                            href=path + "/low",
                        ),
                        spacing="2",
                        padding=".5em",
                        background=rx.color("mauve", 2),
                        border_radius="8px",
                        align_items="center",
                        justify_items="center",
                    ),
                    margin_bottom=".5em",
                )
            else:
                return rx.flex(
                    rx.box(flex_grow="1"),
                    rx.flex(
                        rx.link(
                            rx.center(rx.text("High Level"), style=non_active_style),
                            href=path,
                        ),
                        rx.link(rx.center(rx.text("Low Level"), style=active_style)),
                        spacing="2",
                        padding=".5em",
                        background=rx.color("mauve", 2),
                        border_radius="8px",
                        align_items="center",
                        justify_items="center",
                    ),
                    margin_bottom=".5em",
                )
        return rx.fragment()

    @docpage(set_path=path, t=title)
    def out():
        toc = get_toc(comp, fname, component_list)
        return toc, rx.flex(
            links("hl", ll_doc_exists, path),
            xd.render(comp, filename=fname),
            h1_comp(text="API Reference"),
            rx.vstack(*components),
            direction="column",
            width="100%",
        )

    @docpage(set_path=path + "/low", t=title)
    def ll():
        nonlocal fname
        fname = fname.replace(".md", "-ll.md")
        d2 = flexdown.parse_file(fname)
        toc = get_toc(d2, fname, component_list)
        return toc, rx.flex(
            links("ll", ll_doc_exists, path),
            xd.render_file(fname),
            h1_comp(text="API Reference"),
            rx.vstack(*components),
            direction="column",
            width="100%",
        )

    if ll_doc_exists:
        return (out, ll)
    else:
        return out
