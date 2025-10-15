import reflex as rx
from reflex.vars import Var

from pcweb.constants import SPLINE_RUNTIME_VERSION, SPLINE_SCENE_URL


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = SPLINE_SCENE_URL
    is_default = True

    lib_dependencies: list[str] = [f"@splinetool/runtime@{SPLINE_RUNTIME_VERSION}"]


spline = Spline.create
