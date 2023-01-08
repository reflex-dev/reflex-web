import pandas as pd
import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import doccode, doctext, docdemo

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

def render_chart():
    return pc.vstack(
        doctext(
            "Chart is a wrapper component that renders a given set of children on a set of Cartesian or polar axes. ",
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
    )
 
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
        doctext(
            "Line is a wrapper component that renders a line graph. ",
            "Line expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Line component with a line graph. ",
        ),
        docdemo(line_example),
        doctext(
            "Line also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(line_example_style)
    )

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
            "Bar expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Bar component with a bar graph. ",
        ),
        docdemo(bar_example),
        doctext(
            "Bar also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(bar_example_style)
    )

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
            "Area expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Area component with a area graph. ",
        ),
        docdemo(area_example),
        doctext(
            "Area also accepts a style prop, which is an object of style properties. ",
            "Additionally you can specify the interpolation prop, which determines how data points should be connected when creating a path. ",
        ),
        docdemo(area_example_style)
    )

pie_example = """pc.pie(
    data=pc.data("pie", x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"], y=[1, 2, 3, 10, 4]),
)
"""

def render_pie():
    return pc.vstack(
        doctext(
            "Pie is a wrapper component that renders a pie graph. ",
            "Pie expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Pie component with a pie graph. ",
        ),
        docdemo(pie_example),
    )

candlestick_example = """pc.chart(
    pc.candlestick(
            data=pc.data("candlestick", x=[1, 2, 3, 4, 5], open=[1, 3, 6, 7, 15], close=[1, 2, 3, 4, 10], high=[3, 5, 6, 7, 16], low=[1, 2, 3, 4, 10]),
    )
)
"""

def render_candlestick():
    return pc.vstack(
        doctext(
            "Candlestick is a wrapper component that renders a candlestick graph. ",
            "Candlestick expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Candlestick component with a candlestick graph. ",
        ),
        docdemo(candlestick_example),
    )

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
    return pc.vstack(
        doctext(
            "Scatter is a wrapper component that renders a scatter graph. ",
            "Scatter expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Scatter component with a scatter graph. ",
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

box_plot_example = """pc.chart(
    pc.box_plot(
        data=pc.data("box_plot", x=[1, 2, 3, 4, 5], y=[[1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10], [5, 12, 4, 6, 1], [1, 2, 3, 4, 10]]),
    ),
    domain_padding = {"x": 15, "y": 5},
)
""" 

def render_boxplot():
    return pc.vstack(
        doctext(
            "BoxPlot is a wrapper component that renders a box plot graph. ",
            "BoxPlot expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a BoxPlot component with a box plot graph. ",
        ),      
        docdemo(box_plot_example),
    )

histogram_example = """pc.chart(
    pc.histogram( 
        data=pc.data("histogram", x=[1, 6, 3, 5, 3, 14, 18, 19, 20]),
    ),
)
"""

def render_histogram():
    return pc.vstack(
        doctext(
            "Histogram is a wrapper component that renders a histogram graph. ",
            "Histogram expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a Histogram component with a histogram graph. ",
        ),
        docdemo(histogram_example),
    )

error_bar_example = """pc.chart(
    pc.error_bar(
        data=pc.data("error_bar", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10], error_x=[0.1, 0.2, 0.3, 0.4, 0.5], error_y=[0.1, 0.2, 0.3, 0.4, 0.5]),
    ),
)
"""

def render_errorbar():
    return pc.vstack(
        doctext(
            "ErrorBar is a wrapper component that renders a error bar graph. ",
            "ErrorBar expects a data prop, which is a list of objects with x and y keys. ",
            "The following example shows a ErrorBar component with a error bar graph. ",
        ),
        docdemo(error_bar_example),
    )

stack_example = """pc.stack(
    pc.area(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    pc.area(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[5, 12, 4, 6, 1]),
    ),
)
"""

def render_stack():
    return pc.vstack(
        doctext(
            "Stack is a wrapper component that renders a given set of children in a stacked layout.",
        ),
        docdemo(stack_example),
    )

group_example = """pc.group(
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
    pc.group(
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

def render_group():
    return pc.vstack(
        doctext(
            "Group is a wrapper component that renders a given set of children in a grouped layout.",
        ),
        docdemo(group_example),
        doctext(
            "Group also accepts a style prop, which is an object of style properties. ",
        ),
        docdemo(group_example_style),
    )


voronoe_example = """pc.chart(
    pc.voronoi( 
        data=pc.data("voronoi", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
        style={"data": {"fill": "none", "stroke": "black", "strokeWidth": 1}}
    ),
)
"""

def render_voronoi():
    return pc.vstack(
        doctext(
            "Voronoi is a wrapper component that renders a voronoi graph. ",
            "Voronoi expects a data prop, which is a list of objects with x and y keys. ",
        ), 
        docdemo(voronoe_example),
    )


polar_example = """pc.chart(
    pc.line(
        data=pc.data("line", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 10]),
    ),
    polar = True
)
"""

def render_polar():
    return pc.vstack(
        doctext(
            "Polar is a wrapper component that renders a polar graph. ",
            "Polar expects a data prop, which is a list of objects with x and y keys. ",
        ),
        docdemo(polar_example),
    )