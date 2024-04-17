import reflex as rx

data = [
    {"name": "Jul", "ravenue": 2300},
    {"name": "Aug", "ravenue": 2540},
    {"name": "Sep", "ravenue": 2240},
    {"name": "Dec", "ravenue": 2100},
    {"name": "Jan", "ravenue": 2660},
    {"name": "Feb", "ravenue": 2800},
    {"name": "Mar", "ravenue": 3200},
    {"name": "Apr", "ravenue": 4000},
]

def category_items(categroyName: str, count: str, change: str, clicked: bool):
    return rx.vstack(
        rx.text(
            categroyName,
            line_height="1",
            font_size="12px",
            weight="bold",
            color="#FFFFFF"
        ),
        rx.text(
            count,
            line_height="1",
            font_size="18px",
            weight="bold",
            color="#FFFFFF",
        ),
        rx.text(
            change,
            line_height="1",
            font_size="12px",
            color="#A1A1AA"
        ),
        height="5em",
        width="9em",
        border="1px solid rgba(186, 199, 247, 0.12);",
        border_radius="0.5em",
        align="center",
        justify="center",
        background_color=rx.cond(clicked, "#2e2e2e", "transparent"),
    )

def sample_bar_chart(input_data):
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="ravenue", stroke="#FFFFFF", fill="#FFFFFF",
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
        rx.center(
            "Dashboard",
            font_size="24px",
            color=rx.color("mauve", 12)
        ),
        rx.spacer(),
        rx.button(
            "Download",
            color="#000000",
            background="#FFFFFF",
        ),
        justify_content="flex-end",
        height="3em",
        width="100%",
        padding_x="15px",
        padding_bottom="10px",
    )

def categories():
    return rx.flex(
        category_items("Revenue", "$32,450", "+20.1% from last month", False),
        rx.spacer(),
        category_items("Active Users", "+1230", "+18.1% from last month", False),
        rx.spacer(),
        category_items("Followers", "+930", "+19% from last month", False),
        rx.spacer(),
        category_items("Contributors", "+90", "+20 from last month", False),
        direction="row",
        height="5em",
        width="100%",
    )

def dashboard():
    return rx.theme(rx.flex(
        dashboard_and_download(),
        rx.hstack(
            rx.flex(
                categories(),
                rx.spacer(),
                sample_bar_chart(data),
                direction="column",
                height="100%",
                width="60%",
                align="center",
                justify="center",
                spacing="4",
            ),
            rx.flex(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Full name"),
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
                    recent_sale_item("Duke", "Leto", 8999),
                    )
                ),
                direction="column",
                height="100%",
                width="40%",
            ),
            direction="row",
            height="26em",
            align="center",
            justify="center",
            spacing="4",
            width="100%",   
        ),
        direction="column",
        justify="center",
        align="center",
        padding="1em"
    ),
    appearance="dark",
    )