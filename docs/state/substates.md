```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from
```

# Substates
A substate is a class that inherits from another state class, providing a means for two state classes to share common state resources, such as variables or event handlers.

## Creating a Substate
A substate can typically inherit from a base state(a state that inherits from `rx.State`) or another substate.
Let’s take a look at a simple example illustrating how and when to use substates. 
The code below shows two states, `RectangleState` and `SquareState`, each representing metadata about rectangles and squares, along with the calculation of their respective areas.

```python exec
class RectangleState(rx.State):
    name: str = "rectangle"
    shape_type: str = "quadrilateral"
    length: int = 10
    width: int = 5

    @rx.var
    def area(self) -> int:
        return self.length * self.width 

class SquareState(rx.State):
    name: str = "square"
    shape_type: str = "quadrilateral"
    length: int = 4

    @rx.var
    def area(self) -> int:
        return self.length ** 2



def my_badge():
    return rx.vstack(
        rx.hstack(
            rx.text(RectangleState.name),
            rx.text(RectangleState.area),
        ),
        rx.hstack(
            rx.text(SquareState.name),
            rx.text(SquareState.area),
        ),
    )
```

```python eval
docdemo_from(
    RectangleState,
    SquareState,
    component=my_badge,
)
```



In this code, you can see that both states share a common resource (`shape_type`). We can improve code organization and promote reusability by introducing the concept of substates. 
This involves creating a base state (`QuadrilateralState`), from which other states can inherit or subclass. After refactoring, the code takes on the following structure:

```python exec
class QuadrilateralState(rx.State):
    shape_type: str = "quadrilateral"

class RectangleState(QuadrilateralState):
    name: str = "rectangle"
    length: int = 10
    width: int = 5

    @rx.var
    def area(self) -> int:
        return self.length * self.width 

class SquareState(QuadrilateralState):
    name: str = "square"
    length: int = 4

    @rx.var
    def area(self) -> int:
        return self.length ** 2

```

It's important to note that certain variables, such as `length` and `name`, were not moved into the `QuadrilateralState` as they are not shared among substates. 
This approach streamlines the code, ensuring that only common resources are centralized in the base state while preserving the distinct characteristics of individual substates.

## Accessing Parent State Properties

You can access the parent state properties from a child substate, however you
cannot access the child properties from the parent state.

```python exec
def render_substate2():
    return rx.vstack(
        rx.hstack(
            rx.text(RectangleState.shape_type),
            rx.text(RectangleState.name),
            rx.text(RectangleState.area),
        ),
        rx.hstack(
            rx.text(SquareState.shape_type),
            rx.text(SquareState.name),
            rx.text(SquareState.area),
        ),
    )

```

```python eval
docdemo_from(component=render_substate2)
```
