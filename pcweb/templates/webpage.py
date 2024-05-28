from typing import Callable

import reflex as rx
from pcweb import styles
from pcweb.route import Route

DEFAULT_TITLE = "Web Apps in Pure Python"


def spotlight():
    return rx.flex(
        rx.html(
            """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/css/spotlight.css" />
    <link rel="stylesheet" type="text/css" href="/css/styleguide.css" />
    <link rel="stylesheet" type="text/css" href="/css/globals.css" />
  </head>
  <body style="margin: 0; background: none">
    <input type="hidden" id="anPageName" name="page" value="landing-page" />
    <div class="container-center-horizontal">
      <div class="landing-page screen">
        <div class="flex-col">
          <div class="overlap-group1">
            <div class="group-9">
              <div class="vector-container">
                <img class="vector-2" src="/spotlight_img/vector-2.png" alt="Vector 2" />
                <img class="vector-2-1 vector-2-3" src="/spotlight_img/vector-2.png" alt="Vector 2" />
              </div>
              <div class="vector-container-1">
                <img class="vector-3" src="/spotlight_img/vector-2.png" alt="Vector 3" />
                <img class="vector-3-1" src="/spotlight_img/vector-2.png" alt="Vector 3" />
              </div>
              <img class="vector-2-2 vector-2-3" src="/spotlight_img/vector-2.png" alt="Vector 2" />
              <img class="vector-3-2" src="/spotlight_img/vector-2.png" alt="Vector 3" />
            </div>
            <div class="overlap-group">
              <img class="group-6" src="/spotlight_img/group-6.png" alt="Group 6" />
              <img class="subtract" src="/spotlight_img/subtract.png" alt="Subtract" />
            </div>
            <img class="rectangle-7" src="/spotlight_img/rectangle-7.png" alt="Rectangle 7" />
            <img class="rectangle-8" src="/spotlight_img/rectangle-8.png" alt="Rectangle 8" />
            <img class="rectangle-9" src="/spotlight_img/rectangle-9.png" alt="Rectangle 9" />
            <div class="rectangle-13"></div>
            <div class="rectangle-18"></div>
            <img class="rectangle-10" src="/spotlight_img/rectangle-10.svg" alt="Rectangle 10" />
          </div>
          <div class="rectangle-17"></div>
        </div>
        <img class="vector" src="/spotlight_img/vector.png" alt="Vector" />
      </div>
    </div>
  </body>
</html>
"""
        ),
        z_index=-1,
        position="absolute",
        width="100%",
        height="100%",
        align_items="start",
        justify_content="center",
        opacity=0.97,
    )


def webpage(path: str, title: str = DEFAULT_TITLE, props=None, add_as_page=True) -> Callable:
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        path: The path of the page.
        title: The title of the page.
        props: Props to apply to the template.
        add_as_page: whether to add the route to the app pages.

    Returns:
        A wrapper function that returns the full webpage.
    """
    props = props or {}

    def webpage(contents: Callable[[], Route]) -> Route:
        """Wrapper to create a templated route.

        Args:
            contents: The function to create the page route.

        Returns:
            The templated route.
        """

        def wrapper(*children, **props) -> rx.Component:
            """The template component.

            Args:
                children: The children components.
                props: The props to apply to the component.

            Returns:
                The component with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.webpage.footer import footer
            from pcweb.components.webpage.navbar import navbar
            from pcweb.components.webpage.sidebar import sb

            # Wrap the component in the template.
            return rx.flex(
                navbar(sidebar=sb),
                spotlight(),
                rx.container(
                    margin_top="150px",
                ),
                contents(*children, **props),
                rx.box(flex_grow=1),
                footer(),
                font_family=styles.SANS,
                background="#131217",
                align_items="center",
                justify_content="start",
                width="100%",
                height="100%",
                min_height="100vh",
                position="relative",
                direction="column",
                z_index=-2,
                overflow="hidden",
                **props,
            )

        return Route(
            path=path,
            title=title,
            background_color="#131217",
            component=wrapper,
            add_as_page=add_as_page
        )

    return webpage
