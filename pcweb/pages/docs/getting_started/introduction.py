import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemobox,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)


class CounterExampleState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


@docpage()
def introduction():
    from pcweb.pages.docs.advanced_guide.wrapping_react import wrapping_react
    from pcweb.pages.docs.library import library

    return pc.box(
        docheader("Introduction", first=True),
        doctext(
            "Pynecone is a full-stack framework for building and deploying web apps."
        ),
        subheader("Motivation"),
        doctext("Pynecone was created with the following goals:"),
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
                    "This entire site was built and deployed with Pynecone!",
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
        subheader("First Example"),
        doctext(
            "Let's go over a simple counter app to explore the basics of Pynecone. "
        ),
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
        pc.divider(),
        doctext("Here is the complete code to create this. "),
        doccode(counter_code),
        subheader("The Structure of a Pynecone App"),
        doctext("Let's break down how Pynecone apps are structured."),
        subheader("Import", level=1),
        doccode(counter_code, lines=(0, 1)),
        doctext(
            "We begin by importing the library. ",
            "All Pynecone functions and classes begin with the ",
            pc.code("pc."),
            " prefix.",
        ),
        subheader("State", level=1),
        doccode(counter_code, lines=(2, 5)),
        doctext(
            "The state defines all the variables (called ",
            pc.span("vars", font_weight="bold"),
            ") in an app that can change, as well as the functions that change them. ",
        ),
        doctext(
            "Here our state has by a single var, ",
            pc.code("count"),
            ", which holds the current value of the counter. ",
            " We initialize it to ",
            pc.code("0"),
            ". ",
        ),
        subheader("Event Handlers", level=1),
        doccode(counter_code, lines=(5, 13)),
        doctext(
            "Within the state, we define functions, called ",
            pc.span("event handlers", font_weight="bold"),
            ", that change the state vars. ",
        ),
        doctext(
            "Event handlers are the only way that we can modify the state in Pynecone. ",
            "They can be called in response to user actions, such as clicking a button or typing in a text box. ",
            "These actions are called ",
            pc.span("events", font_weight="bold"),
            ".",
        ),
        doctext(
            "Our counter app has two event handlers, ",
            pc.code("increment"),
            " and ",
            pc.code("decrement"),
            ".",
        ),
        subheader("Frontend", level=1),
        doccode(counter_code, lines=(13, 30)),
        doctext(
            "This function defines the frontend of the app. ",
        ),
        doctext(
            "We use different components such as ",
            pc.code("pc.hstack"),
            ", ",
            pc.code("pc.button"),
            ", and ",
            pc.code("pc.heading"),
            " to build the frontend. ",
            "Components can be nested to create complex layouts, ",
            " and can be styled using the full power of CSS. ",
        ),
        doctext(
            "Pynecone comes with ",
            doclink("50+ built-in components", href=library.path),
            " to help you get started. "
            "We are actively adding more components,  "
            "plus it's easy to ",
            doclink("wrap your own React components", href=wrapping_react.path),
            ". ",
        ),
        doccode(counter_code, lines=(21, 22)),
        doctext(
            "Components can reference the app's state vars. " "The ",
            pc.code("pc.heading"),
            " component displays the current value of the counter by referencing ",
            pc.code("State.count"),
            ". ",
            "All components that reference state will reactively update whenever the state changes.",
        ),
        doccode(counter_code, lines=(15, 21)),
        doctext(
            "Components interact with the state by binding events triggers to event handlers. ",
            "For example, ",
            pc.code("on_click"),
            " is an event that is triggered when a user clicks a component. ",
        ),
        doctext(
            "The first button in our app binds its ",
            pc.code("on_click"),
            " event to the ",
            pc.code("State.decrement"),
            " event handler, ",
            " and the second button binds its to the ",
            pc.code("State.increment"),
            " handler.",
        ),
        subheader("Routing", level=1),
        doccode(counter_code, lines=(31, 32)),
        doctext("Next we define our app and tell it what state to use."),
        doccode(counter_code, lines=(32, 33)),
        doctext(
            "We add a route from the root URL of the app to the counter component. "
        ),
        subheader("Compiling", level=1),
        doccode(counter_code, lines=(33, 34)),
        doctext("Finally, we compile our app, and we are ready to run it."),
        subheader("Next Steps"),
        doctext(
            "And that's it! "
            "We've created an entire frontend and backend in less than 40 lines of code. "
            "From here we can continue developing or deploy it to the web in a single command. "
        ),
        doctext("Keep reading the docs to learn how to try Pynecone yourself!"),
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
