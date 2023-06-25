import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docheader, docpage, doctext, subheader

code1 = """
class ParentState(State):
    checked: bool = True
    count: int = 0


class ChildState1(ParentState):
    value: int = 42


class ChildState2(ParentState):
    color: str = "red"


class ChildState3(ChildState1):
    text: str = "Hello World"
"""
exec(code1)
code2 = """
rx.badge(ChildState3.text, color_scheme=ChildState2.color)
"""

code3 = """
rx.heading(ChildState3.count, color="green")
"""


@docpage()
def substates():
    return rx.box(
        docheader("Substates", first=True),
        doctext(
            "As your app grows, your state will grow too. ",
            "You can split your state into multiple substates from your base state to keep things organized.",
        ),
        subheader("Creating a Substate"),
        doctext(
            "Your base state should inherit from ",
            rx.code("rx.State"),
            ". ",
            "Substates can either inherit from your base state or other substates.",
        ),
        docdemo(code2, code1, eval(code2)),
        doctext(
            "In the example above, we have a base state ",
            rx.code("ParentState"),
            " with two substates ",
            rx.code("ChildState1"),
            " and ",
            rx.code("ChildState2"),
            ". ",
            "Additionally, ",
            rx.code("ChildState3"),
            " inherits from ",
            rx.code("ChildState1"),
            ". ",
            "Components can access any var or event handler from any substate.",
        ),
        doctext(
            "A common use case may be to create a substate for each page of your app, "
            "while keeping general vars such as the logged in user in the base state for easy access."
        ),
        subheader("Accessing Parent State Properties"),
        doctext(
            "You can access the parent state properties from a child substate, however you cannot access the child properties from the parent state."
        ),
        docdemo(code3, None, eval(code3)),
    )
