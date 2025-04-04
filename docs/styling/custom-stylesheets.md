```python exec
import reflex as rx
from pcweb.pages.docs import assets
```

# Custom Stylesheets

Reflex allows you to add custom stylesheets. Simply pass the URLs of the stylesheets to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)
```

## Local Stylesheets

You can also add local stylesheets. Just put the stylesheet under [`assets/`]({assets.upload_and_download_files.path}) and pass the path to the stylesheet to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "/styles.css",  # This path is relative to assets/
    ],
)
```

```md alert warning
# Always use a leading slash (/) when referencing files in the assets directory.
Without a leading slash the path is considered relative to the current page route and may
not work for routes containing more than one path component, like `/blog/my-cool-post`.
```


## Styling with CSS

You can use CSS variables directly in your Reflex app by passing them alongside the appropriae props. Create a `style.css` file inside the `assets` folder with the following lines:

```css
:root {
    --primary-color: blue;
    --accent-color: green;
}
```

Then, after referencing the CSS file within the `stylesheets` props of `rx.App`, you can access the CSS props directly like this

```python
app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/style.css"],
)
app.add_page(
    rx.center(
        rx.text("CSS Variables!"),
        width="100%",
        height="100vh",
        bg="var(--primary-color)",
    ),
    "/",
)
```

## Styling with Tailwind

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

## Fonts

You can take advantage of Reflex's support for custom stylesheets to add custom fonts to your app.

In this example, we will use the [IBM Plex Mono]({"https://fonts.google.com/specimen/IBM+Plex+Mono"}) font from Google Fonts. First, add the stylesheet with the font to your app. You can get this link from the "Get embed code" section of the Google font page.

```python
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)
```

Then you can use the font in your component by setting the `font_family` prop.

```python demo
rx.text(
    "Check out my font",
    font_family="IBM Plex Mono",
    font_size="1.5em",
)
```

## Local Fonts

By making use of the two previous points, we can also make a stylesheet that allow you to use a font hosted on your server.

If your font is called `MyFont.otf`, copy it in `assets/fonts`.

Now we have the font ready, let's create the stylesheet `myfont.css`.

```css
@font-face {
    font-family: MyFont;
    src: url("/fonts/MyFont.otf") format("opentype");
}

@font-face {
    font-family: MyFont;
    font-weight: bold;
    src: url("/fonts/MyFont.otf") format("opentype");
}
```

Add the reference to your new Stylesheet in your App.

```python
app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
)
```

And that's it! You can now use `MyFont` like any other FontFamily to style your components.
