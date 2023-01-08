"""Utility functions for the component docs page."""

import inspect
import os
import re
from typing import Any, Type

import pynecone as pc
from pynecone.base import Base
from pynecone.components.component import Component

from pcweb.component_list import component_list
from pcweb.components.sidebar import SidebarItem
from pcweb.pages.docs.component_lib import *
from pcweb.templates.docpage import docheader, docpage, subheader


class Prop(Base):
    """Hold information about a prop."""

    # The name of the prop.
    name: str

    # The type of the prop.
    type_: Any

    # The description of the prop.
    description: str


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
            for line in inspect.getsource(self.component).split(os.linesep)
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
        # The output.
        out = []

        # Get the props for this component.
        props = self.component.get_props()

        # Loop through the source code.
        for i, line in enumerate(self.code):
            # Check if we've reached the functions.
            reached_functions = re.search("def ", line)
            if reached_functions:
                # We've reached the functions, so stop.
                break

            # Check if this line has a prop.
            match = re.search("\w+:", line)
            if match is None:
                # This line doesn't have a var, so continue.
                continue

            # Get the prop.
            prop = match.group(0).strip(":")
            if prop not in props:
                # This isn't a prop, so continue.
                continue

            # Get the comment for this prop.
            comment = self.code[i - 1].strip()
            assert comment.startswith("#"), f"Expected comment, got {comment}"
            comment = comment[1:].strip()

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


