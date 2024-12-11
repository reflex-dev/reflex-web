"""Flexdown documents."""

from __future__ import annotations

import re
from typing import Any

import yaml
import reflex as rx

from flexdown import constants, types


class Document(rx.Base):
    """A Flexdown document."""

    # Document metadata in the flexdown frontmatter.
    metadata: dict[str, Any] = {}

    # The content of the document.
    content: str

    @staticmethod
    def parse_front_matter(source: str) -> tuple[types.FrontMatter, str]:
        # Extract the front matter and content using the pattern
        match = re.match(constants.FRONT_MATTER_REGEX, source, re.DOTALL)

        # If there is no front matter, return an empty dictionary
        if not match:
            return {}, source

        # Get the front matter and content
        front_matter = yaml.safe_load(match.group(1))
        content = match.group(2)
        return front_matter, content

    @classmethod
    def from_source(cls, source: str) -> Document:
        """Create a document from a source string.

        Args:
            source: The source string of the document.

        Returns:
            The document.
        """
        front_matter, content = cls.parse_front_matter(source)
        return cls(metadata=front_matter, content=content)

    @classmethod
    def from_file(cls, path: str) -> Document:
        """Create a document from a file.

        Args:
            path: The path to the file.

        Returns:
            The document.
        """
        with open(path, "r", encoding="utf-8") as file:
            return cls.from_source(file.read())
