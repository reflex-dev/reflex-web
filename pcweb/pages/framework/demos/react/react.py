import reflex as rx


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
            scene="https://prod.spline.design/1eapv4LnOygEqB66/scene.splinecode",
        ),
        class_name="p-4 lg:px-10 lg:py-12 h-full overflow-hidden",
    )


react_code = """import reflex as rx

class Spline(rx.Component):
    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]

spline = Spline.create

scene = "https://prod.spline.design/1eapv4LnOygEqB66/scene.splinecode"

def spline_demo():
    return spline(scene=scene)
"""
