import reflex as rx
from pcweb import constants, styles
from pcweb.pages.docs import hosting, wrapping_react
from pcweb.pages.docs.gallery import gallery
from pcweb.templates.docpage import doclink
from pcweb.templates.webpage import webpage

faq_items = [
    {
        "Q": "What is Reflex?",
        "A": rx.text(
            "Reflex is an open-source, full-stack Python framework that makes it easy to build and deploy web apps in minutes. It offers the ease of use and accessibility of low-code frameworks, combined with the flexibility, performance, and customizability of traditional web development. Reflex is designed to be easy to get started with for those with no previous web development experience."
        ),
    },
    {
        "Q": "What can I build with Reflex?",
        "A": rx.vstack(
            rx.text(
                """
            With Reflex, data scientists and software engineers can create high-quality web applications quickly and easily without needing to learn specific web development technologies. Whether you want to build a single purpose user interface for a data science project/internal app, or a large multi-page web app, Reflex has the tools and features to handle both and scale up as your project grows.            """
            ),
            rx.text(
                "Check out our ",
                rx.chakra.span(doclink("gallery", href=gallery.path)),
                " to see what ur community has already built with Reflex.",
            ),
            align_items="flex-start",
            width="100%",
        ),
    },
    {
        "Q": "Whats the status on hosting?",
        "A": rx.text(
            """
            Our hosting service is in alpha! See more details in our
            """,
            rx.chakra.span(
                doclink("deployment guide", href=hosting.deploy_quick_start.path)
            ),
            ".",
        ),
    },
    {
        "Q": "How can I contribute?",
        "A": rx.text(
            """
            We're always looking for contributors to help us build Reflex.
            If you're interested in contributing, check out our page on
            """,
            rx.chakra.span(
                doclink(
                    " contributing to Reflex Open Source",
                    href=constants.CONTRIBUTING_URL,
                )
            ),
            ".",
        ),
    },
    {
        "Q": "How does this compare existing solutions?",
        "A": rx.vstack(
            rx.text(
                """
            Web apps are the most common way for developers to share their ideas. But even for skilled engineers, without experience in traditional frontend tools like Javascript or React, making a web app can be overwhelming and time-consuming. And once their app is created, deploying it is often a nightmare. Over the years, many low-code and no-code frameworks have tried to make web development more accessible, but they all have limitations and graduation risks compared to standard web frameworks. With Reflex, we have created a framework that lets developers leverage their existing Python skills to build and deploy apps without compromising on flexibility or customization.
            """
            ),
            rx.text(
                """
            Reflex allows you to make anything from a small data science project to a full-scale, multi-page web app. Since Reflex apps compile down to traditional frontend frameworks, there's no constraint on the type of apps you can build. Instead of reinventing the web development ecosystem, we're making the existing ecosystem more accessible.            """
            ),
            align_items="flex-start",
            width="100%",
        ),
    },
    {
        "Q": "Can Reflex work with X Javascript/React library?",
        "A": rx.text(
            """
            One of Reflex's most powerful features is the ability to wrap existing third-party React components. A few lines of code can provide a Python interface on top the rich, well-supported React ecosystem. Check out our section on
            """,
            rx.chakra.span(
                doclink("wrapping React", href=wrapping_react.overview.path)
            ),
            " to learn more.",
        ),
    },
    {
        "Q": "Why is the initial startup time slower on Windows?",
        "A": rx.text(
            """
            Reflex uses Bun under the hood to install frontend dependencies, significantly reducing our startup times and memory usage. Bun does not yet compile on Windows natively, so we use Node on Windows instead. This creates longer startup times and higher memory usage on Windows. We are actively working on cutting our frontend dependencies improving start up times on all platforms.
            """
        ),
    },
    {
        "Q": "What usage data is collected?",
        "A": rx.markdown(
            """
Anonymous usage data allows us to understand how Reflex is used and how we can improve the product.

The following information is collected:
* Anonymous user / app ID
* Operating System, CPU Count, Memory
* Python / Reflex Version

### How to Opt-Out

To disable telemetry, set `telemetry_enabled=False` in your `rxconfig.py` file.

```python
config = rx.Config(
    app_name="hello",
    telemetry_enabled=False,
)
```

Alternatively, you can set the `TELEMETRY_ENABLED` environment variable to `False`.
"""
        ),
    },
    {
        "Q": "How can I integrate payments into my Reflex App?",
        "A": rx.text(
            """
            There is currently no in-built way to integrate payments into Reflex. However, you can check out this implementation of a Stripe integration in Reflex by one of our community members. Check out the code 
            """,
            rx.chakra.span(
                doclink("here", href="https://github.com/joyhchen/reflex-embedded-checkout")
            ),
            """
            and a tweet thread about it
            """,
            rx.chakra.span(
                doclink("here", href="https://x.com/jhzc_/status/1780857772852314596")
            ),
            ".",
        ),
    },
]


