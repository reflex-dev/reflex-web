from typing import Callable

import reflex as rx

from flexdown import types, utils
from flexdown.blocks.block import Block


class MarkdownBlock(Block):
    """A block of Markdown."""

    line_transforms = [
        utils.evaluate_templates,
    ]
    render_fn: Callable = None

    def render(self, env: types.Env) -> rx.Component:
        return self.render_fn(content=self.get_content(env))
