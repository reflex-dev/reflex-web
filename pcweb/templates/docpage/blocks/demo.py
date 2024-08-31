"""Components for rendering code demos in the documentation."""

import textwrap
from typing import Any

import black
import reflex as rx

from pcweb.styles.colors import c_color
from pcweb.styles.styles import tab_style

from .code import code_block
from .code import code_block_dark

demo_box_style = {
    "padding": "24px",
    "width": "100%",
    "overflow_x": "auto",
    "border-radius": "12px",
    "border": f"1px solid {c_color('slate', 4)}",
    "background": f"{c_color('slate', 2)}",
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
            textwrap.dedent(code),
            mode=black.FileMode(line_length=60),
        ).strip()

    # If needed, only display a subset of the lines.
    if lines is not None:
        code = textwrap.dedent(
            "\n".join(code.strip().split("\n")[lines[0] : lines[1]]),
        ).strip()

    # Create the code snippet.
    cb = code_block_dark if theme == "dark" else code_block
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
    theme: str | None = None,
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
    demobox_props = demobox_props or {}
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

    if demobox_props.pop("toggle", False):
        return rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.hstack(
                        "UI",
                    ),
                    style=tab_style,
                    value="tab1",
                ),
                rx.tabs.trigger(
                    rx.hstack(
                        "Code",
                    ),
                    style=tab_style,
                    value="tab2",
                ),
                justify_content="end",
            ),
            rx.tabs.content(
                rx.box(
                    docdemobox(comp, **(demobox_props or {})),
                    margin_bottom="1em",
                    margin_top="1em",
                ),
                value="tab1",
            ),
            rx.tabs.content(
                doccode(code, theme=theme),
                value="tab2",
            ),
            default_value="tab1",
        )
    # Create the demo.
    return rx.vstack(
        docdemobox(comp, **(demobox_props or {})),
        doccode(code, theme=theme),
        width="100%",
        padding_y="1em",
        gap="1em",
        **props,
    )


def docgraphing(
    code: str,
    comp: rx.Component | None = None,
    data: str | None = None,
):
    return rx.vstack(
        rx.flex(
            comp,
            style=demo_box_style,
        ),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    "Code",
                    value="code",
                    style=tab_style,
                ),
                rx.tabs.trigger(
                    "Data",
                    value="data",
                    style=tab_style,
                ),
                justify_content="end",
            ),
            rx.box(
                rx.tabs.content(
                    doccode(code),
                    width="100%",
                    padding_x=0,
                    padding_y=".25em",
                    value="code",
                ),
                rx.tabs.content(
                    doccode(data or ""),
                    width="100%",
                    padding_x=0,
                    padding_y=".25em",
                    value="data",
                ),
                width="100%",
            ),
            margin_top="23px",
            default_value="code",
            align="end",
            width="100%",
        ),
        width="100%",
        padding_y="1em",
        spacing="0",
    )
