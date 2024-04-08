```python exec
import reflex as rx
from pcweb.pages.docs import library
```

# Theming

As of Reflex `v0.4.0`, you can now theme your Reflex applications. The core of our theming system is directly based on the [Radix Themes](https://www.radix-ui.com) library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.

## Theme

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
```

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the [Theme Panel docs]({library.theming.theme_panel.path}).

## Colors

### Color Scheme

On a high-level, component `color_scheme` inherits from the color specified in the theme. This means that if you change the theme, the color of the component will also change. Available colors can be found [here](https://www.radix-ui.com/colors).

You can also specifiy the `color_scheme` prop.

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color_scheme="tomato",
    ),
    rx.button(
        "Hello World",
        color_scheme="teal",
    ),
    spacing="2"
)
```

### Specific Shades of Palettes

To access a specific shade of color from the theme, you can use the `rx.color`. When switching to light and dark themes, the color will automatically change.

Shades can be accessed by using the color name and the shade number. The shade number ranges from 1 to 12. Additionally, they can have their alpha value set by using the `True` parameter it defaults to `False`.

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color=rx.color("grass", 1),
        background_color=rx.color("grass", 12),
        border_color=f"1px solid {rx.color('grass', 1)}",
    ),
    rx.button(
        "Hello World",
        color=rx.color("grass", 1, True),
        background_color=rx.color("grass", 12, True),
        border_color=f"1px solid {rx.color('grass', 1, True)}",
    ),
    spacing="2"
)
```

### Regular Colors

You can also use standard hex, rgb, and rgba colors.

```python demo
rx.flex(
    rx.button(
        "Hello World",
        color="white",
        background_color="blue",
        border_color="1px solid red",
    ),
    rx.button(
        "Hello World",
        color="#ff0000",
        background_color="rgba(0, 0, 255, 0.5)",
        border_color="1px solid #ff0000",
    ),
    spacing="2"
)
```

### Color Mode

```python
rx.color_mode_cond(
    rx.image(src="/logos/light/reflex.svg", height="4em"),
    rx.image(src="/logos/dark/reflex.svg", height="4em"),
)
```

`rx.color_mode_cond` can be used to render a different component depending on whether the app is in `light` mode or `dark` mode. 

The first argument to the `color_mode_cond` component is the component to render when the app is in `light` mode. 

The second argument is the component to render when the app is in `dark` mode.


```python
rx.color_mode.switch()
```

`rx.color_mode.switch` is used to add a switch to your app to allow the user to easily switch the app between `light` mode and `dark` mode.


```python
rx.color_mode.button()
```

`rx.color_mode.button` is very similar to the `switch` above and is used to add a button to your app to allow the user to easily switch the app between `light` mode and `dark` mode.


```python
rx.color_mode.icon()
```

`rx.color_mode.icon` creates an `icon` component based on `color_mode`. By default it has the sun and moon icon for `light` and `dark` mode. You can change these by passing the icon for `light` mode as `light_component=` and `dark` mode as `dark_component=` to the `rx.color_mode.icon` component.