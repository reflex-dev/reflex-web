import reflex as rx

from pcweb import flexdown
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, subheader, doclink


# Layout


def render_aspectratio():
    return flexdown.render_file("docs/library/layout/aspect_ratio.md")


def render_box():
    return flexdown.render_file("docs/library/layout/box.md")


def render_card():
    return flexdown.render_file("docs/library/layout/card.md")


code51 = """rx.vstack(
    rx.button("Toggle", on_click=CondState.change),
    rx.cond(CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
)
"""
code52 = """class CondState(State):
    show: bool = True

    def change(self):
        self.show = not (self.show)
"""

code51_a = """rx.vstack(
    rx.button("Toggle", on_click=MultiCondState.change),
    rx.text(
        rx.cond(MultiCondState.cond1, "True", "False"), 
        " & True => ", 
        rx.cond(MultiCondState.cond1 & MultiCondState.cond3, "True", "False"),
    ),
    rx.text(
        rx.cond(MultiCondState.cond1, "True", "False"), 
        " & False => ", 
        rx.cond(MultiCondState.cond1 & MultiCondState.cond2, "True", "False"),
    ),  
    rx.text(
        rx.cond(MultiCondState.cond1, "True", "False"), 
        " | False => ", 
        rx.cond(MultiCondState.cond1 | MultiCondState.cond2, "True", "False"),
    ),
)
"""
code52_a = """class MultiCondState(State):
    cond1: bool = True
    cond2: bool = False
    cond3: bool = True

    def change(self):
        self.cond1 = not (self.cond1)
"""

exec(code52)

exec(code52_a)

code52_b = """rx.vstack(
    rx.button("Toggle", on_click=CondState.change),
    rx.cond(CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
    rx.cond(~CondState.show, rx.text("Text 1", color="blue"), rx.text("Text 2", color="red")),
)
"""


def render_cond():
    return rx.vstack(
        doctext("This component is used to conditionally render components."),
        doctext(
            "The cond component takes a condition and two components. If the condition is true, the first component is rendered, otherwise the second component is rendered. "
        ),
        docdemo(code51, state=code52, comp=eval(code51)),
        doctext(
            "The second component is optional and can be omitted. If it is omitted, nothing is rendered if the condition is false."
        ),
        subheader("Negation"),
        doctext(
            "You can use the logical operator ",
            rx.code("~"),
            " to negate a condition.",
        ),
        docdemo(code52_b, state=code52, comp=eval(code52_b)),
        subheader("Multiple Conditions"),
        doctext(
            "You can also use the logical operator ",
            rx.code("&"),
            " and ",
            rx.code("|"),
            " to make up complex conditions",
        ),
        docdemo(code51_a, state=code52_a, comp=eval(code51_a)),
        align_items="start",
    )


def render_center():
    return flexdown.render_file("docs/library/layout/center.md")


def render_container():
    return flexdown.render_file("docs/library/layout/container.md")


def render_flex():
    return flexdown.render_file("docs/library/layout/flex.md")


def render_fragment():
    return flexdown.render_file("docs/library/layout/fragment.md")


def render_grid():
    return flexdown.render_file("docs/library/layout/grid.md")


def render_responsivegrid():
    return flexdown.render_file("docs/library/layout/responsive_grid.md")


def render_spacer():
    return flexdown.render_file("docs/library/layout/spacer.md")


def render_stack():
    return flexdown.render_file("docs/library/layout/stack.md")


def render_wrap():
    return flexdown.render_file("docs/library/layout/wrap.md")


basic_foreach_state = """from typing import List
class ForeachState(State):
    color: List[str] = ["red", "green", "blue", "yellow", "orange", "purple"]

def colored_box(color: str):
    return rx.box(
        rx.text(color),
        bg=color
    )
"""
exec(basic_foreach_state)
basic_foreach = """rx.responsive_grid(
        rx.foreach(
            ForeachState.color,
            colored_box
        ),
        columns=[2, 4, 6],
    )
"""


foreach_index_state = """from typing import List
class ForeachIndexState(State):
    color: List[str] = ["red", "green", "blue", "yellow", "orange", "purple"]

def colored_box_index(color: str, index: int):
    return rx.box(
        rx.text(index),
        bg=color
    )
"""
exec(foreach_index_state)
foreach_index = """rx.responsive_grid(
        rx.foreach(
            ForeachIndexState.color,
            lambda color, index: colored_box_index(color, index)
        ),
        columns=[2, 4, 6],
    )
"""


