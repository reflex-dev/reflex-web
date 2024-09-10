import reflex as rx


class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str] = "#6e56cf"
    on_change: rx.EventHandler[lambda color: [color]]


color_picker = ColorPicker.create

ColorPickerState = rx._x.client_state(default="#6e56cf", var_name="color")


# def react() -> rx.Component:
#     return rx.box(
#         ColorPickerState,
#         rx.box(
#             rx.text(ColorPickerState.value, class_name="font-x-large text-white"),
#             color_picker(on_change=ColorPickerState.set_value),
#             background_color=ColorPickerState.value,
#             class_name="flex flex-col justify-center items-center gap-4 rounded-[1.125rem] w-full h-full shadow-small",
#         ),
#         class_name="flex items-center p-10 w-full h-full overflow-hidden",
#     )
class Spline(rx.Component):
    """Spline component."""

    # The name of the npm package.
    library = "@splinetool/react-spline"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]

    # The name of the component to use from the package.
    tag = "Spline"

    # Spline is a default export from the module.
    is_default = True

    # Class name for the component.
    class_name: rx.Var[str] = "rounded-[1.125rem]"

    # Any props that the component takes.
    scene: rx.Var[str]


# Convenience function to create the Spline component.
spline = Spline.create


# Use the Spline component in your app.
def react():
    return rx.box(
        spline(
            scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode",
            # class_name="rounded-[1.125rem]",
        ),
        class_name="p-8 h-full overflow-hidden",
    )


react_code = """class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str] = "#6e56cf"
    on_change: rx.EventHandler[lambda color: [color]]

color_picker = ColorPicker.create

class ColorPickerState(rx.State):
    color: str = "#6e56cf"

def color_picker():
    return rx.box(
        rx.vstack(
            rx.heading(
                ColorPickerState.color, color="white"
            ),
            color_picker(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        class_name="container",
    )
"""
