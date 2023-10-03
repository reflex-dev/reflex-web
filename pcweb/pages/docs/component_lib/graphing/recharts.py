import reflex as rx
from pcweb import flexdown


def render_areachart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/area_chart.md")
    return rx.box(
        *output,
    )

def render_barchart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/bar_chart.md")
    return rx.box(
        *output,
    )

def render_composedchart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/composed_chart.md")
    return rx.box(
        *output,
    )

def render_funnelchart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/funnel_chart.md")
    return rx.box(
        *output,
    )

def render_linechart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/line_chart.md")
    return rx.box(
        *output,
    )

def render_piechart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/pie_chart.md")
    return rx.box(
        *output,
    )

def render_radarchart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/radar_chart.md")
    return rx.box(
        *output,
    )

def render_scatterchart():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/scatter_chart.md")
    return rx.box(
        *output,
    )

def render_treemap():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/treemap.md")
    return rx.box(
        *output,
    )


def render_errorbar():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/error_bar.md")
    return rx.box(
        *output,
    )

def render_referenceline():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/reference.md")
    return rx.box(
        *output,
    )

def render_cartesianaxis():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/cartesian_axis_grid.md")
    return rx.box(
        *output,
    )

def render_xaxis():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/axis.md")
    return rx.box(
        *output,
    )

def render_brush():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/brush.md")
    return rx.box(
        *output,
    )

def render_legend():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/legend.md")
    return rx.box(
        *output,
    )

def render_label():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/label.md")
    return rx.box(
        *output,
    )

def render_graphingtooltip():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/graphing/tooltip.md")
    return rx.box(
        *output,
    )                      