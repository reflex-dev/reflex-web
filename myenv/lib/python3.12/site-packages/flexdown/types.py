"""Types for Flexdown.""" ""
from typing import Any, Callable

import reflex as rx

# An environment for executing and evaluating code.
Env = dict[str, Any]

# The frontmatter of a Flexdown document.
Frontmatter = dict[str, Any]

# Mapping from markdown tag to a rendering function for Reflex components.
ComponentMap = dict[str, Callable[[str], rx.Component]]
