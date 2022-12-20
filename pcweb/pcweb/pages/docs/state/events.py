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

code1 = """class WordCycleState(State):
    # The words to cycle through.
    text = ["Welcome", "to", "Pynecone", "!"]

    # The index of the current word.
    index = 0

    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @pc.var
    def get_text(self):
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
    count = 0
    show_progress = False

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


code5 = """class ArgState(State):
    colors: list[str] = ["rgba(222,44,12)", "white", "#007ac2"]

    def change_color(self, color, index):
        self.colors[index] = color
        # Colors must be set not mutated (See warning below.)
        self.colors = self.colors
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

code9 = """class CollatzState(State):
    count: int = 0

    def start_collatz(self, count):
        \"""Run the collatz conjecture on the given number.\"""
        self.count = abs(int(count))
        return self.run_step


    async def run_step(self):
        \"""Run a single step of the collatz conjecture.\"""
        await asyncio.sleep(0.2)

        if self.count % 2 == 0:
            # If the number is even, divide by 2.
            self.count /= 2
        else:
            # If the number is odd, multiply by 3 and add 1.
            self.count = self.count * 3 + 1
        if self.count > 1:
            # Keep running until we reach 1.
            return self.run_step

"""
exec(code9)
code10 = """pc.vstack(
    pc.badge(CollatzState.count, font_size="1.5em", color_scheme="green"),
    pc.input(on_blur=CollatzState.start_collatz),
)"""

code11 = """
options = ["1", "2", "3", "4"]
class SetterState1(State):
    selected: str = "1"

    def change(self, value):
        self.selected = value
"""
exec(code11)
code12 = """pc.vstack(
    pc.badge(SetterState1.selected, color_scheme="green"),
    pc.select(
        options,
        on_change= lambda value: SetterState1.change(value),
    )
)"""

code13 = """
options = ["1", "2", "3", "4"]
class SetterState2(State):
    selected: str = "1"
"""
exec(code13)
code14 = """pc.vstack(
    pc.badge(SetterState2.selected, color_scheme="green"),
    pc.select(
        options,
        on_change= SetterState2.set_selected,
    )
)"""


@docpage()
def events():
    from pcweb.pages.docs.events_reference.server_side import server_side
    from pcweb.pages.docs.library import library

    return pc.box(
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
            "They are descibed in each ",
            doclink("component's documentation", href=library.path),
            " in the event trigger section.",
        ),
        doctext(
            "Lets take a look at an example below. Try mousing over the heading to change the word."
        ),
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
        doctext(
            "Try typing a color in an input below and clicking away from it to change the color of the input."
        ),
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
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.box(
                    pc.alert_title("Be careful with mutations."),
                    pc.alert_description(
                        doctext(
                            "Pynecone detects which state vars change and only sends deltas to the frontend. ",
                            "This allows for fast performance as your app state grows. "
                            "However, it cannot automatically detect in-place mutations.",
                        ),
                        doctext(
                            "To ensure your changes are rendered, make sure to always set your var to a new object. ",
                            "For example, instead of ",
                        ),
                        doccode("""self.my_list_var.append("item")"""),
                        doctext(
                            "set the var to a new list: ",
                        ),
                        doccode("""self.my_list_var = self.my_list_var + ["item"]"""),
                    ),
                ),
                status="warning",
            ),
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
        docdemo(code12, code11, eval(code12), context=True),
        doctext("Or you could could use a built-in setter for conciseness."),
        docdemo(code14, code13, eval(code14), context=True),
        doctext(
            "In this example, the setter for ",
            pc.code("selected"),
            " is ",
            pc.code("set_selected"),
            ". Both of these examples are equivalent.",
        ),
        doctext(
            "Setters are a greate way to make your code more concise. But if you want to do something more complicated, you can always write your own function in the state."
        ),
        subheader("Event Chains"),
        doctext(
            "Event triggers can be linked to a list of events, creating an ",
            pc.span("event chain", font_weight="bold"),
            ".  ",
        ),
        doctext(
            "Try clicking on the number before to pause and increment. ",
        ),
        docdemo(code14, code3, eval(code4), context=True),
        doctext(
            "In this example, we show a progress bar while performing a long calculation. ",
            "Event triggers can bind to a list of events, which are executed in order. ",
        ),
        subheader("Triggering Events From Event Handlers"),
        doctext(
            "So far, we have only seen events that are triggered by components. ",
            "However, events can also be triggered by event handlers. ",
            "To do this, you can return either an event, or an event chain from an event handler.",
        ),
        doctext("Try entering an integer in the input below then clicking out."),
        docdemo(code10, code9, eval(code10), context=True),
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
            "Pynecone also has built-in server side events can be found in the ",
            doclink("reference", href=server_side.path),
            ".",
        ),
        doctext(
            "For example, an event handler can trigger an alert on the browser. ",
        ),
        docdemo(code8, code7, eval(code8), context=True),
    )
