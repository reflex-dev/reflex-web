# Customs colors from /assets/custom-colors.css
from typing import Literal

from reflex.utils.types import validate_parameter_literals

ColorType = Literal["white", "slate", "violet", "jade", "red"]
ShadeType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


@validate_parameter_literals
def c_color(color: ColorType, shade: ShadeType, alpha: bool = False) -> str:
    """Create a color variable string."""
    shade_str = str(shade).replace(".", "-")
    return f"var(--c-{color}-{shade_str}{'-a' if alpha else ''})"
