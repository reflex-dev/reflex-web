import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    definition,
    docalert,
    docdemo,
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code1 = """
from typing import List

class ExampleState(State):

    # A base var for the list of colors to cycle through.
    colors: List[str] = ["black", "red", "green", "blue", "purple"]

    # A base var for the index of the current color.
    index: int = 0

    def next_color(self):
        \"""An event handler to go to the next color.\"""
        # Event handlers can modify the base vars.
        # Here we reference the base vars `colors` and `index`.
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self)-> str:
        \"""A computed var that returns the current color.\"""
        # Computed vars update automatically when the state changes.
        return self.colors[self.index]
"""
exec(code1)

code2 = """rx.heading(
    "Welcome to Reflex!",
    # Event handlers can be bound to event triggers.
    on_click=ExampleState.next_color,
    # State vars can be bound to component props.
    color=ExampleState.color,
    _hover={"cursor": "pointer"},
)
"""


@docpage()
def state_overview():
    return rx.box(
        docheader("State", first=True),
        doctext(
            "State allows us to create interactive apps that can respond to user input. ",
            "It defines the variables that can change over time, and the functions that can modify them. ",
        ),
        subheader("State Basics"),
        doctext(
            "The base state is defined as a class that inherits from ",
            rx.code("rx.State"),
            ". ",
        ),
        doccode(
        """
        import reflex as rx
        class State(rx.State):
            \"""Define your app state here.\"""
"""
        ),
        doctext(
            "State is made up of two parts: vars and event handlers. ",
        ),
        doctext(
            rx.span("Vars", font_weight="bold"),
            " are variables in your app that can change over time. ",
            rx.span("Event handlers", font_weight="bold"),
            " are functions that modify these vars in response to events. ",
        ),
        doctext("These are the main concepts to understand how state works in Reflex."),
        rx.responsive_grid(
            definition(
                "Base Var",
                rx.unordered_list(
                    rx.list_item("Any variable in your app that can change over time."),
                    rx.list_item("Defined as a field in the ", rx.code("State"), " class"),
                    rx.list_item("Can only be modified by event handlers."),
                ),
            ),
            definition(
                "Computed Var",
                rx.unordered_list(
                    rx.list_item("Vars that change automatically based on other vars."),
                    rx.list_item("Defined as functions using the ", rx.code("@rx.var"), " decorator."),
                    rx.list_item("Cannot be set by event handlers, are always recomputed when the state changes."),
                ),
            ),
            definition(
                "Event Trigger",
                rx.unordered_list(
                    rx.list_item("A user interaction that triggers an event, such as a button click."),
                    rx.list_item("Defined as special component props, such as ", rx.code("on_click"), "."),
                    rx.list_item("Can be used to trigger event handlers.")
                ),
            ),
            definition(
                "Event Handlers",
                rx.unordered_list(
                    rx.list_item(
                        "Functions that update the state in response to events."
                    ),
                    rx.list_item(
                        "Defined as methods in the ", rx.code("State"), " class."
                    ),
                    rx.list_item(
                        "Can be called by event triggers, or by other event handlers."
                    ),
                ),
            ),
            margin_bottom="1em",
            spacing="1em",
            columns=[1, 1, 2, 2, 2],
        ),
        subheader("Example"),
        doctext(
            "Here is a example of how to use state within a Reflex app. ",
            "Click the text to change its color.",
        ),
        docdemo(code2, code1, eval(code2), context=True),
        doctext(
            "The base vars are ",
            rx.code("colors"),
            " and ",
            rx.code("index"),
            ". They are the only vars in the app that may be directly modified within event handlers.",
        ),
        doctext(
            "There is a single computed var, ",
            rx.code("color"),
            ", that is a function of the base vars. ",
            "It will be computed automatically whenever the base vars change. ",
        ),
        doctext(
            "The heading component links its ",
            rx.code("on_click"),
            " event to the ",
            rx.code("ExampleState.next_color"),
            " event handler, which increments the color index.",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("With Reflex, you never have to write an API."),
                    rx.alert_description(
                        "All interactions between the frontend and backend are handled through events. "
                    ),
                ),
                status="success",
            ),
        ),
        subheader("Client States"),
        doctext(
            "Each user who opens your app has a unique ID and their own copy of the state. ",
            "This means that each user can interact with the app and modify the state "
            "independently of other users. ",
        ),
        docalert(
            "Try opening an app in multiple tabs to see how the state changes independently."
        ),
        doctext(
            "All user state is stored on the server, and all event handlers are executed on the server. ",
            "Reflex uses websockets to send events to the server, and to send state updates back to the client. ",
        ),
    )
