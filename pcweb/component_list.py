"""A list of components to show in the library."""

import reflex as rx

# Form components.
forms_list = [
    [rx.Upload],
    [rx.DebounceInput],
]

# Layout components.
layout_list = [
    [rx.Cond],
    [rx.Foreach],
    [rx.Fragment],
]

# Typography components.
typography_list = [
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

chakra_components = {
    "Typography": [
        [rx.chakra.Text],
        [rx.chakra.Heading],
        [rx.chakra.Highlight],
    ],
    "Forms": [
        [rx.chakra.FormControl, rx.chakra.FormLabel, rx.chakra.FormErrorMessage],
        [rx.chakra.Input],
        [rx.chakra.NumberInput],
        [rx.chakra.Checkbox],
        [rx.chakra.RadioGroup, rx.chakra.Radio],
        [rx.chakra.RangeSlider, rx.chakra.SliderTrack, rx.chakra.SliderFilledTrack, rx.chakra.SliderThumb],
        [rx.chakra.Select],
        [rx.chakra.Slider, rx.chakra.SliderTrack, rx.chakra.SliderFilledTrack, rx.chakra.SliderThumb, rx.chakra.SliderMark],
        [rx.chakra.Switch],
        [rx.chakra.TextArea],
    ],
    "Layout": [
        [rx.chakra.Box],
        [rx.chakra.Center],
        [rx.chakra.Container],
        [rx.chakra.Flex],
        [rx.chakra.Grid],
        [rx.chakra.Spacer],
        [rx.chakra.Stack],
        [rx.chakra.Wrap],
    ],
    "Navigation": [
        [rx.chakra.Breadcrumb, rx.chakra.BreadcrumbItem, rx.chakra.BreadcrumbLink],
        [rx.chakra.Link],
    ],
    "DataDisplay": [
        [rx.chakra.Badge],
        [rx.CodeBlock, rx.chakra.Code], # Including rx.CodeBlock for backwards compatibility
        [rx.chakra.Divider],
        [rx.chakra.List, rx.chakra.ListItem, rx.chakra.UnorderedList, rx.chakra.OrderedList],
        [rx.chakra.Stat, rx.chakra.StatLabel, rx.chakra.StatNumber, rx.chakra.StatHelpText, rx.chakra.StatArrow, rx.chakra.StatGroup],
        [rx.chakra.Table, rx.chakra.Thead, rx.chakra.Tbody, rx.chakra.Tfoot, rx.chakra.Tr, rx.chakra.Th, rx.chakra.Td, rx.chakra.TableCaption, rx.chakra.TableContainer],
    ],
    "Disclosure": [
        [rx.chakra.Accordion, rx.chakra.AccordionItem, rx.chakra.AccordionButton, rx.chakra.AccordionPanel, rx.chakra.AccordionIcon],
        [rx.chakra.Tabs, rx.chakra.Tab, rx.chakra.TabList, rx.chakra.TabPanel, rx.chakra.TabPanels],
    ],
    "Media": [
        [rx.chakra.Image],
        [rx.chakra.Icon],
        [rx.chakra.Avatar, rx.chakra.AvatarBadge, rx.chakra.AvatarGroup],
    ],
}

# The final component list
component_list = {
    "Typography": typography_list,
    "Forms": forms_list,
    "Layout": layout_list,
    "DataDisplay": datadisplay_list,
    "Graphing": graphing_list,
    "Media": media_list,
    "Other": other_list,
}

not_ready_components = [
    rx.IconButton,
    rx.AspectRatio,
]
