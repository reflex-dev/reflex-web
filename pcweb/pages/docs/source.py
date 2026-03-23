import dataclasses
import inspect
import typing
from typing import Callable, Type

import reflex as rx
from typing_extensions import Doc
from typing_inspection.introspection import AnnotationSource, inspect_annotation

from pcweb.flexdown import markdown
from pcweb.templates.docpage import h1_comp, h2_comp


class Source(rx.Base):
    """Parse the source code of a component."""

    # The component to parse.
    module: Type

    def get_docs(self) -> str:
        """Get the docstring of the component.

        Returns:
            The docstring of the component.
        """
        return self.module.__doc__

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

    def _resolve_hints(self) -> dict[str, typing.Any]:
        """Resolve type hints for the module, returning evaluated types."""
        try:
            return typing.get_type_hints(self.module, include_extras=True)
        except Exception:
            return {}

    def _get_field_doc_and_type(
        self, name, prop, resolved_hint
    ) -> tuple[str, typing.Any]:
        """Extract doc and resolved type from a field.

        Returns:
            (doc, resolved_type) — resolved_type is unwrapped from Annotated.
        """
        doc = ""
        resolved_type = resolved_hint

        # Inspect the resolved hint for Annotated metadata
        if resolved_hint is not None:
            inspected = inspect_annotation(
                resolved_hint, annotation_source=AnnotationSource.CLASS
            )
            resolved_type = inspected.type
            for meta in inspected.metadata:
                if isinstance(meta, Doc):
                    doc = meta.documentation
                    break

        # field.doc takes priority over Annotated[..., Doc()]
        field_doc = getattr(prop, "doc", None)
        if field_doc:
            doc = field_doc

        return doc, resolved_type

    def get_annotations(self, props) -> list[dict]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        # Normalize: accept a set (e.g. __class_vars__) or a dict.
        if isinstance(props, set):
            props = dict.fromkeys(props)

        resolved_hints = self._resolve_hints()
        out = []

        for name, prop in props.items():
            if name.startswith("_"):
                continue

            doc, resolved_type = self._get_field_doc_and_type(
                name, prop, resolved_hints.get(name)
            )

            if "PRIVATE" in doc:
                continue

            out.append(
                {
                    "prop": prop,
                    "description": doc,
                    "resolved_type": resolved_type,
                }
            )

        return out


def format_field(field):
    prop = field["prop"]
    # Use pre-resolved type (already unwrapped from Annotated) if available
    type_ = field.get("resolved_type")
    if type_ is None:
        try:
            type_ = prop.type_
        except AttributeError:
            type_ = prop.type
    default = getattr(prop, "default", dataclasses.MISSING)
    default = None if default is dataclasses.MISSING else repr(default)
    # Use __name__ only for plain types (e.g. str, int), not generics (e.g. list[int])
    if hasattr(type_, "__name__") and not typing.get_args(type_):
        type_str = type_.__name__
    else:
        type_str = str(type_)
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
