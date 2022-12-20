import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

code79 = """pc.hstack(
    pc.avatar(size="sm"),
    pc.avatar(name="Barack Obama", size="md"),
    pc.avatar(name="Donald Trump", size="lg"),
    pc.avatar(name="Joe Biden", size="xl"),
)
"""
code80 = """ pc.avatar_group(
    pc.avatar(name="Barack Obama"),
    pc.avatar(name="Donald Trump"),
    pc.avatar(name="Joe Biden"),
)
"""
code81 = """pc.avatar_group(
    pc.avatar(
        pc.avatar_badge(
            box_size="1.25em", bg="green.500", border_color="green.500"
        ),
        name="Barack Obama",
    ),
    pc.avatar(
        pc.avatar_badge(
            box_size="1.25em", bg="yellow.500", border_color="red.500"
        ),
        name="Donald Trump",
    ),
)
"""
code82 = """pc.avatar_group(
    *([pc.avatar(name="Barack Obama")] * 5),
    size="md",
    max_=3,
)
"""
# Media
def render_avatar():
    return pc.box(
        doctext(
            "The Avatar component is used to represent a user, and displays the profile picture, initials or fallback icon."
        ),
        docdemo(code79),
        doctext(
            "Avatar components can be grouped into avatar groups for easier display."
        ),
        docdemo(code80),
        doctext(
            "Badges can also be applied to show elements about the avatar such as activity."
        ),
        docdemo(code81),
        doctext(
            "If there are too many avatar to display a limit can be set using the max_ prop."
        ),
        docdemo(code82),
        align_items="start",
    )


codeicon1 = """pc.icon(
    tag = "CalendarIcon",
)
"""


icon_list = [
    "AddIcon",
    "ArrowBackIcon",
    "ArrowDownIcon",
    "ArrowForwardIcon",
    "ArrowLeftIcon",
    "ArrowRightIcon",
    "ArrowUpIcon",
    "ArrowUpDownIcon",
    "AtSignIcon",
    "AttachmentIcon",
    "BellIcon",
    "CalendarIcon",
    "CheckCircleIcon",
    "CheckIcon",
    "ChevronDownIcon",
    "ChevronLeftIcon",
    "ChevronRightIcon",
    "ChevronUpIcon",
    "CloseIcon",
    "CopyIcon",
    "DeleteIcon",
    "DownloadIcon",
    "DragHandleIcon",
    "EditIcon",
    "EmailIcon",
    "ExternalLinkIcon",
    "HamburgerIcon",
    "InfoIcon",
    "InfoOutlineIcon",
    "LinkIcon",
    "LockIcon",
    "MinusIcon",
    "MoonIcon",
    "NotAllowedIcon",
    "PhoneIcon",
    "PlusSquareIcon",
    "QuestionIcon",
    "QuestionOutlineIcon",
    "RepeatIcon",
    "RepeatClockIcon",
    "SearchIcon",
    "Search2Icon",
    "SettingsIcon",
    "SmallAddIcon",
    "SmallCloseIcon",
    "SpinnerIcon",
    "StarIcon",
    "SunIcon",
    "TimeIcon",
    "TriangleDownIcon",
    "TriangleUpIcon",
    "UnlockIcon",
    "UpDownIcon",
    "ViewIcon",
    "ViewOffIcon",
    "WarningIcon",
    "WarningTwoIcon",
]


def render_icon():
    icons = []
    for icon in icon_list:
        icons.append(
            pc.vstack(
                pc.icon(tag=icon),
                pc.text(icon),
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
        )

    grid = pc.responsive_grid(
        *icons,
        columns=[2, 2, 3, 3, 4],
        spacing="1em",
    )

    return pc.box(
        doctext(
            "The Icon component is used to display an icon from a library of icons."
        ),
        docdemo(codeicon1),
        doctext("Use the tag prop to specify the icon to display."),
        pc.alert(
            pc.alert_icon(),
            pc.alert_title("Below is a list of all available icons."),
            status="success",
        ),
        pc.divider(),
        grid,
        align_items="start",
    )


code83 = """pc.image(src="/black.png", width="100px", height="auto")
"""
code84 = """pc.image(
    src="/black.png",
    width="100px",
    height="auto",
    border_radius="15px 50px",
    border="5px solid #555",
    box_shadow="lg",
)
"""


def render_image():
    return pc.vstack(
        doctext(
            "The image component can display an image given a src path as an argment. This could either be a local path from the assets folder or an external link."
        ),
        docdemo(code83),
        doctext("Image composes a box and can be styled simlarly."),
        docdemo(code84),
        align_items="start",
    )
