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


class VarState(State):
    text = "World"


def property_example():
    return pc.text("Hello " + VarState.text)


code1 = """class TickerState(State):
    ticker: str ="AAPL"
    price: str = "$150"
"""
exec(code1)
code2 = """pc.stat_group(
    pc.stat(
        pc.stat_label(TickerState.ticker),
        pc.stat_number(TickerState.price),
        pc.stat_help_text(
            pc.stat_arrow(type_="increase"),
            "4%",
        ),
    ),
)"""
code3 = """class UppercaseState(State):
    text: str = "hello"

    @pc.var
    def upper_text(self) -> str:
        return self.text.upper()
    """
exec(code3)
code4 = """pc.vstack(
    pc.heading(UppercaseState.upper_text),
    pc.input(on_blur=UppercaseState.set_text, placeholder="Type here..."),
)
"""
code5 = """
coins = ["BTC", "ETH", "LTC", "DOGE"]
class VarSelectState(State):
    selected: str = "LTC"
"""
exec(code5)
code6 = """pc.vstack(
    pc.heading("I just bought a bunch of " + VarSelectState.selected),
    pc.select(
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
code8 = """pc.vstack(
    pc.heading("The number is " + VarNumberState.number),
    pc.cond(
        VarNumberState.number % 2 == 0,
        pc.text("Even", color="green"),
        pc.text("Odd", color="red"),
    ),
    pc.button("Update", on_click=VarNumberState.update),
)"""

code9 = """import numpy as np

class BackendState(State):
    text: str = "Hello World"
    _backend: np.ndarray = np.array([1, 2, 3])

    @pc.var
    def sum(self) -> int:
        return int(self._backend.sum())

    def click(self):
        # Add the next number to the array.
        self._backend = np.append(self._backend, [len(self._backend)])
"""
exec(code9)
code10 = """pc.vstack(
    pc.text("Sum: " + BackendState.sum),
    pc.button("Click Me", on_click=BackendState.click)
)
"""


@docpage()
def vars():
    from pcweb.pages.docs.advanced_guide.custom_vars import custom_vars

    return pc.box(
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
            pc.code("ticker"),
            " and ",
            pc.code("price"),
            " are base vars in the app, which can be modified at runtime.",
        ),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.box(
                    pc.alert_title("Vars must be JSON serializable."),
                    pc.alert_description(
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
            pc.code("upper_text"),
            " is a computed var that always holds the upper case version of ",
            pc.code("text"),
            ".",
        ),
        doctext("We recommend always using type annotations for computed vars. "),
        subheader("Var Operations"),
        doctext(
            "Within your render code, you cannot use arbitrary Python functions on the state vars. "
            "For example, the following code will ",
            pc.span("not work.", font_weight="bold"),
        ),
        doccode(
            """
class State(pc.State):
    number: int

def index():
    pc.text(float(State.number))
            """
        ),
        doctext(
            "This is because we compile the render code to Javascript, but the value of ",
            pc.code("State.number"),
            " is only known at runtime. ",
            "You can use computed vars for more complex operations. ",
        ),
        doctext(
            "However, you can perform basic operations with vars within render functions, as seen below."
        ),
        docdemo(code6, code5, eval(code6), context=True),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.box(
                    pc.alert_title("Vars support many common operations."),
                    pc.alert_description(
                        "They can be used for arithemtic, string concatenation, inequalities, indexing, and more."
                    ),
                ),
                status="success",
            ),
        ),
        docdemo(code8, code7, eval(code8), context=True),
        doctext(
            "Here, we could have made a computed property that returns the parity of ",
            pc.code("number"),
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
    )
