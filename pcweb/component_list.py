"""A list of components to show in the library."""

import pynecone as pc

# Form components.
forms_list = [
    [pc.Button, pc.ButtonGroup],
    [pc.Checkbox],
    [pc.Editable, pc.EditableInput, pc.EditableTextarea, pc.EditablePreview],
    [pc.FormControl, pc.FormLabel, pc.FormErrorMessage, pc.FormHelperText],
    [pc.Input],
    [
        pc.NumberInput,
        pc.NumberInputField,
        pc.NumberInputStepper,
        pc.NumberIncrementStepper,
        pc.NumberDecrementStepper,
    ],
    [pc.PinInput],
    [pc.RadioGroup, pc.Radio],
    [
        pc.RangeSlider,
        pc.RangeSliderTrack,
        pc.RangeSliderFilledTrack,
        pc.RangeSliderThumb,
    ],
    [pc.Select],
    [pc.Slider, pc.SliderTrack, pc.SliderFilledTrack, pc.SliderThumb, pc.SliderMark],
    [pc.Switch],
    [pc.TextArea],
]

# Layout components.
layout_list = [
    [pc.Box],
    [pc.Center, pc.Circle, pc.Square],
    [pc.Cond],
    [pc.Container],
    [pc.Flex],
    [pc.Foreach],
    [pc.Grid, pc.GridItem],
    [pc.ResponsiveGrid],
    [pc.Spacer],
    [pc.Stack, pc.Hstack, pc.Vstack],
    [pc.Wrap, pc.WrapItem],
]

# Overlay components.
overlay_list = [
    [
        pc.AlertDialog,
        pc.AlertDialogBody,
        pc.AlertDialogHeader,
        pc.AlertDialogFooter,
        pc.AlertDialogContent,
        pc.AlertDialogOverlay,
    ],
    [
        pc.Drawer,
        pc.DrawerBody,
        pc.DrawerHeader,
        pc.DrawerFooter,
        pc.DrawerContent,
        pc.DrawerOverlay,
    ],
    [
        pc.Menu,
        pc.MenuButton,
        pc.MenuDivider,
        pc.MenuGroup,
        pc.MenuItem,
        pc.MenuItemOption,
        pc.MenuList,
        pc.MenuOptionGroup,
    ],
    [
        pc.Modal,
        pc.ModalBody,
        pc.ModalHeader,
        pc.ModalFooter,
        pc.ModalContent,
        pc.ModalOverlay,
    ],
    [
        pc.Popover,
        pc.PopoverHeader,
        pc.PopoverBody,
        pc.PopoverFooter,
        pc.PopoverTrigger,
        pc.PopoverAnchor,
        pc.PopoverArrow,
    ],
    [pc.Tooltip],
]

# Typography components.
typography_list = [[pc.Text], [pc.Heading], [pc.Span], [pc.Markdown]]

# Navigation components.
navigation_list = [
    [pc.Breadcrumb, pc.BreadcrumbItem, pc.BreadcrumbLink],
    [pc.Link],
]

# Media components.
media_list = [[pc.Avatar, pc.AvatarBadge, pc.AvatarGroup], [pc.Image], [pc.Icon]]

# Data display components.
datadisplay_list = [
    [pc.Badge],
    [pc.CodeBlock, pc.Code],
    [pc.Divider],
    [pc.DataTable],
    [pc.List, pc.ListItem, pc.UnorderedList, pc.OrderedList],
    [pc.Stat, pc.StatLabel, pc.StatNumber, pc.StatHelpText, pc.StatArrow, pc.StatGroup],
    [
        pc.Table,
        pc.Thead,
        pc.Tbody,
        pc.Tfoot,
        pc.Tr,
        pc.Th,
        pc.Td,
        pc.TableCaption,
        pc.TableContainer,
    ],
]

# Disclosure components.
disclosure_list = [
    [
        pc.Accordion,
        pc.AccordionItem,
        pc.AccordionButton,
        pc.AccordionPanel,
        pc.AccordionIcon,
    ],
    [pc.Tabs, pc.Tab, pc.TabList, pc.TabPanel, pc.TabPanels],
]

# Feedback components.
feedback_list = [
    [pc.Alert, pc.AlertIcon, pc.AlertTitle, pc.AlertDescription],
    [pc.CircularProgress, pc.CircularProgressLabel],
    [pc.Progress],
    [pc.Skeleton, pc.SkeletonCircle, pc.SkeletonText],
    [pc.Spinner],
]

# Graphing components.
graphing_list = [[pc.Plotly]]

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
}
