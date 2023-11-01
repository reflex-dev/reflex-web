import pandas as pd
import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import doccode, docdemo, doctext, code_block
from pcweb import flexdown


style = {
    "box": {
        "borderRadius": "1em",
        "bg": "white",
        "boxShadow": "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
        "padding": 5,
        "width": "100%",
        "overflow_x": "auto",
    }
}


def nba_data():
    return pd.read_csv("data/nba.csv").head(10)


badge_example1 = """rx.hstack(
    rx.badge("Example", variant="solid", color_scheme="green"),
    rx.badge("Example", variant="subtle", color_scheme="green"),
    rx.badge("Example", variant="outline", color_scheme="green"),
)
"""
badge_example2 = """rx.hstack(
    rx.badge("Example", variant="subtle", color_scheme="green"),
    rx.badge("Example", variant="subtle", color_scheme="red"),
    rx.badge("Example", variant="subtle", color_scheme="yellow"),
)
"""
badge_example3 = """rx.badge("Custom Badge", bg  = "#90EE90", color = "#3B7A57", border_color = "#29AB87", border_width = 2)
"""


# Datadisplay
def render_badge():
    return rx.vstack(
        doctext("Badges are used to highlight an item's status for quick recognition."),
        doctext("There are 3 variants of badges: solid, subtle, and outline. "),
        docdemo(badge_example1),
        doctext("Color schemes are an easy way to change the color of a badge."),
        docdemo(badge_example2),
        doctext("You can also customize the badge through traditional style args."),
        docdemo(badge_example3),
        align_items="start",
    )


code68 = """rx.code_block(
    \"""def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))\""",
    language="python",
    show_line_numbers=True,
)
"""


def render_codeblock():
    return rx.vstack(
        doctext(
            "The code component can be used to display code easily within a website. Put in a multiline string with the correct spacing and specify and language to show the desired code."
        ),
        code_block(
            code="""def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2)),
            """,
            language="python",
        ),
        doccode(code68),
        align_items="start",
    )


divider_example_variations = """rx.vstack(
    rx.text("Example"),
    rx.divider(border_color="black"),
    rx.text("Example"),
    rx.divider(variant="dashed", border_color="black"),
    width="100%",
)
"""

divider_example_vertical = """rx.center(
        rx.divider(
            orientation="vertical", 
            border_color = "black"
        ), 
        height = "4em"
    )
"""


def render_divider():
    return rx.vstack(
        doctext("Dividers are a quick built in way to separate sections of content."),
        docdemo(divider_example_variations),
        doctext(
            "If the vertical orientation is used, make sure that the parent component is assigned a height."
        ),
        docdemo(divider_example_vertical),
        align_items="start",
    )


list_example = """rx.list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
"""

unordered_example = """rx.unordered_list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
"""
ordered_example = """rx.ordered_list(
    rx.list_item("Example 1"),
    rx.list_item("Example 2"),
    rx.list_item("Example 3"),
)
"""

icon_example = """rx.list(
    rx.list_item(rx.icon(tag="check_circle", color = "green"), "Allowed"),
    rx.list_item(rx.icon(tag="not_allowed", color = "red"), "Not"),
    rx.list_item(rx.icon(tag="settings", color = "grey"), "Settings"),
    spacing = ".25em"
)

"""

shorthand_list_example = """rx.list(
    items = ["Example 1", "Example 2", "Example 3"],
    spacing = ".25em"
)
"""


def render_list():
    return rx.vstack(
        doctext("There are three types of lists: regular lists, ordered, unordered."),
        doctext(
            "The shorthand syntax used to create a list is by passing in a list of items. These items can be components or Python primitives."
        ),
        docdemo(shorthand_list_example),
        doctext(
            "The examples below have the explicit syntax of list and list_items. Regular lists are used to display a list of items. They have no bullet points or numbers and stack the list items vertically."
        ),
        docdemo(list_example),
        doctext("Unordered have bullet points to display the list items."),
        docdemo(unordered_example),
        doctext("Ordered lists have numbers to display the list items."),
        docdemo(ordered_example),
        doctext("Lists can also be used with icons."),
        docdemo(icon_example),
        doctext(
            "Lists can also be created with a shorthand syntax. Just pass in a list of items and the list items will be created automatically."
        ),
        align_items="start",
    )


basic_stat_example = """rx.stat(
    rx.stat_label("Example Price"),
    rx.stat_number("$25"),
    rx.stat_help_text("The price of the item."),
)
"""
stat_group_example = """rx.stat_group(
        rx.stat(
            rx.stat_number("$250"),
            rx.stat_help_text("%50", rx.stat_arrow(type_="increase")),
        ),
        rx.stat(
            rx.stat_number("£100"),
            rx.stat_help_text("%50", rx.stat_arrow(type_="decrease")),
        ),
        width="100%",
)
"""


def render_stat():
    return rx.vstack(
        doctext(
            "The stat component is a great way to visualize statistics in a clean and concise way."
        ),
        docdemo(basic_stat_example),
        doctext("Example of a stats in a group with arrow."),
        docdemo(stat_group_example),
        align_items="start",
    )