def faq_item(question, answer, index):
    return rx.chakra.accordion(rx.chakra.accordion_item(
        rx.chakra.accordion_button(
            rx.heading(
                question, color="#D6D6ED", font_size=styles.H3_FONT_SIZE
            ),
            rx.chakra.spacer(),
            rx.chakra.accordion_icon(color="#6C6C81"),
            _hover={},
            padding_y="1em",
        ),
        rx.chakra.accordion_panel(answer, color="#6C6C81"),
        border="none",
    ),
    allow_multiple=True,
    border_radius= "12px;",
    border= "1px solid #37363F;",
    background= "rgba(47, 43, 55, 0.50);",
    box_shadow= "0px 3px 22px -2px #0C0B0F;",
    width="100%",
)

def faq_item_mobile(question, answer, index):
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                rx.heading(
                    question, color="#D6D6ED", font_size="1em",
                ),
                rx.chakra.spacer(),
                rx.chakra.accordion_icon(color="#6C6C81"),
                padding_y="1em",
            ),
            rx.chakra.accordion_panel(answer, color="#6C6C81"),
            border="none",
        ),
        allow_multiple=True,
        border_radius="12px",
        border="1px solid #37363F",
        background="rgba(47, 43, 55, 0.50)",
        box_shadow="0px 3px 22px -2px #0C0B0F",
        width="90%",  # Adjust the width to a smaller value, e.g., 90%
        max_width="375px",  # Set a maximum width for the accordion
        margin="0 auto",  # Center the accordion horizontally
    )

def desktop_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Questions",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em"
                ),
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Frequently Asked Questions",
                font_size="64px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
            ),
            rx.text(
                "We've compiled a list of the most common questions we get about Reflex. If you have a question that isn't answered here, feel free to reach out to us on our Discord.",
                color="#6C6C81",
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            faq_item(item["Q"], item["A"], index)
            for index, item in enumerate(faq_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

def mobile_view():
    return rx.vstack(
        rx.vstack(
            rx.flex(
                rx.chakra.text(
                    "Common Questions",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em",
                ),
                padding_buttom="1em",
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
            ),
            rx.chakra.text(
                "Frequently Asked Questions",
                font_size="28px;",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                text_align="center",
                width="650px",
                background_clip="text",
                font_weight="medium",
                letter_spacing="-1.28px;",
            ),
            rx.box(
                rx.text(
                    "We've compiled a list of the most common questions we get about Reflex. If you have a question that isn't answered here, feel free to reach out to us on our Discord.",
                    color="#6C6C81",
                    width="360px",
                    align="center",
                ),
            ),
            align_items="center",
            text_align="left",
            width="100%",
            spacing="1",
            margin_bottom="2em",
        ),
        *[
            faq_item_mobile(item["Q"], item["A"], index)
            for index, item in enumerate(faq_items)
        ],
        align_items="center",
        margin_bottom="4em",
        padding_y="2em",
    )

@webpage(path="/faq", title="Frequently Asked Questions · Reflex")
def faq():
    return rx.container(
        rx.vstack(
            rx.mobile_only(mobile_view()),
            rx.tablet_and_desktop(desktop_view()),
        )
    )

#faq_routes = [faq]
