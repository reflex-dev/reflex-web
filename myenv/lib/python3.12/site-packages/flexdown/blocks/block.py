from __future__ import annotations

from typing import Callable, ClassVar

import reflex as rx

from flexdown import types


class Block(rx.Base):
    """Base class for all Flexdown blocks."""

    # Mapping from markdown tag to a rendering function for Reflex components.
    component_map: types.ComponentMap = {}

    # The string denoting the start of the block.
    starting_indicator: ClassVar[str | None] = None

    # The string denoting the end of the block.
    ending_indicator: ClassVar[str] = ""

    # Whether to include the indicators in the content.
    include_indicators: ClassVar[bool] = False

    # List of transformations to apply to each line.
    line_transforms: ClassVar[list[Callable[[str], str]]] = []

    # The lines of text in the block.
    lines: list[str] = []

    # The starting line number of the block.
    start_line_number: int = 0

    # Filename if the block is from a file.
    filename: str | None = None

    @classmethod
    def from_line(
        cls,
        line: str,
        line_number: int = 0,
        component_map: types.ComponentMap = {},
        filename=None,
    ) -> Block | None:
        """Try to create a block from a line of text.

        This method checks if the line of text is the start of a block.

        Args:
            line: The line of text to check.
            line_number: The line number of the line of text.

        Returns:
            The block if the line is the start of a block, otherwise `None`.
        """
        # If there is no starting indicator, or the line starts with the
        # starting indicator, then create a block.
        if cls.starting_indicator is None or line.startswith(cls.starting_indicator):
            return cls(
                start_line_number=line_number,
                component_map=component_map,
                filename=filename,
            ).append(line)

        # Otherwise, return `None`.
        return None

    def _apply_transforms(self, line: str, env: types.Env) -> str:
        """Apply transformations to a line of text.

        Args:
            line: The line of text to transform.
            env: The environment variables to use for line transformations.

        Returns:
            The transformed line of text.
        """
        for transform in self.line_transforms:
            line = transform(line, env)
        return line

    def get_lines(self, env: types.Env) -> str:
        """The content of the block.

        Args:
            env: The environment variables to use for line transformations.

        Returns:
            The content of the block.
        """
        start_index = (
            0 if self.include_indicators or self.starting_indicator is None else 1
        )
        end_index = None if self.include_indicators else -1
        lines = [
            self._apply_transforms(line, env)
            for line in self.lines[start_index:end_index]
        ]
        return lines

    def get_content(self, env: types.Env) -> str:
        """The content of the block.

        Args:
            env: The environment variables to use for line transformations.

        Returns:
            The content of the block.
        """
        return "\n".join(self.get_lines(env))

    def append(self, line: str) -> Block:
        """Append a line of text to the block.

        Args:
            line: The line of text to append.

        Returns:
            The block with the line of text appended.
        """
        self.lines.append(line)
        return self

    def finish(self):
        """Finish the block."""
        if len(self.lines) == 0 or self.lines[-1] != self.ending_indicator:
            self.lines.append(self.ending_indicator)

    def is_finished(self) -> bool:
        """Whether the block is finished."""
        return len(self.lines) > 0 and self.lines[-1] == self.ending_indicator

    def render(
        self,
        env: types.Env | None = None,
    ) -> rx.Component:
        """Render a block to a Reflex component.

        Args:
            env: The environment to use for rendering.
            component_map: The component map to use.

        Returns:
            The rendered Reflex component.
        """
        pass


# Functions that process blocks before rendering.
BlockProcessor = Callable[[list[Block], types.Env], list[Block]]
