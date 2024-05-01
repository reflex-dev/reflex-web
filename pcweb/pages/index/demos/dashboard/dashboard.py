import reflex as rx
from ..style import demo_height

data = [
    {"name": "Jul", "revenue": 2300},
    {"name": "Aug", "revenue": 2540},
    {"name": "Sep", "revenue": 2240},
    {"name": "Dec", "revenue": 2100},
    {"name": "Jan", "revenue": 2660},
    {"name": "Feb", "revenue": 2800},
    {"name": "Mar", "revenue": 3200},
    {"name": "Apr", "revenue": 4000},
]

def category_items(name: str, count: str, change: str, clicked: bool):
    return  rx.flex(
        rx.card(
            rx.text(
                name,
                font_weight="400",
                color="#FFFFFF",
                size="2"
            ),
            rx.text(
                count,
                font_weight="bold",
                color="#FFFFFF",
                size="3"
            ),
            rx.flex(
                rx.text(
                    change,
                    color_scheme="lime",
                    size="1"
                ),
                rx.text(
                    "since last month",
                    text_wrap="nowrap",
                    size="1"
                ),
                wrap="nowrap",
                direction="row",
                spacing="1",
            ),
        ),
        direction="column",
    )
 
def sample_bar_chart(input_data):
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="revenue", stroke="#FFFFFF", fill="#FFFFFF",
        ),
        rx.recharts.x_axis(data_key="name", axis_line=False, tick_line=False),
        rx.recharts.y_axis(axis_line=False, tick_line=False),
        data=input_data,
        cx="50%",
        cy="50%",
        fill="#8884d8",
        height="100%",
        width="100%",
    )

def recent_sale_item(first_name, last_name, sale_amount):
    fullname = first_name.capitalize() + " " + last_name.capitalize()
    email = first_name.lower() + "." + last_name.lower() + "@email.com",
    formatted_sale_amount = "+${:,.2f}".format(sale_amount)
    return rx.table.row(
        rx.table.cell(rx.text(fullname, color=rx.color("mauve", 12), line_height="1", font_size="12px")),
        rx.table.cell(rx.text(email[0], color=rx.color("mauve", 12), line_height="1", font_size="12px")),
        rx.table.cell(formatted_sale_amount, color=rx.color("mauve", 12), line_height="1", font_size="12px", align="right"),
        width="92%",
        align="center",
        justify="center",
    )

def dashboard_and_download():
    return rx.hstack(
        rx.heading(
            "Dashboard",
            font_size="24px",
        ),
        rx.spacer(),
        rx.button(
            "Export Data",
            rx.icon("download", size=18, stroke_width="1.5px", padding_left=".1em"),
            color="#000000",
            background="#FFFFFF",
        ),
        justify_content="flex-end",
        height="3em",
        width="100%",
        padding_bottom="10px",
    )

def categories():
    return rx.flex(
        category_items("MRR", "$32,450", "+20.1%", False),
        rx.spacer(),
        rx.tablet_and_desktop(category_items("Active Users", "+1230", "+18.1%", False)),
        rx.spacer(),
        category_items("Followers", "+930", "+19%", False),
        direction="row",
        height="5em",
        width="100%",
    )

def dashboard():
    return rx.fragment(
        rx.theme(rx.flex(
        dashboard_and_download(),
        rx.hstack(
            rx.flex(
                categories(),
                rx.spacer(),
                sample_bar_chart(data),
                direction="column",
                height="100%",
                width=["100%", "100%", "60%", "60%", "60%", "60%"],
                align="center",
                justify="center",
                spacing="4",
            ),
            rx.card(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Name"),
                                rx.table.column_header_cell("Email"),
                                rx.table.column_header_cell("Sale"),
                            ),
                        ),
                        rx.table.body(
                        recent_sale_item("Paul", "Atreides", 1999),
                        recent_sale_item("Duncan", "Idaho", 2999),
                        recent_sale_item("Leto", "Atreides", 3999),
                        recent_sale_item("Gurney", "Halleck", 4999),
                        recent_sale_item("Jessica", "Atreides", 5999),
                        recent_sale_item("Chani", "Kynes", 1999),
                        recent_sale_item("Stilgar", "Kynes", 1999),
                        )
                    ),
                    height="100%",
                    width="40%",
                    display=["none", "none", "flex", "flex"],
            ),
            direction="row",
            height="26em",
            align="center",
            justify="center",
            spacing="4",
            width="100%",   
        ),
        display="flex",
        direction="column",
        justify="center",
        align="center",
        padding="1em",
        
        height=demo_height,
    ),
    appearance="dark",
    ))
