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
- `ObjectVar` represents an expression that evalues to an object. For example: `{a: 2, b: 3}`, `{deeply: {nested: {value: false}}}`.
- `NoneVar` represents a null value. This can be either `undefiend` or `null`.

## Creating Vars

State fields are converted to `Var` by default. Additionally, you can create a `Var` from python values using `rx.Var.create()`:

```python
rx.Var.create(4) # NumberVar
rx.Var.create("hello") # StringVar
rx.Var.create([1, 2, 3]) # ArrayVar
```

If you want to create a `Var` from a raw Javascript string, you can pass `_var_is_string=False`:

```python
rx.Var.create("2", _var_is_string=False).to(int) # NumberVar
```

We call `.to(int)` to inform the system about the kind of the raw Javascript expression we passed.

## Operations

The `Var` system supports some basic operations. For example, `NumberVar` supports basic arithmatic operations just like in Python. It also supports comparisions that would result in `BooleanVar`.

You can also define custom `Var` operations with the following:

```python
from reflex.ivars.base import var_operation, var_operation_return

@var_operation
def factorial(value: NumberVar):
    return var_operation_return(
        js_expression=f"{value} <= 1 ? 1 : Array.from({{length: {value}}}, (_, i) => i+1).reduce((p, c) => p * c)",
        var_type=int
    )

def index():
    rx.text(
        factorial(State.int_value)
    )
```

You can also compose existing operations:

```
@var_operation
def multipl
