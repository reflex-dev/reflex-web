import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    definition,
    docalert,
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
)

code1 = """
from typing import List

class ExampleState(State):

    # The colors to cycle through.
    colors: List[str] = ["black", "red", "green", "blue", "purple"]

    # The index of the current color.
    index: int = 0

    def next_color(self):
        \"""Cycle to the next color.\"""
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self)-> str:
        return self.colors[self.index]
"""
exec(code1)

code2 = """rx.heading(
    "Welcome to Reflex!",
    on_click=ExampleState.next_color,
    color=ExampleState.color,
    _hover={"cursor": "pointer"},
)
"""


@docpage()
def state_overview():
    return rx.box(
        docheader("State", first=True),
        doctext(
            "The app's state is where we define all the ",
            rx.span("vars", font_weight="bold"),
            " that can change in the app, as well as all the functions that can modify them.",
        ),
        doctext(
            "State allows us to add interaction in Reflex apps. ",
            "Components can modify the state based on user ",
            rx.span("events", font_weight="bold"),
            " such as clicking a button or entering text in a field. ",
            "This is done through ",
            rx.span("event handlers", font_weight="bold"),
            ".",
        ),
        doctext(
            "Each user who opens your app has a unique ID and their own copy of the state. ",
            "This means that each user can interact with the app and modify the state "
            " independently of other users.",
        ),
        docalert(
            "All user state is stored on the server.",
            "Behind the scenes, events are sent as API calls to update the state on the server. "
            + "The state delta is then sent to the frontend, which updates the UI to reflect the new state.",
        ),
        subheader("State Basics"),
        doctext(
            "These are the main concepts to understand how state works in Reflex."
        ),
        rx.responsive_grid(
            definition(
                "Base Vars",
                rx.unordered_list(
                    rx.list_item("Vars in a app that can change over time."),
                    rx.list_item("Can only be modified within event handlers."),
                ),
            ),
            definition(
                "Computed Vars",
                rx.unordered_list(
                    rx.list_item("Vars that are functions of other vars."),
                    rx.list_item("Cannot be set directly, only derived."),
                ),
            ),
            definition(
                "Events",
                rx.unordered_list(
                    rx.list_item(
                        "Actions that occur in the app that trigger event handlers."
                    ),
                ),
            ),
            definition(
                "Event Handlers",
                rx.unordered_list(
                    rx.list_item(
                        "Functions that update the state in response to events."
                    ),
                    rx.list_item("Defined as functions in the State Class."),
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
            "There is a single computed property, ",
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
    )
