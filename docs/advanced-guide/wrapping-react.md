---
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.templates.docpage import docalert, doccode, docheader, subheader, docdemobox
from pcweb.pages.docs.getting_started.introduction import CounterExampleState, counter_code
---

# Wrapping React

One of Reflex's most powerful features is the ability to wrap React components.
This allows us to build on top of the powerful React ecosystem, but interface with it through Python.

Most of Reflex's base components are just wrappers around the great 
[Chakra UI](https://chakra-ui.com/) React component library.
Let's take a look at how we can wrap React components in Reflex.

## Step 1: Find a Library

If you want a cool component for your app but Reflex doesn't provide it, there's a good chance it's available as a React component.
Search the web for an [npm](https://www.npmjs.com/) package that has the component you want.

In this example, we will wrap the
[react-colorful](https://www.npmjs.com/package/react-colorful) color picker component.

## Step 2: Wrap the Library

To wrap the component, create a subclass of `rx.Component`.

```python
class ColorPicker(rx.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
```

The `library` attribute is the name of the npm package, 
and the `tag` attribute is the name of the component in the package.
