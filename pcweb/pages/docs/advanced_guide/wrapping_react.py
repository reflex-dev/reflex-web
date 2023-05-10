import pynecone as pc

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

code0 = """class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
"""
code1 = """
class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: Var[str]
"""

code4 = """class ColorPickerState(State):
    color: str = "#db114b"
"""
code3 = """pc.box(
    pc.vstack(
        pc.heading(ColorPickerState.color),
        color_picker(on_change=ColorPickerState.set_color),
    ),
    background_color=ColorPickerState.color,
    padding="5em",
    border_radius="1em",
)"""
exec(code4)

code5 = """
class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: pc.Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_change": pc.EVENT_ARG}
"""
exec(code5)
code2 = """color_picker = ColorPicker.create"""
exec(code2)

code6 = """
 class AnotherColorPicker(pc.Component):
     library = "some-other-colorpicker"
     tag = "HexColorPicker"
     color: pc.Var[str]
     @classmethod
     def get_controlled_triggers(cls) -> dict[str, pc.Var]:
         return {"on_change": pc.EVENT_ARG}
     @classmethod
     def get_alias(cls) -> Optional[str]:
         return "OtherHexColorPicker"
 """


@docpage()
def wrapping_react():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.styling.overview import styling_overview

    return pc.box(
        docheader("Wrapping React", first=True),
        doctext(
            "One of Pynecone's most powerful features is the ability to wrap React components. ",
            "This allows us to build on top of the powerful React ecosystem, but interface with it through Python. ",
        ),
        doctext(
            "Most of Pynecone's base components are just wrappers around the great ",
            doclink("Chakra UI", "https://chakra-ui.com/"),
            " library. Let's see how you can wrap your own component in three easy steps. ",
        ),
        subheader("Step 1: Install the Library"),
        doctext(
            "If you want a cool component for your app but Pynecone doesn't provide it, there's a good chance it's available as a React component. ",
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
            "Simply specify the package name in your ",
            pc.code("pcconfig.py"),
            " file. ",
        ),
        doccode(
            """
config = pc.Config(
    app_name="colors",
    frontend_packages=[
        "react-colorful",
    ]
)
        """
        ),
        subheader("Step 2: Wrap the Library"),
        doctext(
            "To wrap the component, create a subclass of ",
            pc.code("pc.Component"),
            ". ",
        ),
        doccode(code0),
        doctext(
            "The two most important props are ",
            pc.code("library"),
            ", which is the name of the npm package, and ",
            pc.code("tag"),
            ", which is the name of the React component. ",
        ),
        doctext(
            "A component may also have many props. ",
            "You can add props by declaring them as ",
            pc.code("pc.Var"),
            "s in the class. ",
            " In this example, we have just one prop, ",
            pc.code("value"),
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
            pc.code("create"),
            " method. Usually you'll want to store this for easy access. ",
        ),
        doccode(code2),
        doctext("Then you can use it like any other Pynecone component."),
        docdemo(code3, code4, comp=eval(code3), context=True),
        doctext(
            "That's it! ",
            "We hope over time the Pynecone ecosystem will grow to include many useful components. ",
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
    )
