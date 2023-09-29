---
import reflex as rx
from pcweb.templates.docpage import docdemo, docdemobox
from pcweb.pages.docs.component_lib.forms.button import (
          ButtonState,
          ExampleButtonState, 
          button_state, 
          button_state_code, 
          button_state_example, 
          button_state2, 
          button_state2_code, 
          button_state2_render_code,
          basic_button,
          button_sizes,
          button_colors,
          button_variants,
          button_disable,
          loading_states,
          stack_buttons_vertical,
          stack_buttons_horizontal,
          button_group 
                                
)
---
Buttons are essential elements in your application's user interface that users can click to trigger events. 
This documentation will help you understand how to use button components effectively in your Reflex application.

## Basic Usage
A basic button component is created using the `rx.button` method:

```reflex
docdemo(basic_button)
```
## Button Sizing
You can change the size of a button by setting the size prop to one of the following 
values: `xs`,`sm`,`md`, or `lg`.

```reflex
docdemo(button_sizes)
```

## Button colors
Customize the appearance of buttons by adjusting their color scheme through the color_scheme prop. 
You have the flexibility to choose from a range of color scales provided by your design 
system, such as whiteAlpha, blackAlpha, gray, red, blue, or even utilize your own custom color scale.

```reflex
docdemo(button_colors)
```

## Button Variants
You can customize the visual style of your buttons using the variant prop. Here are the available button variants:
- `ghost`: A button with a transparent background and visible text.
- `outline`: A button with no background color but with a border.
- `solid`: The default button style with a solid background color.
- `link`: A button that resembles a text link.
- `unstyled`: A button with no specific styling.

```reflex
docdemo(button_variants)
```
## Disabling Buttons
Make buttons inactive by setting the `is_disabled` prop to `True`.

```reflex
docdemo(button_disable)
```

## Handling Loading States
To indicate a loading state for a button after it's clicked, you can use the following properties:
- `is_loading`: Set this property to `True` to display a loading spinner.
- `loading_text`: Optionally, you can provide loading text to display alongside the spinner.
- `spinner_placement`: You can specify the placement of the spinner element, which is 'start' by default.


```reflex
docdemo(loading_states)
```

## Handling Click Events
You can define what happens when a button is clicked using the `on_click` event argument. 
For example, to change a value in your application state when a button is clicked:

```reflex
docdemobox(
    eval(button_state2_render_code)
)
```

```python
{button_state2_code.strip()}
```

In the code above, The value of `text_value` is changed through the `set_text_value` event handler upon clicking the button. 
Reflex provides a default setter event_handler for every base var which can be accessed by prefixing the base var with the `set_` keyword.

Here’s another example that creates two buttons to increase and decrease a count value:

```reflex
docdemobox(
    eval(button_state_example)
)
```

```python
{button_state_code.strip()}
```

In this example, we have a `ButtonState` state class that maintains a count base var. 
When the "Increment" button is clicked, it triggers the `ButtonState.increment` event handler, and when the "Decrement" 
button is clicked, it triggers the `ButtonState.decrement` event handler.

## Special Events and Server-Side Actions

Buttons in Reflex can trigger special events and server-side actions,
allowing you to create dynamic and interactive user experiences.
You can bind these events to buttons using the `on_click` prop.
For a comprehensive list of 
available special events and server-side actions, please refer to the
[Special Events Documentation](file:///docs/advanced-guide/background-tasks) ```reflex rx.text('click', on_click=rx.redirect('/docs/api-reference/special-events/'))``` for detailed information and usage examples.

## Grouping Buttons
In your Reflex application, you can group buttons effectively using the `Stack` component and 
the `ButtonGroup` component. Each of these options offers unique capabilities to help you structure 
and style your buttons.

## Using the `Stack` Component
The `Stack` component allows you to stack buttons both vertically and horizontally, providing a flexible
layout for your button arrangements.

## Stack Buttons Vertically:

```reflex
docdemo(stack_buttons_vertical)
```

## Stack Buttons Horizontally:

```reflex
docdemo(stack_buttons_horizontal)
```
With the `stack` component, you can easily create both vertical and horizontal button arrangements.

## Using the `rx.button_group` Component
The `ButtonGroup` component is designed specifically for grouping buttons. It allows you to:
- Set the `size` and `variant` of all buttons within it.
- Add `spacing` between the buttons.
- Flush the buttons together by removing the border radius of their children as needed.

```reflex
docdemo(button_group)
```
```reflex
rx.alert(
    icon=True,
    title=rx.text(
        "The ",
        rx.code("button_group"),
        " component stacks buttons horizontally, whereas the ",
        rx.code("stack"),
        " component allows stacking buttons both vertically and horizontally.",
    ),
)
```

