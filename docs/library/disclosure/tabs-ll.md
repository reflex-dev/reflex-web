---
components:
    - rx.radix.tabs.root
    - rx.radix.tabs.list
    - rx.radix.tabs.trigger
    - rx.radix.tabs.content
---

```python exec
import reflex as rx
rdx = rx.radix
```


# Tabs
Tabs are a set of layered sections of content—known as tab panels—that are displayed one at a time.
They facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.

## Basic Example

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"), 
        rdx.tabs.trigger("Tab 2", value="tab2")
    ),
    rdx.tabs.content(
        rdx.text("item on tab 1"),
        value="tab1",
    ),
    rdx.tabs.content(
        rdx.text("item on tab 2"),
        value="tab2",
    ),
)

```

The `tabs` component is made up of a `rdx.tabs.root` which groups `rdx.tabs.list` and `rdx.tabs.content` parts.

## Styling

### Default value
We use the `default_value` prop to set a default active tab, this will select the specified tab by default.

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2")
    ),
    rdx.tabs.content(
        rdx.text("item on tab 1"),
        value="tab1",
    ),
    rdx.tabs.content(
        rdx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab2",
)
```

### Orientation
We use `orientation` prop to set the orientation of the tabs component to `vertical` or `horizontal`. By default, the orientation
will be set to `horizontal`. Note that, the orientation prop wont change the visual orientation but the 
functional orientation. This means for vertical orientation, the up and down arrow keys moves focus between the next or previous tab,
while for horizontal orientation, the left and right arrow keys moves focus between tabs.

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2")
    ),
    rdx.tabs.content(
        rdx.text("item on tab 1"),
        value="tab1",
    ),
    rdx.tabs.content(
        rdx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="vertical",
)
```

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2")
    ),
    rdx.tabs.content(
        rdx.text("item on tab 1"),
        value="tab1",
    ),
    rdx.tabs.content(
        rdx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="horizontal",
)
```
### Value
We use the `value` prop to specify the controlled value of the tab that we want to activate. This property should be used in conjunction with the `on_change` event argument.

```python demo exec
class TabsState(rx.State):
    """The app state."""

    value = "tab1"
    tab_selected = ""

    def change_value(self, val):
        self.tab_selected = f"{val} clicked!"
        self.value = val


def index() -> rx.Component:
    return rdx.theme(
        rdx.container(
            rdx.flex(
                rdx.text(f"{TabsState.value}  clicked !"),
                rdx.tabs.root(
                    rdx.tabs.list(
                        rdx.tabs.trigger("Tab 1", value="tab1"),
                        rdx.tabs.trigger("Tab 2", value="tab2"),
                    ),
                    rdx.tabs.content(
                         rdx.text("items on tab 1"),
                        value="tab1",
                    ),
                    rdx.tabs.content(
                        rdx.text("items on tab 2"),
                        value="tab2",
                    ),
                    default_value="tab1",
                    value=TabsState.value,
                    on_change=lambda x: TabsState.change_value(x),
                ),
                direction="column",
                gap="2",
            ),
            padding="2em",
            font_size="2em",
            text_align="center",
        )
    )
```


## Tablist 
The Tablist is used to list the respective tabs to the tab component


## Tab Trigger
This is the button that activates the tab's associated content. It is typically used in the `Tablist`

## Styling

### Value
We use the `value` prop to assign a unique value that associates the trigger with content.

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2"),
        rdx.tabs.trigger("Tab 3", value="tab3")
    ),
)
```

### Disable
We use the `disabled` prop to disable the tab.

```python demo 
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2"),
        rdx.tabs.trigger("Tab 3", value="tab3", disabled=True)
    ),
)
```

## Tabs Content
Contains the content associated with each trigger.

## Styling 

### Value
We use the `value` prop to assign a unique value that associates the content with a trigger.

```python
rdx.tabs.root(
    rdx.tabs.list(
        rdx.tabs.trigger("Tab 1", value="tab1"),
        rdx.tabs.trigger("Tab 2", value="tab2")
    ),
    rdx.tabs.content(
        rdx.text("item on tab 1"),
        value="tab1",
    ),
    rdx.tabs.content(
        rdx.text("item on tab 2"),
        value="tab2",
    ),
    default_value="tab1",
    orientation="vertical",
)
```