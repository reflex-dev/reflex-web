---
from pcweb.templates.docpage import docalert, doccode, docheader, subheader, docdemobox

console_log = (
"""
def index():
    return rx.button(
        'Log', on_click=rx.console_log('Hello World!')
    )
"""
)

redirect = (
"""
# Redirect to a new path within the application (opens in the same tab)
rx.redirect('/docs/api-reference/special-events')

# Redirect to an external URL in a new tab
rx.redirect('https://example.com', external=True)

"""
)

set_clipboard = (
"""
def index():
    return rx.button(
        'Copy 'Hello World' to clipboard',
        on_click=rx.set_clipboard('Hello World'),
    )
"""
)
set_value = (
"""
def index():
    return rx.hstack(
        rx.input(id='input1'),
        rx.button(
            'Erase', on_click=rx.set_value('input1', '')
        ),
    )
"""
)

window_alert = (
"""
def index():
    return rx.button(
        'Alert', on_click=rx.window_alert('Hello World!')
    )
"""
)
---

# Special Events.

Reflex includes a set of built-in special events that can be utilized as event triggers 
or returned from event handlers in your applications. These events enhance interactivity and user experience. 
Below are the special events available in Reflex, along with explanations of their functionality:

## console_log
Perform a console.log in the browser's console.

```python
{console_log}
```

When triggered, this event logs a specified message to the browser's developer console. 
It's useful for debugging and monitoring the behavior of your application.

## redirect
Redirect the user to a new path within the application.

### Parameters:
- `path`: The destination path or URL to which the user should be redirected.
- `external`: If set to True, the redirection will open in a new tab. Defaults to `False`.

```python
{redirect}
```

When this event is triggered, it navigates the user to a different page or location within your Reflex application. 
By default, the redirection occurs in the same tab. However, if you set the external parameter to True, the redirection 
will open in a new tab or window, providing a seamless user experience.

## set_clipboard
Set the specified text content to the clipboard.

```python
{set_clipboard}
```

This event allows you to copy a given text or content to the user's clipboard. 
It's handy when you want to provide a "Copy to Clipboard" feature in your application, 
allowing users to easily copy information to paste elsewhere.

## set_value
Set the value of a specified reference element.

```python
{set_value}
```

With this event, you can modify the value of a particular HTML element, typically an input field or another form element. 
It's useful for implementing dynamic updates and user interactions.

## window_alert
Create a window alert in the browser.

```python
{window_alert}
```
This event generates a browser alert dialog with the specified message. 
It's commonly used to display important messages or notifications to the user, such 
as warnings or confirmations.
