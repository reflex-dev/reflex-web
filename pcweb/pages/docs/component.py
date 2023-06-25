"""Utility functions for the component docs page."""

import inspect
import re
from typing import Any, Type

from pynecone.base import Base
from pynecone.components.component import Component

from pcweb.component_list import component_list, not_ready_components
from pcweb.components.sidebar import SidebarItem
from pcweb.pages.docs.component_lib import *
from pcweb.templates.docpage import docheader, docpage, subheader
from pcweb import constants, styles

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
            match = re.search("\w+:", line)
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


def prop_docs(prop: Prop) -> list[pc.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if pc.utils.types._issubclass(prop.type_, pc.Var):
        # For vars, get the type of the var.
        type_ = pc.utils.types.get_args(type_)[0]
    try:
        type_ = type_.__name__
    except AttributeError:
        print(type_)

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
    "on_copy": {
        "description": "The on_copy event handler is called in CopyToClipboard component"
    },
}


# Docs page
def component_docs(component):
    src = Source(component=component)
    props = []

    if len(src.get_props()) > 0:
        props = [
            pc.accordion(
                pc.accordion_item(
                pc.accordion_button(pc.accordion_icon(), pc.heading("Props", font_size="1em")),
                pc.accordion_panel(pc.box(
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
                    box_shadow=styles.DOC_SHADOW_LIGHT,
                    padding="1em",
                    max_width="100%",
                    overflow_x="auto",
                )
                )
                ),
                border_color="rgb(255, 255, 255)",
                width = "100%",
                allow_toggle = True
            )
        ]
    else:
        props = [
            pc.box(
                pc.unordered_list(
                    pc.list_item(
                        pc.heading(
                            f"No props for {component.__name__}.", font_size="1em"
                        )
                    )
                ),
                padding_x="1.5em",
                max_width="100%",
                overflow_x="auto",
            ),
        ]

    triggers = []

    trig = []
    for event in component().get_triggers():
        if event not in pc.event.EVENT_TRIGGERS and event not in ("on_drop",):
            trig.append(event)

    if trig:
        specific_triggers = pc.accordion_item(
                            pc.accordion_button(pc.accordion_icon(), pc.heading("Component Specific Triggers", font_size="1em")),
                            pc.accordion_panel(
                                *[
                                    pc.accordion_item(
                                        pc.accordion_button(
                                            pc.accordion_icon(),
                                            pc.code(event),
                                        ),
                                        pc.accordion_panel(pc.text(EVENTS[event]["description"])),
                                    )
                                    for event in component().get_triggers()
                                    if event not in pc.event.EVENT_TRIGGERS
                                    and event not in ("on_drop",)
                                ],
                            ),
                            border_color="rgb(255, 255, 255)",
                        )
        
        component_specific_triggers =  pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(pc.accordion_icon(), pc.heading("Event Triggers", font_size="1em")),
                    pc.accordion_panel(
                        pc.accordion_item(
                            pc.accordion_button(
                                pc.link(
                                    pc.hstack(pc.icon(tag="link"), 
                                    pc.heading("Base Event Triggers", font_size="1em")), 
                                    href="/docs/api-reference/event-triggers"
                                )
                            ),
                            border_color="rgb(255, 255, 255)",
                        ),
                        specific_triggers
                    ),
                ),
                border_color="rgb(255, 255, 255)",
                allow_multiple=True,
                width = "100%",
                align_items = "left"
            )
                        
    else:
        component_specific_triggers = pc.box(
                pc.unordered_list(
                    pc.list_item(
                        pc.heading("Base Event Triggers", font_size="1em")
                    )
                ),
                padding_top  = "1.5em",
                padding_x="1.5em",
                max_width="100%",
                overflow_x="auto",
            )

    triggers = [
        pc.box(
            component_specific_triggers,
            max_width="100%",
            overflow_x="auto",
        ),
    ]

    return pc.box(
        docheader(component.__name__),
        pc.markdown(src.get_docs()),
        pc.divider(),
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
    coming_soon_components = [c.__name__ for c in not_ready_components]

    @docpage(set_path=path)
    def out():
        name = component_list[0].__name__
        return pc.box(
            pc.box(
                pc.box(
                    docheader(
                        name, first=True, coming_soon=name in coming_soon_components
                    ),
                    get_examples(name),
                    text_align="left",
                ),
                *components,
            ),
        )

    return out
