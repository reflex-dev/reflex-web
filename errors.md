```python exec
import reflex as rx
from pcweb.templates.docpage.blocks.headings import h_comp_common
```

```python exec
@rx.memo
def h_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        font_size="1.5em",
        font_weight="700",
        margin_top="0em",
        scroll_margin="0em",
    )
```

```python exec
def error_message(heading: str, error_code: str, solution: rx.Component, error_type: str = "") -> rx.Component:
    if error_type != "":
        error_type = rx.badge(error_type, color_scheme="red")
    else:
        error_type = rx.box()
    return rx.card(
        rx.stack(
            h_comp(text=heading),
            rx.code(error_code, high_contrast=True),
            direction="column",
            align="start",
        ),
        rx.divider(),
        rx.accordion.root(
                rx.accordion.item(
                    header=error_type,
                    content=rx.stack(
                        *solution,
                        style={"color": "white"},
                        direction="column",
                        align="start",
                    ),
                    style={
                        "& .AccordionTrigger:hover": {
                                "background_color": "transparent",
                        }
                    },
                ),
                collapsible=True,
                variant="ghost",
            ),
            background_color=rx.color("mauve", 3),
            width="100%",
    )
```






```python eval
error_message(
    heading="Object null is not iterable",
    error_code="TypeError: object null is not iterable (cannot read property Symbol(Symbol.iterator))",
    solution=[
                rx.heading("This is caused by using an older version of nodejs."),
                rx.text("👉 Ensure the latest version of reflex is being used."),
                rx.text("👉 Remove the .web and ~/.reflex directories and re-run reflex init."),
    ],
    error_type="Server Error",

)
```

```python eval
error_message(
    heading="Hydration failed because the initial UI does not match",
    error_code="Error: Hydration failed because the initial UI does not match what was rendered on the server.",
    solution=[
                rx.heading("Often caused by incorrect nesting of components"),
                rx.text("Particularly `<p>` and `<div>`, but may also occur with tables"),
                rx.text("👉 Ensure there are no nested rx.text or layout components within `rx.text`"),
                rx.text("👉 Ensure that all tables are using rx.table.header and rx.table.body to wrap the rx.table.row rows"),
                rx.text.strong("No ❌"),
                rx.code_block(
"""rx.text(rx.text("foo"))
rx.text(rx.box("foo"))
rx.text(rx.center("foo"))""",
                    language="python",
                ),
                rx.code_block(
"""rx.table.root(
rx.table.row(
    rx.table.column_header_cell("Full name"),
),
)""",
                    language="python",
                ),
                rx.text.strong("Yes ✅"),
                rx.code_block(
"""rx.text("foo")
rx.box(rx.text("foo"))
rx.center(rx.text("foo"))""",
                    language="python",
                ),
                rx.code_block(
"""rx.table.root(
rx.table.header(
    rx.table.row(
        rx.table.column_header_cell("Full name"),
    ),
),
)""",
                    language="python",
                ),
                rx.text(
                    "See upstream docs ",
                    rx.link("here", href="https://nextjs.org/docs/messages/react-hydration-error"),
                    "."
                ),
    ],
    error_type="Unhandled Runtime Error",

)
```


```python eval
error_message(
    heading="Invalid var passed for prop",
    error_code="TypeError: Invalid var passed for prop href, expected type <class 'str'>, got value {state.my_list.at(i)} of type typing.Any.",
    solution=[
                rx.heading("Add a type annotation for list Vars"),
                rx.text("For certain props, reflex validates type correctness of the variable. Expecially when de-referencing lists and dicts, it is important to supply the correct annotation."),
                rx.code_block(
"""class State(rx.State):
    # NO
    my_list = ["a", "b", "c"]

    # YES
    my_indexable_list: list[str] = ["a", "b", "c"]""",
                    language="python",
                ),
                rx.text("👉 Add type annotations to all state Vars."),
    ],

)
```

