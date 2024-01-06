"""A list of components to show in the library."""

import reflex as rx

from reflex.components.radix.themes import (
    Text, 
    Badge, 
    Heading, 
    Code, 
    Link, 
    Blockquote, 
    Em, 
    Kbd, 
    Quote, 
    Strong,
    CalloutRoot,
    Checkbox,
    AlertDialogTrigger,
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

chakra_components = {
    "Typography": [
        [rx.chakra.Text],
        [rx.chakra.Heading],
        [rx.chakra.Highlight],
    ],
    "Forms": [
        [rx.chakra.Form],
        [rx.chakra.FormControl, rx.chakra.FormLabel, rx.chakra.FormErrorMessage, rx.chakra.FormHelperText],
        [rx.chakra.Button, rx.chakra.IconButton],
        [rx.chakra.ButtonGroup],
        [rx.chakra.Checkbox],
        [rx.chakra.Editable, rx.chakra.EditablePreview, rx.chakra.EditableInput, rx.chakra.EditableTextarea],
        [rx.chakra.Input],
        [rx.chakra.NumberInput, rx.chakra.NumberInputField, rx.chakra.NumberInputStepper, rx.chakra.NumberIncrementStepper, rx.chakra.NumberDecrementStepper],
        [rx.chakra.PinInput],
        [rx.chakra.RadioGroup, rx.chakra.Radio],
        [rx.chakra.RangeSlider, rx.chakra.SliderTrack, rx.chakra.SliderFilledTrack, rx.chakra.SliderThumb],
        [rx.chakra.Select],
        [rx.chakra.Slider, rx.chakra.SliderTrack, rx.chakra.SliderFilledTrack, rx.chakra.SliderThumb, rx.chakra.SliderMark],
        [rx.chakra.Switch],
        [rx.chakra.TextArea],
    ],
    "Layout": [
        [rx.chakra.AspectRatio],
        [rx.chakra.Box],
        [rx.chakra.Card, rx.chakra.CardHeader, rx.chakra.CardBody, rx.chakra.CardFooter],
        [rx.chakra.Center, rx.chakra.Circle, rx.chakra.Square],
        [rx.chakra.Container],
        [rx.chakra.Flex],
        [rx.chakra.Grid, rx.chakra.GridItem],
        [rx.chakra.ResponsiveGrid],
        [rx.chakra.Spacer],
        [rx.chakra.Stack, rx.chakra.Hstack, rx.chakra.Vstack],
        [rx.chakra.Wrap, rx.chakra.WrapItem],
    ],
    "Navigation": [
        [rx.chakra.Breadcrumb, rx.chakra.BreadcrumbItem, rx.chakra.BreadcrumbLink],
        [rx.chakra.Link],
    ],
    "Overlay": [
        [rx.chakra.AlertDialog, rx.chakra.AlertDialogBody, rx.chakra.AlertDialogFooter, rx.chakra.AlertDialogHeader, rx.chakra.AlertDialogContent, rx.chakra.AlertDialogOverlay],
        [rx.chakra.Drawer, rx.chakra.DrawerBody, rx.chakra.DrawerFooter, rx.chakra.DrawerHeader, rx.chakra.DrawerContent, rx.chakra.DrawerOverlay],
        [rx.chakra.Menu, rx.chakra.MenuButton, rx.chakra.MenuList, rx.chakra.MenuItem, rx.chakra.MenuGroup, rx.chakra.MenuDivider, rx.chakra.MenuOptionGroup, rx.chakra.MenuItemOption],
        [rx.chakra.Modal, rx.chakra.ModalOverlay, rx.chakra.ModalContent, rx.chakra.ModalHeader, rx.chakra.ModalBody, rx.chakra.ModalFooter],
        [rx.chakra.Popover, rx.chakra.PopoverTrigger, rx.chakra.PopoverHeader, rx.chakra.PopoverBody, rx.chakra.PopoverFooter, rx.chakra.PopoverArrow, rx.chakra.PopoverAnchor],
        [rx.chakra.Tooltip],
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
    "Feedback": [
        [rx.chakra.Alert, rx.chakra.AlertIcon, rx.chakra.AlertTitle, rx.chakra.AlertDescription],
        [rx.chakra.Progress],
        [rx.chakra.Skeleton, rx.chakra.SkeletonText, rx.chakra.SkeletonCircle],
        [rx.chakra.Spinner],
        [rx.chakra.CircularProgress, rx.chakra.CircularProgressLabel],
    ]
}

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

not_ready_components = [
    rx.IconButton,
    rx.AspectRatio,
]
