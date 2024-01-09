---
components:
    - rx.chakra.Tabs
    - rx.chakra.TabList
    - rx.chakra.Tab
    - rx.chakra.TabPanel
    - rx.chakra.TabPanels
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Tabs

Tab components allow you display content in multiple pages within a container.
These page are organized by a tab list and the corresponding tab panel can take in children components if needed.

```python demo
rx.tabs(
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
```

You can create a tab component using the shorthand syntax.
Pass a list of tuples to the `items` prop.
Each tuple should contain a label and a panel.

```python demo
rx.tabs(
    items = [("Tab 1", rx.text("Text from tab 1.")), ("Tab 2", rx.checkbox("Text from tab 2.")), ("Tab 3", rx.button("Text from tab 3.", color="black"))],
    bg="black",
    color="white",
    shadow="lg",
)
```