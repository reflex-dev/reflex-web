import reflex as rx

from pcweb.templates.docpage import docpage
from pcweb import flexdown

basic_button_group = """rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
        )
"""

button_group_attached = """rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            is_attached=True,
        )

"""

button_group_variant = """rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            variant='ghost',
        )

"""

button_group_sizes = """rx.button_group(
            rx.button('Large Button', size='lg'),
            rx.button('Medium Button', size='md'),
            rx.button('Small Button', size='sm'),
        )
"""

button_group_disable = """rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            is_disabled=True,
        )

"""

button_group_spacing = """rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            spacing=8,
        )

"""

@docpage()
def button_group():
    _, output = flexdown.read("docs/library/forms/button_group.md")
    return rx.box(
        *output,
    )
