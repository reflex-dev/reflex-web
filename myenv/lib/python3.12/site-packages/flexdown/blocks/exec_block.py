import os
import sys

import reflex as rx

from flexdown import types
from flexdown.blocks.block import Block


class ExecBlock(Block):
    """A block of executable Python code."""

    starting_indicator = "```python exec"
    ending_indicator = "```"

    def render(self, env: types.Env) -> rx.Component:
        # Get the content of the block.
        content = self.get_content(env)

        # Get the directory of the filename.
        if self.filename is not None:
            directory = os.path.dirname(os.path.abspath(self.filename))

            # Add the directory to the Python path.
            sys.path.insert(0, directory)

        env["__xd"].exec(content, env, self.filename)

        # Clean up the Python path.
        if self.filename is not None:
            sys.path.remove(directory)

        # Return an empty fragment.
        return rx.fragment()
