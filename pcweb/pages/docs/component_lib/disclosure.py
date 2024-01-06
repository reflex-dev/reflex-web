import reflex as rx

from pcweb.templates.docpage import docdemo, doctext


short_hand_accordion_example = """rx.accordion(
   items = [("Label 1", rx.center("Panel 1")), ("Label 2", rx.center("Panel 2"))],
   width = "100%"
   )
"""

basic_example = """rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        )
    ),
    allow_toggle = True,
    width = "100%"
)
"""

accordion_example = """rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example 1"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        ),
    ),
    rx.accordion_item(
        rx.accordion_button(
            rx.heading("Example 2"),
            rx.accordion_icon(),
        ),
        rx.accordion_panel(
            rx.text("This is an example of an accordion component.")
        ),
    ),
    allow_multiple = True,
    bg="black",
    color="white",
    width = "100%"
)
"""

accordion_example_nested = """rx.accordion(
    rx.accordion_item(
        rx.accordion_button(
            rx.accordion_icon(),
            rx.heading("Outer"),
            
        ),
        rx.accordion_panel(
            rx.accordion(
            rx.accordion_item(
                rx.accordion_button(
                    rx.accordion_icon(),
                    rx.heading("Inner"),    
                ),
                rx.accordion_panel(
                    rx.badge("Inner Panel", variant="solid", color_scheme="green"),
                )
            )
            ),
        )  
    ),
    width = "100%"
)
"""


# Disclosure
def render_accordion():
    return rx.vstack(
        doctext(
            "Accordions allow you to hide and show content in a container under a header."
        ),
        doctext(
            "Accordion consist of an outer accordion component and inner accordion items. Each item has a optional button and panel. The button is used to toggle the panel's visibility."
        ),
        docdemo(basic_example),
        doctext("An accordion can have multiple items."),
        docdemo(accordion_example),
        doctext(
            "You can create multilevel accordions by nesting accordions within the outer accordion panel."
        ),
        docdemo(accordion_example_nested),
        doctext(
            "You can also create an accordion using the shorthand syntax. ",
            "Pass a list of tuples to the ",
            rx.code("items"),
            " prop. Each tuple should contain a label and a panel.",
        ),
        docdemo(short_hand_accordion_example),
        align_items="start",
    )


tab_example = """rx.tabs(
    rx.tab_list(
        rx.tab("Tab 1"),
        rx.tab("Tab 2"),
        rx.tab("Tab 3"),
    ),
    rx.tab_panels(
        rx.tab_panel(rx.text("Text from tab 1.")),
        rx.tab_panel(rx.checkbox("Text from tab 2.")),
        rx.tab_panel(rx.button("Text from tab 3.", color="black")),
    ),
    bg="black",
    color="white",
    shadow="lg",
)
"""

short_hand_tab_example = """rx.tabs(
    items = [("Tab 1", rx.text("Text from tab 1.")), ("Tab 2", rx.checkbox("Text from tab 2.")), ("Tab 3", rx.button("Text from tab 3.", color="black"))],
    bg="black",
    color="white",
    shadow="lg",
)
"""


def render_tabs():
    return rx.vstack(
        doctext(
            "Tab components allow you display content in multiple pages within a container. These page are organized by a tab list and the corresponding tab panel can take in children components if needed."
        ),
        docdemo(tab_example),
        doctext(
            "You can create a tab component using the shorthand syntax. ",
            "Pass a list of tuples to the ",
            rx.code("items"),
            " prop. Each tuple should contain a label and a panel.",
        ),
        docdemo(short_hand_tab_example),
        align_items="start",
    )
