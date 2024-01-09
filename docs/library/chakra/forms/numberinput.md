---
components:
    - rx.chakra.NumberInput
    - rx.chakra.NumberInputField
    - rx.chakra.NumberInputStepper
    - rx.chakra.NumberIncrementStepper
    - rx.chakra.NumberDecrementStepper
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
```

# NumberInput

The NumberInput component is similar to the Input component, but it has controls for incrementing or decrementing numeric values.


```python exec
class NumberInputState(rx.State):
    number: int


def number_input_example():
    return rx.number_input(
        value=NumberInputState.number,
        on_change=NumberInputState.set_number,
    )
```

```python eval
docdemo_from(NumberInputState, component=number_input_example)
```
