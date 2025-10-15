import dataclasses
import inspect
import re

# Get the comment for a specific field.
from typing import Callable, Type

import reflex as rx

from pcweb.flexdown import markdown
from pcweb.templates.docpage import h1_comp, h2_comp


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
        return inspect.cleandoc(self.module.__doc__ or "")

    def get_class_fields(self) -> list[dict]:
        if not issubclass(self.module, rx.Base):
            return []
        out = self.get_annotations(self.module.__class_vars__)
        return out

    def get_fields(self) -> list[dict]:
        if dataclasses.is_dataclass(self.module):
            return self.get_annotations(
                {f.name: f for f in dataclasses.fields(self.module)}
            )
        elif isinstance(self.module, type) and issubclass(self.module, rx.Base):
            return self.get_annotations(self.module.__fields__)
        return []

    def get_methods(self):
        return [
            {
                "name": name,
                "signature": str(
                    inspect.signature(
                        fn.__func__
                        if isinstance(fn, (classmethod, staticmethod))
                        else fn
                    )
                ),
                "description": (
                    fn.__func__.__doc__
                    if isinstance(fn, (classmethod, staticmethod))
                    else fn.__doc__
                )
                .split("Args:")[0]
                .split("Returns:")[0]
                .strip(),
                "params": dict(
                    inspect.signature(
                        fn.__func__
                        if isinstance(fn, (classmethod, staticmethod))
                        else fn
                    ).parameters
                ),
                "ret": inspect.signature(
                    fn.__func__ if isinstance(fn, (classmethod, staticmethod)) else fn
                ).return_annotation,
            }
            for name, fn in self.module.__dict__.items()
            if (
                fn.__func__.__doc__
                if isinstance(fn, (classmethod, staticmethod))
                else fn.__doc__
            )
            and isinstance(fn, (Callable, classmethod, staticmethod))
            and not name.startswith("_")
            and name != "Config"
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

            # If we've reached a docstring, clear the comments.
            if line.strip() == '"""':
                comments.clear()
                continue

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
            if prop not in props or prop.startswith("_"):
                # This isn't a prop, so continue.
                comments.clear()
                continue

            prop = props[prop]
            # redundant check just to double-check line above prop is a comment
            assert self.code[i - 1].strip().startswith("#"), (
                f"Expected comment, got {self.code[i - 1]}"
            )

            # Get the comment for this prop.
            comment = Source.get_comment(comments)
            # reset comments
            comments.clear()

            # Skip private props.
            if "PRIVATE" in comment:
                continue

            # Add the prop to the output.
            out.append(
                {
                    "prop": prop,
                    "description": comment,
                }
            )

        # Return the output.
        return out


def format_field(field):
    prop = field["prop"]
    try:
        type_ = prop.type_
    except AttributeError:
        type_ = prop.type
    default = field["prop"].default
    default = None if default is dataclasses.MISSING else repr(default)
    type_str = type_.__name__ if hasattr(type_, "__name__") else str(type_)
    if default:
        type_str += f" = {default}"
    return rx.code(field["prop"].name, ": ", type_str, class_name="code-style")


table_header_class_name = (
    "font-small text-slate-12 text-normal w-auto justify-start pl-4 font-bold"
)


def format_fields(headers, fields):
    return (
        rx.scroll_area(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        *[
                            rx.table.column_header_cell(
                                header, class_name=table_header_class_name
                            )
                            for header in headers
                        ]
                    )
                ),
                rx.table.body(
                    *[
                        rx.table.row(
                            rx.table.cell(
                                format_field(field),
                            ),
                            rx.table.cell(
                                markdown(field["description"]),
                                class_name="font-small text-slate-11",
                            ),
                        )
                        for field in fields
                    ],
                ),
            ),
            max_height="35em",
        ),
    )


def generate_docs(title: str, s: Source, extra_fields: list[dict] | None = None):
    fields = s.get_fields()
    if extra_fields:
        fields.extend(extra_fields)
    class_fields = s.get_class_fields()
    return rx.box(
        h1_comp(text=title.title()),
        rx.code(s.get_name(), class_name="code-style text-[18px]"),
        rx.divider(),
        markdown(s.get_overview()),
        (
            rx.box(
                h2_comp(text="Class Fields"),
                format_fields(["Prop", "Description"], class_fields),
                overflow="auto",
            )
            if class_fields
            else rx.fragment()
        ),
        (
            rx.box(
                h2_comp(text="Fields"),
                format_fields(["Prop", "Description"], fields),
                overflow="auto",
            )
            if fields
            else rx.fragment()
        ),
        rx.box(
            h2_comp(text="Methods"),
            rx.scroll_area(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Signature"),
                            rx.table.column_header_cell("Description"),
                        )
                    ),
                    rx.table.body(
                        *[
                            rx.table.row(
                                rx.table.cell(
                                    rx.code(
                                        field["name"] + field["signature"],
                                        class_name="code-style",
                                    ),
                                    white_space="normal",
                                ),
                                rx.table.cell(
                                    field["description"],
                                    white_space="normal",
                                    class_name="font-small text-slate-11 text-nowrap",
                                ),
                            )
                            for field in s.get_methods()
                        ],
                    ),
                ),
                max_height="35em",
            ),
        ),
    )
