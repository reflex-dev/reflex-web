---
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.templates.docpage import docalert, doccode, docheader, subheader
from pcweb.pages.docs.getting_started.introduction import CounterExampleState, counter_code
---

# Introduction

Reflex is a full-stack framework for building and deploying web apps.

## Motivation

Reflex was created with the following goals:

**Pure Python**

Use Python for everything. Don't worry about learning a new language.

**Easy to Learn**

Build and share your first app in minutes. No webdev experience required.

**Full Flexibility**

Remain as flexible as traditional web frameworks.
Reflex is easy to get started with, but powerful enough for advanced use cases.

Build anything from small data science apps to large, multi-page websites.

```reflex
rx.text(
    "This entire site was built and deployed with Reflex!",
    color=styles.ACCENT_COLOR_DARK,
)
```

**Batteries Included**

No need to reach for a bunch of different tools. Reflex handles the frontend, backend, and deployment of your app.

## First Example

Let's go over a simple counter app to explore the basics of Reflex.

```reflex
rx.hstack(
    rx.button(
        "Decrement",
        bg="#fef2f2",
        color="#b91c1c",
        border_radius="lg",
        on_click=CounterExampleState.decrement,
    ),
    rx.heading(
        CounterExampleState.count, font_size="2em", padding_x="0.5em"
    ),
    rx.button(
        "Increment",
        bg="#ecfdf5",
        color="#047857",
        border_radius="lg",
        on_click=CounterExampleState.increment,
    ),
)
```

Here is the full code for this example:

```python
{counter_code}
```

### The Structure of a Reflex App

Let's break this example down.

### Import

We begin by importing the `reflex` library. All Reflex functions and classes begin with the `rx` prefix.

## State
