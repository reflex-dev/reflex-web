import pandas as pd
import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import doccode, docdemo, doctext

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


badge_example1 = """pc.hstack(
    pc.badge("Example", variant="solid", color_scheme="green"),
    pc.badge("Example", variant="subtle", color_scheme="green"),
    pc.badge("Example", variant="outline", color_scheme="green"),
)
"""
badge_example2 = """pc.hstack(
    pc.badge("Example", variant="subtle", color_scheme="green"),
    pc.badge("Example", variant="subtle", color_scheme="red"),
    pc.badge("Example", variant="subtle", color_scheme="yellow"),
)
"""
badge_example3 = """pc.badge("Custom Badge", bg  = "#90EE90", color = "#3B7A57", border_color = "#29AB87", border_width = 2)
"""
# Datadisplay
def render_badge():
    return pc.vstack(
        doctext("Badges are used to highlight an item's status for quick recognition."),
        doctext("There are 3 variants of badges: solid, subtle, and outline. "),
        docdemo(badge_example1),
        doctext("Color schemes are an easy way to change the color of a badge."),
        docdemo(badge_example2),
        doctext("You can also customize the badge through traditional style args."),
        docdemo(badge_example3),
        align_items="start",
    )


code68 = """pc.code_block(
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
    return pc.vstack(
        doctext(
            "The code component can be used to display code easily within a website. Put in a multiline string with the correct spacing and specify and language to show the desired code."
        ),
        docdemo(code68),
        align_items="start",
    )


divider_example_variations = """pc.vstack(
    pc.text("Example"),
    pc.divider(border_color="black"),
    pc.text("Example"),
    pc.divider(variant="dashed", border_color="black"),
    width="100%",
)
"""

divider_example_vertical = """pc.center(
        pc.divider(
            orientation="vertical", 
            border_color = "black"
        ), 
        height = "4em"
    )
"""


def render_divider():
    return pc.vstack(
        doctext("Dividers are a quick built in way to separate sections of content."),
        docdemo(divider_example_variations),
        doctext(
            "If the vertical orientation is used, make sure that the parent component is assigned a height."
        ),
        docdemo(divider_example_vertical),
        align_items="start",
    )


list_example = """pc.list(
    pc.list_item("Example 1"),
    pc.list_item("Example 2"),
    pc.list_item("Example 3"),
)
"""

unordered_example = """pc.unordered_list(
    pc.list_item("Example 1"),
    pc.list_item("Example 2"),
    pc.list_item("Example 3"),
)
"""
ordered_example = """pc.ordered_list(
    pc.list_item("Example 1"),
    pc.list_item("Example 2"),
    pc.list_item("Example 3"),
)
"""

icon_example = """pc.list(
    pc.list_item(pc.icon(tag="CheckCircleIcon", color = "green"), "Allowed"),
    pc.list_item(pc.icon(tag="NotAllowedIcon", color = "red"), "Not"),
    pc.list_item(pc.icon(tag="SettingsIcon", color = "grey"), "Settings"),
    spacing = ".25em"
)

"""

shorthand_list_example = """pc.list(
    items = ["Example 1", "Example 2", "Example 3"],
    spacing = ".25em"
)
"""


def render_list():
    return pc.vstack(
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


basic_stat_example = """pc.stat(
    pc.stat_label("Example Price"),
    pc.stat_number("$25"),
    pc.stat_help_text("The price of the item."),
)
"""
stat_group_example = """pc.stat_group(
        pc.stat(
            pc.stat_number("$250"),
            pc.stat_help_text("%50", pc.stat_arrow(type_="increase")),
        ),
        pc.stat(
            pc.stat_number("£100"),
            pc.stat_help_text("%50", pc.stat_arrow(type_="decrease")),
        ),
        width="100%",
)
"""


def render_stat():
    return pc.vstack(
        doctext(
            "The stat component is a great way to visualize statistics in a clean and concise way."
        ),
        docdemo(basic_stat_example),
        doctext("Example of a stats in a group with arrow."),
        docdemo(stat_group_example),
        align_items="start",
    )


datatable_example_2_df = """nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")"""
datatable_example_2_table = """
pc.data_table(
    data = nba_data[["Name", "Height", "Age"]],
    pagination= True,
    search= True,
    sort= True,
)           
"""


def render_datatable():
    return pc.vstack(
        doctext(
            "The datatable component is a great way to display data in a table format. You can passs in a pandas dataframe to the df prop to create the table."
        ),
        doctext(
            "In this example we will read data from a csv file and display it in a data_table."
        ),
        doctext(
            "We will also add a search, pagination, sorting to the data_table to make it more accessible."
        ),
        pc.center(
            pc.data_table(
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
                # data=nba_data()[["Name", "Height", "Age"]],
                pagination=True,
                search=True,
                sort=True,
            ),
            style=style["box"],
        ),
        doccode(datatable_example_2_df),
        doccode(datatable_example_2_table),
        align_items="start",
    )


data_example = """
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]

"""
intro_table_example = """pc.table(
    pc.thead(
        pc.tr(
            pc.th("Name"),
            pc.th("Age"),
        )
    ),
    pc.tbody(
        pc.tr(
            pc.td("John"),
            pc.td(30),
        )
    ),
)
"""
exec(data_example)

table_example = """pc.table_container(
    pc.table(
        pc.table_caption("Example Table"),
        pc.thead(
            pc.tr(
                *[pc.th(column) for column in columns]
            )
        ),
        pc.tbody(
            *[pc.tr(*[pc.td(item) for item in row]) for row in data]
        ),
        pc.tfoot(
            pc.tr(
                *[pc.th(item) for item in footer]
            )
        ),
    )
)
"""

styled_table_example = """pc.table_container(
    pc.table(
        pc.thead(
        pc.tr(
            pc.th("Name"),
            pc.th("Age"),
            pc.th("Location"),
            )
        ),
        pc.tbody(
            pc.tr(
                pc.td("John"),
                pc.td(30),
                pc.td("New York"),
            ),
            pc.tr(
                pc.td("Jane"), 
                pc.td(31),
                pc.td("San Francisco"),
            ),
            pc.tr(
                pc.td("Joe"),
                pc.td(32),
                pc.td("Los Angeles"),
            )
        ),
        variant='striped',
        color_scheme='teal'
    )
)
"""


shorthand_table_example = """pc.table_container(
    pc.table(
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
    return pc.vstack(
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
            pc.code("headers"),
            ", ",
            pc.code("rows"),
            ", and ",
            pc.code("footers"),
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
        pc.center(
            pc.table_container(
                pc.table(
                    pc.table_caption("Example Table"),
                    pc.thead(pc.tr(*[pc.th(column) for column in columns])),
                    pc.tbody(*[pc.tr(*[pc.td(item) for item in row]) for row in data]),
                    pc.tfoot(pc.tr(*[pc.th(item) for item in footer])),
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
