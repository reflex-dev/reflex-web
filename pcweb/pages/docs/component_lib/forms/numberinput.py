import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext, demo_box_style, doccode, doclink, subheader

code22 = """pc.number_input(
    on_change=NumberInputState.set_number,
)
"""
code23 = """class NumberInputState(State):
    number: int
"""
exec(code23)


def render_numberinput():
    return pc.vstack(
        doctext(
            "The NumberInput component is similar to the Input component, but it has controls for incrementing or decrementing numeric values."
        ),
        docdemo(code22, state=code23, comp=eval(code22), context=True),
        align_items="start",
    )

