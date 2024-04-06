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
        height="4.5em",
        width="10em",
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
        height="90%",
        width="90%",
        padding_right="20px",
    )

def recent_sale_item(first_name, last_name, sale_amount):
    fullname = first_name.capitalize() + " " + last_name.capitalize()
    email = first_name.lower() + "." + last_name.lower() + "@email.com",
    formatted_sale_amount = "+${:,.2f}".format(sale_amount)
    return rx.flex(
        rx.vstack(
            rx.text(fullname, color="#FFFFFF", line_height="1", font_size="16px"),
            rx.text(email[0], color="#FFFFFF", line_height="1", font_size="12px"),
            align="center",
        ),
        rx.spacer(),
        rx.text(formatted_sale_amount, color="#FFFFFF", line_height="1", font_size="16px", align="right"),
        width="92%",
        direction="row",
        align="center",
        justify="center",
        padding="5px 5px 5px 5px",
    )

def dashboard_and_download():
    return rx.hstack(
        rx.center(
            "Dashboard",
            font_size="24px",
            color="#FFFFFF",
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
        padding_left="20px",
        padding_right="20px",
    )

def categories():
    return rx.flex(
        rx.box(width="20px"),
        category_items("Revenue", "$32,450", "+20.1% from last month", True),
        rx.spacer(),
        category_items("Active Users", "+1230", "+18.1% from last month", False),
        rx.spacer(),
        category_items("Followers", "+930", "+19% from last month", False),
        rx.spacer(),
        category_items("Contributors", "+90", "+20 from last month", False),
        rx.box(width="20px"),
        direction="row",
        height="5em",
        padding_left="10px",
        padding_right="10px",
        align="center",
        justify="center",
    )

def dashboard():
    return rx.flex(
        dashboard_and_download(),
        rx.flex(
            categories(),
            rx.flex(
                rx.flex(
                    sample_bar_chart(data),
                    direction="row",
                    height="21em",
                    width="60%",
                    align="center",
                    justify="center",
                ),
                rx.flex(
                    rx.vstack(
                        rx.flex(
                            "Recent Sales", 
                            color="#FFFFFF", 
                            width="100%",
                            line_height="1",
                            height="1em",
                            align="center",
                            justify="start",
                            padding_left="25px",
                            weight="bold",
                            font_size="14",
                        ),
                        rx.flex(
                            "You made 265 sales this month.",
                            color="#FFFFFF", 
                            width="100%",
                            line_height="1",
                            height="1em",
                            align="center",
                            justify="start",
                            padding_left="25px",
                            font_size="14",
                        ),
                    ),
                    rx.vstack(
                        rx.box(height="10px"),
                        recent_sale_item("jason", "mars", 1999),
                        recent_sale_item("Sofia", "Kim", 499),
                        recent_sale_item("angela", "baby", 799),
                        recent_sale_item("jack", "dawson", 1099),
                        height="18em",
                        padding_buttom="5px",
                    ),
                    direction="column",
                    height="21em",
                    width="40%",
                    padding_top="10px",
                ),
                direction="row",
                height="22em",
                align="center",
                justify="center",
            ),
            direction="column",
            height="27em",
            width="100%",
        ),
        direction="column",
        justify="center",
        align="center",
    )