import reflex as rx
from pcweb.constants import SPLINE_SCENE_URL
from reflex.vars import Var


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = SPLINE_SCENE_URL
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]


spline = Spline.create
