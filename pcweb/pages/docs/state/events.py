import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code1 = """
from typing import List

class WordCycleState(State):
    # The words to cycle through.
    text: List[str] = ["Welcome", "to", "Reflex", "!"]

    # The index of the current word.
    index: int = 0

    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @rx.var
    def get_text(self) -> str:
        return self.text[self.index]

"""
exec(code1)
code2 = """rx.heading(
    WordCycleState.get_text,
    on_mouse_over=WordCycleState.next_word,
    color="green",
)
"""

code3 = """import asyncio

class ProgressExampleState(State):
    count: int = 0
    show_progress: bool = False

    async def increment(self):
        self.show_progress = True
        yield
        # Think really hard.
        await asyncio.sleep(0.5)
        self.count += 1
        self.show_progress = False
"""
exec(code3)
code4 = """rx.cond(
    ProgressExampleState.show_progress,
    rx.circular_progress(is_indeterminate=True),
    rx.heading(
        ProgressExampleState.count,
        on_click=[ProgressExampleState.increment],
        _hover={"cursor": "pointer"},
    )
)"""


code5 = """
from typing import List

class ArgState(State):
    colors: List[str] = ["rgba(222,44,12)", "white", "#007ac2"]

    def change_color(self, color: str, index: int):
        self.colors[index] = color
"""
exec(code5)
code6 = """rx.hstack(
    rx.input(default_value=ArgState.colors[0], on_blur=lambda c: ArgState.change_color(c, 0), bg=ArgState.colors[0]),
    rx.input(default_value=ArgState.colors[1], on_blur=lambda c: ArgState.change_color(c, 1), bg=ArgState.colors[1]),
    rx.input(default_value=ArgState.colors[2], on_blur=lambda c: ArgState.change_color(c, 2), bg=ArgState.colors[2]),
)
"""


code7 = """class ServerSideState2(State):
    def alert(self):
        return rx.window_alert("Hello World!")
"""
exec(code7)
code8 = """rx.button("Alert", on_click=ServerSideState2.alert)"""

code_collatz_state = """class CollatzState(State):
    count: int = 0

    def start_collatz(self, count: str):
        \"""Run the collatz conjecture on the given number.\"""
        self.count = abs(int(count))
        return CollatzState.run_step

    async def run_step(self):
        \"""Run a single step of the collatz conjecture.\"""

        while self.count > 1:
            await asyncio.sleep(0.5)

            if self.count % 2 == 0:
                # If the number is even, divide by 2.
                self.count /= 2
            else:
                # If the number is odd, multiply by 3 and add 1.
                self.count = self.count * 3 + 1
            yield
"""

exec(code_collatz_state)
code_collatz_render = """rx.vstack(
    rx.badge(CollatzState.count, font_size="1.5em", color_scheme="green"),
    rx.input(on_blur=CollatzState.start_collatz),
)"""

code_setter_state = """
from typing import List

options: List[str] = ["1", "2", "3", "4"]
class SetterState1(State):
    selected: str = "1"

    def change(self, value):
        self.selected = value
"""

exec(code_setter_state)
code_setter_render = """rx.vstack(
    rx.badge(SetterState1.selected, color_scheme="green"),
    rx.select(
        options,
        on_change= lambda value: SetterState1.change(value),
    )
)"""

code_setter2_state = """
from typing import List

options: List[str] = ["1", "2", "3", "4"]
class SetterState2(State):
    selected: str = "1"
"""
exec(code_setter2_state)
code_setter2_render = """rx.vstack(
    rx.badge(SetterState2.selected, color_scheme="green"),
    rx.select(
        options,
        on_change= SetterState2.set_selected,
    )
)"""

code_yield_state = """class MultiUpdateState(State):
    count: int = 0

    async def timed_update(self):
        for i in range(5):
            await asyncio.sleep(0.5)
            self.count += 1
            yield
"""
exec(code_yield_state)
code_yield_render = """rx.vstack(
    rx.text(MultiUpdateState.count),
    rx.button("Start", on_click=MultiUpdateState.timed_update)
)"""


code_callhandler_state = """class CallHandlerState(State):
    count: int = 0
    progress: int = 0

    def set_progress(self, count: int):
        self.progress = count

    async def run(self):
        # Reset the count.
        self.set_progress(0)
        yield

        # Count to 10 while showing progress.
        for i in range(10):
            # Wait and increment.
            await asyncio.sleep(0.5)
            self.count += 1

            # Update the progress.
            self.set_progress(i + 1)

            # Yield to send the update.
            yield
"""
exec(code_callhandler_state)
code_callhandler_render = """rx.vstack(
    rx.badge(CallHandlerState.count, font_size="1.5em", color_scheme="green"),
    rx.progress(value=CallHandlerState.progress, max_=10, width="100%"),
    rx.button("Run", on_click=CallHandlerState.run),
)"""


