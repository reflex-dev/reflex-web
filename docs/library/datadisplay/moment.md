---
components:
    - rx.moment

---
Displaying date and relative time to now sometimes can be more complicated than necessary.

To make it easy, Reflex is wrapping [react-moment](https://www.npmjs.com/package/react-moment)  under `rx.moment`.


```python exec
import reflex as rx
from reflex.utils.serializers import serialize_datetime
from datetime import datetime
from pcweb.templates.docpage import docdemo, docdemobox, doccode, docgraphing

class MomentState(rx.State):
    date_now: datetime = datetime.now()
```

## Examples

Using the same date as a value, we will display it in a few different way using `rx.moment`

```python
class MomentState(rx.State):
    date_now: datetime = datetime.now()
```

### Display the date as-is:

```python exec
as_is_example="rx.moment(MomentState.date_now)"
```

```python eval
docdemo(
    as_is_example,
    comp=eval(as_is_example)
)
```

### Humanized interval

```python exec
from_now_example = "rx.moment(MomentState.date_now, from_now=True)"
to_now_example = "rx.moment(MomentState.date_now, to_now=True)"
from_now_during_example = "rx.moment(MomentState.date_now, from_now_during=100000)  # after 100 seconds, date will display normally"
```

Sometimes we don't want to display just a raw date, but we want something more instinctive to read. That's when we can use `from_now` and `to_now`.

```python eval
docdemo(from_now_example, comp=eval(from_now_example))
```

```python eval
docdemo(to_now_example, comp=eval(to_now_example))
```
You can also set a duration (in milliseconds) with `from_now_during` where the date will display as relative, then after that, it will be displayed as defined in `format`.

```python eval
docdemo(from_now_during_example, comp=eval(from_now_during_example))
```

### Formatting dates

```python exec
format_example_1 = 'rx.moment(MomentState.date_now, format="YYYY-MM-DD")'
format_example_2 = 'rx.moment(MomentState.date_now, format="HH:mm:SS")'
```

```python eval
docdemo(format_example_1, comp=eval(format_example_1))
```

```python eval
docdemo(format_example_2, comp=eval(format_example_2)
)
```

### Offset Date

With the props `add` and `substract`, you can pass an `rx.MomentDelta` object to modify the displayed date without affecting the stored date in your state.

```python exec
add_example = """rx.vstack(
    rx.moment(MomentState.date_now, add=rx.MomentDelta(years=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(quarters=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(weeks=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(days=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(hours=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(minutes=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, add=rx.MomentDelta(seconds=2), format="YYYY-MM-DD - HH:mm:SS"),
)
"""
subtract_example = """rx.vstack(
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(years=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(quarters=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(months=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(weeks=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(days=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(hours=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(minutes=2), format="YYYY-MM-DD - HH:mm:SS"),
    rx.moment(MomentState.date_now, subtract=rx.MomentDelta(seconds=2), format="YYYY-MM-DD - HH:mm:SS"),
)
"""
```

```python eval
rx.tabs(
    rx.tabs.list(
        rx.tabs.trigger("Add", value="add"), 
        rx.tabs.trigger("Substract", value="substract")
    ),
    rx.tabs.content(docdemo(add_example, comp=eval(add_example)), value="add"),
    rx.tabs.content(docdemo(subtract_example, comp=eval(subtract_example)), value="substract"),
)
```

### Timezones

You can also set dates to display in a specific timezone:

```python exec
timezone_example1 = """rx.vstack(
    rx.moment(MomentState.date_now, tz="America/Los_Angeles"),
    rx.moment(MomentState.date_now, tz="Europe/Paris"),
    rx.moment(MomentState.date_now, tz="Asia/Tokyo"),
)
"""
```

```python eval
docdemo(timezone_example1, comp=eval(timezone_example1))
```