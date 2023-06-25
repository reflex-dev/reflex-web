import reflex as rx

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


class VarState(State):
    text = "World"


def property_example():
    return rx.text("Hello " + VarState.text)


code1 = """class TickerState(State):
    ticker: str ="AAPL"
    price: str = "$150"
"""
exec(code1)
code2 = """rx.stat_group(
    rx.stat(
        rx.stat_label(TickerState.ticker),
        rx.stat_number(TickerState.price),
        rx.stat_help_text(
            rx.stat_arrow(type_="increase"),
            "4%",
        ),
    ),
)"""
code3 = """class UppercaseState(State):
    text: str = "hello"

    @rx.var
    def upper_text(self) -> str:
        return self.text.upper()
    """
exec(code3)
code4 = """rx.vstack(
    rx.heading(UppercaseState.upper_text),
    rx.input(on_blur=UppercaseState.set_text, placeholder="Type here..."),
)
"""
code5 = """
coins = ["BTC", "ETH", "LTC", "DOGE"]
class VarSelectState(State):
    selected: str = "LTC"
"""
exec(code5)
code6 = """rx.vstack(
    rx.heading("I just bought a bunch of " + VarSelectState.selected),
    rx.select(
        coins,
        on_change=VarSelectState.set_selected,
    )
)"""
code7 = """import random
class VarNumberState(State):
    number: int

    def update(self):
        self.number = random.randint(0, 100)
"""
exec(code7)
code8 = """rx.vstack(
    rx.heading("The number is " + VarNumberState.number),
    rx.cond(
        VarNumberState.number % 2 == 0,
        rx.text("Even", color="green"),
        rx.text("Odd", color="red"),
    ),
    rx.button("Update", on_click=VarNumberState.update),
)"""

code9 = """import numpy as np

class BackendState(State):
    text: str = "Hello World"
    _backend: np.ndarray = np.array([1, 2, 3])

    @rx.var
    def sum(self) -> int:
        return int(self._backend.sum())

    def click(self):
        # Add the next number to the array.
        self._backend = np.append(self._backend, [len(self._backend)])
"""
exec(code9)
code10 = """rx.vstack(
    rx.text("Sum: " + BackendState.sum),
    rx.button("Click Me", on_click=BackendState.click)
)
"""


@docpage()
def vars():
    from pcweb.pages.docs.advanced_guide.custom_vars import custom_vars

    return rx.box(
        docheader("Vars", first=True),
        doctext(
            "Vars are any fields in your app that may change over time. ",
        ),
        subheader("Base Vars"),
        doctext(
            "Base vars are defined as fields in your State class. ",
        ),
        doctext(
            "They can have a set default value. "
            "If you don't provide a default value, you must provide a type annotation. "
        ),
        docdemo(code2, code1, eval(code2), context=True),
        doctext(
            "In this example, ",
            rx.code("ticker"),
            " and ",
            rx.code("price"),
            " are base vars in the app, which can be modified at runtime.",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Vars must be JSON serializable."),
                    rx.alert_description(
                        "Vars are used to communicate between the frontend and backend, so they must be Python builtin types. ",
                        "For more complex use cases you can use a ",
                        doclink("custom var", custom_vars.path),
                        ".",
                    ),
                ),
                status="warning",
            ),
        ),
        subheader("Computed Vars"),
        doctext(
            " Computed properties are properties that are computed from other properties."
        ),
        doctext("Try typing in the input box and clicking out. "),
        docdemo(code4, code3, eval(code4), context=True),
        doctext(
            "Here, ",
            rx.code("upper_text"),
            " is a computed var that always holds the upper case version of ",
            rx.code("text"),
            ".",
        ),
        doctext("We recommend always using type annotations for computed vars. "),
        subheader("Var Operations"),
        doctext(
            "Within your render code, you cannot use arbitrary Python functions on the state vars. "
            "For example, the following code will ",
            rx.span("not work.", font_weight="bold"),
        ),
        doccode(
            """
class State(rx.State):
    number: int

def index():
    rx.text(float(State.number))
            """
        ),
        doctext(
            "This is because we compile the render code to Javascript, but the value of ",
            rx.code("State.number"),
            " is only known at runtime. ",
            "You can use computed vars for more complex operations. ",
        ),
        doctext(
            "However, you can perform basic operations with vars within render functions, as seen below."
        ),
        docdemo(code6, code5, eval(code6), context=True),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Vars support many common operations."),
                    rx.alert_description(
                        "They can be used for arithemtic, string concatenation, inequalities, indexing, and more."
                    ),
                ),
                status="success",
            ),
        ),
        docdemo(code8, code7, eval(code8), context=True),
        doctext(
            "Here, we could have made a computed property that returns the parity of ",
            rx.code("number"),
            ", but it can be simpler just to use a var operation instead.",
        ),
        subheader("Backend Vars"),
        doctext(
            "Backend vars are only stored on the backend and are not sent to the client. ",
            "They have the advantage that they don't need to be JSON serializable. ",
            "This means you can only use them within event handlers, they can't be used in render functions. ",
        ),
        doctext(
            "Backend vars are prefixed with an underscore. ",
        ),
        docdemo(code10, code9, eval(code10), context=True),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("State Vars must provide type annotations."),
                    rx.alert_description(
                        "Reflex relies on type annotations to determine the type of state vars during the "
                        "compilation process.",
                        " Therefore, all state vars should be annotated correctly.",
                        ".",
                    ),
                ),
                status="warning",
            ),
        ),
    )
