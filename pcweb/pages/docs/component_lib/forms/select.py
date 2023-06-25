import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

basic_select_state = """from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class SelectState(State):
    option: str = "No selection yet."

"""


multi_select_state = """from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class MultiSelectState(State):
    option: List[str] = []
"""


basic_select = """rx.vstack(
    rx.heading(SelectState.option),
    rx.select(
        options,
        placeholder="Select an example.",
        on_change=SelectState.set_option,
        color_schemes="twitter",
    ),
)
"""


multi_select = """rx.vstack(
    rx.heading(MultiSelectState.option),
    rx.select(
        options, 
        placeholder="Select examples", 
        is_multi=True,
        on_change=MultiSelectState.set_option,
        close_menu_on_select=False,
        color_schemes="twitter",
    ),
)
"""


customized_select = """rx.vstack(
    rx.select(options, placeholder="Select an example.", size="xs"),
    rx.select(options, placeholder="Select an example.", size="sm"),
    rx.select(options, placeholder="Select an example.", size="md"),
    rx.select(options, placeholder="Select an example.", size="lg"),
)
"""

styled_select = """rx.vstack(
    rx.select(options, placeholder="Select an example.", variant="outline"),
    rx.select(options, placeholder="Select an example.", variant="filled"),
    rx.select(options, placeholder="Select an example.", variant="flushed"),
    rx.select(options, placeholder="Select an example.", variant="unstyled"),
)
"""

fully_styled_select = """rx.select(
    options,
    placeholder="Select an example.",
    color = "white",
    bg = "#68D391",
    border_color = "#38A169",
)
"""


exec(basic_select_state)
exec(multi_select_state)


def render_select():
    return rx.vstack(
        doctext("Simple Select (one choice)"),
        docdemo(
            basic_select,
            state=basic_select_state,
            comp=eval(basic_select),
            context=True,
        ),
        doctext("Select with multiple choices"),
        docdemo(
            multi_select,
            state=multi_select_state,
            comp=eval(multi_select),
            context=True,
        ),
        docdemo(customized_select, comp=eval(customized_select)),
        docdemo(styled_select, comp=eval(styled_select)),
        docdemo(fully_styled_select, comp=eval(fully_styled_select)),
        align_items="start",
    )
