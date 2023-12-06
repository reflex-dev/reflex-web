```python exec
import inspect
import random
import time

import numpy as np

import reflex as rx

from pcweb.base_state import State
from pcweb.pages.docs.advanced_guide.custom_vars import custom_vars
from pcweb.templates.docpage import (
    doccode,
    docdemo_from,
    docheader,
    doclink,
    docpage,
    doctext,
)
```

# Var Operations

Var operations transform the placeholder representation of the value on the
frontend and provide a way to perform basic operations on the Var without having
to define a computed var.

Within your frontend components, you cannot use arbitrary Python functions on
the state vars. For example, the following code will **not work.**

```python
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, before `State.number` has a known value.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
```
This is because we compile the frontend to Javascript, but the value of `State.number`
is only known at runtime.


In this example below we use a var operation to concatenate a `string` with a `var`, meaning we do not have to do in within state as a computed var.

```python exec
coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(State):
    selected: str = "DOGE"

def var_operations_example():
    return rx.vstack(
        # Using a var operation to concatenate a string with a var.
        rx.heading("I just bought a bunch of " + VarSelectState.selected),
        # Using an f-string to interpolate a var.
        rx.text(f"{VarSelectState.selected} is going to the moon!"),
        rx.select(
            coins,
            value=VarSelectState.selected,
            on_change=VarSelectState.set_selected,
        )
    )
```

```python eval
docdemo_from(VarSelectState, component=var_operations_example, assignments={"coins": coins})
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Vars support many common operations."),
        rx.alert_description(
            "They can be used for arithemtic, string concatenation, inequalities, indexing, and more. "
            "See the ",
            doclink(
                "full list of supported operations",
                "/docs/api-reference/var",
            ),
            ".",
        ),
    ),
    status="success",
    margin_bottom="3em",
)
```




## Supported Operations

Var operations allow us to change vars on the front-end without having to create more computed vars on the back-end in the state.

The `==` var operator is used to check if two vars are equal. The `to_string()` var operator is used to convert a var to a string.

```python exec

fruits = ["Apple", "Banana", "Orange", "Mango"]

class VarEqualsState(State):
    selected: str = "Apple"
    favorite: str = "Banana"


def var_equals_example():
    return rx.vstack(
        rx.text(VarEqualsState.favorite.to_string() + "is my favorite fruit!"),
        rx.select(
            fruits,
            value=VarEqualsState.selected,
            on_change=VarEqualsState.set_selected,
        ),
        rx.cond(
            VarEqualsState.selected == VarEqualsState.favorite,
            rx.text("The selected fruit is equal to the favorite fruit!"),
            rx.text("The selected fruit is not equal to the favorite fruit."),
        ),
    )

```

```python eval
docdemo_from(VarEqualsState, component=var_equals_example, assignments={"fruits": fruits})
```

### Negate, Absolute and Length

The `-` operator is used to get the negative version of the var. The `abs()` operator is used to get the absolute value of the var. The `.length()` operator is used to get the length of a list var.


```python exec
import random

class VarOperationState(State):
    number: int
    numbers_seen: list = []
    def update(self):
        self.number = random.randint(-100, 100)
        self.numbers_seen.append(self.number)

def var_operation_example():
    return rx.vstack(
        rx.heading(f"The number is {VarOperationState.number}"),
    
        rx.text(f"The negated number is {-VarOperationState.number}"),
        rx.text(f"The absolute value of the number is {abs(VarOperationState.number)}"),
        rx.text(f"Number of values seen so far {VarOperationState.numbers_seen.length()}"),
        rx.button("Update", on_click=VarOperationState.update),
    )
```

```python eval
docdemo_from(VarOperationState, component=var_operation_example, imports=["import random"])
```

### Comparisons and Mathematical Operators

All of the comparison operators are used as expected in python. These include `==`, `!=`, `>`, `>=`, `<`, `<=`. 

There are operators to add two vars `+`, subract two vars `-`, multiply two vars `*` and raise a var to a power `pow()`.

```python exec
import random

class VarComparisonState(State):
    number_1: int
    number_2: int

    def update(self):
        self.number_1 = random.randint(-10, 10)
        self.number_2 = random.randint(-10, 10)

def var_comparison_example():
    return rx.vstack(
        rx.heading(f"Integer 1 is {VarComparisonState.number_1}"),
        rx.heading(f"Integer 2 is {VarComparisonState.number_2}"),
        # Var operations can be composed for more complex expressions.
        
        rx.text(f"Integer 1 and Integer 2 are equal (==): {VarComparisonState.number_1 == VarComparisonState.number_2}"),
        rx.text(f"Integer 1 and Integer 2 are not equal (!=): {VarComparisonState.number_1 != VarComparisonState.number_2}"),
        rx.text(f"Integer 1 is larger than Integer 2 (>): {VarComparisonState.number_1 > VarComparisonState.number_2}"),
        rx.text(f"Integer 1 is larger than or equal to Integer 2 (>=): {VarComparisonState.number_1 >= VarComparisonState.number_2}"),
        rx.text(f"Integer 1 is less than Integer 2 (<): {VarComparisonState.number_1 < VarComparisonState.number_2}"),
        rx.text(f"Integer 1 is less than or equal Integer 2 (<=): {VarComparisonState.number_1 <= VarComparisonState.number_2}"),
        rx.text(f"Sum of Integer 1 and Integer 2 (+): {VarComparisonState.number_1 + VarComparisonState.number_2}"),
        rx.text(f"Take Integer 2 away from Integer 1 (-): {VarComparisonState.number_1 - VarComparisonState.number_2}"),
        rx.text(f"Multiplication of Integer 1 and Integer 2 (*): {VarComparisonState.number_1 * VarComparisonState.number_2}"),
        rx.text(f"Integer 1 to the power of Integer 2 (pow()): {pow(VarComparisonState.number_1, VarComparisonState.number_2)}"),
        rx.button("Update", on_click=VarComparisonState.update),
    )
```

