```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# Progress

Alerts are used to communicate a state that affects a system, feature or page.
An example of the different alert statuses is shown below.

```python demo
rx.vstack(
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Error Reflex version is out of date."),
        status="error",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Warning Reflex version is out of date."),
        status="warning",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is 0.1.32."),
        status="info",
    ),
    width="100%",
)
```

Along with different status types, alerts can also have different style variants and an optional description.
By default the variant is 'subtle'.

```python demo
rx.vstack(
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        rx.alert_description("No need to update."),
        status="success",
        variant="subtle",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
        variant="solid",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
        variant="top-accent",
    ),
    width="100%",
)
```