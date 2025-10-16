"""Code block components for documentation pages."""

import reflex as rx

import pcweb.styles.fonts as fonts
from pcweb import styles


@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx._x.code_block(
            code,
            language=language,
            class_name="code-block",
            can_copy=True,
        ),
        class_name="relative mb-4",
    )


@rx.memo
def code_block_dark(code: str, language: str):
    return rx.box(
        rx._x.code_block(
            code,
            language=language,
            class_name="code-block",
            can_copy=True,
        ),
        class_name="relative",
    )


def code_block_markdown(*children, **props):
    language = props.get("language", "plain")
    return code_block(code=children[0], language=language)


def code_block_markdown_dark(*children, **props):
    language = props.get("language", "plain")
    return code_block_dark(code=children[0], language=language)


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
    return rx.vstack(
        rx._x.code_block(
            command,
            can_copy=True,
            border_radius=styles.DOC_BORDER_RADIUS,
            background="transparent",
            theme="ayu-dark",
            language="bash",
            code_tag_props={
                "style": {
                    "fontFamily": "inherit",
                }
            },
            style=fonts.code,
            font_family="Source Code Pro",
            width="100%",
        ),
        rx._x.code_block(
            output,
            can_copy=False,
            border_radius="12px",
            background="transparent",
            theme="ayu-dark",
            language="log",
            code_tag_props={
                "style": {
                    "fontFamily": "inherit",
                }
            },
            style=fonts.code,
            font_family="Source Code Pro",
            width="100%",
        ),
        padding_y="1em",
    )
