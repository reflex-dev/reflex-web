import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import doccode, docdemo, doclink, doctext, subheader
from pcweb.pages.docs.styling.overview import styling_overview

example = """rx.vstack(
    rx.html("<h1>Hello World</h1>"),
    rx.html("<h2>Hello World</h2>"),
    rx.html("<h3>Hello World</h3>"),
    rx.html("<h4>Hello World</h4>"),
    rx.html("<h5>Hello World</h5>"),
    rx.html("<h6>Hello World</h6>"),
)
"""

example2 = """ rx.vstack(
    rx.html("<img src='https://reflex.dev/reflex_banner.png' />"),
)
"""


def render_html():
    return rx.vstack(
        doctext(
            "The HTML component can be used to render raw HTML code. ",
            "It takes in a string of HTML code and renders it.",
        ),
        doctext(
            "Before you reach for this component, consider using Reflex's raw HTML element support instead."
        ),
        docdemo(example),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title("Missing Styles?"),
                    rx.alert_description(
                        "Reflex uses Chakra-UI and Tailwind for styling, both of ",
                        "which reset default styles for headings. If you are ",
                        "using the html component and want pretty default ",
                        "styles, consider setting ",
                        rx.code('class_name="prose"'),
                        ", adding ",
                        rx.code("@tailwindcss/typography"),
                        " package to ",
                        rx.code("frontend_packages"),
                        " and enabling it via ",
                        rx.code("tailwind"),
                        " config in ",
                        rx.code("rxconfig.py"),
                        ". See the ",
                        doclink("Tailwind docs", href=styling_overview.path),
                        " for an example of adding this plugin.",
                    ),
                ),
            ),
        ),
        doctext(
            "Here is another example of the HTML component. In this example, we render an image."
        ),
        docdemo(example2),
    )


script_example = """rx.script("console.log('inline javascript')")"""

script_example2 = """rx.script(src="/my-custom.js")"""

script_example3 = """rx.script(src="//gc.zgo.at/count.js", custom_attrs={"data-goatcounter": "https://reflextoys.goatcounter.com/count"}),"""


def render_script():
    return rx.vstack(
        doctext(
            "The Script component can be used to include inline javascript or javascript files by URL. ",
            "It uses the ",
            rx.link(
                "next/script component",
                href="https://nextjs.org/docs/app/api-reference/components/script",
            ),
            " to inject the script and can be safely used with conditional rendering ",
            "to allow script side effects to be controlled by the state.",
        ),
        doccode(script_example),
        doctext(
            "Complex inline scripting should be avoided. If the code to be included is more than a couple lines, ",
            "it is more maintainable ",
            "to implement it in a separate javascript file in the ",
            rx.code("assets"),
            " directory and include it via the ",
            rx.code("src"),
            " prop.",
        ),
        doccode(script_example2),
        doctext(
            "This component is particularly helpful for including tracking and social scripts. Any additional attrs needed ",
            "for the script tag can be supplied via ",
            rx.code("custom_attrs"),
            " prop.",
        ),
        doccode(script_example3),
        doctext(
            "This code renders to something like the following to enable stat counting with a third party service."
        ),
        doccode(
            '<script src="//gc.zgo.at/count.js" data-goatcounter="https://reflextoys.goatcounter.com/count" data-nscript="afterInteractive"></script>',
            language="html",
        ),
    )
