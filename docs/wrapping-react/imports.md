```python exec
import reflex as rx
from typing import Any
from pcweb.base_state import State
```
# Wrapping React


One of Reflex's most powerful features is the ability to wrap React components. This allows us to build on top of the existing React ecosystem, and leverage the vast array of existing React components and libraries.

If you want a specific component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component. Search for it on [npm](https://www.npmjs.com/), and if it's there, you can use it in your Reflex app.

In this section, we'll learn how to wrap React components and use them in Reflex apps.

## ColorPicker Example

Lets take a color picker example. We'll use the [react-colorful](https://www.npmjs.com/package/react-colorful) component, which is a simple color picker component.
