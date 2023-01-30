import pynecone as pc

from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemobox,
    header_comp,
    subheader_comp,
    text_comp,
    doclink,
    docpage,
    doctext,
)


class CounterExampleState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


@pc.component
def intro_code1(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code)


@pc.component
def intro_code2(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(0, 1))


@pc.component
def intro_code3(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(2, 5))


@pc.component
def intro_code4(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(5, 13))


@pc.component
def intro_code5(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(13, 30))


@pc.component
def intro_code6(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(21, 22))


@pc.component
def intro_code7(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(15, 21))


@pc.component
def intro_code8(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(31, 32))


@pc.component
def intro_code9(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(32, 33))


@pc.component
def intro_code10(state: pc.Var[dict]) -> pc.Component:
    return doccode(counter_code, lines=(33, 34))


@pc.component
def intro1() -> pc.Component:
    return pc.fragment(
        header_comp(text="Introduction", first=True),
        text_comp(
            "Pynecone is a full-stack framework for building and deploying web apps."
        ),
        subheader_comp(text="Motivation"),
        text_comp(text="Pynecone was created with the following goals:"),
        pc.unordered_list(
            pc.vstack(
                pc.list_item(
                    pc.span(
                        "Pure Python",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                pc.text(
                    "Use Python for everything. Don't worry about learning a new language.",
                    width="100%",
                ),
                pc.list_item(
                    pc.span(
                        "Easy to Learn",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                pc.text(
                    "Build and share your first app in minutes. No webdev experience required.",
                    width="100%",
                ),
                pc.list_item(
                    pc.span(
                        "Full Flexibility",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                pc.text(
                    "Remain as flexible as traditional web frameworks. ",
                    "Pynecone is easy to get started with, but powerful enough for advanced use cases.",
                    width="100%",
                ),
                pc.text(
                    "Build anything from small data science apps to large, multi-page websites. ",
                    width="100%",
                ),
                pc.text(
                    "This entire site was built and deployed with Pynecone!",
                    color=styles.ACCENT_COLOR_DARK,
                    width="100%",
                ),
                pc.list_item(
                    pc.span(
                        "Batteries Included",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                pc.text(
                    "No need to reach for a bunch of different tools. Pynecone handles the frontend, backend, and deployment of your app.",
                    width="100%",
                ),
                text_align="left",
            ),
        ),
        subheader_comp(text="First Example"),
        text_comp(
            text="Let's go over a simple counter app to explore the basics of Pynecone. "
        ),
    )


@pc.component
def intro2(state: pc.Var[dict]) -> pc.Component:
    from pcweb.pages.docs.advanced_guide.wrapping_react import wrapping_react
    from pcweb.pages.docs.library import library

    return pc.fragment(
        pc.divider(margin_y="1em"),
        text_comp(text="Here is the complete code to create this. "),
        intro_code1(state=state),
        subheader_comp(text="The Structure of a Pynecone App"),
        text_comp(text="Let's break this down."),
        subheader_comp(text="Import"),
        intro_code2(state=BaseVar(name="state")),
        pc.text(
            "We begin by importing the library. ",
            "All Pynecone functions and classes begin with the ",
            pc.code("pc.", color=styles.ACCENT_COLOR),
            " prefix.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="State"),
        intro_code3(state=BaseVar(name="state")),
        pc.text(
            "The state defines all the variables (called ",
            pc.span("vars", font_weight="bold"),
            ") in an app that can change, as well as the functions that change them. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        pc.text(
            "Here our state has by a single var, ",
            pc.code(
                "count",
                color=styles.ACCENT_COLOR,
            ),
            ", which holds the current value of the counter. ",
            " We initialize it to ",
            pc.code(
                "0",
                color=styles.ACCENT_COLOR,
            ),
            ". ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Event Handlers"),
        intro_code4(state=BaseVar(name="state")),
        pc.text(
            "Within the state, we define functions, called ",
            pc.span("event handlers", font_weight="bold"),
            ", that change the state vars. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        pc.text(
            "Event handlers are the only way that we can modify the state in Pynecone. ",
            "They can be called in response to user actions, such as clicking a button or typing in a text box. ",
            "These actions are called ",
            pc.span("events", font_weight="bold"),
            ".",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        pc.text(
            "Our counter app has two event handlers, ",
            pc.code(
                "increment",
                color=styles.ACCENT_COLOR,
            ),
            " and ",
            pc.code(
                "decrement",
                color=styles.ACCENT_COLOR,
            ),
            ".",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Frontend"),
        intro_code5(state=BaseVar(name="state")),
        text_comp(
            text="This function defines the frontend of the app. ",
        ),
        pc.text(
            "We use different components such as ",
            pc.code(
                "pc.hstack",
                color=styles.ACCENT_COLOR,
            ),
            ", ",
            pc.code(
                "pc.button",
                color=styles.ACCENT_COLOR,
            ),
            ", and ",
            pc.code(
                "pc.heading",
                color=styles.ACCENT_COLOR,
            ),
            " to build the frontend. ",
            "Components can be nested to create complex layouts, ",
            " and can be styled using the full power of CSS. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        pc.text(
            "Pynecone comes with ",
            doclink("50+ built-in components", href=library.path),
            " to help you get started. "
            "We are actively adding more components,  "
            "plus it's easy to ",
            doclink("wrap your own React components", href=wrapping_react.path),
            ". ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        intro_code6(state=BaseVar(name="state")),
        pc.text(
            "Components can reference the app's state vars. " "The ",
            pc.code(
                "pc.heading",
                color=styles.ACCENT_COLOR,
            ),
            " component displays the current value of the counter by referencing ",
            pc.code(
                "State.count",
                color=styles.ACCENT_COLOR,
            ),
            ". ",
            "All components that reference state will reactively update whenever the state changes.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        intro_code7(state=BaseVar(name="state")),
        pc.text(
            "Components interact with the state by binding events triggers to event handlers. ",
            "For example, ",
            pc.code(
                "on_click",
                color=styles.ACCENT_COLOR,
            ),
            " is an event that is triggered when a user clicks a component. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        pc.text(
            "The first button in our app binds its ",
            pc.code(
                "on_click",
                color=styles.ACCENT_COLOR,
            ),
            " event to the ",
            pc.code(
                "State.decrement",
                color=styles.ACCENT_COLOR,
            ),
            " event handler, ",
            " and the second button binds its to the ",
            pc.code(
                "State.increment",
                color=styles.ACCENT_COLOR,
            ),
            " handler.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Routing"),
        intro_code8(state=BaseVar(name="state")),
        text_comp(text="Next we define our app and tell it what state to use."),
        intro_code9(state=BaseVar(name="state")),
        text_comp(
            text="We add a route from the root URL of the app to the counter component. "
        ),
        subheader_comp(text="Compiling"),
        intro_code10(state=BaseVar(name="state")),
        text_comp(text="Finally, we compile our app, and we are ready to run it."),
        subheader_comp(text="Next Steps"),
        text_comp(
            text="And that's it! "
            "We've created an entire frontend and backend in less than 40 lines of code. "
            "From here we can continue developing or deploy it to the web in a single command. "
        ),
        doctext("Keep reading the docs to learn how to try Pynecone yourself!"),
    )


from pynecone.var import BaseVar


@docpage()
def introduction():
    return pc.box(
        intro1(),
        docdemobox(
            pc.hstack(
                pc.button(
                    "Decrement",
                    color_scheme="red",
                    border_radius="1em",
                    on_click=CounterExampleState.decrement,
                ),
                pc.heading(
                    CounterExampleState.count, font_size="2em", padding_x="0.5em"
                ),
                pc.button(
                    "Increment",
                    color_scheme="green",
                    border_radius="1em",
                    on_click=CounterExampleState.increment,
                ),
            ),
        ),
        intro2(state=BaseVar(name="state")),
    )


render_code = """pc.hstack(
    pc.button("Decrement", color_scheme = "red", border_radius="1em", on_click = State.decrement),
    pc.heading(State.count, font_size="2em"),
    pc.button("Increment", color_scheme = "green", border_radius="1em", on_click = State.increment),
)"""
counter_code = f"""
import pynecone as pc

class State(pc.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return {render_code} 


app = pc.App(state=State)
app.add_page(index)
app.compile()
"""
