---
components:
    - rx.radix.themes.TabsRoot


---

```python exec
import reflex as rx
from reflex.components.radix.themes.components import *
from reflex.components.radix.themes.layout import *
from reflex.components.radix.themes.typography import *
import reflex.components.radix.themes as rdxt
```


# Tabs
A set of layered sections of content—known as tab panels—that are displayed one at a time.
Tabs facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.

## Basic Example

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 2"
                        ),
                    ),
                    value="tab2"
                ),
                default_value="tab1"
            )



```

The `tabs` component is made up of a `tabs_root` which groups `tabs_list` and `tabs_content` parts

### Variant

We use the variant prop to control the visual style of the avatar fallback text. The variant prop can be `"surface"` or `"ghost"`.

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 2"
                        ),
                    ),
                    value="tab2"
                ),
                default_value="tab1",
                variant="surface"
            )

```

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 2"
                        ),
                    ),
                    value="tab2"
                ),
                default_value="tab1",
                variant="ghost"
            )



```


### value
The controlled value of the tab to activate. Should be used in conjunction with onValueChange.

```python demo exec
class TabsState(rx.State):
    """The app state."""

    default_value = "tab1"
    tab_selected = ""
    def change_value(self, val):
        self.tab_selected = f"{val} clicked!"
        self.default_value = val



def index() -> rx.Component:
    return rdxt.theme(
        rdxt.container(
            rdxt.flex(
                rx.text(f"{TabsState.default_value}  clicked !"),
                rdxt.tabs_root(
                    rdxt.tabs_list(
                        rdxt.tabs_trigger(
                            "Account",
                            value="tab1"
                        ),
                        rdxt.tabs_trigger(
                            "Password",
                            value="tab2"
                        )
                    ),
                    rdxt.tabs_content(
                        rdxt.flex(
                            rdxt.text(
                                "Somthing on this page"
                            ),
                        ),
                        value="tab1"
                    ),
                    rdxt.tabs_content(
                        rdxt.flex(
                            rdxt.text(
                                "Another thing on this page"
                            ),
                        ),
                        value="tab2"
                    ),
                    default_value="tab1",
                    value=TabsState.default_value,
                    on_value_change=lambda x: TabsState.change_value(x),
                ),
                direction="column",
                gap="2"
            ),


            padding="2em",
            font_size="2em",
            text_align="center",
            background="var(--accent-2)",
            height="100vh",
        )
    )


```



### default value
You can use the value prop to set a default active tab, this will select the specified tab by default.

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 2"
                        ),
                    ),
                    value="tab2"
                ),
                default_value="tab2"
            )



```

### Orientation
You can set the orientation of the tabs component to `vertical` or `horizontal`. By default, the orientation
will be set to horizontal.

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 2"
                        ),
                    ),
                    value="tab2"
                ),
                default_value="tab1",
                orientation="vertical"
            )



```



## Tablist 
The Tablist is used to list the respective tabs to the tab component


### Tab Trigger
This is the button that activates its associated content. It is typically used in the `Tablist`

### Value
A unique value that associates the trigger with a content.

```python demo 

tabs_root(
    tabs_list(
    tabs_trigger(
                        "Tab 1",
                        value="tab1"
    ),
    tabs_trigger(
                        "Tab 2",
                        value="tab2"
                    )
                ),
    tabs_content(
        flex(
           text(
                            "item on tab 1"
                        ),
                    ),
                    value="tab1"
                ),
                default_value="tab1",
            )



```

### disabled


## Tabs Content


### value