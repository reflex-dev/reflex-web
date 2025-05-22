---
title: Library and Tags
---

```python exec
from pcweb.pages.docs import api_reference
```

# Find The Component

There are two ways to find a component to wrap:
1. Write the component yourself locally.
2. Find a well-maintained React library on [npm](https://www.npmjs.com/) that contains the component you need.

In both cases, the process of wrapping the component is the same except for the `library` field.

# Wrapping the Component

To start wrapping your React component, the first step is to create a new component in your Reflex app. This is done by creating a new class that inherits from `rx.Component` or `rx.NoSSRComponent`. 

See the [API Reference]({api_reference.component.path}) for more details on the `rx.Component` class.

This is when we will define the most important attributes of the component:
1. **library**: The name of the npm package that contains the component.
2. **tag**: The name of the component to import from the package.
3. **alias**: (Optional) The name of the alias to use for the component. This is useful if multiple component from different package have a name in common. If `alias` is not specified, `tag` will be used.
4. **lib_dependencies**: Any additional libraries needed to use the component.
5. **is_default**: (Optional) If the component is a default export from the module, set this to `True`. Default is `False`.

```md alert warning
# When setting the `library` attribute, it is recommended to included a pinned version of the package. Doing so, the package will only change when you intentionally update the version, avoid unexpected breaking changes.
```

```python
class MyBaseComponent(rx.Component):
    """MyBaseComponent."""

    # The name of the npm package.
    library = "my-library@x.y.z"

    # The name of the component to use from the package.
    tag = "MyComponent"

    # Any additional libraries needed to use the component.
    lib_dependencies: list[str] = ["package-deps@x.y.z"]

    # The name of the alias to use for the component.
    alias = "MyComponentAlias"

    # If the component is a default export from the module, set this to True.
    is_default = True/False
```

# Wrapping a Dynamic Component 

When wrapping some libraries, you may want to use dynamic imports. This is because they may not be compatible with Server-Side Rendering (SSR).

To handle this in Reflex, subclass `NoSSRComponent` when defining your component. It works the same as `rx.Component`, but it will automatically add the correct custom code for a dynamic import.

Often times when you see an import something like this:

```javascript
import dynamic from 'next/dynamic';

const MyLibraryComponent = dynamic(() => import('./MyLibraryComponent'), {
  ssr: false
});
```

You can wrap it in Reflex like this:

```python
from reflex.components.component import NoSSRComponent

class MyLibraryComponent(NoSSRComponent):
    """A component that wraps a lib needing dynamic import."""

    library = "my-library@x.y.z"

    tag="MyLibraryComponent"
```

It may not always be clear when a library requires dynamic imports. A few things to keep in mind are if the component is very client side heavy i.e. the view and structure depends on things that are fetched at run time, or if it uses `window` or `document` objects directly it will need to be wrapped as a `NoSSRComponent`. 

Some examples are:

1. Video and Audio Players
2. Maps
3. Drawing Canvas
4. 3D Graphics
5. QR Scanners
6. Reactflow

The reason for this is that it does not make sense for your server to render these components as the server does not have access to your camera, it cannot draw on your canvas or render a video from a file. 

In addition, if in the component documentation it mentions nextJS compatibility or server side rendering compatibility, it is a good sign that it requires dynamic imports.

