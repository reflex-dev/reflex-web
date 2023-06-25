import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, subheader

code49 = """pc.vstack(
    pc.box("Example", bg="yellow", border_radius="sm", width="20%"),
    pc.box("Example", bg="orange", border_radius="md", width="40%"),
    pc.box("Example", bg="red", border_radius="md", width="60%"),
    pc.box("Example", bg="lightblue", border_radius="lg", width="80%"),
    pc.box("Example", bg="lightgreen", border_radius="xl", width="100%"),
    width="100%",
)
"""
code50 = """pc.box(
    pc.button("Click Me"),
    bg="lightgreen",
    border_radius="15px",
    border_color="green",
    border_width="thick",
    padding=5,
)
"""

iframe_example = """pc.box(
        element= "iframe",
        src="https://www.youtube.com/embed/9bZkp7q19f0",
        width = "100%",
    )
"""


# Layout
def render_box():
    return pc.vstack(
        doctext(
            "Box is a generic container component that can be used to group other components."
        ),
        docdemo(code49),
        doctext(
            "Below is an example of how a box component can contain other components."
        ),
        docdemo(code50),
        doctext("Box can also compose videos and iframe elements."),
        docdemo(iframe_example),
        align_items="start",
    )


code51 = """pc.vstack(
    pc.button("Toggle", on_click=CondState.change),
    pc.cond(CondState.show, pc.text("Text 1", color="blue"), pc.text("Text 2", color="red")),
)
"""
code52 = """class CondState(State):
    show: bool = True

    def change(self):
        self.show = not (self.show)
"""

code51_a = """pc.vstack(
    pc.button("Toggle", on_click=MultiCondState.change),
    pc.text(
        pc.cond(MultiCondState.cond1, "True", "False"), 
        " & True => ", 
        pc.cond(MultiCondState.cond1 & MultiCondState.cond3, "True", "False"),
    ),
    pc.text(
        pc.cond(MultiCondState.cond1, "True", "False"), 
        " & False => ", 
        pc.cond(MultiCondState.cond1 & MultiCondState.cond2, "True", "False"),
    ),  
    pc.text(
        pc.cond(MultiCondState.cond1, "True", "False"), 
        " | False => ", 
        pc.cond(MultiCondState.cond1 | MultiCondState.cond2, "True", "False"),
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


def render_cond():
    return pc.vstack(
        doctext("This component is used to conditionally render components."),
        doctext(
            "The cond component takes a condition and two components. If the condition is true, the first component is rendered, otherwise the second component is rendered. "
        ),
        docdemo(code51, state=code52, comp=eval(code51)),
        doctext(
            "The second component is optional and can be omitted. If it is omitted, nothing is rendered if the condition is false."
        ),
        subheader("Multiple Conditions"),
        doctext(
            "You can also use the logical operator ",
            pc.code("&"),
            "and ",
            pc.code("|"),
            "to make up complex conditions",
        ),
        docdemo(code51_a, state=code52_a, comp=eval(code51_a)),
        align_items="start",
    )


code53 = """pc.center(
    pc.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)
