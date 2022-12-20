import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
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
        doctext("You can perform basic operations with vars within render functions."),
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
    )
