import reflex as rx
from pcweb import styles
from pcweb.pages.docs.gallery import gallery
from pcweb.templates.docpage import doclink
from pcweb.templates.webpage import webpage

error_items = [
    {
        "error": "object null is not iterable",
        "error_explanation": rx.stack(
            rx.code("Server Error"),
            rx.code("TypeError: object null is not iterable (cannot read property Symbol(Symbol.iterator))"),
            direction="column",
            align="start",
        ),
        "solution": rx.stack(
            rx.heading("This is caused by using an older version of nodejs.", size="4"),
            rx.text("👉 Ensure the latest version of reflex is being used."),
            rx.text("👉 Remove the .web and ~/.reflex directories and re-run reflex init."),
            direction="column",
            align="start",
        ),
    },
    {
        "error": "Hydration failed because the initial UI does not match",
        "error_explanation": rx.stack(
            rx.code("Unhandled Runtime Error"),
            rx.code("Error: Hydration failed because the initial UI does not match what was rendered on the server."),
            direction="column",
            align="start",
        ),
        "solution": rx.stack(
            rx.heading("Often caused by incorrect nesting of components", size="4"),
            rx.text("Particularly <p> and <div>, but may also occur with tables."),
            rx.text("👉 Ensure there are no nested rx.text or layout components within rx.text."),
            rx.text("👉 Ensure that all tables are using rx.thead and rx.tbody to wrap the rx.tr rows."),
            rx.text.strong("No ❌"),
            rx.markdown(
                    r"""
                ```python
                rx.text(rx.text("foo"))
                rx.text(rx.box("foo"))
                rx.text(rx.center("foo"))
                ```
                """
                ),
            rx.markdown(
                    r"""
                ```python
                rx.table(
                    rx.tr(
                        rx.td("foo"),
                    )
                )
                ```
                """
                ),
            rx.text.strong("Yes ✅"),
            rx.markdown(
                    r"""
                ```python
                rx.text("foo")
                rx.box(rx.text("foo"))
                rx.center(rx.text("foo"))
                ```
                """
            ),
            rx.markdown(
                    r"""
                ```python
                rx.table(
                    rx.tbody(
                        rx.tr(
                            rx.td("foo"),
                        ),
                    )
                )
                ```
                """
            ),
            rx.text(f"See upstream docs: {rx.link('here.', href='https://nextjs.org/docs/messages/react-hydration-error')}"),
            direction="column",
            align="start",
        ),
    },
    {
        "error": "Invalid var passed for prop",
        "error_explanation": rx.code("TypeError: Invalid var passed for prop href, expected type <class 'str'>, got value \${state.my_list.at(i)} of type typing.Any."),
        "solution": rx.stack(
            rx.heading("Add a type annotation for list Vars", size="4"),
            rx.text("For certain props, reflex validates type correctness of the variable. Expecially when de-referencing lists and dicts, it is important to supply the correct annotation."),
            rx.markdown(
                    r"""
                ```python
                class State(rx.State):
                    # NO
                    my_list = ["a", "b", "c"]

                    # YES
                    my_indexable_list: list[str] = ["a", "b", "c"]
                ```
                """
            ),
            rx.text("👉 Add type annotations to all state Vars."),
            direction="column",
            align="start",
        ),
    },
    
]


def error_item(error, error_explanation, solution, index):
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                rx.vstack(
                    rx.heading(
                        error, color="#D6D6ED", font_size=styles.H3_FONT_SIZE
                    ),
                    rx.code(error_explanation, color="#D6D6ED"),
                    align_items="start",
                ),
                rx.chakra.spacer(),
                rx.chakra.accordion_icon(color="#6C6C81"),
                _hover={},
                padding_y="1em",
            ),
            rx.chakra.accordion_panel(solution, color="#6C6C81"),
            border="none",
        ),
        allow_multiple=True,
        border_radius= "12px;",
        border= "1px solid #37363F;",
        background= "rgba(47, 43, 55, 0.50);",
        box_shadow= "0px 3px 22px -2px #0C0B0F;",
        width="100%",
    )

def error_item_mobile(error, error_explanation, solution, index):
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                rx.vstack(
                    rx.heading(
                        error, color="#D6D6ED", font_size="1em",
                    ),
                    rx.code(error_explanation, color="#D6D6ED"),
                    align_items="start",
                ),
                rx.chakra.spacer(),
                rx.chakra.accordion_icon(color="#6C6C81"),
                padding_y="1em",
            ),
            rx.chakra.accordion_panel(solution, color="#6C6C81"),
            border="none",
        ),
        allow_multiple=True,
        border_radius="12px",
        border="1px solid #37363F",
        background="rgba(47, 43, 55, 0.50)",
        box_shadow="0px 3px 22px -2px #0C0B0F",
        width="90%",  # Adjust the width to a smaller value, e.g., 90%
        max_width="375px",  # Set a maximum width for the accordion
        margin="0 auto",  # Center the accordion horizontally
    )

def desktop_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Errors",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em"
                ),
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Reflex Errors",
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
            ),
            rx.text(
                "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our Discord.",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            error_item(item["error"], item["error_explanation"], item["solution"], index)
            for index, item in enumerate(error_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

def mobile_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Errors",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em",
                ),
                padding_buttom="1em",
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Reflex Errors",
                font_size="28px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="medium",
                letter_spacing="-1.28px;",
            ),
            rx.box(
                rx.text(
                    "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our Discord.",
                    color="#6C6C81",
                    width="360px",
                    align="center",
                ),
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            error_item(item["error"], item["error_explanation"], item["solution"], index)
            for index, item in enumerate(error_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

@webpage(path="/errors", title="Common Errors · Reflex")
def errors():
    return rx.container(
        rx.vstack(
            rx.mobile_only(mobile_view()),
            rx.tablet_and_desktop(desktop_view()),
        )
    )