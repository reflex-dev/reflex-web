"""Logo reveal component with mouse-following gradient effect."""

import reflex as rx
from reflex.vars.base import Var


class LogoReveal(rx.NoSSRComponent):
    """A logo reveal component with mouse-tracking gradient effect."""

    library = "$/public/components/LogoReveal"

    tag = "LogoReveal"

    # Source URL for the background grid image
    grid_bg_src: Var[str]

    # Radius of the reveal circle effect
    reveal_radius: Var[int]

    # Stroke width of the revealed lines
    stroke_width: Var[int]

    def add_imports(self) -> rx.ImportDict:
        """Add imports to the component."""
        return {
            "clsx-for-tailwind": "cn",
        }


logo_reveal = LogoReveal.create
