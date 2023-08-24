import reflex as rx
from reflex.components.media.icon import ICON_LIST

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, doccode, docdemobox

from PIL import Image
import random
import requests


code79 = """rx.hstack(
    rx.avatar(size="sm"),
    rx.avatar(name="Barack Obama", size="md"),
    rx.avatar(name="Donald Trump", size="lg"),
    rx.avatar(name="Joe Biden", size="xl"),
)
"""
code80 = """ rx.avatar_group(
    rx.avatar(name="Barack Obama"),
    rx.avatar(name="Donald Trump"),
    rx.avatar(name="Joe Biden"),
)
"""
code81 = """rx.avatar_group(
    rx.avatar(
        rx.avatar_badge(
            box_size="1.25em", bg="green.500", border_color="green.500"
        ),
        name="Barack Obama",
    ),
    rx.avatar(
        rx.avatar_badge(
            box_size="1.25em", bg="yellow.500", border_color="red.500"
        ),
        name="Donald Trump",
    ),
)
"""
code82 = """rx.avatar_group(
    *([rx.avatar(name="Barack Obama")] * 5),
    size="md",
    max_=3,
)
"""


# Media
def render_avatar():
    return rx.box(
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


codeicon1 = """rx.icon(
    tag = "calendar",
)
"""


def render_icon():
    icons = []
    for icon in ICON_LIST:
        icons.append(
            rx.vstack(
                rx.icon(tag=icon),
                rx.text(icon),
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
        )

    grid = rx.responsive_grid(
        *icons,
        columns=[2, 2, 3, 3, 4],
        spacing="1em",
    )

    return rx.box(
        doctext(
            "The Icon component is used to display an icon from a library of icons."
        ),
        docdemo(codeicon1),
        doctext("Use the tag prop to specify the icon to display."),
        rx.alert(
            rx.alert_icon(),
            rx.alert_title("Below is a list of all available icons."),
            status="success",
        ),
        rx.divider(),
        grid,
        align_items="start",
    )


code83 = """rx.image(src="/reflex_logo.png", width="100px", height="auto")
"""
code84 = """rx.image(
    src="/reflex_logo.png",
    width="100px",
    height="auto",
    border_radius="15px 50px",
    border="5px solid #555",
    box_shadow="lg",
)
"""


image_state = """class ImageState(State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)
"""
image_pil_example = """rx.vstack(
        rx.image(src=ImageState.image, alt="=An Unsplash Image")
    )
"""


image_pil_example_show = """rx.vstack(
        rx.image(src="https://picsum.photos/id/1/200/300", alt="=An Unsplash Image")
    )
"""


def render_image():
    return rx.vstack(
        doctext(
            "The image component can display an image given a src path as an argment. This could either be a local path from the assets folder or an external link."
        ),
        docdemo(code83),
        doctext("Image composes a box and can be styled simlarly."),
        docdemo(code84),
        doctext("You can also pass a PIL image object as the src."),
        docdemobox(eval(image_pil_example_show)),
        doccode(image_state),
        doccode(image_pil_example),
        align_items="start",
    )
