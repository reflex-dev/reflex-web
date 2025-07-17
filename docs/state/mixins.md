```python exec
import reflex as rx
from pcweb.templates.docpage import definition
```

# State Mixins

State mixins allow you to define shared functionality that can be reused across multiple State classes. This is useful for creating reusable components, shared business logic, or common state patterns.

## What are State Mixins?

A state mixin is a State class marked with `mixin=True` that cannot be instantiated directly but can be inherited by other State classes. Mixins provide a way to share:

- Base variables
- Computed variables  
- Event handlers
- Backend variables

## Basic Mixin Definition

To create a state mixin, inherit from `rx.State` and pass `mixin=True`:

```python demo exec
class CounterMixin(rx.State, mixin=True):
    count: int = 0

    @rx.var
    def count_display(self) -> str:
        return f"Count: {self.count}"

    @rx.event
    def increment(self):
        self.count += 1

class MyState(CounterMixin, rx.State):
    name: str = "App"

def counter_example():
    return rx.vstack(
        rx.heading(MyState.name),
        rx.text(MyState.count_display),
        rx.button("Increment", on_click=MyState.increment),
        spacing="4",
        align="center",
    )
```

In this example, `MyState` automatically inherits the `count` variable, `count_display` computed variable, and `increment` event handler from `CounterMixin`.

## Multiple Mixin Inheritance

You can inherit from multiple mixins to combine different pieces of functionality:

```python demo exec
class TimestampMixin(rx.State, mixin=True):
    last_updated: str = ""

    @rx.event
    def update_timestamp(self):
        import datetime
        self.last_updated = datetime.datetime.now().strftime("%H:%M:%S")

class LoggingMixin(rx.State, mixin=True):
    log_messages: list[str] = []

    @rx.event
    def log_message(self, message: str):
        self.log_messages.append(message)

class CombinedState(CounterMixin, TimestampMixin, LoggingMixin, rx.State):
    app_name: str = "Multi-Mixin App"

    @rx.event
    def increment_with_log(self):
        self.increment()
        self.update_timestamp()
        self.log_message(f"Count incremented to {self.count}")

def multi_mixin_example():
    return rx.vstack(
        rx.heading(CombinedState.app_name),
        rx.text(CombinedState.count_display),
        rx.text(f"Last updated: {CombinedState.last_updated}"),
        rx.button("Increment & Log", on_click=CombinedState.increment_with_log),
        rx.cond(
            CombinedState.log_messages.length() > 0,
            rx.vstack(
                rx.foreach(
                    CombinedState.log_messages[-3:],
                    rx.text
                ),
                spacing="1"
            ),
            rx.text("No logs yet")
        ),
        spacing="4",
        align="center",
    )
```

## Backend Variables in Mixins

Mixins can also include backend variables (prefixed with `_`) that are not sent to the client:

```python demo box
class DatabaseMixin(rx.State, mixin=True):
    _db_connection: dict = {}  # Backend only
    user_count: int = 0        # Sent to client

    @rx.event
    def fetch_user_count(self):
        # Simulate database query
        self.user_count = len(self._db_connection.get("users", []))

class AppState(DatabaseMixin, rx.State):
    app_title: str = "User Management"
```

Backend variables are useful for storing sensitive data, database connections, or other server-side state that shouldn't be exposed to the client.

## Computed Variables in Mixins

Computed variables in mixins work the same as in regular State classes:

```python demo exec
class FormattingMixin(rx.State, mixin=True):
    value: float = 0.0

    @rx.var
    def formatted_value(self) -> str:
        return f"${self.value:.2f}"

    @rx.var
    def is_positive(self) -> bool:
        return self.value > 0

class PriceState(FormattingMixin, rx.State):
    product_name: str = "Widget"

    @rx.event
    def set_price(self, price: str):
        try:
            self.value = float(price)
        except ValueError:
            self.value = 0.0

def formatting_example():
    return rx.vstack(
        rx.heading(f"Product: {PriceState.product_name}"),
        rx.text(f"Price: {PriceState.formatted_value}"),
        rx.text(f"Positive: {PriceState.is_positive}"),
        rx.input(
            placeholder="Enter price",
            on_blur=PriceState.set_price,
        ),
        spacing="4",
        align="center",
    )
```

## Nested Mixin Inheritance

Mixins can inherit from other mixins to create hierarchical functionality:

```python demo box
class BaseMixin(rx.State, mixin=True):
    base_value: str = "base"

class ExtendedMixin(BaseMixin, mixin=True):
    extended_value: str = "extended"

    @rx.var
    def combined_value(self) -> str:
        return f"{self.base_value}-{self.extended_value}"

class FinalState(ExtendedMixin, rx.State):
    final_value: str = "final"
    # Inherits base_value, extended_value, and combined_value
```

This pattern allows you to build complex functionality by composing simpler mixins.

## Best Practices

```md alert info
# Mixin Design Guidelines

- **Single Responsibility**: Each mixin should have a focused purpose
- **Avoid Deep Inheritance**: Keep mixin hierarchies shallow for clarity  
- **Document Dependencies**: If mixins depend on specific variables, document them
- **Test Mixins**: Create test cases for mixin functionality
- **Naming Convention**: Use descriptive names ending with "Mixin"
```

## Limitations

```md alert warning
# Important Limitations

- Mixins cannot be instantiated directly - they must be inherited by concrete State classes
- Variable name conflicts between mixins are resolved by method resolution order (MRO)
- Mixins cannot override methods from the base State class
- The `mixin=True` parameter is required when defining a mixin
```

## Common Use Cases

State mixins are particularly useful for:

- **Authentication**: Shared login/logout functionality
- **Validation**: Common form validation logic
- **Logging**: Centralized logging and debugging
- **API Integration**: Shared HTTP client functionality
- **UI State**: Common modal, loading, or notification patterns

```python demo box
class AuthMixin(rx.State, mixin=True):
    is_authenticated: bool = False
    username: str = ""

    @rx.event
    def login(self, username: str):
        # Simplified login logic
        self.username = username
        self.is_authenticated = True

    @rx.event
    def logout(self):
        self.username = ""
        self.is_authenticated = False

class DashboardState(AuthMixin, rx.State):
    dashboard_data: list[str] = []

    @rx.var
    def welcome_message(self) -> str:
        return rx.cond(
            self.is_authenticated,
            f"Welcome, {self.username}!",
            "Please log in"
        )
```

By using state mixins, you can create modular, reusable state logic that keeps your application organized and reduces code duplication.
