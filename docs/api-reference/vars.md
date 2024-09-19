# Var System

## Motivation

Reflex supports some basic operations on state variables in the frontend. Those compile to their equivalent in Javascript. For example:

```python
rx.cond(
    State.threshold >= 50,
    "Pass",
    "Fail",
)
```

This would compile to roughly the following Javascript:

```js
state.threshold >= 50 ? "Pass" : "Fail";
```

## Overview

To put it in simple terms, a `Var` in Reflex represents a Javascript expression. If the type is known it can be any of the following:

- `NumberVar` representing an expression that evaluates to a Javascript `number`. This includes both integers and floating point values.
- `BooleanVar` represents a boolean expression. For example: `false`, `3 > 2`.
- `StringVar` represents an expression that evaluates to a string. For example: `'hello'`, `(2).toString()`.
- `ArrayVar` represents an expression that evalues to an array object. For example: `[1, 2, 3]`, `'words'.split()`.
- `ObjectVar` represents an expression that evalues to an object. For example: `\{a: 2, b: 3}`, `\{deeply: \{nested: \{value: false}}}`.
- `NoneVar` represents a null value. This can be either `undefiend` or `null`.

## Creating Vars

State fields are converted to `Var` by default. Additionally, you can create a `Var` from python values using `rx.Var.create()`:

```py
rx.Var.create(4) # NumberVar
rx.Var.create("hello") # StringVar
rx.Var.create([1, 2, 3]) # ArrayVar
```

If you want to create a `Var` from a raw Javascript string, you can call the init function instead:

```py
rx.Var("2", _var_type=int).guess_type() # NumberVar
```

We call `.guess_type()` to downcast the Var type into `NumberVar`. Calling `.to(int)` is also possible.

## Operations

The `Var` system supports some basic operations. For example, `NumberVar` supports basic arithmatic operations just like in Python. It also supports comparisions that would result in `BooleanVar`.

You can also define custom `Var` operations as such:

```python
from reflex.vars import var_operation, var_operation_return, ArrayVar, NumberVar

@var_operation
def multiply_array_values(a: ArrayVar):
    return var_operation_return(
        js_expression=f"\{a}.reduce((p, c) => p * c, 1)",
        var_type=int
    )

def factorial(value: NumberVar):
    return rx.cond(
        value <= 1,
        1,
        multiply_array_values(rx.Var.range(1, value+1))
    )
```
