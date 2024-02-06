```python exec
import reflex as rx
```

# Conditional Props

Sometimes you want to set a prop based on a condition. You can use the `rx.cond` function to do this.

```python demo exec
class PropCondState(rx.State):
    value: int


def cond_prop():
    return rx.chakra.slider(
        on_change_end=PropCondState.set_value,
        color_scheme=rx.cond(PropCondState.value > 50, "green", "pink"),
    )
```