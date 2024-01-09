"""A list of components to show in the library."""

import reflex as rx
from reflex.components.radix.themes import (
    AlertDialogTrigger,
    Badge,
    Blockquote,
    CalloutRoot,
    Checkbox,
    Code,
    DialogRoot,
    Em,
    Heading,
    Kbd,
    Link,
    Quote,
    Strong,
    Text,
)

# Form components.
forms_list = [
    [Checkbox],
    [rx.Upload],
    [rx.Editor],
    [rx.DebounceInput],
]

# Layout components.
layout_list = [
    [rx.Cond],
    [rx.Foreach],
    [rx.Fragment],
]

# Feedback components.
feedback_list = [
    [CalloutRoot],
]

# Overlay components.
overlay_list = [
    [AlertDialogTrigger],
    [DialogRoot],
]

# Typography components.
typography_list = [
    [Blockquote],
    [Code],
    [Em],
    [Heading],
    [Kbd],
    [Link],
    [Quote],
    [Strong],
    [Text],
    [rx.Span],
    [rx.Markdown],
]

# Media components.
media_list = [
    [rx.Audio],
    [rx.Image],
    [rx.Video],
]

# Data display components.
datadisplay_list = [
    [rx.CodeBlock],
    [Badge],
    [rx.DataTable],
    [rx.DataEditor],
]

# Graphing components.
graphing_list = [
    ["Core Charts"],
    [rx.recharts.AreaChart, rx.recharts.Area],
    [rx.recharts.BarChart, rx.recharts.RadialBarChart, rx.recharts.Bar],
    [rx.recharts.ComposedChart],
    [rx.recharts.FunnelChart, rx.recharts.Funnel],
    [rx.recharts.LineChart, rx.recharts.Line],
    [rx.recharts.PieChart],
    [rx.recharts.RadarChart],
    [rx.recharts.ScatterChart, rx.recharts.Scatter],
    ["Core Helpers"],
    [rx.recharts.ReferenceLine, rx.recharts.ReferenceDot, rx.recharts.ReferenceArea],
    [rx.recharts.CartesianAxis, rx.recharts.CartesianGrid],
    [rx.recharts.XAxis, rx.recharts.YAxis, rx.recharts.ZAxis],
    [rx.recharts.Brush],
    [rx.recharts.Legend],
    [rx.recharts.Label, rx.recharts.LabelList],
    [rx.recharts.GraphingTooltip],
    ["Other Graphing"],
    [rx.Plotly],
]

# Other
other_list = [[rx.Html], [rx.Script]]

# The final component list
component_list = {
    "Typography": typography_list,
    "Forms": forms_list,
    "Feedback": feedback_list,
    "Layout": layout_list,
    "DataDisplay": datadisplay_list,
    "Overlay": overlay_list,
    "Graphing": graphing_list,
    "Media": media_list,
    "Other": other_list,
}