def prop_docs(prop: Prop) -> list[pc.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if pc.utils._issubclass(prop.type_, pc.Var):
        # For vars, get the type of the var.
        type_ = pc.utils.get_args(type_)[0]
    type_ = type_.__name__

    # Get the color of the prop.
    color = TYPE_COLORS.get(type_, "gray")

    # Return the docs for the prop.
    return [
        pc.td(pc.code(prop.name, color="#333")),
        pc.td(pc.badge(type_, color_scheme=color, variant="solid")),
        pc.td(pc.markdown(prop.description)),
    ]


def get_examples(component: str) -> pc.Component:
    return eval(f"render_{component.lower()}()")


EVENTS = {
    "on_focus": {
        "description": "Called when the element (or some element inside of it) receives focus. For example, it’s called when the user clicks on a text input."
    },
    "on_blur": {
        "description": "Called when focus has left the element (or left some element inside of it). For example, it’s called when the user clicks outside of a focused text input."
    },
    "on_change": {
        "description": "Called when the value of an element has changed. For example, it’s called when the user types into a text input each keystoke triggers the on change."
    },
    "on_click": {
        "description": "Called when the user clicks on an element. For example, it’s called when the user clicks on a button."
    },
    "on_context_menu": {
        "description": "Called when the user right-clicks on an element. For example, it’s called when the user right-clicks on a button."
    },
    "on_double_click": {
        "description": "Called when the user double-clicks on an element. For example, it’s called when the user double-clicks on a button."
    },
    "on_mouse_up": {
        "description": "Called when the user releases a mouse button on an element. For example, it’s called when the user releases the left mouse button on a button."
    },
    "on_mouse_down": {
        "description": "Called when the user presses a mouse button on an element. For example, it’s called when the user presses the left mouse button on a button."
    },
    "on_mouse_enter": {
        "description": "Called when the user’s mouse enters an element. For example, it’s called when the user’s mouse enters a button."
    },
    "on_mouse_leave": {
        "description": "Called when the user’s mouse leaves an element. For example, it’s called when the user’s mouse leaves a button."
    },
    "on_mouse_move": {
        "description": "Called when the user moves the mouse over an element. For example, it’s called when the user moves the mouse over a button."
    },
    "on_mouse_out": {
        "description": "Called when the user’s mouse leaves an element. For example, it’s called when the user’s mouse leaves a button."
    },
    "on_mouse_over": {
        "description": "Called when the user’s mouse enters an element. For example, it’s called when the user’s mouse enters a button."
    },
    "on_scroll": {
        "description": "Called when the user scrolls the page. For example, it’s called when the user scrolls the page down."
    },
    "on_submit": {
        "description": "Called when the user submits a form. For example, it’s called when the user clicks on a submit button."
    },
    "on_cancel": {
        "description": "Called when the user cancels a form. For example, it’s called when the user clicks on a cancel button."
    },
    "on_edit": {
        "description": "Called when the user edits a form. For example, it’s called when the user clicks on a edit button."
    },
    "on_change_start": {
        "description": "Called when the user starts to change a form. For example, it’s called when the user clicks on a change start button."
    },
    "on_change_end": {
        "description": "Called when the user ends to change a form. For example, it’s called when the user clicks on a change end button."
    },
    "on_complete": {
        "description": "Called when the user completes a form. For example, it’s called when the user clicks on a complete button."
    },
    "on_error": {
        "description": "The on_error event handler is called when the user encounters an error in a form. For example, it’s called when the user clicks on a error button."
    },
    "on_load": {
        "description": "The on_load event handler is called when the user loads a form. For example, it’s called when the user clicks on a load button."
    },
    "on_esc": {
        "description": "The on_esc event handler is called when the user presses the escape key. For example, it’s called when the user presses the escape key."
    },
    "on_open": {
        "description": "The on_open event handler is called when the user opens a form. For example, it’s called when the user clicks on a open button."
    },
    "on_close": {
        "description": "The on_close event handler is called when the user closes a form. For example, it’s called when the user clicks on a close button."
    },
    "on_close_complete": {
        "description": "The on_close_complete event handler is called when the user closes a form. For example, it’s called when the user clicks on a close complete button."
    },
    "on_overlay_click": {
        "description": "The on_overlay_click event handler is called when the user clicks on an overlay. For example, it’s called when the user clicks on a overlay button."
    },
}

# Docs page
def component_docs(component):
    src = Source(component=component)
    props = []

    if len(src.get_props()) > 0:
        props = [
            subheader("Props"),
            pc.box(
                pc.table(
                    pc.thead(
                        pc.tr(
                            pc.th("Prop"),
                            pc.th("Type"),
                            pc.th("Description"),
                        )
                    ),
                    pc.tbody(*[pc.tr(*prop_docs(prop)) for prop in src.get_props()]),
                ),
                background_color="rgb(255, 255, 255)",
                border_radius="1em",
                box_shadow="rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
                padding="1em",
                max_width="100%",
                overflow_x="auto",
            ),
        ]
    else:
        props = [
            subheader("Props"),
            pc.box(
                pc.unordered_list(
                    pc.list_item(
                        pc.heading(
                            f"No props for {component.__name__}.", font_size="1em"
                        )
                    )
                ),
                padding_x="1em",
                max_width="100%",
                overflow_x="auto",
            ),
        ]

    triggers = []

    triggers = [
        subheader("Event Triggers"),
        pc.box(
            pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(
                        pc.accordion_icon(),
                        pc.heading("Base Events Triggers", font_size="1em"),
                    ),
                    pc.accordion_panel(
                        pc.text(
                            "These triggers are available for all Pynecone components. "
                            "They take in no arguments. ",
                            margin_bottom="1em",
                        ),
                        *[
                            pc.accordion_item(
                                pc.accordion_button(
                                    pc.accordion_icon(),
                                    pc.code(event),
                                ),
                                pc.accordion_panel(
                                    pc.text(
                                        EVENTS[event].get(
                                            "description",
                                        )
                                    )
                                ),
                            )
                            for event in component.get_triggers()
                            if event in pc.event.EVENT_TRIGGERS
                        ],
                    ),
                ),
                *[
                    pc.accordion_item(
                        pc.accordion_button(
                            pc.code(event),
                            pc.accordion_icon(),
                        ),
                        pc.accordion_panel(pc.text(EVENTS[event]["description"])),
                    )
                    for event in component.get_triggers()
                    if event not in pc.event.EVENT_TRIGGERS
                ],
                border_color="rgb(255, 255, 255)",
                allow_multiple=True,
            ),
            background_color="rgb(255, 255, 255)",
            border_radius="1em",
            box_shadow="rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
            padding="1em",
            max_width="100%",
            overflow_x="auto",
        ),
    ]
    return pc.box(
        docheader(component.__name__),
        pc.markdown(src.get_docs()),
        *props,
        *triggers,
        text_align="left",
    )


sidebar_items = [
    SidebarItem(
        name=category,
        children=[
            SidebarItem(
                name=c[0].__name__,
            )
            for c in component_list[category]
        ],
    )
    for category in component_list
]


def multi_docs(path, component_list):
    components = [component_docs(component) for component in component_list]

    @docpage(set_path=path)
    def out():
        return pc.box(
            pc.box(
                pc.box(
                    docheader(
                        component_list[0].__name__,
                        first=True,
                    ),
                    get_examples(component_list[0].__name__),
                    text_align="left",
                ),
                *components,
            ),
        )

    return out
