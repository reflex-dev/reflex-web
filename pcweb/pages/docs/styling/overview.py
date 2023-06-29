import reflex as rx

from pcweb import styles
from pcweb.templates.docpage import (
    doccode,
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

text_style = {"color": "white", "bg": "black", "font_size": "20px"}


code1 = """rx.text("Hello World", background_image = "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                background_clip = "text", font_weight="bold", font_size="2em")"""
code2 = """rx.box(
    rx.hstack(
        rx.button("Default Button"),
        rx.button("Red Button", color="red"),
    ),
    color="blue",
)"""
code3 = """text_style = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "font_size": "1.2em",
    "font_weight": "bold",
    "box_shadow": "rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px"
}"""
exec(code3)
code4 = """
rx.vstack(
    rx.text("Hello", style = text_style),
    rx.text("World", style = text_style),
)"""

hover_example = """
rx.box(
    rx.text("Hover Me",  _hover = {"color": "red"}),
)
"""

code5 = """
style1 = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "border_radius": "10px",
    "background_color": "rgb(107,99,246)",
}
style2 = {
    "color": "white",
    "border": "5px solid #EE756A",
    "padding": "10px",
}
"""
exec(code5)
multiple_styles = """
rx.box(
    "Multiple Styles",
    style=[style1, style2],
)
"""


@docpage()
def styling_overview():
    return rx.box(
        docheader("Styling", first=True),
        doctext(
            "Reflex components can be styled using the full power of ",
            doclink("CSS", href="https://www.w3schools.com/css/"),
            ". ",
        ),
        doctext(
            "There are three main ways to add style to your app and they take precedence in the following order:",
        ),
        doctext(
            rx.ordered_list(
                rx.vstack(
                    rx.list_item(
                        rx.span("Inline: ", font_weight="bold"),
                        "Styles applied to a single component instance.",
                        width="100%",
                    ),
                    rx.list_item(
                        rx.span("Component: ", font_weight="bold"),
                        "Styles applied to components of a specific type.",
                        width="100%",
                    ),
                    rx.list_item(
                        rx.span("Global: ", font_weight="bold"),
                        "Styles applied to all components.",
                        width="100%",
                    ),
                ),
                padding_left="2em",
            )
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Style keys can be any valid CSS property name."),
                    rx.alert_description(
                        "To be consistent with Python standards, you can specify keys in ",
                        rx.code("snake_case"),
                        ".",
                    ),
                ),
                status="success",
            ),
        ),
        subheader("Global Styles"),
        doctext(
            "You can pass a style dictionary to your app to apply base styles to all components. "
        ),
        doctext(
            "For example, you can set the default font family and font size for your app here just once "
            " rather than having to set it on every component."
        ),
        doccode(
            """
style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px"
}
        
app = rx.App(state=State, style=style)"""
        ),
        subheader("Component Styles"),
        doctext(
            "In your style dictionary, you can also specify default styles for specific component types. "
        ),
        doccode(
            """
accent_color = "#f81ce5"
style = {
    "::selection": {
        "background_color": accent_color,
    },
    rx.Text: {
        "font_family": styles.SANS,
    },
    rx.Divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rx.Heading: {
        "font_weight": "500",
    },
    rx.Code: {
        "color": accent_color,
    },
}
        
app = rx.App(state=State, style=style)"""
        ),
        doctext(
            "Using style dictionaries like this, you can easily create a consistent theme for your app. "
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Note the use of the uppercase component names."),
                    rx.alert_description(
                        "We specify the component classes as keys, rather than their constructors. ",
                    ),
                ),
                status="warning",
            ),
        ),
        subheader("Inline Styles"),
        doctext(
            "Inline styles apply to a single component instance. ",
            "They are passed in as regular props to the component.",
        ),
        docdemo(code1),
        doctext(
            "Children components inherit inline styles unless they are overridden by their own inline styles. "
        ),
        docdemo(code2),
        subheader("Tailwind"),
        doctext(
            "Reflex supports ",
            doclink("Tailwind CSS", href="https://tailwindcss.com/"),
            " out of the box. To enable it, pass in a dictionary for the ",
            rx.code("tailwind"),
            " argument of your ",
            rx.code("rxconfig.py"),
            ":",
        ),
        doccode(
            """
import reflex as rx


class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={},
)"""
        ),
        doctext(
            "All Tailwind configuration options are supported.",
            " Plugins and presets are automatically wrapped in ",
            rx.code("require()"),
            ":",
        ),
        doccode(
            """
config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
    frontend_packages=["@tailwindcss/typography"],
)"""
        ),
        doctext(
            "You can use any of the ",
            doclink(
                "utility classes", href="https://tailwindcss.com/docs/utility-first"
            ),
            " under the ",
            rx.code("class_name"),
            " prop: ",
        ),
        docdemo(
            """rx.box(
    "Hello World",
    class_name="text-4xl text-center text-blue-500",
)"""
        ),
        subheader("Special Styles"),
        doctext(
            "We support all of Chakra UI's ",
            doclink(
                "pseudo styles",
                href="https://chakra-ui.com/docs/features/style-props#pseudo",
            ),
            ". ",
        ),
        doctext(
            "Below is an example of text that changes color when you hover over it.",
        ),
        docdemo(hover_example),
        subheader("Style Prop"),
        doctext(
            "Inline styles can also be set with a ",
            rx.code("style"),
            " prop. ",
            " This is useful for reusing styles betweeen multiple components.",
        ),
        docdemo(code4, code3, eval(code4)),
        doctext(
            "You can also pass in multiple style dictionaries to the ",
            rx.code("style"),
            " prop to combine styles.",
        ),
        docdemo(multiple_styles, code5, eval(multiple_styles)),
        doctext(
            "The style dictionaries are applied in the order they are passed in. ",
            "This means that styles defined later will override styles defined earlier. ",
        ),
    )
