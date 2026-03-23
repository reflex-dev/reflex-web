"""Tests for documentation generation from component fields."""

from __future__ import annotations

import dataclasses
from typing import Annotated

import reflex as rx
from typing_extensions import Doc


def test_class_doc_extraction():
    """generate_class_documentation extracts Doc from Annotated types and unwraps the type."""
    from reflex_docgen import generate_class_documentation

    @dataclasses.dataclass
    class FakeModule:
        """A fake module for testing."""

        name: Annotated[str, Doc("The name of the thing.")]
        count: Annotated[int, Doc("How many things.")] = 0
        plain: str = "hello"

    doc = generate_class_documentation(FakeModule)
    by_name = {f.name: f for f in doc.fields}

    # Doc is extracted from Annotated metadata
    assert by_name["name"].description == "The name of the thing."
    assert by_name["count"].description == "How many things."
    assert by_name["plain"].description is None

    # type is unwrapped (not Annotated)
    assert by_name["name"].type is str
    assert by_name["count"].type is int
    assert by_name["plain"].type is str


def test_class_no_annotated_in_format():
    """format_field should never produce a string containing 'Annotated'."""
    from reflex_docgen import generate_class_documentation

    from pcweb.pages.docs.source import format_field

    @dataclasses.dataclass
    class FakeModule:
        """A fake module for testing."""

        name: Annotated[str, Doc("The name.")] = "default"
        items: Annotated[list[int], Doc("A list.")] = dataclasses.field(
            default_factory=list
        )

    doc = generate_class_documentation(FakeModule)

    for f in doc.fields:
        rendered = format_field(f)
        rendered_str = str(rendered)
        assert "Annotated" not in rendered_str, (
            f"format_field produced 'Annotated' in output for {f.name}: {rendered_str}"
        )


def test_format_field_preserves_generic_subtypes():
    """format_field should show list[int], not just list."""
    from reflex_docgen import generate_class_documentation

    from pcweb.pages.docs.source import format_field

    @dataclasses.dataclass
    class FakeModule:
        """A fake module for testing."""

        items: Annotated[list[int], Doc("A list of ints.")] = dataclasses.field(
            default_factory=list
        )
        mapping: Annotated[dict[str, int], Doc("A mapping.")] = dataclasses.field(
            default_factory=dict
        )
        plain: str = "hello"

    doc = generate_class_documentation(FakeModule)
    by_name = {f.name: f for f in doc.fields}

    items_str = str(format_field(by_name["items"]))
    assert "list[int]" in items_str, f"Expected 'list[int]' in: {items_str}"

    mapping_str = str(format_field(by_name["mapping"]))
    assert "dict[str, int]" in mapping_str, (
        f"Expected 'dict[str, int]' in: {mapping_str}"
    )

    plain_str = str(format_field(by_name["plain"]))
    assert "str" in plain_str, f"Expected 'str' in: {plain_str}"


def test_class_string_annotations():
    """Annotations that are strings (from __future__ annotations) should be resolved."""
    from reflex_docgen import generate_class_documentation

    # rx.App uses `from __future__ import annotations`, so its field types are strings.
    # Verify we still extract docs and unwrap Annotated.
    doc = generate_class_documentation(rx.App)

    for f in doc.fields:
        type_str = str(f.type)
        assert "Annotated" not in type_str, (
            f"Unresolved Annotated in {f.name}: {type_str}"
        )


def test_component_props_no_annotated():
    """Component prop types should not contain 'Annotated'."""
    from reflex.components.radix.themes.components.button import Button
    from reflex_docgen import get_component_props

    props = get_component_props(Button)

    for prop in props:
        type_str = str(prop.type)
        assert "Annotated" not in type_str, (
            f"Component prop {prop.name} has Annotated in type: {type_str}"
        )


def test_component_props_default_parsed_from_doc():
    """Default values should be parsed from 'Defaults to'/'Default:' in doc strings."""
    from reflex.components.radix.primitives.drawer import DrawerRoot
    from reflex_docgen import get_component_props

    props = get_component_props(DrawerRoot)
    by_name = {p.name: p for p in props}

    # 'modal' doc contains "Defaults to `True`"
    assert by_name["modal"].default_value, "modal should have a parsed default"
    assert "Defaults to" not in by_name["modal"].description, (
        "Default indicator should be stripped from description"
    )

    # 'direction' doc contains 'Defaults to `"bottom"`'
    assert by_name["direction"].default_value, "direction should have a parsed default"
    assert "Defaults to" not in by_name["direction"].description, (
        "Default indicator should be stripped from description"
    )
