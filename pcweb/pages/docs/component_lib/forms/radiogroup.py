import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, demo_box_style, doccode, doclink, subheader

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
exec(basic_radio_state)


def render_radiogroup():
    return pc.vstack(
        doctext(
            "Radios are used when only one choice may be selected in a series of options."
        ),
        docdemo(
            basic_radio, state=basic_radio_state, comp=eval(basic_radio), context=True
        ),
        align_items="start",
    )
