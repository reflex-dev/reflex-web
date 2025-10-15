import reflex as rx

from pcweb.components.webpage.comps import h1_title
from pcweb.constants import CONTRIBUTING_URL, DISCORD_URL
from pcweb.flexdown import markdown_with_shiki
from pcweb.pages.docs import hosting, wrapping_react
from pcweb.pages.gallery import gallery
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
        "A": rx.box(
            rx.text(
                "With Reflex, data scientists and software engineers can create high-quality web applications quickly and easily without needing to learn specific web development technologies. Whether you want to build a single purpose user interface for a data science project/internal app, or a large multi-page web app, Reflex has the tools and features to handle both and scale up as your project grows."
            ),
            rx.text(
                "Check out our ",
                doclink("gallery", href=gallery.path),
                " to see what ur community has already built with Reflex.",
            ),
            class_name="flex flex-col gap-4 w-full",
        ),
    },
    {
        "Q": "What's the status on hosting?",
        "A": rx.text(
            "Our hosting service is in alpha! See more details in our ",
            doclink("deployment guide", href=hosting.deploy_quick_start.path),
            ".",
        ),
    },
    {
        "Q": "How can I contribute?",
        "A": rx.text(
            "We're always looking for contributors to help us build Reflex. If you're interested in contributing, check out our page on ",
            doclink(
                "contributing to Reflex Open Source",
                href=CONTRIBUTING_URL,
            ),
            ".",
        ),
    },
    {
        "Q": "How does this compare existing solutions?",
        "A": rx.box(
            rx.text(
                "Web apps are the most common way for developers to share their ideas. But even for skilled engineers, without experience in traditional frontend tools like Javascript or React, making a web app can be overwhelming and time-consuming. And once their app is created, deploying it is often a nightmare. Over the years, many low-code and no-code frameworks have tried to make web development more accessible, but they all have limitations and graduation risks compared to standard web frameworks. With Reflex, we have created a framework that lets developers leverage their existing Python skills to build and deploy apps without compromising on flexibility or customization."
            ),
            rx.text(
                "Reflex allows you to make anything from a small data science project to a full-scale, multi-page web app. Since Reflex apps compile down to traditional frontend frameworks, there's no constraint on the type of apps you can build. Instead of reinventing the web development ecosystem, we're making the existing ecosystem more accessible."
            ),
            class_name="flex flex-col gap-4 w-full",
        ),
    },
    {
        "Q": "Can Reflex work with X Javascript/React library?",
        "A": rx.text(
            "One of Reflex's most powerful features is the ability to wrap existing third-party React components. A few lines of code can provide a Python interface on top the rich, well-supported React ecosystem. Check out our section on ",
            doclink("wrapping React", href=wrapping_react.overview.path),
            " to learn more.",
        ),
    },
    {
        "Q": "Why is the initial startup time slower on Windows?",
        "A": rx.text(
            "Reflex uses Bun under the hood to install frontend dependencies, significantly reducing our startup times and memory usage. Bun does not yet compile on Windows natively, so we use Node on Windows instead. This creates longer startup times and higher memory usage on Windows. We are actively working on cutting our frontend dependencies improving start up times on all platforms."
        ),
    },
    {
        "Q": "What usage data is collected?",
        "A": markdown_with_shiki(
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
            "There is currently no in-built way to integrate payments into Reflex. However, you can check out this implementation of a Stripe integration in Reflex by one of our community members. Check out the code ",
            doclink(
                "here", href="https://github.com/joyhchen/reflex-embedded-checkout"
            ),
            " and a tweet thread about it ",
            doclink("here", href="https://x.com/jhzc_/status/1780857772852314596"),
            ".",
        ),
    },
    {
        "Q": "How can I convert a Figma file into Reflex code?",
        "A": rx.text(
            "Check out this ",
            doclink(
                "Notion doc",
                href="https://www.notion.so/reflex-dev/Convert-HTML-to-Reflex-fe22d0641dcd4d5c91c8404ca41c7e77",
            ),
            " for a walk through on how to convert a Figma file into Reflex code.",
        ),
    },
]


def faq_item(question: str, answer: str, index: int):
    return rx.el.li(
        rx.accordion.root(
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.el.h3(
                            question, class_name="font-smbold !text-slate-12 text-start"
                        ),
                        rx.spacer(),
                        rx.accordion.icon(class_name="!text-slate-12"),
                        class_name="!bg-transparent hover:!bg-transparent !p-4 lg:!p-6",
                    ),
                ),
                rx.accordion.content(
                    answer,
                    class_name="!p-[0rem_1rem_1rem_1rem] lg:!p-[0rem_1.5rem_1.5rem_1.5rem] !font-small !text-slate-11 text-start [&>code]:!font-code before:!h-0 after:!h-0",
                ),
                class_name="border-none",
            ),
            type="multiple",
            collapsible=True,
            class_name="border-slate-4 !bg-slate-2 p-0 border rounded-xl w-full !shadow-none",
        ),
        class_name="w-full",
    )


@webpage(path="/faq", title="Frequently Asked Questions · Reflex")
def faq():
    return rx.el.section(
        rx.box(
            h1_title(title="Frequently Asked Questions"),
            rx.el.h2(
                "We've compiled a list of the most common questions we get about Reflex. If you have a question that isn't answered here, feel free to reach out to us on our ",
                rx.link(
                    "Discord",
                    href=DISCORD_URL,
                    underline="always",
                    class_name="text-violet-9",
                ),
                ".",
                class_name="font-md text-balance text-slate-10",
            ),
            class_name="section-header",
        ),
        rx.el.ul(
            *[
                faq_item(question=item["Q"], answer=item["A"], index=index)
                for index, item in enumerate(faq_items)
            ],
            class_name="flex flex-col gap-4 w-full",
        ),
        id="faq",
        class_name="section-content",
    )
