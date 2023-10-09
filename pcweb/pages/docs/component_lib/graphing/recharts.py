import reflex as rx
from pcweb.flexdown import component_map
import flexdown


def render_areachart():
    return flexdown.render_file(
        "docs/library/graphing/area_chart.md", component_map=component_map
    )


def render_barchart():
    return flexdown.render_file(
        "docs/library/graphing/bar_chart.md", component_map=component_map
    )


def render_composedchart():
    return flexdown.render_file(
        "docs/library/graphing/composed_chart.md", component_map=component_map
    )


def render_funnelchart():
    return flexdown.render_file(
        "docs/library/graphing/funnel_chart.md", component_map=component_map
    )


def render_linechart():
    return flexdown.render_file(
        "docs/library/graphing/line_chart.md", component_map=component_map
    )


def render_piechart():
    return flexdown.render_file(
        "docs/library/graphing/pie_chart.md", component_map=component_map
    )


def render_radarchart():
    return flexdown.render_file(
        "docs/library/graphing/radar_chart.md", component_map=component_map
    )


def render_scatterchart():
    return flexdown.render_file(
        "docs/library/graphing/scatter_chart.md", component_map=component_map
    )


def render_treemap():
    return flexdown.render_file(
        "docs/library/graphing/treemap.md", component_map=component_map
    )


def render_errorbar():
    return flexdown.render_file(
        "docs/library/graphing/error_bar.md", component_map=component_map
    )


def render_referenceline():
    return flexdown.render_file(
        "docs/library/graphing/reference.md", component_map=component_map
    )


def render_cartesianaxis():
    return flexdown.render_file(
        "docs/library/graphing/cartesian_axis_grid.md", component_map=component_map
    )


def render_xaxis():
    return flexdown.render_file(
        "docs/library/graphing/axis.md", component_map=component_map
    )


def render_brush():
    return flexdown.render_file(
        "docs/library/graphing/brush.md", component_map=component_map
    )


def render_legend():
    return flexdown.render_file(
        "docs/library/graphing/legend.md", component_map=component_map
    )


def render_label():
    return flexdown.render_file(
        "docs/library/graphing/label.md", component_map=component_map
    )


def render_graphingtooltip():
    return flexdown.render_file(
        "docs/library/graphing/tooltip.md", component_map=component_map
    )
