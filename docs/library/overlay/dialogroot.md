---
components:
    - rx.radix.themes.DialogRoot
---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
from pcweb.templates.docpage import docdemo_from
```

# Radix Dialog

A modal dialog window displayed above the page.

The `dialog` component is made up of several lower level components. The first is the `dialog_root`, which contains all the parts of a dialog. Within this there is the `dialog_trigger`, which wraps the control that will open the dialog. In our example we have a `button` for this. 

The `dialog_content` comes next and this contains everything that we showcase within the `dialog` component. It can contain a `dialog_title`, a `dialog_description`, more components of our choice to showcase, and finally a `dialog_close` component. The `dialog_close` component, similar in nature to the `dialog_trigger` component, wraps the control that will close the dialog, in this case we use a `button` again.


```python demo
dialog_root(
    dialog_trigger(button("Open Dialog", size="4", variant="outline")),
    dialog_content(
        dialog_title("Welcome to Reflex!"),
        dialog_description(
            "This is a dialog component. You can render anything you want in here.",
        ),
        dialog_close(
            button("Close Dialog", size="3", variant="classic"),
        ),
    ),
)
```





## examples of using all the props (exclude the style props: color, variant, size)

N/A

## examples using all the event handlers

```python exec
class DialogState(rx.State):
    """The app state."""

    counter: int = 0

    def count_opens(self, open: bool) -> None:
        print(open)
        if open == True:
            self.counter += 1


def on_open_change_event():
    return dialog_root(
        dialog_trigger(button("Open Dialog", size="4", variant="outline")),
        dialog_content(
            dialog_title("Welcome to Reflex!"),
            dialog_description(
                "This is a dialog component. You can render anything you want in here.",
            ),
            dialog_close(
                button("Close Dialog", size="3", variant="classic"),
            ),
        ),
        on_open_change=DialogState.count_opens,
        #modal=False,
    )
```

The `on_open_change` event handler is called when the open state of the dialog changes. In this example we create an event handler `count_opens` that prints the value of `open`, which is the controlled open state of the dialog. We hook this `count_opens` event handler to the `dialog_root` event handler `on_open_change`. This means when the `dialog` component is opened up our `count_opens` event handler is triggered and we print the value of `open` and if this value of `open` is `True`, then we add 1 to our `counter` state var. 

As we click on the dialog component and then close it, we see the following printed in our terminal due to the `count_opens` event handler.

```bash
True
False
True
False
True
False
```


```python eval
docdemo_from(DialogState, component=on_open_change_event)
```

```python demo
text(DialogState.counter)
```




## give in context examples 


```python demo
dialog_root(
    dialog_trigger(
        button("Edit Profile", size="4", variant="outline")
    ),
    dialog_content(
        dialog_title("Edit Profile"),
        dialog_description(
            "Change your profile details and preferences.",
            size="2",
            mb="4",
        ),
        flex(
            text("Name", as_="div", size="2", mb="1", weight="bold"),
            textfield_input(default_value="Freja Johnson", placeholder="Enter your name"),
            text("Email", as_="div", size="2", mb="1", weight="bold"),
            textfield_input(default_value="freja@example.com", placeholder="Enter your email"),
            direction="column",
            gap="3",
        ),
        flex(
            dialog_close(
                button("Cancel", color_scheme="gray", variant="soft"),
            ),
            dialog_close(
                button("Save"),
            ),
            gap="3",
            mt="4",
            justify="end",
        ),
    ),
)
```


```python demo
dialog_root(
    dialog_trigger(button("View users", size="4", variant="outline")),
    dialog_content(
        dialog_title("Users"),
        dialog_description("The following users have access to this project."),

        inset(
            table_root(
                table_header(
                    table_row(
                        table_column_header_cell("Full Name"),
                        table_column_header_cell("Email"),
                        table_column_header_cell("Group"),
                    ),
                ),
                table_body(
                    table_row(
                        table_row_header_cell("Danilo Rosa"),
                        table_cell("danilo@example.com"),
                        table_cell("Developer"),
                    ),
                    table_row(
                        table_row_header_cell("Zahra Ambessa"),
                        table_cell("zahra@example.com"),
                        table_cell("Admin"),
                    ),
                ),
            ),
            side="x",
            my="5",
        ),
        flex(
            dialog_close(
                button("Close", variant="soft", color_scheme="gray"),
            ),
            gap="3",
            justify="end",
        ),
    ),
)
```