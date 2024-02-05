"""Code block components for documentation pages."""

import reflex as rx
import reflex.components.radix.themes as rdxt
from pcweb.styles import text_colors as tc
from pcweb import styles

@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx.code_block(
            code,
            border_radius=styles.DOC_BORDER_RADIUS,
            theme="light",
            background="transparent",
            language=language,
            code_tag_props={
                "style": {
                    "fontFamily": "inherit",
                }
            },
        ),
        rx.button(
            rx.icon(tag="copy"),
            on_click=rx.set_clipboard(code),
            position="absolute",
            top="0.5em",
            right="0.5em",
            color=tc["docs"]["body"],
            background="transparent",
            _hover={
                "background": "transparent",
                "color": styles.ACCENT_COLOR,
            },
        ),
        border_radius=styles.DOC_BORDER_RADIUS,
        border=f"2px solid {rx.color('mauve', 4)}",
        background_color=f"{rx.color('mauve', 2)}",
        position="relative",
        margin_bottom="1em",
        margin_top="1em",
        width="100%",
    )


def code_block_markdown(*children, **props):
    language = props.get("language", "none")
    return code_block(code=children[0], language=language)

def doccmdoutput(
    command: str,
    output: str,
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        command: The command to display.
        output: The output of the command.
        theme: The theme of the component.

    Returns:
        The styled command and its example output.
    """
    return rdxt.flex(
        rdxt.flex(
            rdxt.icon(tag="double_arrow_right", color="white", width=18, height=18),
            rx.code_block(
                command,
                border_radius=styles.DOC_BORDER_RADIUS,
                background="transparent",
                theme="a11y-dark",
                language="bash",
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
            rx.button(
                rx.icon(tag="copy"),
                on_click=rx.set_clipboard(command),
                position="absolute",
                top="0.5em",
                right="0.5em",
                color=tc["docs"]["body"],
                background="transparent",
                _hover={
                    "background": "transparent",
                    "color": styles.ACCENT_COLOR,
                },
            ),
            direction="row",
            align="center",
            gap="1",
            margin_left="1em",
        ),
        rdxt.separator(size="4", color_scheme="green"),
        rdxt.flex(
            rx.code_block(
                output,
                border_radius=styles.DOC_BORDER_RADIUS,
                background="transparent",
                theme="a11y-dark",
                language="log",
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
        ),
        direction="column",
        gap="2",
        border_radius=styles.DOC_BORDER_RADIUS,
        border=f"2px solid {rx.color('mauve', 4)}",
        position="relative",
        margin="1em",
        width="100%",
        background_color="black",
    )
