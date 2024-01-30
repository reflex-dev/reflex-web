# Navigation Bar

A navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application.
It typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages.

Navigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app.
Having a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app.


## Basic Navbar

In this recipe, we will create a navbar component that can be used to create a navigation bar for a web app.
The navbar will be a simple horizontal bar that contains a logo and a list of links to the different pages of the app.

In this example we want the navbar to stick to the top of the page, so we will use the `position="fixed"` 
 prop to make the navbar fixed to the top of the page.
We will also use the `top= 0` and `z_index="1"` props to make sure the navbar is always on top of the screen and above the other components on the page.

```python exec
import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico"),
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
            rx.menu_list(
                rx.menu_item("Item 1"),
                rx.menu_divider(),
                rx.menu_item("Item 2"),
                rx.menu_item("Item 3"),
            ),
        ),
        # position="fixed",
        # top="0px",
        background_color="lightgray",
        padding="1em",
        width="100%",
        z_index="5",
    )
```

```python demo box
navbar()
```

```python
def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico"),
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
            rx.menu_list(
                rx.menu_item("Item 1"),
                rx.menu_divider(),
                rx.menu_item("Item 2"),
                rx.menu_item("Item 3"),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        width="100%",
        z_index="5",
    )
```

## Adding Main Content

Now that we have a navbar, we can add some content to the page.

We wrap both the navbar and the main content in a `rx.fragment` component so that they are rendered together as a single page.
We add some padding to the top of the main content so that it is not hidden behind the navbar.

```python demo exec
def content():
    return rx.box(
        rx.heading("Welcome to My App"),
        rx.text("This is the main content of the page."),
    )

def index():
    return rx.fragment(
        navbar(),
        rx.container(
            content(),
            padding_top="6em",
            max_width="60em",
        ),
    )
```

Here is the full code for a basic navbar with main content:

```python
import reflex as rx

def content():
    return rx.box(
        rx.heading("Welcome to My App"),
        rx.text("This is the main content of the page."),
    )

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico", width="2em"),
            rx.heading("My App", font_size="2em"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
            rx.menu_list(
                rx.menu_item("Item 1"),
                rx.menu_divider(),
                rx.menu_item("Item 2"),
                rx.menu_item("Item 3"),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        width="100%",
        z_index="5",
    )


def index():
    return rx.fragment(
        navbar(),
        rx.container(
            content(),
            padding_top="6em",
            max_width="60em",
        ),
    )


app = rx.App()
app.add_page(index)
```