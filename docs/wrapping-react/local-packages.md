---
title: Wrapping Local Packages
---

```python exec
import reflex as rx
```

# Assets

If a wrapped component depends on assets such as images, scripts, or
stylesheets, these can be kept adjacent to the component code and
included in the final build using the `rx.asset` function.

`rx.asset` returns a relative path that references the asset in the compiled
output. The target files are copied into a subdirectory of `assets/external`
based on the module where they are initially used. This allows third-party
components to have external assets with the same name without conflicting
with each other.

For example, if there is an SVG file named `wave.svg` in the same directory as
this component, it can be rendered using `rx.image` and `rx.asset`.

```python
class Hello(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.hstack(
            rx.image(src=rx.asset("wave.svg", shared=True), width="50px", height="50px"),
            rx.heading("Hello ", *children),
            **props
        )
```


# Local Components

You can also wrap components that you have written yourself. For local components (when the code source is directly in the project), we recommend putting it beside the files that is wrapping it.

You can then use the path obtained via `rx.asset` to reference the component path.

So if you create a file called `hello.js` in the same directory as the component with this content:

```javascript
// /path/to/components/hello.js
import React from 'react';

export function Hello() {
  return (
    <div>
      <h1>Hello!</h1>
    </div>
  )
}
```

You can specify the library as follow (note: we use the `public` directory here instead of `assets` as this is the directory that is served by the web server):

```python
import reflex as rx

hello_path = rx.asset("hello.js", shared=True)
public_hello_path = "$/public/" + hello_path

class Hello(rx.Component):
    # Use an absolute path starting with $/public
    library = public_hello_path

    # Define everything else as normal.
    tag = "Hello"
```

# Local Packages

If the component is part of a local package, available on Github, or
downloadable via a web URL, it can also be wrapped in Reflex. Specify the path
or URL after an `@` following the package name.

Any local paths are relative to the `.web` folder, so you can use `../` prefix
to reference the Reflex project root.

Some examples of valid specifiers for a package called 
[`@masenf/hello-react`](https://github.com/masenf/hello-react) are:

* GitHub: `@masenf/hello-react@github:masenf/hello-react`
* URL: `@masenf/hello-react@https://github.com/masenf/hello-react/archive/refs/heads/main.tar.gz`
* Local Archive: `@masenf/hello-react@../hello-react.tgz`
* Local Directory: `@masenf/hello-react@../hello-react`

It is important that the package name matches the name in `package.json` so
Reflex can generate the correct import statement in the generated javascript
code.

These package specifiers can be used for `library` or `lib_dependencies`.

```python demo exec toggle
class GithubComponent(rx.Component):
    library = "@masenf/hello-react@github:masenf/hello-react"
    tag = "Counter"

    def add_imports(self):
        return {
            "": ["@masenf/hello-react/dist/style.css"]
        }

def github_component_example():
    return GithubComponent.create()
```

Although more complicated, this approach is useful when the local components
have additional dependencies or build steps required to prepare the component
for use.

Some important notes regarding this approach:

* The repo or archive must contain a `package.json` file.
* `prepare` or `build` scripts will NOT be executed. The distribution archive,
  directory, or repo must already contain the built javascript files (this is common).

```md alert
# Ensure CSS files are exported in `package.json`

In addition to exporting the module containing the component, any CSS files
intended to be imported by the wrapped component must also be listed in the
`exports` key of `package.json`.

```json
{
  // ...,
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.umd.cjs"
    },
    "./dist/style.css": {
      "import": "./dist/style.css",
      "require": "./dist/style.css"
    }
  },
  // ...
}
```