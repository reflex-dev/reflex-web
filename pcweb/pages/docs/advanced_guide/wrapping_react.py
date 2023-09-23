import reflex as rx
from typing import Any

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code0 = """class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
"""
code1 = """
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]
"""

code4 = """class ColorPickerState(State):
    color: str = "#db114b"
"""
code3 = """rx.box(
    rx.vstack(
        rx.heading(ColorPickerState.color),
        color_picker(on_change=ColorPickerState.set_color),
    ),
    background_color=ColorPickerState.color,
    padding="5em",
    border_radius="1em",
)"""
exec(code4)

code5 = """
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0]
        }
"""
exec(code5)
code2 = """color_picker = ColorPicker.create"""
exec(code2)

code6 = """
class AnotherColorPicker(rx.Component):
    library = "some-other-colorpicker"
    tag = "HexColorPicker"
    color: rx.Var[str]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0]
        }

    @classmethod
    def get_alias(cls) -> Optional[str]:
        return "OtherHexColorPicker"
"""

custom_component_js_code = """export function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
}"""

custom_component_python_code = """class Welcome(rx.Component):
    library = "../public/welcome.js"
    tag = "Welcome"

    name: rx.Var[str]

welcome = Welcome.create"""

custom_component_python_usage_code = """def index():
    return rx.vstack(
        welcome(name="Reflex")
    )"""

no_ssr_code = '''
class ReactPlayerComponent(rx.Component):
    library = "react-player"
    tag = "ReactPlayer"

    def _get_imports(self) -> Optional[imports.ImportDict]:
        return {}

    def _get_custom_code(self) -> Optional[str]:
        return """
import dynamic from "next/dynamic";
const ReactPlayer = dynamic(() => import("react-player/lazy"), { ssr: false });
"""
'''


@docpage()
def wrapping_react():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.styling.overview import styling_overview

    return rx.box(
        docheader("Wrapping React", first=True),
        doctext(
            "One of Reflex's most powerful features is the ability to wrap React components. ",
            "This allows us to build on top of the powerful React ecosystem, but interface with it through Python. ",
        ),
        doctext(
            "Most of Reflex's base components are just wrappers around the great ",
            doclink("Chakra UI", "https://chakra-ui.com/"),
            " library. Let's see how you can wrap your own component in three easy steps. ",
        ),
        subheader("Step 1: Install the Library"),
        doctext(
            "If you want a cool component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. ",
            "Search the web for an ",
            doclink("npm package", "https://www.npmjs.com/"),
            " that provides the component you want. ",
        ),
        doctext(
            "In this example, we will wrap the ",
            doclink(
                "react-colorful", href="https://www.npmjs.com/package/react-colorful"
            ),
            " color picker component. ",
        ),
        subheader("Step 2: Wrap the Library"),
        doctext(
            "To wrap the component, create a subclass of ",
            rx.code("rx.Component"),
            ". ",
        ),
        doccode(code0),
        doctext(
            "The two most important props are ",
            rx.code("library"),
            ", which is the name of the npm package, and ",
            rx.code("tag"),
            ", which is the name of the React component. ",
        ),
        doctext(
            "Reflex will automatically install the ",
            rx.code("library"),
            " specified in your code if needed. ",
        ),
        doctext(
            "If your component depends on non-react JS libs to work, add them as a list in ",
            rx.code("lib_dependencies"),
            " and the dependencies will be installed automatically.",
        ),
        doctext(
            "A component may also have many props. ",
            "You can add props by declaring them as ",
            rx.code("rx.Var"),
            "s in the class. ",
            " In this example, we have just one prop, ",
            rx.code("value"),
            ", which is the current color. ",
        ),
        doccode(code1),
        doctext(
            "Finally, we must specify any event triggers that the component takes. "
            "This component has a single trigger to specify when the color changes. "
        ),
        doccode(code5),
        subheader("Step 3: Use the Component"),
        doctext(
            "Now we're ready to use the component! ",
            "Every component has a ",
            rx.code("create"),
            " method. Usually you'll want to store this for easy access. ",
        ),
        doccode(code2),
        doctext("Then you can use it like any other Reflex component."),
        docdemo(code3, code4, comp=eval(code3), context=True),
        doctext(
            "That's it! ",
            "We hope over time the Reflex ecosystem will grow to include many useful components. ",
            "Our goal is to bring the full power of web development to Python. ",
        ),
        subheader("Aliases"),
        doctext(
            """If you are wrapping another components with the same tag as a 
 component in your project you can use aliases to
 differentiate between them and avoid naming conflicts."""
        ),
        doctext(
            """
         Lets check out the code below, in this case if we needed to wrap another color picker 
         library with the same tag we use an alias to avoid a conflict.
         """
        ),
        doccode(code6),
        subheader("Local Components"),
        doctext(
            "Javascript files containing custom React components may be added to the ",
            rx.code("assets"),
            " directory of a Reflex project and then wrapped in python code using a relative path ",
            "for the ",
            rx.code("library"),
            " attribute.",
        ),
        doctext(
            "As an example, save the following code as ",
            rx.code("./assets/welcome.js"),
        ),
        doccode(custom_component_js_code, language="javascript"),
        doctext(
            "Then in your Reflex app, create a ",
            rx.code("Component"),
            " wrapper referencing the relative path and exported component name. ",
        ),
        doccode(custom_component_python_code),
        doctext(
            "(Note that the contents of ",
            rx.code("assets"),
            " are compiled to ",
            rx.code(".web/public"),
            " so the wrapped component uses the ",
            rx.code("../public"),
            " prefix for ",
            rx.code("library"),
            " because the page code is compiled to a sibling directory, ",
            rx.code(".web/pages"),
            ")",
        ),
        doctext(
            "The local wrapped component can now be used like any other Reflex component.",
        ),
        doccode(custom_component_python_usage_code),
        subheader("Import Types"),
        doctext(
            """By default, the library and tag specified in the Component are used to generate
            a javascript import where the tag name is treated as the default import from the
            library module.""",
        ),
        doccode('import HexColorPicker from "react-colorful"', language="javascript"),
        subheader("Non-default", level=1),
        doctext(
            "If the tag is not the default export from the module, then set ",
            rx.code("is_default = False"),
            " in the component class definition to generate an import using the curly brace syntax.",
        ),
        doccode(
            'import { HexColorPicker } from "react-colorful"', language="javascript"
        ),
        subheader("Client-side Only", level=1),
        doctext(
            "For components that do not work properly during server-side rendering, use ",
            rx.code("_get_custom_code"),
            " to emit a dynamic loader.",
        ),
        doccode(no_ssr_code),
        doctext(
            """The strategy of emitting custom code can be used to surpass any current
            limitations of the Reflex component compiler."""
        ),
    )
