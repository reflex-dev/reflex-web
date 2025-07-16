import reflex as rx
from pcweb.constants import SPLINE_SCENE_URL, SPLINE_RUNTIME_VERSION
from reflex.vars import Var


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = SPLINE_SCENE_URL
    is_default = True

    lib_dependencies: list[str] = [f"@splinetool/runtime@{SPLINE_RUNTIME_VERSION}"]


spline = Spline.create
