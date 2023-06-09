import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

basic_editable_class = """class EditableState(State):
    example_input: str
    example_textarea: str
    example_state: str

    def set_uppertext(self, example_state: str):
        print("testing")
        self.example_state = example_state.upper()
"""
basic_editable_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_input(),
    placeholder="An input example...",
    on_submit=EditableState.set_uppertext,
    width="100%", 
    )
"""

exec(basic_editable_class)

textarea_editable_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_textarea(),
    placeholder="A textarea example...",
    on_submit=EditableState.set_example_textarea,
    width="100%",
)
"""

state_editable_blur_example = """pc.editable(
    pc.editable_preview(),
    pc.editable_input(),
    on_blur=EditableState.set_uppertext,
    width="100%",
)
"""


def render_editable():
    return pc.vstack(
        doctext(
            "Editable is used for inline renaming of some text. It appears as normal UI text but transforms into a text input field when the user clicks on or focuses it."
        ),
        docdemo(
            basic_editable_example,
            state=basic_editable_class,
            comp=eval(basic_editable_example),
            context=True,
        ),
        doctext(
            "Another variant of editable can be made with a textarea instead of an input."
        ),
        docdemo(textarea_editable_example, comp=eval(textarea_editable_example)),
        align_items="start",
    )
