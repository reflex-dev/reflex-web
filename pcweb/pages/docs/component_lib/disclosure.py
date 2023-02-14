import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext


short_hand_accordian_example = """pc.accordion(
   items = [("Label 1", pc.center("Panel 1")), ("Label 2", pc.center("Panel 2"))],
   width = "100%"
   )
"""

basic_example = """pc.accordion(
    pc.accordion_item(
        pc.accordion_button(
            pc.heading("Example"),
            pc.accordion_icon(),
        ),
        pc.accordion_panel(
            pc.text("This is an example of an accordion component.")
        )
    ),
    width = "100%"
)
"""

accordian_example = """pc.accordion(
    pc.accordion_item(
        pc.accordion_button(
            pc.heading("Example 1"),
            pc.accordion_icon(),
        ),
        pc.accordion_panel(
            pc.text("This is an example of an accordion component.")
        ),
    ),
    pc.accordion_item(
        pc.accordion_button(
            pc.heading("Example 2"),
            pc.accordion_icon(),
        ),
        pc.accordion_panel(
            pc.text("This is an example of an accordion component.")
        ),
    ),
    allow_multiple = True,
    bg="black",
    color="white",
    width = "100%"
)
"""

accordian_example_nested = """pc.accordion(
    pc.accordion_item(
        pc.accordion_button(
            pc.accordion_icon(),
            pc.heading("Outer"),
            
        ),
        pc.accordion_panel(
            pc.accordion(
            pc.accordion_item(
                pc.accordion_button(
                    pc.accordion_icon(),
                    pc.heading("Inner"),    
                ),
                pc.accordion_panel(
                    pc.badge("Inner Panel", variant="solid", color_scheme="green"),
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
    return pc.vstack(
        doctext(
            "Accordions allow you to hide and show content in a container under a header."
        ),
        doctext(
            "Accordion consist of an outer accordion component and inner accordion items. Each item has a optional button and panel. The button is used to toggle the panel's visibility."
        ),
        docdemo(basic_example),
        doctext("An accordian can have multiple items."),
        docdemo(accordian_example),
        doctext(
            "You can create multilevel accordions by nesting accordions within the outer accordian panel."
        ),
        docdemo(accordian_example_nested),
        doctext(
            "You can also create an accordion using the shorthand syntax. ",
            "Pass a list of tuples to the ",
            pc.code("items"),
            " prop. Each tuple should contain a label and a panel."
        ),
        docdemo(short_hand_accordian_example),
        align_items="start",
    )


tab_example = """pc.tabs(
    pc.tab_list(
        pc.tab("Tab 1"),
        pc.tab("Tab 2"),
        pc.tab("Tab 3"),
    ),
    pc.tab_panels(
        pc.tab_panel(pc.text("Text from tab 1.")),
        pc.tab_panel(pc.checkbox("Text from tab 2.")),
        pc.tab_panel(pc.button("Text from tab 3.", color="black")),
    ),
    bg="black",
    color="white",
    shadow="lg",
)
"""

short_hand_tab_example = """pc.tabs(
    items = [("Tab 1", pc.text("Text from tab 1.")), ("Tab 2", pc.checkbox("Text from tab 2.")), ("Tab 3", pc.button("Text from tab 3.", color="black"))],
    bg="black",
    color="white",
    shadow="lg",
)
""" 


def render_tabs():
    return pc.vstack(
        doctext(
            "Tab components allow you display conent in multiple pages within a container. These page are organized by a tab list and the corresponoding tab panel can take in children components if needed."
        ),
        docdemo(tab_example),
        doctext(
            "You can create a tab component using the shorthand syntax. ",
            "Pass a list of tuples to the ",
            pc.code("items"),
            " prop. Each tuple should contain a label and a panel."
        ),
        docdemo(short_hand_tab_example),
        align_items="start",
    )
