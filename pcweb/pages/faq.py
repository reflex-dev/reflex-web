import reflex as rx
from pcweb import constants, styles
from pcweb.templates.docpage import doccode, docheader, doclink, doctext, subheader
from pcweb.templates.webpage import webpage
from pcweb.route import Route
from pcweb.styles import text_colors as tc
from pcweb.styles import colors as c
from pcweb.pages.docs import wrapping_react
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.hosting.deploy import deploy

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
                rx.span(doclink("gallery", href=gallery.path)),
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
            rx.span(doclink("deployment guide", href=deploy.path)),
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
            rx.span(
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
            rx.span(doclink("wrapping React", href=wrapping_react.overview.path)),
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
]


def faq_item(question, answer, index):
    return rx.accordion_item(
        rx.accordion_button(
            rx.heading(
                question, color=tc["docs"]["body"], font_size=styles.H3_FONT_SIZE
            ),
            rx.spacer(),
            rx.accordion_icon(color=tc["docs"]["body"]),
            border_bottom="none" if index == len(faq_items) - 1 else styles.DOC_BORDER,
            _hover={},
            padding_y="1em",
        ),
        rx.accordion_panel(answer),
        border="none",
    )


@webpage(path="/faq", title="FAQ")
def faq():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading(
                    "Reflex FAQ",
                    font_size=styles.H1_FONT_SIZE,
                    mt=12,
                    mb=4,
                    color=tc["docs"]["body"],
                ),
                rx.text(
                    "Frequently asked questions about Reflex.",
                    color=tc["docs"]["body"],
                ),
                rx.divider(),
                rx.accordion(
                    *[
                        faq_item(item["Q"], item["A"], index)
                        for index, item in enumerate(faq_items)
                    ],
                    border=styles.DOC_BORDER,
                    border_radius=styles.DOC_BORDER_RADIUS,
                    allow_multiple=True,
                    width="100%",
                    padding_y="1em",
                ),
                text_align="left",
                width="100%",
            ),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        max_width="960px",
    )


faq_routes = [faq]
