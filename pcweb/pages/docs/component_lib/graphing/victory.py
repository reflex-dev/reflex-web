import pandas as pd
import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    doctext,
    docdemo,
    docheader,
    subheader,
    docgraphing,
)

# Graphing

chart_demo1 = """pc.hstack(pc.chart(), pc.chart(polar=True))"""
chart_demo_line = """pc.chart(
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    )
)
"""

chart_demo_styled = """pc.chart(
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
        interpolation="natural",
        style = {"data": {"stroke": "green", "strokeWidth": 2}},
    ),
    pc.scatter(
        data=pc.data("scatter", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1], amount=[6, 5, 3, 9, 3]),
        bubble_property="amount",
        min_bubble_size=0.0,
        max_bubble_size=10.0,
        style={"data": {"fill": "#00FFFF", "opacity": 0.5}},
    ),
    domainPadding={"x": 50, "y": 50},
)
"""


stack_example = """pc.chart_stack(
    pc.area(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    pc.area(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
    ),
)
"""
group_example = """pc.chart_group(
    pc.bar(
        data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[1, 2, 3, 4, 10]),
    ),
    pc.bar(
        data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[5, 12, 4, 6, 1]),
    ),
    pc.bar(
        data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[3, 2, 5, 14, 1]),
    ),
    offset=20.0
)
"""

group_example_style = """pc.chart(
    pc.chart_group(
        pc.bar(
            data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[1, 2, 3, 4, 10]),
        ),
        pc.bar(
            data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[5, 12, 4, 6, 1]),
        ),
        pc.bar(
            data=pc.data("bar", x=["a", "b", "c", "d", "e"], y=[3, 2, 5, 14, 1]),
        ),
        offset=20.0,
        color_scale="qualitative", 
    )
)
"""


def render_chart():
    return pc.vstack(
        doctext(
            "Chart is a wrapper component that renders a given set of children on a set of Cartesian or polar axes. ",
            "Chart reconciles the domain for all its children, controls the layout of the chart, and coordinates animations and shared events. "
            "If no children are provided, Chart will render a default set of axes. ",
        ),
        doctext(
            "The following example shows an empty Chart component, by default it uses Cartesian axis. ",
        ),
        docdemo(chart_demo1),
        doctext(
            "The following example shows a Chart component with a line graph. ",
        ),
        docdemo(chart_demo_line),
        doctext(
            "You can also mix and match different types of graphs as children of Chart. ",
        ),
        docdemo(chart_demo_styled),
        docheader("ChartGroup"),
        doctext(
            "Group is a wrapper component that renders a given set of children in a grouped layout.",
        ),
        docdemo(group_example),
        doctext(
            "Group also accepts a style prop, which is an object of style properties. ",
        ),
        docdemo(group_example_style),
        docheader("ChartStack"),
        doctext(
            "Stack is a wrapper component that renders a given set of children in a stacked layout. Unlike Chart it does not provide axis or domain reconciliation.",
        ),
        docdemo(stack_example),
    )


line_data_example = """data = pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10])"""
line_data_rendered = """data = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
    {"x": 4, "y": 4},
    {"x": 5, "y": 10},
]"""

line_example = """pc.chart(
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
    ),
)
"""

line_example_style = """pc.chart(
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
        interpolation="natural",
        style={"data": {"stroke": "red"}}
    ),
    domain_padding = {"x": 0, "y": 3},
)
"""


