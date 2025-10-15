import random

import reflex as rx

from pcweb.components.button import button_with_icon

data = [
    {
        "month": "Jan",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "Feb",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "Mar",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "Apr",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "May",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "Jun",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
    {
        "month": "Jul",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 700),
    },
]


class ChartsState(rx.State):
    data = data

    @rx.event
    def randomize_data(self):
        self.data = [
            {
                "month": item["month"],
                "Mobile": random.randint(100, 500),
                "Desktop": random.randint(400, 700),
            }
            for item in self.data
        ]


def charts():
    return rx.box(
        rx.el.style(
            """
.recharts-tooltip-item-unit {
    display: none;
}
.recharts-tooltip-item-value {
    font-family: "JetBrains Mono", monospace;
    color: var(--c-slate-12);
}

.recharts-tooltip-item:first-child .recharts-tooltip-item-name {
    color: var(--c-violet-9);
}

.recharts-tooltip-item:nth-child(2) .recharts-tooltip-item-name {
    color: var(--c-slate-10);
}
.recharts-tooltip-item-list {
    margin-top: 4px !important;
}
"""
        ),
        button_with_icon(
            "Randomize",
            "dice",
            variant="muted",
            on_click=ChartsState.randomize_data,
            class_name="!bg-slate-5 !border-t-[rgba(255,255,255,0.05)] !rounded-[0.625rem] hover:!bg-slate-6 !text-slate-9 gap-2",
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="Desktop",
                stroke=rx.color("slate", 6),
                fill=rx.color("slate", 3),
                type_="natural",
                active_dot={
                    "stroke": rx.color("slate", 10),
                    "fill": rx.color("slate", 10),
                },
            ),
            rx.recharts.area(
                data_key="Mobile",
                stroke=rx.color("violet", 6),
                fill=rx.color("violet", 3),
                type_="natural",
                active_dot={
                    "stroke": rx.color("violet", 6),
                    "fill": rx.color("violet", 6),
                },
            ),
            rx.recharts.graphing_tooltip(
                content_style={
                    "background": rx.color("slate", 1),
                    "borderColor": rx.color("slate", 5),
                    "borderRadius": "0.75rem",
                    "boxShadow": "0px 2px 4px 0px rgba(28, 32, 36, 0.05)",
                    "fontFamily": "var(--font-instrument-sans)",
                    "fontSize": "0.9rem",
                    "fontStyle": "normal",
                    "fontWeight": "500",
                    "lineHeight": "1rem",
                    "letterSpacing": "-0.01094rem",
                    "minWidth": "8rem",
                    "padding": "6px 10px",
                    "position": "relative",
                    "::after": {
                        "content": "''",
                        "position": "absolute",
                        "left": "0",
                        "top": "0",
                        "width": "4px",
                        "height": "100%",
                        "backgroundColor": rx.color("violet", 9),
                        "borderTopLeftRadius": "0.75rem",
                        "borderBottomLeftRadius": "0.75rem",
                    },
                },
                item_style={
                    "color": "currentColor",
                    "display": "flex",
                    "paddingBottom": "0px",
                    "justifyContent": "space-between",
                },
                label_style={"color": rx.color("slate", 12)},
                cursor={
                    "strokeWidth": 1,
                    "stroke": rx.color("slate", 5),
                    "fill": rx.color("slate", 5),
                },
                separator="",
            ),
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="!stroke-slateA-3"
            ),
            rx.recharts.x_axis(
                # interval="preserveStartEnd",  # This prop doesn't exist in the current reflex version
                include_hidden=True,
                data_key="month",
                stroke="currentColor",
                type_="category",
                class_name="!font-small text-slate-9 [&>line]:!text-slateA-3",
            ),
            data=ChartsState.data,
            class_name="w-full h-full overflow-visible",
        ),
        class_name="flex flex-col items-end gap-6 p-4 lg:px-10 lg:py-12 h-full overflow-hidden",
    )


charts_code = """import reflex as rx
import random

class ChartsState(rx.State):
    data = data

    def randomize_data(self):
        self.data = [
            {
                "month": item["month"],
                "Mobile": random.randint(100, 500),
                "Desktop": random.randint(400, 700),
            }
            for item in self.data
        ]

def chart():
    return rx.box(
        rx.button(
            "Randomize",
            on_click=ChartsState.randomize_data,
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="Mobile",
                stroke=rx.color("violet", 9),
                fill=rx.color("violet", 8),
                type_="natural",
            ),
            rx.recharts.area(
                data_key="Desktop",
                stroke=rx.color("slate", 8),
                fill=rx.color("slate", 7),
                type_="natural"
            ),
            rx.recharts.graphing_tooltip(),
            rx.recharts.cartesian_grid(horizontal=True, vertical=False),
            rx.recharts.x_axis(
                data_key="name",
                type_="category",
            ),
            data=ChartsState.data,
        ),
    )
"""
