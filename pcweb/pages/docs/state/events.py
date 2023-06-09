import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
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
    text: List[str] = ["Welcome", "to", "Pynecone", "!"]

    # The index of the current word.
    index: int = 0

    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @pc.var
    def get_text(self) -> str:
        return self.text[self.index]

"""
exec(code1)
code2 = """pc.heading(
    WordCycleState.get_text,
    on_mouse_over=WordCycleState.next_word,
    color="green",
)
"""
code3 = """import asyncio

class ChainExampleState(State):
    count: int = 0
    show_progress: bool = False

    def toggle_progress(self):
        self.show_progress = not self.show_progress

    async def increment(self):
        # Think really hard.
        await asyncio.sleep(0.5)
        self.count += 1
"""
exec(code3)
code4 = """pc.cond(
    ChainExampleState.show_progress,
    pc.circular_progress(is_indeterminate=True),
    pc.heading(
        ChainExampleState.count,
        on_click=[ChainExampleState.toggle_progress, ChainExampleState.increment, ChainExampleState.toggle_progress],
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
code6 = """pc.hstack(
    pc.input(default_value=ArgState.colors[0], on_blur=lambda c: ArgState.change_color(c, 0), bg=ArgState.colors[0]),
    pc.input(default_value=ArgState.colors[1], on_blur=lambda c: ArgState.change_color(c, 1), bg=ArgState.colors[1]),
    pc.input(default_value=ArgState.colors[2], on_blur=lambda c: ArgState.change_color(c, 2), bg=ArgState.colors[2]),
)
"""

code7 = """class ServerSideState2(State):
    def alert(self):
        return pc.window_alert("Hello World!")
"""
exec(code7)
code8 = """pc.button("Alert", on_click=ServerSideState2.alert)"""

code_collatz_state = """class CollatzState(State):
    count: int = 0

    def start_collatz(self, count: str):
        \"""Run the collatz conjecture on the given number.\"""
        self.count = abs(int(count))
        return CollatzState.run_step

    async def run_step(self):
        \"""Run a single step of the collatz conjecture.\"""

        while self.count > 1:
            await asyncio.sleep(0.2)

            if self.count % 2 == 0:
                # If the number is even, divide by 2.
                self.count /= 2
            else:
                # If the number is odd, multiply by 3 and add 1.
                self.count = self.count * 3 + 1
            yield
"""

exec(code_collatz_state)
code_collatz_render = """pc.vstack(
    pc.badge(CollatzState.count, font_size="1.5em", color_scheme="green"),
    pc.input(on_blur=CollatzState.start_collatz),
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
code_setter_render = """pc.vstack(
    pc.badge(SetterState1.selected, color_scheme="green"),
    pc.select(
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
code_setter2_render = """pc.vstack(
    pc.badge(SetterState2.selected, color_scheme="green"),
    pc.select(
        options,
        on_change= SetterState2.set_selected,
    )
)"""

code_yield_state = """class MultiUpdateState(State):
    count: int = 0

    async def timed_update(self):
        for i in range(5):
            await asyncio.sleep(1)
            self.count += 1
            yield
"""
exec(code_yield_state)
code_yield_render = """pc.vstack(
    pc.text(MultiUpdateState.count),
    pc.button("Start", on_click=MultiUpdateState.timed_update)
)"""


code_callargs_state = """class CallArgsState(State):
    count: int = 0

    def run(self):
        if self.count == 0:
            yield CallArgsState.run_args(1, 2)
        else:
            yield CallArgsState.run_noargs
    
    def run_slow(self):
        if self.count == 0:
            yield CallArgsState.slow_run_args(1, 2)
        else:
            yield CallArgsState.run_noargs

    def run_noargs(self):
        self.count = 0

    def run_args(self, arg1, arg2):
        self.count = int(arg1) + int(arg2)

    async def slow_run_args(self, arg1, arg2):
        await asyncio.sleep(2)
        self.count = int(arg1) + int(arg2)
"""
exec(code_callargs_state)
code_callargs_render = """pc.vstack(
    pc.badge(CallArgsState.count, font_size="1.5em", color_scheme="green"),
    pc.button("Start", on_click=CallArgsState.run),
    pc.button("Start Slow", on_click=CallArgsState.run_slow),
)"""


@docpage()
def events():
    from pcweb.pages.docs.api_reference.special_events import special_events
    from pcweb.pages.docs.library import library

    return pc.box(
        docheader("Events", first=True),
        doctext(
            "Events are how we modify the state and ",
            "make the app interactive.",
        ),
        subheader("Event Triggers"),
        doctext("Event triggers are component actions that create an event to be sent to an event handler."),
        doctext(
            "Each component supports a set of events triggers. ",
            "They are described in each ",
            doclink("component's documentation", href=library.path),
            " in the event trigger section.",
        ),
        doctext("Lets take a look at an example below. Try mousing over the heading to change the word."),
        docdemo(code2, code1, eval(code2), context=True),
        doctext(
            "In this example, the heading component has the event trigger, ",
            pc.code("on_mouse_over"),
            ".",
        ),
        doctext(
            "Whenever the user hovers over the heading, the ",
            pc.code("next_word"),
            " handler will be called to cycle the word. ",
            "Once the handler returns, the UI will be updated to reflect the new state.",
        ),
        subheader("Event Arguments"),
        doctext(
            "In some use cases, you want to pass additional arguments to your event handlers. ",
            "To do this you can bind an event trigger to a lambda, which can call your event handler with the arguments you want.",
        ),
        doctext("Try typing a color in an input below and clicking away from it to change the color of the input."),
        docdemo(code6, code5, eval(code6), context=True),
        doctext(
            "In this case, in we want to pass two arguments to the event handler ",
            pc.code("change_color"),
            ", the color and the index of the color to change.",
        ),
        doctext(
            "The ",
            pc.code("on_blur"),
            " event trigger passes the text of the input as an argument to the lambda, ",
            " and the lambda calls the ",
            pc.code("change_color"),
            " event handler with the text and the index of the input.",
        ),
        subheader("Setters"),
        doctext(
            "Every base var has a built-in event handler to set it's value for convenience, called",
            pc.code("set_VARNAME"),
            ".",
        ),
        doctext(
            "Say you wanted to change the value of the select component. ",
            "You could write your own event handler to do this: ",
        ),
        docdemo(code_setter_render, code_setter_state, eval(code_setter_render), context=True),
        doctext("Or you could could use a built-in setter for conciseness."),
        docdemo(code_setter2_render, code_setter2_state, eval(code_setter2_render), context=True),
        doctext(
            "In this example, the setter for ",
            pc.code("selected"),
            " is ",
            pc.code("set_selected"),
            ". Both of these examples are equivalent.",
        ),
        doctext(
            "Setters are a great way to make your code more concise. ",
            "But if you want to do something more complicated, you can always write your own function in the state.",
        ),
        subheader("Yielding Multiple Updates"),
        doctext(
            "A regular event handler will send a ",
            pc.code("StateUpdate"),
            " when it has finished running. ",
            "This work fine for basic event, but sometimes we need more complex logic, ",
            "and we eventually want the frontend to update multiple times during the event handler.",
        ),
        doctext(
            "To do so, we can use the python keyword ",
            pc.code("yield"),
            ". ",
            "For every yield inside the function, a ",
            pc.code("StateUpdate"),
            "will be sent to the frontend",
            " with the changes up to this point in the execution of the event handler.",
        ),
        docdemo(code_yield_render, code_yield_state, eval(code_yield_render), context=True),
        subheader("Event Chains"),
        doctext(
            "Event triggers can be linked to a list of events, creating an ",
            pc.span("event chain", font_weight="bold"),
            ".  ",
        ),
        doctext(
            "Try clicking on the number before to pause and increment. ",
        ),
        docdemo(code4, code3, eval(code4), context=True),
        doctext(
            "In this example, we show a progress bar while performing a long calculation. ",
            "Event triggers can bind to a list of events, which are executed in order. ",
        ),
        subheader("Triggering Events From Event Handlers"),
        doctext(
            "So far, we have only seen events that are triggered by components. ",
            "However, an event handler can also trigger others event handlers.",
        ),
        doctext("This way to call event handlers work with either async or non-async events."),
        doctext(
            pc.alert(
                icon=True,
                title=pc.text(
                    "Be sure to use the class name ",
                    pc.code("State"),
                    " (or any substate) rather than ",
                    pc.code("self"),
                    ".",
                ),
            )
        ),
        docdemo(code_callargs_render, code_callargs_state, eval(code_callargs_render), context=True),
        doctext("Try entering an integer in the input below then clicking out."),
        docdemo(code_collatz_render, code_collatz_state, eval(code_collatz_render), context=True),
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
            pc.code("on_blur"),
            " event is triggered, the event handler ",
            pc.code("start_collatz"),
            " is called. ",
            "It sets the initial count, then calls ",
            pc.code("run_step"),
            " which runs a single step of the collatz conjecture. ",
            "The ",
            pc.code("run_step"),
            " then repeatedly calls itself until the count reaches ",
            pc.code("1"),
            ". ",
        ),
        doctext(
            "Pynecone also has built-in special events can be found in the ",
            doclink("reference", href=special_events.path),
            ".",
        ),
        doctext(
            "For example, an event handler can trigger an alert on the browser. ",
        ),
        docdemo(code8, code7, eval(code8), context=True),
    )
