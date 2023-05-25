import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

basic_radio_state = """
options = ["Option 1", "Option 2", "Option 3"]

class RadioState(State):
    text: str = "No Selection"
"""
basic_radio = """pc.vstack(
    pc.badge(RadioState.text, color_scheme="green"),
    pc.radio_group(
        options,
        on_change=RadioState.set_text,
    ),
)
"""

default_checked_radio = """pc.vstack(
    pc.radio_group(
        options,
        default_value="Option 2",
        default_checked=True,
    ),
)
"""

spacing_radio = """pc.radio_group(
    pc.radio_group(
        pc.hstack(
            pc.foreach(
                options,
                lambda option: pc.radio(option),
            ),
        spacing="2em",
        ),
    ),
)
"""

vertical_radio = """pc.radio_group(
    pc.radio_group(
        pc.vstack(
            pc.foreach(
                options,
                lambda option: pc.radio(option),
            ),
        ),
    ),
)
"""

exec(basic_radio_state)


def render_radiogroup():
    return pc.vstack(
        doctext(
            "Radios are used when only one choice may be selected in a series of options."
        ),
        docdemo(
            basic_radio, state=basic_radio_state, comp=eval(basic_radio), context=True
        ),
        doctext(
            "The `default_value` and `default_checked` arguments can be used to set the default value of the radio group."
        ),
        docdemo(
            default_checked_radio,
            state=basic_radio_state,
            comp=eval(default_checked_radio),
            context=True,
        ),
        doctext(
            "A hstack with the `spacing` argument can be used to set the spacing between the radio buttons."
        ),
        docdemo(
            spacing_radio,
            state=basic_radio_state,
            comp=eval(spacing_radio),
            context=True,
        ),
        doctext("A vstack can be used to stack the radio buttons vertically."),
        docdemo(
            vertical_radio,
            state=basic_radio_state,
            comp=eval(vertical_radio),
            context=True,
        ),
        align_items="start",
    )
