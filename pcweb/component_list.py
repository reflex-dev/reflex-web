"""A list of components to show in the library."""

import reflex as rx

# Form components.
forms_list = [
    [rx.Form],
    [rx.FormControl, rx.FormLabel, rx.FormErrorMessage, rx.FormHelperText],
    [rx.Button, rx.ButtonGroup, rx.IconButton],
    [rx.Checkbox],
    [rx.Editable, rx.EditableInput, rx.EditableTextarea, rx.EditablePreview],
    [rx.Input],
    [
        rx.NumberInput,
        rx.NumberInputField,
        rx.NumberInputStepper,
        rx.NumberIncrementStepper,
        rx.NumberDecrementStepper,
    ],
    [rx.PinInput],
    [rx.RadioGroup, rx.Radio],
    [
        rx.RangeSlider,
        rx.RangeSliderTrack,
        rx.RangeSliderFilledTrack,
        rx.RangeSliderThumb,
    ],
    [rx.Select],
    [rx.Slider, rx.SliderTrack, rx.SliderFilledTrack, rx.SliderThumb, rx.SliderMark],
    [rx.Switch],
    [rx.TextArea],
    # [rx.CopyToClipboard],
    [rx.Upload],
    [rx.DebounceInput],
]

# Layout components.
layout_list = [
    [rx.Box],
    [rx.Center, rx.Circle, rx.Square],
    [rx.Cond],
    [rx.Container],
    [rx.Flex],
    [rx.Foreach],
    [rx.Grid, rx.GridItem],
    [rx.ResponsiveGrid],
    [rx.Card, rx.CardHeader, rx.CardBody, rx.CardFooter],
    [rx.Spacer],
    [rx.Stack, rx.Hstack, rx.Vstack],
    [rx.Wrap, rx.WrapItem],
    [rx.AspectRatio],
    [rx.Fragment],
]

# Overlay components.
overlay_list = [
    [
        rx.AlertDialog,
        rx.AlertDialogBody,
        rx.AlertDialogHeader,
        rx.AlertDialogFooter,
        rx.AlertDialogContent,
        rx.AlertDialogOverlay,
    ],
    [
        rx.Drawer,
        rx.DrawerBody,
        rx.DrawerHeader,
        rx.DrawerFooter,
        rx.DrawerContent,
        rx.DrawerOverlay,
    ],
    [
        rx.Menu,
        rx.MenuButton,
        rx.MenuDivider,
        rx.MenuGroup,
        rx.MenuItem,
        rx.MenuItemOption,
        rx.MenuList,
        rx.MenuOptionGroup,
    ],
    [
        rx.Modal,
        rx.ModalBody,
        rx.ModalHeader,
        rx.ModalFooter,
        rx.ModalContent,
        rx.ModalOverlay,
    ],
    [
        rx.Popover,
        rx.PopoverHeader,
        rx.PopoverBody,
        rx.PopoverFooter,
        rx.PopoverTrigger,
        rx.PopoverAnchor,
        rx.PopoverArrow,
    ],
    [rx.Tooltip],
]

# Typography components.
typography_list = [
    [rx.Text],
    [rx.Heading],
    [rx.Span],
    [rx.Markdown],
    [rx.Highlight],
]

# Navigation components.
navigation_list = [
    [rx.Breadcrumb, rx.BreadcrumbItem, rx.BreadcrumbLink],
    [rx.Link],
]

# Media components.
media_list = [
    [rx.Avatar, rx.AvatarBadge, rx.AvatarGroup],
    [rx.Image],
    [rx.Icon],
]

# Data display components.
datadisplay_list = [
    [rx.Badge],
    [rx.CodeBlock, rx.Code],
    [rx.Divider],
    [rx.DataTable],
    [rx.List, rx.ListItem, rx.UnorderedList, rx.OrderedList],
    [
        rx.Stat,
        rx.StatLabel,
        rx.StatNumber,
        rx.StatHelpText,
        rx.StatArrow,
        rx.StatGroup,
    ],
    [
        rx.Table,
        rx.Thead,
        rx.Tbody,
        rx.Tfoot,
        rx.Tr,
        rx.Th,
        rx.Td,
        rx.TableCaption,
        rx.TableContainer,
    ],
]

# Disclosure components.
disclosure_list = [
    [
        rx.Accordion,
        rx.AccordionItem,
        rx.AccordionButton,
        rx.AccordionPanel,
        rx.AccordionIcon,
    ],
    [rx.Tabs, rx.Tab, rx.TabList, rx.TabPanel, rx.TabPanels],
]

# Feedback components.
feedback_list = [
    [rx.Alert, rx.AlertIcon, rx.AlertTitle, rx.AlertDescription],
    [rx.CircularProgress, rx.CircularProgressLabel],
    [rx.Progress],
    [rx.Skeleton, rx.SkeletonCircle, rx.SkeletonText],
    [rx.Spinner],
]

# Graphing components.
graphing_list = [
    [rx.Chart, rx.ChartGroup, rx.ChartStack],
    [rx.Area],
    [rx.BoxPlot],
    [rx.Candlestick],
    [rx.ErrorBar],
    [rx.Line],
    [rx.Bar],
    [rx.Histogram],
    [rx.Pie],
    [rx.Polar],
    [rx.Scatter],
    [rx.Voronoi],
    [rx.Plotly],
]

# Other
other_list = [[rx.Html]]

# The final component list
component_list = {
    "Typography": typography_list,
    "Forms": forms_list,
    "Layout": layout_list,
    "Navigation": navigation_list,
    "DataDisplay": datadisplay_list,
    "Graphing": graphing_list,
    "Disclosure": disclosure_list,
    "Feedback": feedback_list,
    "Media": media_list,
    "Overlay": overlay_list,
    "Other": other_list,
}

not_ready_components = [
    rx.CopyToClipboard,
    rx.IconButton,
    rx.AspectRatio,
]
