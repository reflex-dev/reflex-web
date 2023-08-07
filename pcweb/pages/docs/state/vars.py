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
        # This will be recomputed whenever `text` changes.
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
    selected: str = "DOGE"
"""
exec(code5)
code6 = """rx.vstack(
    # Using a var operation to concatenate a string with a var.
    rx.heading("I just bought a bunch of " + VarSelectState.selected),
    rx.select(
        coins,
        value=VarSelectState.selected,
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
    # Var operations can be composed for more complex expressions.
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
                        "Vars are used to communicate between the frontend and backend. ",
                        "They must be primitive Python types, ",
                        "Plotly figures, Pandas dataframes, or ",
                        doclink("a custom defined type", custom_vars.path),
                        ".",
                    ),
                ),
                status="warning",
            ),
        ),
        subheader("Computed Vars"),
        doctext(
            "Computed vars are vars that are computed from other properties. "
            "They are defined as methods in your State class with the ",
            rx.code("@rx.var"),
            " decorator. ",
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
            "Within your frontend components, you cannot use arbitrary Python functions on the state vars. "
            "For example, the following code will ",
            rx.span("not work.", font_weight="bold"),
        ),
        doccode(
            """
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, when we don't know the value of `State.number`.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
            """
        ),
        doctext(
            "This is because we compile the frontend to Javascript, but the value of ",
            rx.code("State.number"),
            " is only known at runtime. ",
            "You can use computed vars for more complex operations. ",
        ),
        doctext(
            "However, you can perform basic operations with vars within components, as seen below."
        ),
        docdemo(code6, code5, eval(code6), context=True),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Vars support many common operations."),
                    rx.alert_description(
                        "They can be used for arithemtic, string concatenation, inequalities, indexing, and more. "
                        "See the ",
                        doclink("full list of supported operations", "/api-reference/var"),
                        ".",

                    ),
                ),
                status="success",
            ),
        ),
        doctext(
            "You can also combine multiple var operations together, as seen in the next example. "
        ),
        docdemo(code8, code7, eval(code8), context=True),
        doctext(
            "Here, we could have made a computed var that returns the parity of ",
            rx.code("number"),
            ", but it can be simpler just to use a var operation instead.",
        ),
        subheader("Backend Vars"),
        doctext(
            "Backend vars are only stored on the backend and are not sent to the client. ",
            "They have the advantage that they don't need to be JSON serializable. ",
            "This means you can only use them within event handlers, they can't be used in frontend components. ",
        ),
        doctext(
            "Backend vars are prefixed with an underscore. ",
        ),
        docdemo(code10, code9, eval(code10), context=True),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("State Vars should provide type annotations."),
                    rx.alert_description(
                        "Reflex relies on type annotations to determine the type of state vars during the "
                        "compilation process. ",
                        ".",
                    ),
                ),
                status="warning",
            ),
        ),
    )
