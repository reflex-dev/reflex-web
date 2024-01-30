"""Components for rendering code demos in the documentation."""

import reflex as rx
import textwrap
from typing import Any, Callable
from .code import code_block
import black

demo_box_style = {
    "bg": rx.color("mauve", 2),
    "border_radius": "8px;",
    "box_shadow": "rgba(99, 99, 99, 0.1) 0px 2px 8px 0px;",
    "padding": 5,
    "width": "100%",
    "overflow_x": "auto",
    "border": f"2px solid {rx.color('mauve', 2)}",
    "align_items": "center",
    "justify_content": "center",
}
 
def docdemobox(*children, **props) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.vstack(
        *children,
        style=demo_box_style,
        **props,
    )

def doccode(
    code: str,
    language: str = "python",
    lines: tuple[int, int] | None = None,
    theme: str = "light",
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        code: The code to display.
        language: The language of the code.
        lines: The start/end lines to display.
        props: Props to apply to the code snippet.

    Returns:
        The styled code snippet.
    """
    # For Python snippets, lint the code with black.
    if language == "python":
        code = black.format_str(
            textwrap.dedent(code), mode=black.FileMode(line_length=60)
        ).strip()

    # If needed, only display a subset of the lines.
    if lines is not None:
        code = textwrap.dedent(
            "\n".join(code.strip().split("\n")[lines[0] : lines[1]])
        ).strip()

    # Create the code snippet.
    cb = code_block
    return cb(
        code=code,
        language=language,
    )

def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    demobox_props: dict[str, Any] | None = None,
    **props,
) -> rx.Component:
    """Create a documentation demo with code and output.

    Args:
        code: The code to render the component.
        state: Code for any state needed for the component.
        comp: The pre-rendered component.
        context: Whether to wrap the render code in a function.
        props: Additional props to apply to the component.

    Returns:
        The styled demo.
    """
    # Render the component if necessary.
    if comp is None:
        comp = eval(code)

    # Wrap the render code in a function if needed.
    if context:
        code = f"""def index():
        return {code}
        """

    # Add the state code
    if state is not None:
        code = state + code

    # Create the demo.
    return rx.vstack(
        docdemobox(comp, **(demobox_props or {})),
        doccode(code),
        width="100%",
        padding_bottom="2em",
        spacing="1em",
        **props,
    )

tab_style = {
    "color": "#494369",
    "font_weight": 600,
    "_selected": {
        "color": "#5646ED",
        "bg": "#F5EFFE",
        "padding_x": "0.5em",
        "padding_y": "0.25em",
        "border_radius": "8px",
    },
}

def docgraphing(
    code: str,
    comp: rx.Component | None = None,
    data: str | None = None,
):
    return rx.vstack(
        rx.flex(
            comp,
            height="15em",
            style=demo_box_style,
        ),
        rx.tabs(
            rx.tab_list(
                rx.tab("Code", style=tab_style),
                rx.tab("Data", style=tab_style),
                padding_x=0,
            ),
            rx.tab_panels(
                rx.tab_panel(
                    doccode(code), width="100%", padding_x=0, padding_y=".25em"
                ),
                rx.tab_panel(
                    doccode(data or ""), width="100%", padding_x=0, padding_y=".25em"
                ),
                width="100%",
            ),
            variant="unstyled",
            color_scheme="purple",
            align="end",
            width="100%",
            padding_top=".5em",
        ),
        width="100%",
    )