---
components:
    - rx.Match
---

```python exec
import reflex as rx
```
# Match

The `rx.match` feature in Reflex serves as a powerful alternative to `rx.cond` for handling conditional statements. 
While `rx.cond` excels at conditionally rendering two components based on a single condition, 
`rx.match` extends this functionality by allowing developers to handle multiple conditions and their associated components. 
This feature is especially valuable when dealing with intricate conditional logic or nested scenarios, 
where the limitations of `rx.cond` might lead to less readable and more complex code.

With `rx.match`, developers can not only handle multiple conditions but also perform structural pattern matching, 
making it a versatile tool for managing various scenarios in Reflex applications.

## Basic Usage
The rx.match function provides a clear and expressive syntax for handling multiple 
conditions and their corresponding components:

```python
rx.match(
    condition,
    (case_1, component_1),
    (case_2, component_2),
    ...
    default_component,
)


```
- `condition`: The value to match against.
- `(case_i, component_i)`: A Tuple of matching cases and their corresponding return components.
- `default_component`: A special case for the default component when the condition isnt matched by any of the match cases.

Example

```python demo exec
from typing import List

options: List[str] = ["red", "green", "blue"]

class MatchState(rx.State):
    color: str = ""



def match_demo():
    return rx.vstack(
        rx.match(
            MatchState.color,
            ("red", rx.text("red color selected")),
            ("green", rx.text("green color selected")),
            rx.text("Default color selected.")
        ),
        rx.select(
            options,
            placeholder="Select a color.",
            on_change=MatchState.set_color,
            color_schemes="twitter",
        ),
    )


```


## Default Case
The default case in rx.match serves as a universal handler for scenarios where none of 
the specified match cases aligns with the given match condition. Here are key considerations 
when working with the default case:

- **Placement in the Match Function**: The default case must be the last non-tuple argument in the rx.match function. 
All match cases should be enclosed in tuples; any non-tuple value is automatically treated as the default case. For example:
    
 ```python
rx.match(
            MatchState.color,
            ("red", rx.text("red color selected")),
            rx.text("Default color selected.")
            ("green", rx.text("green color selected")),
        )
```
The above code snippet will result in an error due to the misplaced default case.

- **Single Default Case**: Only one default case is allowed in the rx.match function. 
Attempting to specify multiple default cases will lead to an error. For instance:

 ```python
rx.match(
            MatchState.color,
            ("red", rx.text("red color selected")),
            ("green", rx.text("green color selected")),
            rx.text("Default color selected."),
            rx.text("Another default color selected.")
        )
```

- **Optional Default Case for Component Return Values**: If the match cases in a rx.match component 
return components, the default case can be optional. In this scenario, if a default case is 
not provided, rx.fragment will be implicitly assigned as the default. For example:

 ```python
rx.match(
            MatchState.color,
            ("red", rx.text("red color selected")),
            ("green", rx.text("green color selected")),
        )
```
In this case, rx.fragment is the default case. However, not providing a default case for non-component 
return values will result in an error:

 ```python
rx.match(
            MatchState.color,
            ("red", "first value"),
            ("green", "second value"),
        )
```
The above code snippet will result in an error as a default case must be explicitly 
provided in this scenario.


## Handling Multiple Conditions

`rx.match` excels in efficiently managing multiple conditions and their corresponding components, 
providing a cleaner and more readable alternative compared to nested `rx.cond` structures.

Consider the following example:

```python demo exec
from typing import List

options: List[str] = ["red", "green", "blue", "yellow", "orange", "black", "white"]

class MultiMatchState(rx.State):
    color: str = ""



def multi_match_demo():
    return rx.vstack(
        rx.match(
            MultiMatchState.color,
            ("red", "yellow", "blue", rx.text("primary color")),
            ("green","orange", rx.text("secondary color")),
            rx.text("neither primary nor secondary.")
        ),
        rx.select(
            options,
            placeholder="Select a color.",
            on_change=MultiMatchState.set_color,
        ),
    )


```

In a match case tuple, you can specify multiple conditions. The last value of the match case 
tuple is automatically considered as the return value. It's important to note that a match case
tuple should contain a minimum of two elements: a match case and a return value. 
The following code snippet will result in an error:

```python
rx.match(
            MatchState.color,
            ("red",),
            ("green", rx.text("green color selected")),
        )

```
## Usage as Props
Similar to rx.cond, rx.match can be used as prop values, allowing dynamic behavior for UI components:

```python demo exec
class MatchPropState(rx.State):
    value: int = 0
    
    def incr(self):
        self.value += 1
    
    def decr(self):
        self.value -= 1


def match_prop_demo_():
    return rx.vstack(
        rx.text(
            MatchPropState.value, 
            color= rx.match(
                MatchPropState.value,
                (1, "red"),
                (5, "blue"),
                (10, "green"),
                (15, "orange"),
                "black"
                
            )
        ),
        rx.hstack(
            rx.button("increment", on_click=MatchPropState.incr),
            rx.button("decrement", on_click=MatchPropState.decr),
        ),
    )


```

In the example above, the color property of the text component containing `State.value` changes to red when 
`state.value` is 1, blue when its 5, green when its 5, orange when its 15 and black for any other value.

The example below also shows handling multiple conditions with the match component as props.

```python demo exec
class MatchMultiPropState(rx.State):
    value: int = 0
    
    def incr(self):
        self.value += 1
    
    def decr(self):
        self.value -= 1


def match_multi_prop_demo_():
    return rx.vstack(
        rx.text(
            MatchMultiPropState.value, 
            color= rx.match(
                MatchMultiPropState.value,
                (1, 3, 9, "red"),
                (2, 4, 5, "blue"),
                (6, 8, 12, "green"),
                (10, 15, 20, 25, "orange"),
                "black"
                
            )
        ),
        rx.hstack(
            rx.button("increment", on_click=MatchMultiPropState.incr),
            rx.button("decrement", on_click=MatchMultiPropState.decr),
        ),
    )


```


```md alert warning
# Usage with Structural Pattern Matching

The `rx.match` component is designed for structural pattern matching. If the value of your match condition evaluates to a boolean (True or False), it is recommended to use `rx.cond` instead. 

Consider the following example, which is more suitable for `rx.cond`:

```python
rx.cond(
    MatchPropState.value == 10,
    "true value",
    "false value"
)
```
```