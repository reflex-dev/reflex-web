```python exec
import reflex as rx
```

# Assets

Static files such as images, stylesheets, fonts, and other resources can be placed in the `assets/` folder of your Reflex project. These files are automatically made available to your application during both development and production.

```md alert
# Assets are copied during the build process.

Any files placed within the `assets/` folder at runtime will not be available to the app
when running in production mode. The `assets/` folder should only be used for static files.
```

## Types of Assets

Reflex supports various types of static assets:

- **Images**: PNG, JPG, GIF, SVG, WebP, etc.
- **Stylesheets**: CSS files
- **Fonts**: TTF, OTF, WOFF, WOFF2
- **Scripts**: JavaScript files
- **Data files**: JSON, CSV, etc.
- **Media**: Audio, video files
- **Documents**: PDF, etc.

## Asset Directory Structure

The `assets/` directory is located at the root of your Reflex project. You can organize your assets in subdirectories for better management:

```bash
assets/
├── images/
│   ├── logo.png
│   └── background.jpg
├── css/
│   └── custom.css
├── fonts/
│   └── custom-font.ttf
├── js/
│   └── script.js
└── favicon.ico
```

## Referencing Assets

To reference an asset in your Reflex app, use the path relative to the `assets/` directory, prefixed with a forward slash `/`.

For example, you can store your logo in your assets folder:

```bash
assets
└── Reflex.svg
```

Then you can display it using a `rx.image` component:

```python demo
rx.image(src="/Reflex.svg", width="5em")
```

```md alert
# Always prefix the asset path with a forward slash `/` to reference the asset from the root of the project, or it may not display correctly on non-root pages.
```

## Using Assets in Different Components

Assets can be used in various Reflex components:

### Images

```python
rx.image(src="/images/logo.png", width="100px")
```

### CSS Stylesheets

```python
rx.link(rel="stylesheet", href="/css/custom.css")
```

### JavaScript Files

```python
rx.script(src="/js/script.js")
```

### Background Images in Style Props

```python
rx.box(
    width="100%",
    height="200px",
    background_image="url('/images/background.jpg')",
    background_size="cover",
)
```

## Shared Assets

For library developers, Reflex provides a way to share assets from your library with applications that use your library. This is done using the `rx.asset()` function:

```python
rx.image(src=rx.asset(path="my_image.png", shared=True))
```

When `shared=True`, the asset is expected to be located next to the Python file that references it, not in the app's `assets/` directory. Reflex will automatically create a symlink to make the asset available to the app.

You can also specify a subfolder for shared assets:

```python
rx.image(src=rx.asset(path="my_image.png", shared=True, subfolder="images"))
```

## Favicon

The favicon is the small icon that appears in the browser tab.

You can add a `favicon.ico` file to the `assets/` folder to change the favicon. Reflex will automatically detect and use this file.

For more modern favicon formats, you can also include:

```html
<!-- In your head component -->
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
```

## Asset Optimization

When building your app for production with `reflex deploy` or `reflex export`, Reflex will automatically optimize your assets:

- Images may be compressed
- CSS and JavaScript files may be minified
- Assets are given unique filenames for cache busting

This optimization helps improve the performance of your application in production.
