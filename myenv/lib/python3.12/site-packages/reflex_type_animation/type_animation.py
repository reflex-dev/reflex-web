"""Reflex custom component TypeAnimation."""
import reflex as rx


class TypeAnimation(rx.Component):
    """ReflexTypeAnimation component."""
    tag = "TypeAnimation"
    library = "react-type-animation"

    sequence: rx.Var[list]
    speed: rx.Var[int]
    repeat: rx.Var[float] = 0
    wrapper: rx.Var[str] = "span"
    cursor: rx.Var[bool] = True
    pre_render_first_string: rx.Var[bool] = False
    deletion_speed: rx.Var[int] = 40
    omit_deletion_animation: rx.Var[bool] = False


type_animation = TypeAnimation.create