def render_line():
    return pc.vstack(
        doctext("Line is a wrapper component that renders a line graph. ", ""),
        docgraphing(
            line_data_example,
            line_data_rendered,
            doctext(
                "Line accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data array, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a ",
            pc.code("pc.line"),
            " component.",
        ),
        docdemo(line_example),
        doctext(
            "Line also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(line_example_style),
    )


bar_data_example = """data = pc.data("bar", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 4, 10])"""
bar_data_rendered = """data = [
    {"x": "Cats", "y": 1},
    {"x": "Dogs", "y": 2},
    {"x": "Birds", "y": 3},
    {"x": "Fish", "y": 4},
    {"x": "Reptiles", "y": 10},
]"""

bar_example = """pc.bar(
    data=pc.data("bar", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 4, 10]),
)
"""

bar_example_style = """pc.chart(
    pc.bar(
        data=pc.data("bar", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 4, 10]),
        style={"data": {"fill": "rgb(107,99,246)", "stroke": "black", "strokeWidth": 2}},
    ),
    domain_padding = {"x": 20, "y": 0},
)
"""


def render_bar():
    return pc.vstack(
        doctext(
            "Bar is a wrapper component that renders a bar graph. ",
        ),
        docgraphing(
            bar_data_example,
            bar_data_rendered,
            doctext(
                "Bar accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data array, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.bar"),
            " component.",
        ),
        docdemo(bar_example),
        doctext(
            "Bar also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(bar_example_style),
    )


area_data_example = """data = pc.data("area", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10])"""
area_data_rendered = """data = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
    {"x": 4, "y": 4},
    {"x": 5, "y": 10},
]"""

area_example = """pc.area(
    data=pc.data("area", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
)
"""

area_example_style = """pc.chart(
    pc.area(
        data=pc.data("area", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
        style={"data": {"fill": "orange", "stroke": "black", "strokeWidth": 2}},
    ),
    pc.area(
        data=pc.data("area", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
        style={"data": {"fill": "rgb(107,99,246)", "stroke": "black", "strokeWidth": 2, "opacity": 0.5}},
        interpolation="natural",
    ),
    domain_padding = {"y": 5},
)
"""


def render_area():
    return pc.vstack(
        doctext(
            "Area is a wrapper component that renders an area graph. ",
        ),
        docgraphing(
            area_data_example,
            area_data_rendered,
            doctext(
                "Area accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.area"),
            " component.",
        ),
        docdemo(area_example),
        doctext(
            "Area also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(area_example_style),
    )


pie_data_example = """data = pc.data("pie", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 10, 4])"""
pie_data_rendered = """data = [
    {"x": "Cats", "y": 1},
    {"x": "Dogs", "y": 2},
    {"x": "Birds", "y": 3},
    {"x": "Fish", "y": 10},
    {"x": "Reptiles", "y": 4},
]"""

pie_example = """pc.pie(
    data=pc.data("pie", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 10, 4]),
)
"""

pie_example_style = """pc.pie(
    data=pc.data("pie", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 10, 4]),
    color_scale="qualitative",
    pad_angle=5.0,
    inner_radius=100.0,
    start_angle=90.0, 
)
"""


def render_pie():
    return pc.vstack(
        doctext(
            "Pie is a wrapper component that renders a pie graph. ",
        ),
        docgraphing(
            pie_data_example,
            pie_data_rendered,
            doctext(
                "Pie accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.pie"),
            " component.",
        ),
        docdemo(pie_example),
        doctext(
            "Pie also accepts a color_scale prop, which is a string that determines the color scale used to color the pie slices. ",
        ),
        docdemo(pie_example_style),
    )


candlestick_data_example = """data = pc.data("candlestick", x=[1, 2, 3, 4, 5], open=[1, 3, 6, 7, 15], close=[1, 2, 3, 4, 10], high=[3, 5, 6, 7, 16], low=[1, 2, 3, 4, 10])"""
candlestick_data_rendered = """data = [
    {"x": 1, "open": 1, "close": 1, "high": 3, "low": 1},
    {"x": 2, "open": 3, "close": 2, "high": 5, "low": 2},
    {"x": 3, "open": 6, "close": 3, "high": 6, "low": 3},
    {"x": 4, "open": 7, "close": 4, "high": 7, "low": 4},
    {"x": 5, "open": 15, "close": 10, "high": 16, "low": 10},
]"""

candlestick_example = """pc.chart(
    pc.candlestick(
            data=pc.data("candlestick", x=[1, 2, 3, 4, 5], open=[1, 3, 6, 7, 15], close=[1, 2, 3, 4, 10], high=[3, 5, 6, 7, 16], low=[1, 2, 3, 4, 10]),
    )
)
"""

candlestick_example_style = """pc.chart(
    pc.candlestick(
            data=pc.data("candlestick", x=[1, 2, 3, 4, 5], open=[1, 3, 6, 7, 15], close=[1, 11, 3, 4, 10], high=[3, 14, 6, 7, 16], low=[1, 2, 3, 4, 10]),
            candle_colors={"positive": "green", "negative": "red"},
            candle_width=10.0,
            candle_ratio=0.5,
    )
)
"""


def render_candlestick():
    return pc.vstack(
        doctext(
            "Candlestick is a wrapper component that renders a candlestick graph. ",
        ),
        docgraphing(
            candlestick_data_example,
            candlestick_data_rendered,
            doctext(
                "Candlestick accepts a data prop, which is an array of dictionaries with x, open, close, high, and low keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x, open, close, high, and low lists.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.candlestick"),
            " component.",
        ),
        docdemo(candlestick_example),
        doctext(
            "You can also style the candlestick graph by passing in a candle_colors prop. ",
        ),
        docdemo(candlestick_example_style),
    )


scatter_data_example = (
    """data = pc.data("scatter", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10])"""
)
scatter_data_rendered = """data = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
    {"x": 4, "y": 4},
    {"x": 5, "y": 10},
]"""

scatter_example = """pc.chart(
    pc.scatter(
        data=pc.data("scatter", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    )
)
"""

scatter_example_style = """pc.chart(
    pc.scatter(
        data=pc.data("scatter", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    pc.scatter(
        data=pc.data("scatter", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
        style={"data": {"fill": "red"}}
    ),
)
"""

scatter_example_bubble = """pc.chart(
    pc.scatter(
        data=pc.data("scatter", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10], amount=[1, 2, 3, 4, 10]),
        min_bubble_size=1.0,
        max_bubble_size=10.0,
        bubble_property="amount",
    )
)
"""


def render_scatter():
    return pc.box(
        doctext(
            "Scatter is a wrapper component that renders a scatter graph. ",
        ),
        docgraphing(
            scatter_data_example,
            scatter_data_rendered,
            doctext(
                "Scatter accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.scatter"),
            " component.",
        ),
        docdemo(scatter_example),
        doctext(
            "Scatter also accepts a style prop, which is an object of style properties. ",
        ),
        docdemo(scatter_example_style),
        doctext(
            "Scatter also accepts a bubble_property prop, which is a string that specifies which property of the data object should be used to determine the size of the bubble. ",
            "Additionally you can specify the min_bubble_size and max_bubble_size props, which determine the minimum and maximum size of the bubbles. ",
        ),
        docdemo(scatter_example_bubble),
    )


box_plot_data_example = """data = pc.data("box_plot", x=[1, 2, 3, 4, 5], y=[[1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10]])"""
box_plot_data_rendered = """data = [
    {"x": 1, "y": [1, 2, 3, 4, 10]},
    {"x": 2, "y": [5, 12, 4, 6, 1]},
    {"x": 3, "y": [1, 2, 3, 4, 10]},
    {"x": 4, "y": [5, 12, 4, 6, 1]},
    {"x": 5, "y": [1, 2, 3, 4, 10]},
]"""

box_plot_example = """pc.chart(
    pc.box_plot(
        data=pc.data("box_plot", x=[1, 2, 3, 4, 5], y=[[1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10]]),
    ),
    domain_padding = {"x": 15, "y": 5},
)
"""

box_plot_example_style = """pc.chart(
    pc.box_plot(
        data=pc.data("box_plot", x=[1, 2, 3, 4, 5], y=[[1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10]]),
        style={
            "min": {"stroke": "tomato"},
            "max": {"stroke": "orange"},
            "q1": {"fill": "tomato"},
            "q3": {"fill": "orange"},
            "median": {"stroke": "white", "strokeWidth": 5},
        }
    ),
    domain_padding = {"x": 15, "y": 5},
)
"""


def render_boxplot():
    return pc.box(
        doctext(
            "BoxPlot is a wrapper component that renders a box plot graph. ",
        ),
        docgraphing(
            box_plot_data_example,
            box_plot_data_rendered,
            doctext(
                "BoxPlot accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " The y key should be a list of lists, where each list represents a box plot. ",
                " Repeat x values will be grouped together.",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.box_plot"),
            " component.",
        ),
        docdemo(box_plot_example),
        doctext(
            "BoxPlot also accepts a style prop, which is an object of style properties. ",
        ),
        docdemo(box_plot_example_style),
    )


histogram_data_example = (
    """data = pc.data("histogram", x=[1, 6, 3, 5, 3, 14, 18, 19, 20])"""
)
histogram_data_rendered = """data = [
    {"x": 1},
    {"x": 6},
    {"x": 3},
    {"x": 5},
    {"x": 3},
    {"x": 14},
    {"x": 18},
    {"x": 19},
    {"x": 20},
]"""

histogram_example = """pc.chart(
    pc.histogram( 
        data=pc.data("histogram", x=[1, 6, 3, 5, 3, 14, 18, 19, 20]),
    ),
)
"""

histogram_example_style = """pc.chart(
    pc.histogram(
        data=pc.data("histogram", x=[1, 6, 3, 5, 3, 14, 18, 19, 20]),
        style={
            "data": {"fill": "orange", "stroke": "tomato", "strokeWidth": 2, "opacity": 0.5},
            "labels": {"fill": "white", "fontSize": 12},
        }
    ),
    domain_padding = {"x": 100}, 
)
"""


def render_histogram():
    return pc.box(
        doctext(
            "Histogram is a wrapper component that renders a histogram graph. ",
        ),
        docgraphing(
            histogram_data_example,
            histogram_data_rendered,
            doctext(
                "Histogram accepts a data prop, which is an array of dictionaries with x keys. ",
                " x values will be grouped together and counted. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.histogram"),
            " component.",
        ),
        docdemo(histogram_example),
        doctext(
            "Histogram also accepts a style prop, which is an object of style properties. ",
        ),
        docdemo(histogram_example_style),
    )


error_bar_data_example = """data = pc.data("error_bar", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10], error_x=[0.1, 0.2, 0.3, 0.4, 0.5], error_y=[0.1, 0.2, 0.3, 0.4, 0.5])"""
error_bar_data_rendered = """data = [
    {"x": 1, "y": 1, "error_x": 0.1, "error_y": 0.1},
    {"x": 2, "y": 2, "error_x": 0.2, "error_y": 0.2},
    {"x": 3, "y": 3, "error_x": 0.3, "error_y": 0.3},
    {"x": 4, "y": 4, "error_x": 0.4, "error_y": 0.4},
    {"x": 5, "y": 10, "error_x": 0.5, "error_y": 0.5},
]"""

error_bar_example = """pc.chart(
    pc.error_bar(
        data=pc.data("error_bar", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10], error_x=[0.1, 0.2, 0.3, 0.4, 0.5], error_y=[0.1, 0.2, 0.3, 0.4, 0.5]),
    ),
)
"""


def render_errorbar():
    return pc.box(
        doctext(
            "ErrorBar is a wrapper component that renders a error bar graph. ",
        ),
        docgraphing(
            error_bar_data_example,
            error_bar_data_rendered,
            doctext(
                "ErrorBar accepts a data prop, which is an array of dictionaries with x, y, error_x, and error_y keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x, y, error_x, and error_y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.error_bar"),
            " component.",
        ),
        docdemo(error_bar_example),
    )


voronoi_data_example = (
    """data = pc.data("voronoi", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10])"""
)
voronoi_data_rendered = """data = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
    {"x": 4, "y": 4},
    {"x": 5, "y": 10},
]"""

voronoi_example = """pc.chart(
    pc.voronoi( 
        data=pc.data("voronoi", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
        style={"data": {"fill": "none", "stroke": "black", "strokeWidth": 1}}
    ),
)
"""

voronoi_style_example = """pc.chart(
    pc.voronoi(
        data=pc.data("voronoi", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
        style={"data": {"fill": "none", "stroke": "#000C66", "strokeWidth": 1}}
    ),
    pc.voronoi(
        data=pc.data("voronoi", x=[1, 3, 5, 7, 8], y=[1, 5, 6, 9, 10]),
        style={"data": {"fill": "#7EC8E3", "stroke": "#050A30", "strokeWidth": 1, "opacity": 0.5}}
    ),
)
"""


def render_voronoi():
    return pc.box(
        doctext(
            "Voronoi is a wrapper component that renders a voronoi graph. ",
        ),
        docgraphing(
            voronoi_data_example,
            voronoi_data_rendered,
            doctext(
                "Voronoi accepts a data prop, which is an array of dictionaries with x and y keys. ",
                " You can contruct your own data as input, or use the ",
                pc.code("pc.data"),
                " helper function to generate a data array from a x and y list.",
            ),
        ),
        doctext(
            "The following example shows a basic ",
            pc.code("pc.voronoi"),
            " component.",
        ),
        docdemo(voronoi_example),
        doctext(
            "The following example shows a ",
            pc.code("pc.voronoi"),
            " component with multiple data sets and custom styles.",
        ),
        docdemo(voronoi_style_example),
    )


polar_example = """pc.chart(
    pc.polar(),
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    polar = True
)
"""


def render_polar():
    return pc.box(
        doctext(
            "Polar is a wrapper component that renders a polar graph. ",
            "Polar expects a data prop, which is a list of objects with x and y keys. ",
        ),
        docdemo(polar_example),
    )
