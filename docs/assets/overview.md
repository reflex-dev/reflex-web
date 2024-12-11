```python exec
import reflex as rx
```

# Assets

Static files such as images and stylesheets can be placed in the `assets/` folder of your project. These files are served as frontend assets and are available to your application's frontend components.

## Overview

The `assets/` folder is designed for frontend static assets such as:
- Images
- Stylesheets
- Fonts
- Other static files

```md alert
# Assets are copied during the build process.

Any files placed within the `assets/` folder at runtime will not be available to the app
when running in production mode. The `assets/` folder should only be used for static files.
```

## Referencing Assets

To reference an asset in the `assets/` folder, use the relative path as a prop:

For example, you can store your logo in your assets folder:

```bash
assets
└── Reflex.svg
```

Then display it using an `rx.image` component:

```python demo
rx.image(src="/Reflex.svg", width="5em")
```

```md alert
# Always prefix the asset path with a forward slash `/` to reference the asset from the root of the project, or it may not display correctly on non-root pages.
```

## Frontend vs Backend Assets

### Current Behavior
Assets in the `assets/` folder are primarily intended for frontend use. When you reference an asset, it is:
1. Copied to the frontend build directory during compilation
2. Served statically by the frontend server

### Using Assets in Backend Code
While it's possible to access assets from backend code (they are copied to the backend), this is not the recommended approach and may not be supported in future versions. Instead:

1. For backend-only files: Store them outside the `assets/` directory
2. For files needed in both frontend and backend:
   - Store a copy in both locations
   - Use appropriate paths for each context

## Experimental Features Status

The experimental assets module (`rx._x.asset`) is being deprecated in favor of the core implementation. Use `rx.asset` with `shared=True` for all new code:

```python
# Old way (deprecated)
rx._x.asset("my_file.png")

# New way
rx.asset("my_file.png", shared=True)
```

## Favicon

The favicon is the small icon that appears in the browser tab. Add a `favicon.ico` file to the `assets/` folder to change it.