nested_foreach_state = """from typing import List
class NestedForeachState(State):
    numbers: List[List[str]] = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def display_row(row):
    return rx.hstack(
        rx.foreach(
            row,
            lambda item: rx.box(
                item,
                border="1px solid black",
                padding="0.5em",
            )
        ),
    )
"""
exec(nested_foreach_state)
nested_foreach = """rx.vstack(
        rx.foreach(
             NestedForeachState.numbers,
            display_row
        )
    )
"""

simple_dict_foreach_state = """from typing import List
class SimpleDictForeachState(State):
    color_chart: dict[int, str] = {
         1 : "blue",
         2: "red",
         3: "green"
    }

def display_color(color: List):
    # color is presented as a list key-value pair([1, "blue"],[2, "red"], [3, "green"])
    return rx.box(rx.text(color[0]), bg=color[1])
"""
exec(simple_dict_foreach_state)
simple_dict_foreach = """rx.responsive_grid(
        rx.foreach(
             SimpleDictForeachState.color_chart,
            display_color
        ),
        columns = [2, 4, 6]
    )
"""

complex_dict_foreach_state = """from typing import List, Dict
class ComplexDictForeachState(State):
    color_chart: Dict[str, List[str]] = {
        "purple": ["red", "blue"],
        "orange": ["yellow", "red"],
        "green": ["blue", "yellow"]
    }

def display_colors(color: List):
    return rx.vstack(
            rx.text(color[0], color=color[0]),
            rx.hstack(
                rx.foreach(
                    color[1], lambda x: rx.box(rx.text(x, color="black"), bg=x)
                )

            )
        )
"""
exec(complex_dict_foreach_state)
complex_dict_foreach = """rx.responsive_grid(
        rx.foreach(
             ComplexDictForeachState.color_chart,
            display_colors
        ),
        columns = [2, 4, 6]
    )
"""

todo1 = """from typing import List
class ListState(State):
    items: List[str] = ["Write Code", "Sleep", "Have Fun"]
    new_item: str

    def add_item(self):
        self.items += [self.new_item]

    def finish_item(self, item: str):
        self.items = [i for i in self.items if i != item]

def get_item(item):
    return rx.list_item(
        rx.hstack(
            rx.button(
                on_click=lambda: ListState.finish_item(item),
                height="1.5em",
                background_color="white",
                border="1px solid blue",
            ),
            rx.text(item, font_size="1.25em"),
        ),
    )
"""
exec(todo1)
todo2 = """rx.vstack(
    rx.heading("Todos"),
    rx.input(on_blur=ListState.set_new_item, placeholder="Add a todo...", bg  = "white"),
    rx.button("Add", on_click=ListState.add_item, bg = "white"),
    rx.divider(),
    rx.ordered_list(
        rx.foreach(
            ListState.items,
            get_item,
        ),
    ),
    bg = "#ededed",
    padding = "1em",
    border_radius = "0.5em",
    shadow = "lg"
)"""

todo3 = f"""def index():
    {todo2}
"""


def render_foreach():
    return rx.vstack(
        doctext(
            "The ",
            rx.code("rx.foreach"),
            " component takes an iterable(list, tuple or dict) and a function that renders each item in the list. ",
            "This is useful for dynamically rendering a list of items defined in a state.",
        ),
        docdemo(basic_foreach, basic_foreach_state, eval(basic_foreach), context=True),
        doctext(
            "The function can also take an index as a second argument. ",
        ),
        docdemo(foreach_index, foreach_index_state, eval(foreach_index), context=True),
        doctext(
            "Nested foreach components can be used to render nested lists.",
        ),
        doctext(
            "When indexing into a nested list, it's important to declare the list's type as Reflex requires it for type checking. This ensures that any potential frontend JS errors are caught before the user can encounter them."
        ),
        docdemo(
            nested_foreach, nested_foreach_state, eval(nested_foreach), context=True
        ),
        doctext("Below is a more complex example of foreach within a todo list."),
        docdemo(todo3, todo1, eval(todo2)),
        subheader("Dictionaries"),
        doctext(
            "Items in a dictionary can be accessed as list of key-value pairs. Using the color example, we can slightly modify ",
            "the code to use dicts as shown below",
        ),
        docdemo(
            simple_dict_foreach,
            simple_dict_foreach_state,
            eval(simple_dict_foreach),
            context=True,
        ),
        doctext(
            "Now let's show a more complex example with dicts using the color example. Assuming we want to ",
            "display a dictionary of secondary colors as keys and their constituent primary colors as values, ",
            "we can modify the code as below: ",
        ),
        docdemo(
            complex_dict_foreach,
            complex_dict_foreach_state,
            eval(complex_dict_foreach),
            context=True,
        ),
        align_items="start",
    )
