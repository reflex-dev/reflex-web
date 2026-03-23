"""Tests for documentation generation from component fields."""

from __future__ import annotations

import dataclasses
from typing import Annotated

import reflex as rx
from typing_extensions import Doc


def test_source_annotated_doc_extraction():
    """Source.get_annotations extracts Doc from Annotated types and unwraps the type."""
    from pcweb.pages.docs.source import Source

    @dataclasses.dataclass
    class FakeModule:
        """A fake module for testing."""

        name: Annotated[str, Doc("The name of the thing.")]
        count: Annotated[int, Doc("How many things.")] = 0
        plain: str = "hello"

    s = Source(module=FakeModule)
    fields = s.get_fields()

    by_name = {f["prop"].name: f for f in fields}

    # Doc is extracted from Annotated metadata
    assert by_name["name"]["description"] == "The name of the thing."
    assert by_name["count"]["description"] == "How many things."
    assert by_name["plain"]["description"] == ""

    # resolved_type is unwrapped (not Annotated)
    assert by_name["name"]["resolved_type"] is str
    assert by_name["count"]["resolved_type"] is int
    assert by_name["plain"]["resolved_type"] is str


def test_source_annotated_no_annotated_in_format():
    """format_field should never produce a string containing 'Annotated'."""
    from pcweb.pages.docs.source import Source, format_field

    @dataclasses.dataclass
    class FakeModule:
        """A fake module for testing."""

        name: Annotated[str, Doc("The name.")] = "default"
        items: Annotated[list[int], Doc("A list.")] = dataclasses.field(
            default_factory=list
        )

    s = Source(module=FakeModule)
    fields = s.get_fields()

    for f in fields:
        rendered = format_field(f)
        # format_field returns an rx.code component; check its children for "Annotated"
        rendered_str = str(rendered)
        assert "Annotated" not in rendered_str, (
            f"format_field produced 'Annotated' in output for {f['prop'].name}: {rendered_str}"
        )


def test_format_field_preserves_generic_subtypes():
    """format_field should show list[int], not just list."""
    from pcweb.pages.docs.source import Source, format_field

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

    s = Source(module=FakeModule)
    fields = s.get_fields()
    by_name = {f["prop"].name: f for f in fields}

    items_str = str(format_field(by_name["items"]))
    assert "list[int]" in items_str, f"Expected 'list[int]' in: {items_str}"

    mapping_str = str(format_field(by_name["mapping"]))
    assert "dict[str, int]" in mapping_str, (
        f"Expected 'dict[str, int]' in: {mapping_str}"
    )

    plain_str = str(format_field(by_name["plain"]))
    assert "str" in plain_str, f"Expected 'str' in: {plain_str}"


def test_source_string_annotations():
    """Annotations that are strings (from __future__ annotations) should be resolved."""
    from pcweb.pages.docs.source import Source

    # rx.App uses `from __future__ import annotations`, so its field types are strings.
    # Verify we still extract docs and unwrap Annotated.
    s = Source(module=rx.App)
    fields = s.get_fields()

    for f in fields:
        type_str = str(f.get("resolved_type", ""))
        assert "Annotated" not in type_str, (
            f"Unresolved Annotated in {f['prop'].name}: {type_str}"
        )


def test_component_props_no_annotated():
    """Component prop types should not contain 'Annotated'."""
    from reflex.components.radix.themes.components.button import Button

    from pcweb.pages.docs.component import Source

    s = Source(component=Button)
    props = s.get_props()

    for prop in props:
        type_str = str(prop.type_)
        assert "Annotated" not in type_str, (
            f"Component prop {prop.name} has Annotated in type: {type_str}"
        )


def test_component_props_default_parsed_from_doc():
    """Default values should be parsed from 'Defaults to'/'Default:' in doc strings."""
    from reflex.components.radix.primitives.drawer import DrawerRoot

    from pcweb.pages.docs.component import Source

    s = Source(component=DrawerRoot)
    props = s.get_props()
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