```python eval
docdemo_from(VarComparisonState, component=var_comparison_example, imports=["import random"])
```

### True Division, Floor Division and Remainder

The operator `/` represents true division. The operator `//` represents floor division. The operator `%` represents the remainder of the division.

```python exec
import random

class VarDivState(State):
    number_1: float = 3.5
    number_2: float = 1.4

    def update(self):
        self.number_1 = round(random.uniform(5.1, 9.9), 2)
        self.number_2 = round(random.uniform(0.1, 4.9), 2)

def var_div_example():
    return rx.vstack(
        rx.heading(f"Integer 1 is {VarDivState.number_1}"),
        rx.heading(f"Integer 2 is {VarDivState.number_2}"),
        
        rx.text(f"True Division of Integer 1 and Integer 2 (/): {VarDivState.number_1 / VarDivState.number_2}"),
        rx.text(f"Floor Division of Integer 1 and Integer 2 (//): {VarDivState.number_1 // VarDivState.number_2}"),
        rx.text(f"Remainder of Integer 1 and Integer 2 (%): {VarDivState.number_1 % VarDivState.number_2}"),
        
        rx.button("Update", on_click=VarDivState.update),
    )
```

```python eval
docdemo_from(VarDivState, component=var_div_example, imports=["import random"])
```


### And, Or and Not

In Reflex the `&` operator represents the logical AND when used in the front end. This means that it returns true only when both conditions are true simultaneously. 
The `|` operator represents the logical OR when used in the front end. This means that it returns true when either one or both conditions are true.
The `~` operator is used to invert a var. It is used on a var of type `bool` and is equivalent to the `not` operator.

```python exec
import random

class VarLogicalState(State):
    var_1: bool = True
    var_2: bool = True

    def update(self):
        self.var_1 = random.choice([True, False])
        self.var_2 = random.choice([True, False])

def var_logical_example():
    return rx.vstack(
        rx.heading(f"Var 1 is {VarLogicalState.var_1}"),
        rx.heading(f"Var 2 is {VarLogicalState.var_2}"),
        
        rx.text(f"Logical AND: {VarLogicalState.var_1 & VarLogicalState.var_2}"),
        rx.text(f"Logical OR: {VarLogicalState.var_1 | VarLogicalState.var_2}"),
        rx.text(f"The inverted var is {~VarOperationState.number}"),

        rx.button("Update", on_click=VarLogicalState.update),
    )
```

```python eval
docdemo_from(VarLogicalState, component=var_logical_example, imports=["import random"])
```

### Contains, Reverse and Join


The 'in' operator is not supported for Var types, we must use the `Var.contains()` instead. When we use `contains`, the var must be of type: `dict`, `list`, `tuple` or `str`. 
`contains` checks if a var contains the object that we pass to it as an argument.

We use the `reverse` operation to reverse a list var. The var must be of type `list`.

Finally we use the `join` operation to join a list var into a string. 

```python exec
class VarListState(State):
    list_1: list = [1, 2, 3, 4, 6]
    list_2: list = [7, 8, 9, 10]
    list_3: list = ["p","y","t","h","o","n"]

def var_list_example():
    return rx.vstack(
        rx.heading(f"List 1 is {VarListState.list_1}"),
        rx.heading(f"List 2 is {VarListState.list_2}"),
        
        rx.text(f"Does List 1 contain the number 3: {VarListState.list_1.contains(3)}"),
        rx.text(f"Reverse List 2: {VarListState.list_2.reverse()}"),
        rx.text(f"Join List 3 into string: {VarListState.list_3.join()}"),

    )
```

```python eval
docdemo_from(VarListState, component=var_list_example)
```



### Lower, Upper, Split

The `lower` operator converts a string var to lowercase. The `upper` operator converts a string var to uppercase. The `split` operator splits a string var into a list.

```python exec
class VarStringState(State):
    string_1: str = "PYTHON is FUN"
    string_2: str = "react is hard"
   

def var_string_example():
    return rx.vstack(
        rx.heading(f"List 1 is {VarStringState.string_1}"),
        rx.heading(f"List 2 is {VarStringState.string_2}"),

        rx.heading(f"Lower Case output: {VarStringState.string_1.lower()}"),
        rx.heading(f"Upper Case output: {VarStringState.string_2.upper()}"),
        rx.heading(f"Split String 2: {VarStringState.string_2.split()}"),   
    )
```

```python eval
docdemo_from(VarStringState, component=var_string_example)
```






## Combine Multiple Var Operations

You can also combine multiple var operations together, as seen in the next example.

```python exec
import random

class VarNumberState(State):
    number: int

    def update(self):
        self.number = random.randint(0, 100)

def var_number_example():
    return rx.vstack(
        rx.heading(f"The number is {VarNumberState.number}"),
        # Var operations can be composed for more complex expressions.
        rx.cond(
            VarNumberState.number % 2 == 0,
            rx.text("Even", color="green"),
            rx.text("Odd", color="red"),
        ),
        rx.button("Update", on_click=VarNumberState.update),
    )
```

```python eval
docdemo_from(VarNumberState, component=var_number_example, imports=["import random"])
```

We could have made a computed var that returns the parity of `number`, but
it can be simpler just to use a var operation instead.

Var operations may be generally chained to make compound expressions, however
some complex transformations not supported by var operations must use computed vars
to calculate the value on the backend.