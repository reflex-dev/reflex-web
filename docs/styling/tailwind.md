```python exec
import reflex as rx
from pcweb.pages.docs import library

```

# Tailwind

Reflex supports [Tailwind CSS]({"https://tailwindcss.com/"}) out of the box. To enable it, pass in a dictionary for the `tailwind` argument of your `rxconfig.py`:

```python
import reflex as rx

config = rx.Config(
    app_name="myapp",
    tailwind=\{},
)
```

All Tailwind configuration options are supported. Plugins and presets are automatically wrapped in `require()`:

```python
config = rx.Config(
    app_name="app",
    tailwind={
        "plugins": ["@tailwindcss/typography"],
    },
)
```

You can use any of the [utility classes]({"https://tailwindcss.com/docs/utility-first"}) under the `class_name` prop:

```python demo
rx.box(
    "Hello World",
    class_name="text-4xl text-center text-blue-500",
)
```

### Disabling Tailwind

If you want to disable Tailwind in your configuration, you can do so by setting the `tailwind` config to `None`. This can be useful if you need to temporarily turn off Tailwind for your project:

```python
config = rx.Config(app_name="app", tailwind=None)
```

With this configuration, Tailwind will be disabled, and no Tailwind styles will be applied to your application.


## Custom theme

You can integrate custom Tailwind themes within your Reflex app as well. The setup process is similar to the CSS Styling method mentioned above, with only a few minor variations.

Begin by creating a CSS file inside your `assets` folder. Inside the CSS file, include the following Tailwind directives:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: blue;
  --foreground: green;
}

.dark {
  --background: darkblue;
  --foreground: lightgreen;
}
```

We define a couple of custom CSS variables (--background and --foreground) that will be used throughout your app for styling. These variables can be dynamically updated based on the theme.

Tailwind defaults to light mode, but to handle dark mode, you can define a separate set of CSS variables under the .dark class. 

Tailwind Directives (@tailwind base, @tailwind components, @tailwind utilities): These are essential Tailwind CSS imports that enable the default base styles, components, and utility classes.

Next, you'll need to configure Tailwind in your `rxconfig.py` file to ensure that the Reflex app uses your custom Tailwind setup.

```python
import reflex as rx

tailwind_config = {
    "plugins": ["@tailwindcss/typography"],
    "theme": {
        "extend": {
            "colors": {
                "background": "var(--background)",
                "foreground": "var(--foreground)"
            },
        }
    },
}

config = rx.Config(
    app_name="app",
    tailwind=tailwind_config,
)
```

In the theme section, we're extending the default Tailwind theme to include custom colors. Specifically, we're referencing the CSS variables (--background and --foreground) that were defined earlier in your CSS file.

The rx.Config object is used to initialize and configure your Reflex app. Here, we're passing the tailwind_config dictionary to ensure Tailwind's custom setup is applied to the app.

Finally, to apply your custom styles and Tailwind configuration, you need to reference the CSS file you created in your `assets` folder inside the `rx.App` setup. This will allow you to use the custom properties (variables) directly within your Tailwind classes.

In your `app.py` (or main application file), make the following changes:

```python
app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/style.css"],
)
app.add_page(
    rx.center(
        rx.text("Tailwind & Reflex!"),
        class_name="bg-background w-full h-[100vh]",
    ),
    "/",
)
```

The bg-background class uses the --background variable (defined in the CSS file), which will be applied as the background color.

## Dynamic Styling

You can style a component based of a condition using `rx.cond` or `rx.match`.

```python demo exec
class TailwindState(rx.State):
    active = False

    @rx.event
    def toggle_active(self):
        self.active = not self.active

def tailwind_demo():
    return rx.el.div(
        rx.el.button(
            "Click me",
            on_click=TailwindState.toggle_active,
            class_name=(
                "px-4 py-2 text-white rounded-md",
                rx.cond(
                    TailwindState.active,
                    "bg-red-500",
                    "bg-blue-500",
                ),
            ),
        ),
    )
```

## Using Tailwind Classes from the State

When using Tailwind with Reflex, it's important to understand that class names must be statically defined in your code for Tailwind to properly compile them. If you dynamically generate class names from state variables or functions at runtime, Tailwind won't be able to detect these classes during the build process, resulting in missing styles in your application.

For example, this won't work correctly because the class names are defined in the state:

```python demo exec
class TailwindState(rx.State):
    active = False

    @rx.var
    def button_class(self) -> str:
        return "bg-accent" if self.active else "bg-secondary"

    @rx.event
    def toggle_active(self):
        self.active = not self.active

def tailwind_demo():
    return rx.el.button(
        f"Click me: {TailwindState.active}",
        class_name=TailwindState.button_class,
        on_click=TailwindState.toggle_active,
    )
```

## Using Tailwind with Reflex Core Components

Reflex core components are built on Radix Themes, which means they come with pre-defined styling. When you apply Tailwind classes to these components, you may encounter styling conflicts or unexpected behavior as the Tailwind styles compete with the built-in Radix styles.

For the best experience when using Tailwind CSS in your Reflex application, we recommend using the lower-level `rx.el` components. These components don't have pre-applied styles, giving you complete control over styling with Tailwind classes without any conflicts. Check the list of HTML components [here]({library.other.html.path}).

