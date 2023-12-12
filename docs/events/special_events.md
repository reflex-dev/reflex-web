```python exec
import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from
from pcweb.pages.docs.api_reference.special_events import special_events
```


# Special Events

Reflex also has built-in special events can be found in the [reference]({special_events.path}).

For example, an event handler can trigger an alert on the browser.


```python exec
class SpecialEventsState(State):
    def alert(self):
        return rx.window_alert("Hello World!")

def special_events_example():
    return rx.button("Alert", on_click=SpecialEventsState.alert)

```

```python eval
docdemo_from(SpecialEventsState, component=special_events_example)
```