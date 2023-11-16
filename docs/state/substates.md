```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from
```

# Substates
As your app grows, your state will grow too.  You can split your state into
multiple substates from your base state to keep things organized.

## Creating a Substate
Your base state should inherit from `rx.State`. Substates can either inherit
from your base state or other substates.

```python exec
class ParentState(State):
    checked: bool = True
    count: int = 0


class ChildState1(ParentState):
    value: int = 42


class ChildState2(ParentState):
    color: str = "red"


class ChildState3(ChildState1):
    text: str = "Hello World"


def my_badge():
    return rx.badge(ChildState3.text, color_scheme=ChildState2.color)
```

```python eval
docdemo_from(
    ParentState,
    ChildState1,
    ChildState2,
    ChildState3,
    component=my_badge,
)
```

In the example above, we have a base state, `ParentState`, with two substates
`ChildState1` and `ChildState2`. Additionally, `ChildState3` inherits from
`ChildState1`. Components can access any var or event handler from any substate.

A common use case may be to create a substate for each page of your app, while
keeping general vars such as the logged in user in the base state for easy
access.

## Accessing Parent State Properties

You can access the parent state properties from a child substate, however you
cannot access the child properties from the parent state.

```python exec
def my_heading():
    return rx.heading(ChildState3.count, color="green")
```

```python eval
docdemo_from(component=my_heading)
```