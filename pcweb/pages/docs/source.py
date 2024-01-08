import inspect
import re

# Get the comment for a specific field.
from typing import Callable, Type

import reflex as rx
from pcweb import styles
from pcweb.styles import font_weights as fw
from pcweb.templates.docpage import (
    docheader,
    doctext,
    subheader,
)


class Source(rx.Base):
    """Parse the source code of a component."""

    # The component to parse.
    module: Type

    # The source code.
    code: list[str] = []

    def __init__(self, *args, **kwargs):
        """Initialize the source code parser."""
        super().__init__(*args, **kwargs)

        # Get the source code.
        self.code = [
            line
            for line in inspect.getsource(self.module).splitlines()
            if len(line) > 0
        ]

    def get_docs(self) -> str:
        """Get the docstring of the component.

        Returns:
            The docstring of the component.
        """
        return self.module.__doc__

    @staticmethod
    def get_comment(comments: list[str]):
        return "".join([comment.strip().strip("#") for comment in comments])

    def get_name(self) -> str:
        return ".".join((self.module.__module__, self.module.__qualname__))

    def get_overview(self) -> str:
        return self.module.__doc__

    def get_class_fields(self) -> list[dict]:
        if not issubclass(self.module, rx.Base):
            return []
        return self.get_annotations(self.module.__class_vars__)

    def get_fields(self) -> list[dict]:
        if not issubclass(self.module, rx.Base):
            return []
        return self.get_annotations(self.module.__fields__)

    def get_methods(self):
        return [
            dict(
                name=name,
                signature=str(inspect.signature(fn)),
                description=fn.__doc__.split("Args:")[0].split("Returns:")[0].strip(),
                params=dict(inspect.signature(fn).parameters),
                ret=inspect.signature(fn).return_annotation,
            )
            for name, fn in self.module.__dict__.items()
            if fn.__doc__ and isinstance(fn, Callable)
        ]

    def get_annotations(self, props) -> list[dict]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        # The output.
        out = []

        comments = []
        # Loop through the source code.
        for i, line in enumerate(self.code):
            # Check if we've reached the functions.
            reached_functions = re.search("def ", line)
            if reached_functions:
                # We've reached the functions, so stop.
                break

            # Get comments for prop
            if line.strip().startswith("#"):
                comments.append(line)
                continue

            # Check if this line has a prop.
            match = re.search("\\w+:", line)
            if match is None:
                # This line doesn't have a var, so continue.
                continue

            # Get the prop.
            prop = match.group(0).strip(":")
            if prop not in props:
                # This isn't a prop, so continue.
                comments.clear()
                continue

            # redundant check just to double-check line above prop is a comment
            assert (
                self.code[i - 1].strip().startswith("#")
            ), f"Expected comment, got {comment}"

            # Get the comment for this prop.
            comment = Source.get_comment(comments)
            # reset comments
            comments.clear()

            # Add the prop to the output.
            out.append(
                dict(
                    name=prop,
                    description=comment,
                )
            )

        # Return the output.
        return out


def generate_docs(title: str, s: Source):
    return rx.box(
        docheader(title.title(), first=True),
        rx.code(s.get_name(), font_size=styles.H3_FONT_SIZE, font_weight=fw["section"]),
        rx.divider(),
        doctext(s.get_overview()),
        subheader("Class Fields"),
        rx.box(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Field"),
                        rx.th("Description"),
                    )
                ),
                rx.tbody(
                    *[
                        rx.tr(
                            rx.td(
                                rx.code(field["name"], font_weight=styles.BOLD_WEIGHT)
                            ),
                            rx.td(field["description"]),
                        )
                        for field in s.get_class_fields()
                    ],
                ),
            ),
            style={"overflow": "auto"},
        ),
        subheader("Fields"),
        rx.box(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Field"),
                        rx.th("Description"),
                    )
                ),
                rx.tbody(
                    *[
                        rx.tr(
                            rx.td(
                                rx.code(field["name"], font_weight=styles.BOLD_WEIGHT)
                            ),
                            rx.td(field["description"]),
                        )
                        for field in s.get_fields()
                    ],
                ),
            ),
            style={"overflow": "auto"},
        ),
        subheader("Methods"),
        rx.box(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Signature"),
                        rx.th("Description"),
                    )
                ),
                rx.tbody(
                    *[
                        rx.tr(
                            rx.td(
                                rx.code(
                                    field["name"] + field["signature"],
                                    font_weight=styles.BOLD_WEIGHT,
                                ),
                                white_space="normal",
                            ),
                            rx.td(field["description"], white_space="normal"),
                        )
                        for field in s.get_methods()
                    ],
                ),
            ),
            style={"overflow": "auto"},
        ),
    )
