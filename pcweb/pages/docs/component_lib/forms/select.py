import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

basic_select_state = """
options = ["Option 1", "Option 2", "Option 3"]

class SelectState(State):
    option: str = "No selection yet."

"""

basic_select = """pc.vstack(
    pc.heading(SelectState.option),
    pc.select(
        options,
        placeholder="Select an example.",
        on_change=SelectState.set_option,
    ),
)
"""

customized_select = """pc.vstack(
    pc.select(options, placeholder="Select an example.", size="xs"),
    pc.select(options, placeholder="Select an example.", size="sm"),
    pc.select(options, placeholder="Select an example.", size="md"),
    pc.select(options, placeholder="Select an example.", size="lg"),
)
"""

styled_select = """pc.vstack(
    pc.select(options, placeholder="Select an example.", variant="outline"),
    pc.select(options, placeholder="Select an example.", variant="filled"),
    pc.select(options, placeholder="Select an example.", variant="flushed"),
    pc.select(options, placeholder="Select an example.", variant="unstyled"),
)
"""

fully_styled_select = """pc.select(
    options,
    placeholder="Select an example.",
    color = "white",
    bg = "#68D391",
    border_color = "#38A169",
)
"""

exec(basic_select_state)


def render_select():
    return pc.vstack(
        doctext(""),
        docdemo(
            basic_select,
            state=basic_select_state,
            comp=eval(basic_select),
            context=True,
        ),
        docdemo(customized_select, comp=eval(customized_select)),
        docdemo(styled_select, comp=eval(styled_select)),
        docdemo(fully_styled_select, comp=eval(fully_styled_select)),
        align_items="start",
    )
