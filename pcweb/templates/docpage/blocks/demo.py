"""Components for rendering code demos in the documentation."""

import reflex as rx
import textwrap
from typing import Any, Callable
from .code import code_block, code_block_dark, code_block_expanded
import black
from pcweb.components.button import button


def expand_code_script(id: str):
    """Copy script for the code block.
    Args:
        id (str): The ID of the button element.
    Returns:
        Any: The result of calling the script.
    """
    return rx.call_script(
        f"""
const button = document.getElementById('{id}');
const collapsedCode = button.nextElementSibling;
const expandedCode = collapsedCode.nextElementSibling;
button.addEventListener('click', () => {{
    if (collapsedCode.classList.contains('hidden')) {{
        collapsedCode.classList.remove('hidden');
        expandedCode.classList.add('hidden');
        button.textContent = 'Expand Code';
    }} else {{
        collapsedCode.classList.add('hidden');
        expandedCode.classList.remove('hidden');
        button.textContent = 'Collapse Code';
    }}
}});
"""
    )


def expand_button(id: str) -> rx.Component:
    return button(
        "Expand Code",
        class_name="!w-fit scale-90 self-end",
        id=id,
    )


def docdemobox(*children, **props) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.box(
        *children,
        **props,
        class_name="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full",
    )


def doccode(
    code: str,
    code_copy: str = "",
    language: str = "python",
    lines: tuple[int, int] | None = None,
    theme: str = "light",
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        code: The code to display.
        code_copy: The original code to copy.
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
    cb = code_block_dark if theme == "dark" else code_block
    cb = code_block_expanded if code_copy != "" else cb
    return cb(
        code=code,
        language=language,
        code_copy=code_copy,
    )


def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    demobox_props: dict[str, Any] | None = None,
    theme: str | None = None,
    expanded: bool = False,
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
    if expanded:
        code_copy = code
        code = "\n".join(line for line in code.split("\n") if "\\start" not in line and "\\end" not in line)

        lines = code_copy.split("\n")
        start_line = next((i for i, line in enumerate(lines) if "\\start" in line), None)
        end_line = next((i for i, line in enumerate(lines) if "\\end" in line), None)

        if start_line is not None and end_line is not None:
            collapsed_code = "\n".join(lines[start_line + 1 : end_line])
        else:
            collapsed_code = code
        button_id = f"expand-button-{hash(collapsed_code)}"

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
                    rx.box(
                        "UI",
                    ),
                    value="tab1",
                    class_name="tab-style",
                ),
                rx.tabs.trigger(
                    rx.box(
                        "Code",
                    ),
                    value="tab2",
                    class_name="tab-style",
                ),
                class_name="justify-end",
            ),
            rx.tabs.content(
                rx.box(docdemobox(comp, **(demobox_props or {})), class_name="my-4"),
                value="tab1",
            ),
            # Add the expand button and the collapsed code
            (
                rx.tabs.content(
                    rx.box(
                        expand_button(button_id),
                        # Collapsed code
                        rx.box(
                            doccode(collapsed_code, theme=theme, code_copy=code),
                            class_name="",
                        ),
                        # Expanded code
                        rx.box(
                            doccode(code, theme=theme, code_copy=code),
                            class_name="hidden",
                        ),
                        on_mount=expand_code_script(button_id),
                        spacing="4",
                        width="100%",
                        class_name="mt-4 relative flex flex-col",
                    ),
                    value="tab2",
                )
                if expanded
                else rx.tabs.content(
                    rx.box(
                        doccode(code, theme=theme),
                    ),
                    value="tab2",
                )
            ),
            default_value="tab1",
        )

    # Create the demo.
    return rx.box(
        docdemobox(comp, **(demobox_props or {})),
        rx.box(
            expand_button(button_id) if demobox_props.pop("expand", False) else None,
            rx.box(
                doccode(code, theme=theme, code_copy=code),
                class_name="hidden" if demobox_props.get("expand", False) else "",
            ),
            spacing="4",
            width="100%",
        ),
        class_name="py-4 gap-4 flex flex-col w-full relative",
        **props,
    )


def docgraphing(
    code: str,
    comp: rx.Component | None = None,
    data: str | None = None,
):
    return rx.box(
        rx.flex(
            comp,
            class_name="w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center",
        ),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Code", value="code", class_name="tab-style"),
                rx.tabs.trigger("Data", value="data", class_name="tab-style"),
                justify_content="end",
            ),
            rx.box(
                rx.tabs.content(doccode(code), value="code", class_name="w-full px-0"),
                rx.tabs.content(
                    doccode(data or ""), value="data", class_name="w-full px-0"
                ),
                class_name="w-full my-4",
            ),
            default_value="code",
            class_name="w-full mt-6 justify-end",
        ),
        class_name="w-full py-4 flex flex-col",
    )