@docpage()
def events():
    from pcweb.pages.docs.api_reference.special_events import special_events
    from pcweb.pages.docs.library import library

    return rx.box(
        docheader("Events", first=True),
        doctext(
            "Events are how we modify the state and ",
            "make the app interactive.",
        ),
        subheader("Event Triggers"),
        doctext(
            "Event triggers are component actions that create an event to be sent to an event handler."
        ),
        doctext(
            "Each component supports a set of events triggers. ",
            "They are described in each ",
            doclink("component's documentation", href=library.path),
            " in the event trigger section.",
        ),
        doctext(
            "Lets take a look at an example below. Try mousing over the heading to change the word."
        ),
        docdemo(code2, code1, eval(code2), context=True),
        doctext(
            "In this example, the heading component has the event trigger, ",
            rx.code("on_mouse_over"),
            ".",
        ),
        doctext(
            "Whenever the user hovers over the heading, the ",
            rx.code("next_word"),
            " handler will be called to cycle the word. ",
            "Once the handler returns, the UI will be updated to reflect the new state.",
        ),
        subheader("Event Arguments"),
        doctext(
            "In some use cases, you want to pass additional arguments to your event handlers. ",
            "To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.",
        ),
        doctext(
            "Try typing a color in an input below and clicking away from it to change the color of the input."
        ),
        docdemo(code6, code5, eval(code6), context=True),
        doctext(
            "In this case, in we want to pass two arguments to the event handler ",
            rx.code("change_color"),
            ", the color and the index of the color to change.",
        ),
        doctext(
            "The ",
            rx.code("on_blur"),
            " event trigger passes the text of the input as an argument to the lambda, ",
            " and the lambda calls the ",
            rx.code("change_color"),
            " event handler with the text and the index of the input.",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title(
                        "Event Handler Parameters must provide type annotations."
                    ),
                    rx.alert_description(
                        "Like state vars, be sure to provide the right type annotations for the prameters in an event "
                        "handler."
                    ),
                ),
                status="warning",
            ),
        ),
        subheader("Setters"),
        doctext(
            "Every base var has a built-in event handler to set it's value for convenience, called",
            rx.code("set_VARNAME"),
            ".",
        ),
        doctext(
            "Say you wanted to change the value of the select component. ",
            "You could write your own event handler to do this: ",
        ),
        docdemo(
            code_setter_render,
            code_setter_state,
            eval(code_setter_render),
            context=True,
        ),
        doctext("Or you could could use a built-in setter for conciseness."),
        docdemo(
            code_setter2_render,
            code_setter2_state,
            eval(code_setter2_render),
            context=True,
        ),
        doctext(
            "In this example, the setter for ",
            rx.code("selected"),
            " is ",
            rx.code("set_selected"),
            ". Both of these examples are equivalent.",
        ),
        doctext(
            "Setters are a great way to make your code more concise. ",
            "But if you want to do something more complicated, you can always write your own function in the state.",
        ),
        subheader("Yielding Multiple Updates"),
        doctext(
            "A regular event handler will send a ",
            rx.code("StateUpdate"),
            " when it has finished running. ",
            "This works fine for basic event, but sometimes we need more complex logic.",
            "To update the UI multiple times in an event handler, we can yield when we want to send an update.",
        ),
        doctext(
            "To do so, we can use the Python keyword ",
            rx.code("yield"),
            ". ",
            "For every yield inside the function, a ",
            rx.code("StateUpdate"),
            "will be sent to the frontend",
            " with the changes up to this point in the execution of the event handler.",
        ),
        docdemo(
            code_yield_render, code_yield_state, eval(code_yield_render), context=True
        ),
        doctext(
            "Here is another example of yielding multiple updates with a loading icon. ",
        ),
        docdemo(code4, code3, eval(code4), context=True),
        subheader("Calling Event Handlers From Event Handlers"),
        doctext(
            "You can call other event handlers from event handlers to keep your code modular. ",
            "Just use the ",
            rx.code("self.call_handler"),
            " syntax to run another event handler. ",
            " As always, you can yield within your function to send incremental updates to the frontend.",
        ),
        docdemo(
            code_callhandler_render,
            code_callhandler_state,
            eval(code_callhandler_render),
            context=True,
        ),
        subheader("Returning Events From Event Handlers"),
        doctext(
            "So far, we have only seen events that are triggered by components. ",
            "However, an event handler can also return events.",
        ),
        doctext(
            "In Reflex, event handlers run synchronously, so only one event handler can run at a time, ",
            " and the events in the queue will be blocked until the current event handler finishes.",
            "The difference between returning an event and calling an event handler is that ",
            " returning an event will send the event to the frontend and unblock the queue. ",
        ),
        doctext(
            rx.alert(
                icon=True,
                title=rx.text(
                    "Be sure to use the class name ",
                    rx.code("State"),
                    " (or any substate) rather than ",
                    rx.code("self"),
                    " when returning events.",
                ),
            )
        ),
        doctext("Try entering an integer in the input below then clicking out."),
        docdemo(
            code_collatz_render,
            code_collatz_state,
            eval(code_collatz_render),
            context=True,
        ),
        doctext(
            "In this example, we run the ",
            doclink(
                "Collatz Conjecture",
                href="https://en.wikipedia.org/wiki/Collatz_conjecture",
            ),
            " on a number entered by the user. ",
        ),
        doctext(
            "When the ",
            rx.code("on_blur"),
            " event is triggered, the event handler ",
            rx.code("start_collatz"),
            " is called. ",
            "It sets the initial count, then calls ",
            rx.code("run_step"),
            " which runs until the count reaches ",
            rx.code("1"),
            ". ",
        ),
        subheader("Special Events"),
        doctext(
            "Reflex also has built-in special events can be found in the ",
            doclink("reference", href=special_events.path),
            ".",
        ),
        doctext(
            "For example, an event handler can trigger an alert on the browser. ",
        ),
        docdemo(code8, code7, eval(code8), context=True),
    )