"""
code54 = """pc.hstack(
    pc.square(
        pc.vstack(pc.text("Square")),
        border_width="thick",
        border_color="purple",
        padding="1em",
    ),
    pc.circle(
        pc.vstack(pc.text("Circle")),
        border_width="thick",
        border_color="orange",
        padding="1em",
    ),
    spacing="2em",
)"""


def render_center():
    return pc.vstack(
        doctext(
            "Center, Square, and Circle  are components that center its children within itself."
        ),
        docdemo(code53),
        doctext("Below are examples of circle and sqaure."),
        docdemo(code54),
        align_items="start",
    )


code55 = """pc.container(
    pc.box("Example", bg="blue", color="white", width="50%"),
    center_content=True,
    bg="lightblue",
)
"""


def render_container():
    return pc.vstack(
        doctext(
            "Containers are used to constrain a content's width to the current breakpoint, while keeping it fluid."
        ),
        docdemo(code55),
        align_items="start",
    )


code56 = """pc.flex(
    pc.center("Center", bg="lightblue"),
    pc.square("Square", bg="lightgreen", padding=10),
    pc.box("Box", bg="salmon", width="150px"),
)
"""
code57 = """pc.flex(
    pc.center("Center", bg="lightblue"),
    pc.spacer(),
    pc.square("Square", bg="lightgreen", padding=10),
    pc.spacer(),
    pc.box("Box", bg="salmon", width="150px"),
    width = "100%",
)
"""


def render_flex():
    return pc.vstack(
        doctext(
            "Flexbox is a layout model that allows elements to align and distribute space within a container. Using flexible widths and heights, elements can be aligned to fill a space or distribute space between elements, which makes it a great tool to use for responsive design systems."
        ),
        docdemo(code56),
        doctext(
            "Combining flex with spacer allows for stackable and responsive components."
        ),
        docdemo(code57),
        align_items="start",
    )


code58 = """pc.grid(
    pc.grid_item(row_span=1, col_span=1, bg="lightgreen"),
    pc.grid_item(row_span=1, col_span=1, bg="lightblue"),
    pc.grid_item(row_span=1, col_span=1, bg="purple"),
    pc.grid_item(row_span=1, col_span=1, bg="orange"),
    pc.grid_item(row_span=1, col_span=1, bg="yellow"),
    template_columns="repeat(5, 1fr)",
    h="10em",
    width="100%",
    gap=4,
)
"""
code59 = """pc.grid(
    pc.grid_item(row_span=2, col_span=1, bg="lightblue"),
    pc.grid_item(col_span=2, bg="lightgreen"),
    pc.grid_item(col_span=2, bg="yellow"),
    pc.grid_item(col_span=4, bg="orange"),
    template_rows="repeat(2, 1fr)",
    template_columns="repeat(5, 1fr)",
    h="200px",
    width="100%",
    gap=4,
)
"""


def render_grid():
    return pc.vstack(
        doctext(
            "A primitive useful for grid layouts. Grid is Box with display, grid and it comes with helpful style shorthand. It renders a div element."
        ),
        docdemo(code58),
        doctext(
            "In some layouts, you may need certain grid items to span specific amount of columns or rows instead of an even distribution. To achieve this, you need to pass the col_span prop to the GridItem component to span across columns and also pass the row_span component to span across rows. You also need to specify the template_columns and template_rows."
        ),
        docdemo(code59),
        align_items="start",
    )


code60 = """pc.responsive_grid(
    pc.box(height="5em", width="5em", bg="lightgreen"),
    pc.box(height="5em", width="5em", bg="lightblue"),
    pc.box(height="5em", width="5em", bg="purple"),
    pc.box(height="5em", width="5em", bg="tomato"),
    pc.box(height="5em", width="5em", bg="orange"),
    pc.box(height="5em", width="5em", bg="yellow"),
    columns=[3],
    spacing="4",
)
"""
code61 = """pc.responsive_grid(
    pc.box(height="5em", width="5em", bg="lightgreen"),
    pc.box(height="5em", width="5em", bg="lightblue"),
    pc.box(height="5em", width="5em", bg="purple"),
    pc.box(height="5em", width="5em", bg="tomato"),
    pc.box(height="5em", width="5em", bg="orange"),
    pc.box(height="5em", width="5em", bg="yellow"),
    columns=[1, 2, 3, 4, 5, 6],
)
"""


def render_responsivegrid():
    return pc.vstack(
        doctext(
            "ResponsiveGrid provides a friendly interface to create responsive grid layouts with ease. SimpleGrid composes Box so you can pass all the Box props and css grid props with addition to the ones below."
        ),
        doctext("Specify a fixed number of columns for the grid layout."),
        docdemo(code60),
        docdemo(code61),
        align_items="start",
    )


code62 = """pc.hstack(
    pc.box("Example", bg="red", border_radius="md", width="10%"),
    pc.box("Example", bg="orange", border_radius="md", width="10%"),
    pc.box("Example", bg="yellow", border_radius="md", width="10%"),
    pc.box("Example", bg="lightblue", border_radius="md", width="10%"),
    pc.box("Example", bg="lightgreen", border_radius="md", width="60%"),
    width="100%",
)
"""
code63 = """pc.vstack(
    pc.box("Example", bg="red", border_radius="md", width="20%"),
    pc.box("Example", bg="orange", border_radius="md", width="40%"),
    pc.box("Example", bg="yellow", border_radius="md", width="60%"),
    pc.box("Example", bg="lightblue", border_radius="md", width="80%"),
    pc.box("Example", bg="lightgreen", border_radius="md", width="100%"),
    width="100%",
)
"""


def render_stack():
    return pc.vstack(
        doctext(
            "Below are two examples the different types of stack components vstack and hstack."
        ),
        docdemo(code62),
        docdemo(code63),
        align_items="start",
    )


code64 = """pc.flex(
    pc.center(pc.text("Example"), bg="lightblue"),
    pc.spacer(),
    pc.center(pc.text("Example"), bg="lightgreen"),
    pc.spacer(),
    pc.center(pc.text("Example"), bg="salmon"),
    width="100%",
)
"""


def render_spacer():
    return pc.vstack(
        doctext(
            "Creates an adjustable, empty space that can be used to tune the spacing between child elements within Flex."
        ),
        docdemo(code64),
        align_items="start",
    )


code65 = """pc.wrap(
    pc.wrap_item(pc.box("Example", bg="lightgreen", w="100px", h="80px")),
    pc.wrap_item(pc.box("Example", bg="lightblue", w="200px", h="80px")),
    pc.wrap_item(pc.box("Example", bg="red", w="300px", h="80px")),
    pc.wrap_item(pc.box("Example", bg="orange", w="400px", h="80px")),
    width="100%",
    spacing="2em",
    align="center",
)
"""


def render_wrap():
    return pc.vstack(
        doctext(
            "Wrap is a layout component that adds a defined space between its children."
        ),
        doctext(
            "It wraps its children automatically if there isn't enough space to fit any more in the same row. Think of it as a smarter flex-wrap with spacing support."
        ),
        docdemo(code65),
        align_items="start",
    )


basic_foreach_state = """from typing import List
class ForeachState(State):
    color: List[str] = ["red", "green", "blue", "yellow", "orange", "purple"]