datatable_example_2_df = """import pandas as pd
...
nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")"""
datatable_example_2_table = """
rx.data_table(
    data = nba_data[["Name", "Height", "Age"]],
    pagination= True,
    search= True,
    sort= True,
)           
"""

datatable_example_3 = """class State(rx.State):
    data: List = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"]
     ]
    columns: List[str] = ["First Name", "Last Name"]
    
    def index():  
        return rx.data_table(
        data =State.data,
        columns=State.columns,
        )   

    
    """


def render_datatable():
    return rx.vstack(
        doctext(
            "The datatable component is a great way to display data in a table format. You can pass in a pandas dataframe to the data prop to create the table."
        ),
        doctext(
            "In this example we will read data from a csv file, convert it to a pandas dataframe and display it in a data_table."
        ),
        doctext(
            "We will also add a search, pagination, sorting to the data_table to make it more accessible."
        ),
        rx.center(
            rx.data_table(
                data=[
                    ["Avery Bradley", "6-2", 25.0],
                    ["Jae Crowder", "6-6", 25.0],
                    ["John Holland", "6-5", 27.0],
                    ["R.J. Hunter", "6-5", 22.0],
                    ["Jonas Jerebko", "6-10", 29.0],
                    ["Amir Johnson", "6-9", 29.0],
                    ["Jordan Mickey", "6-8", 21.0],
                    ["Kelly Olynyk", "7-0", 25.0],
                    ["Terry Rozier", "6-2", 22.0],
                    ["Marcus Smart", "6-4", 22.0],
                ],
                columns=["Name", "Height", "Age"],
                pagination=True,
                search=True,
                sort=True,
            ),
            style=style["box"],
        ),
        doccode(datatable_example_2_df),
        doccode(datatable_example_2_table),
        doctext("The example below shows how to create a data table from from a list."),
        doccode(datatable_example_3),
        align_items="start",
    )


def render_dataeditor():
    return flexdown.render_file("docs/library/datadisplay/data_editor.md")


data_example = """
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]

"""
intro_table_example = """rx.table(
    rx.thead(
        rx.tr(
            rx.th("Name"),
            rx.th("Age"),
        )
    ),
    rx.tbody(
        rx.tr(
            rx.td("John"),
            rx.td(30),
        )
    ),
)
"""
exec(data_example)

table_example = """rx.table_container(
    rx.table(
        rx.table_caption("Example Table"),
        rx.thead(
            rx.tr(
                *[rx.th(column) for column in columns]
            )
        ),
        rx.tbody(
            *[rx.tr(*[rx.td(item) for item in row]) for row in data]
        ),
        rx.tfoot(
            rx.tr(
                *[rx.th(item) for item in footer]
            )
        ),
    )
)
"""

styled_table_example = """rx.table_container(
    rx.table(
        rx.thead(
        rx.tr(
            rx.th("Name"),
            rx.th("Age"),
            rx.th("Location"),
            )
        ),
        rx.tbody(
            rx.tr(
                rx.td("John"),
                rx.td(30),
                rx.td("New York"),
            ),
            rx.tr(
                rx.td("Jane"), 
                rx.td(31),
                rx.td("San Francisco"),
            ),
            rx.tr(
                rx.td("Joe"),
                rx.td(32),
                rx.td("Los Angeles"),
            )
        ),
        variant='striped',
        color_scheme='teal'
    )
)
"""


shorthand_table_example = """rx.table_container(
    rx.table(
        headers=["Name", "Age", "Location"],
        rows=[
            ("John", 30, "New York"),
            ("Jane", 31, "San Francisco"),
            ("Joe", 32, "Los Angeles")
        ],
        footers=["Footer 1", "Footer 2", "Footer 3"],
        variant='striped'
    )
)
"""


def render_table():
    return rx.vstack(
        doctext(
            "Tables are used to organize and display data efficiently. The table component differs from the data_table component in that it is not meant to display large amounts of data. It is meant to display data in a more organized way."
        ),
        doctext(
            "Tables can be created with a shorthand syntax or by explicitly creating the table components. ",
            "The shorthand syntax is great for simple tables, but if you need more control over the table you can use the explicit syntax.",
        ),
        doctext(
            "Lets start with the shorthand syntax. ",
            "The shorthand syntax has ",
            rx.code("headers"),
            ", ",
            rx.code("rows"),
            ", and ",
            rx.code("footers"),
            " props. These props are used to create the table.",
        ),
        docdemo(shorthand_table_example),
        doctext(
            "Lets create a simple table explicitly. In this example we will make a table with 2 columns Name and Age."
        ),
        docdemo(intro_table_example),
        doctext("In the examples we will be using this data to display in a table."),
        doccode(data_example),
        doctext("Now lets create a table with the data we created."),
        rx.center(
            rx.table_container(
                rx.table(
                    rx.table_caption("Example Table"),
                    rx.thead(rx.tr(*[rx.th(column) for column in columns])),
                    rx.tbody(*[rx.tr(*[rx.td(item) for item in row]) for row in data]),
                    rx.tfoot(rx.tr(*[rx.th(item) for item in footer])),
                )
            ),
            style=style["box"],
        ),
        doccode(table_example),
        doctext(
            "Tables can also be styled with the variant and color_scheme arguments."
        ),
        docdemo(styled_table_example),
        align_items="start",
    )