def colored_box(color: str):
    return pc.box(
        pc.text(color),
        bg=color
    )
"""
exec(basic_foreach_state)
basic_foreach = """pc.responsive_grid(
        pc.foreach(
            ForeachState.color,
            colored_box
        ),
        columns=[2, 4, 6],
    )
"""


foreach_index_state = """from typing import List
class ForeachIndexState(State):
    count: List[str] = ["red", "green", "blue", "yellow", "orange", "purple"]

def colored_box(color: str, index: int):
    return pc.box(
        pc.text(index),
        bg=color
    )
"""
exec(foreach_index_state)
foreach_index = """pc.responsive_grid(
        pc.foreach(
            ForeachIndexState.count,
            lambda color, index: colored_box(color, index)
        ),
        columns=[2, 4, 6],
    )
"""


nested_foreach_state = """from typing import List
class NestedForeachState(State):
    numbers: List[List[str]] = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def display_row(row):
    return pc.hstack(
        pc.foreach(
            row,
            lambda item: pc.box(
                item,
                border="1px solid black",
                padding="0.5em",
            )
        ),
    )
"""
exec(nested_foreach_state)
nested_foreach = """pc.vstack(
        pc.foreach(
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
    return pc.box(pc.text(color[0]), bg=color[1])
"""
exec(simple_dict_foreach_state)
simple_dict_foreach = """pc.responsive_grid(
        pc.foreach(
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
    return pc.vstack(
            pc.text(color[0], color=color[0]),
            pc.hstack(
                pc.foreach(
                    color[1], lambda x: pc.box(pc.text(x, color="black"), bg=x)
                )

            )
        )
"""
exec(complex_dict_foreach_state)
complex_dict_foreach = """pc.responsive_grid(
        pc.foreach(
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
    return pc.list_item(
        pc.hstack(
            pc.button(
                on_click=lambda: ListState.finish_item(item),
                height="1.5em",
                background_color="white",
                border="1px solid blue",
            ),
            pc.text(item, font_size="1.25em"),
        ),
    )
"""
exec(todo1)
todo2 = """pc.vstack(
    pc.heading("Todos"),
    pc.input(on_blur=ListState.set_new_item, placeholder="Add a todo...", bg  = "white"),
    pc.button("Add", on_click=ListState.add_item, bg = "white"),
    pc.divider(),
    pc.ordered_list(
        pc.foreach(
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
    return pc.vstack(
        doctext(
            "The ",
            pc.code("pc.foreach"),
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
            "When indexing into a nested list, it's important to declare the list's type as Pynecone requires it for type checking. This ensures that any potential frontend JS errors are caught before the user can encounter them."
        ),
        docdemo(
            nested_foreach, nested_foreach_state, eval(nested_foreach), context=True
        ),
        doctext("Below is a more complex example of foreach within a todo list."),
        docdemo(todo3, todo1, eval(todo2)),
        subheader('Dictionaries'),
        doctext(
            "Items in a dictionary can be accessed as list of key-value pairs. Using the color example, we can slightly modify ",
            "the code to use dicts as shown below"
        ),
        docdemo(simple_dict_foreach, simple_dict_foreach_state, eval(simple_dict_foreach), context=True),
        doctext(
            "Now let's show a more complex example with dicts using the color example. Assuming we want to ",
            "display a dictionary of secondary colors as keys and their constituent primary colors as values, ",
            "we can modify the code as below: "
        ),
        docdemo(complex_dict_foreach, complex_dict_foreach_state, eval(complex_dict_foreach), context=True),
        align_items="start",

    )


card_example1 = """pc.card(pc.text("Body of the Card Component"), header=pc.heading("Header", size="lg"), footer=pc.heading("Footer",size="sm"))"""


def render_card():
    return pc.vstack(
        doctext(
            "Card is a flexible component used to group and display content in a clear and concise format."
        ),
        docdemo(card_example1),
        doctext(
            "You can pass a header with ",
            pc.code("header="),
            " and/or a footer with ",
            pc.code("footer="),
        ),
    )


image_example = (
    """pc.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")"""
)

aspect_ratio_example = f"""pc.aspect_ratio({image_example}, ratio=4/3)"""


def render_aspectratio():
    return pc.vstack(
        doctext("Preserve the ratio of the components contained within"),
        docdemo(image_example),
        docdemo(aspect_ratio_example),
    )


fragment_example = """pc.fragment(pc.text("Component1"), pc.text("Component2"))"""


def render_fragment():
    return pc.vstack(
        doctext(
            "A Fragment is a Component that allow you to group multiple Components without a wrapper node."
        ),
        doctext(
            "Refer to the React docs at ",
            pc.link(
                "React/Fragment", href="https://react.dev/reference/react/Fragment"
            ),
            " for more information on its use-case",
        ),
        docdemo(fragment_example),
    )
