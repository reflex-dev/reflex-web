import functools
from typing import Callable

import reflex as rx
from pcweb.route import Route
from pcweb.pages.framework.index_colors import index_colors
from pcweb.components.icons.icons import get_icon


def hero(company: str, description: str, stats: list[dict[str, str]]) -> rx.Component:
    return rx.box(
        rx.link(
            rx.icon(
                tag="chevron-left",
                stroke_width="2.25",
                class_name="size-3.5",
            ),
            rx.text("Customer stories", class_name="font-small"),
            href="/customers",
            underline="none",
            class_name="flex items-center gap-2 text-slate-9 hover:!text-slate-11 transition-color w-fit",
        ),
        rx.el.h1(
            company,
            class_name="gradient-heading font-x-large lg:font-xx-large text-start text-transparent",
        ),
        rx.el.h2(description, class_name="text-slate-9 font-md-smbold"),
        rx.box(
            *[
                rx.box(
                    rx.text(stat["value"], class_name="text-slate-12 font-x-large"),
                    rx.text(stat["metric"], class_name="text-slate-9 font-small"),
                    class_name="flex flex-col gap-2 mt-4",
                )
                for stat in stats
            ],
            class_name="grid grid-cols-3 gap-4 lg:gap-10",
        ),
        class_name="flex flex-col gap-4 mb-10",
    )


def company_card(company: str, founded: str, investors: str, url: str) -> rx.Component:
    return rx.box(
        # Logo
        rx.image(
            src=rx.color_mode_cond(
                light=f"/customers/light/{company.lower()}/{company.lower()}_small.svg",
                dark=f"/customers/dark/{company.lower()}/{company.lower()}_small.svg",
            ),
            alt=f"{company} logo",
            loading="lazy",
            class_name="h-[3.5rem] w-auto shrink-0 mb-2 self-start",
        ),
        # Url
        rx.link(
            rx.text(
                url.split("//")[-1].split("/")[0],  # Get the domain name formatted
                class_name="font-base truncate",
            ),
            rx.icon(
                tag="arrow-up-right",
                stroke_width="2.25",
                class_name="size-3.5",
            ),
            href=url,
            underline="none",
            is_external=True,
            class_name="flex flex-row items-center gap-1.5 text-slate-12 hover:!text-slate-10 transition-color",
        ),
        # Founded
        rx.box(
            rx.text("Founded", class_name="text-slate-9 font-small-smbold"),
            rx.text(founded, class_name="text-slate-12 font-base truncate"),
            class_name="flex flex-col",
        ),
        # Investors
        rx.cond(
            investors,
            rx.box(
                rx.text("Investors", class_name="text-slate-9 font-small-smbold"),
                rx.text(investors, class_name="text-slate-12 font-base truncate"),
                class_name="flex flex-col",
            ),
        ),
        class_name="flex-col gap-4 w-[13rem] p-8 rounded-[1.125rem] border border-slate-3 bg-slate-2 z-[1] justify-start absolute right-[-6.5rem] top-[12rem] hidden xl:flex",
        is_external=True,
    )


def more_customers(current_customer: str) -> rx.Component:
    from pcweb.pages.customers.data.customers import customer_data

    customer_items = list(customer_data.items())

    # Filter out the current company
    other_customers = [
        c for c in customer_items if c[1].metadata.get("company") != current_customer
    ]
    if not other_customers:
        return rx.box()  # Return an empty box if there are no other customers

    # Find the index of the current company in the original list
    current_index = next(
        (
            i
            for i, (_, doc) in enumerate(customer_items)
            if doc.metadata.get("company") == current_customer
        ),
        0,
    )

    # Get the previous and next customers
    prev_index = (current_index - 1) % len(customer_items)
    next_index = (current_index + 1) % len(customer_items)

    prev_customer = customer_items[prev_index]
    next_customer = customer_items[next_index]

    # Ensure we're not using the current company
    while prev_customer[1].metadata.get("company") == current_customer:
        prev_index = (prev_index - 1) % len(customer_items)
        prev_customer = customer_items[prev_index]

    while next_customer[1].metadata.get("company") == current_customer:
        next_index = (next_index + 1) % len(customer_items)
        next_customer = customer_items[next_index]

    customers = [
        rx.box(
            rx.link(
                rx.box(
                    "Previous",
                    get_icon(icon="arrow_right", class_name="rotate-180"),
                    class_name="flex flex-row-reverse justify-center lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                ),
                underline="none",
                href=f"/customers/{prev_customer[1].metadata['company'].lower()}",
                class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
            ),
            rx.box(
                rx.image(
                    src=rx.color_mode_cond(
                        light=f"/customers/light/{prev_customer[1].metadata['company'].lower()}/{prev_customer[1].metadata['company'].lower()}_small.svg",
                        dark=f"/customers/dark/{prev_customer[1].metadata['company'].lower()}/{prev_customer[1].metadata['company'].lower()}_small.svg",
                    ),
                    alt=f"{next_customer[1].metadata['company']} logo",
                    loading="lazy",
                    class_name="h-[1.25rem] w-auto",
                ),
                rx.text(
                    prev_customer[1].metadata["company"],
                    class_name="font-smbold text-slate-12",
                ),
                class_name="flex flex-row justify-start gap-2.5 items-center",
            ),
            class_name="flex flex-col justify-start gap-1 items-start",
        ),
        rx.box(
            rx.link(
                rx.box(
                    "Next",
                    get_icon(icon="arrow_right"),
                    class_name="flex flex-row justify-center lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                ),
                underline="none",
                href=f"/customers/{next_customer[1].metadata['company'].lower()}",
                class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
            ),
            rx.box(
                rx.text(
                    next_customer[1].metadata["company"],
                    class_name="font-smbold text-slate-12",
                ),
                rx.image(
                    src=rx.color_mode_cond(
                        light=f"/customers/light/{next_customer[1].metadata['company'].lower()}/{next_customer[1].metadata['company'].lower()}_small.svg",
                        dark=f"/customers/dark/{next_customer[1].metadata['company'].lower()}/{next_customer[1].metadata['company'].lower()}_small.svg",
                    ),
                    alt=f"{next_customer[1].metadata['company']} logo",
                    loading="lazy",
                    class_name="h-[1.25rem] w-auto",
                ),
                class_name="flex flex-row justify-start gap-2.5 items-center",
            ),
            class_name="flex flex-col justify-start gap-1 items-end",
        ),
    ]

    return rx.box(
        rx.box(
            *customers,
            class_name="flex flex-row gap-4 justify-between items-center",
        ),
        class_name="flex flex-col gap-6 mt-20",
    )


def storypage(
    path: str,
    description: str,
    company: str,
    domain: str = None,
    founded: str = None,
    investors: str = None,
    stats: list[dict[str, str]] = None,
    meta: list[dict[str, str]] = None,
    props=None,
    add_as_page=True,
) -> Callable:
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

    def storypage(contents: Callable[[], Route]) -> Route:
        """Wrapper to create a templated route.

        Args:
            contents: The function to create the page route.

        Returns:
            The templated route.
        """

        @functools.wraps(contents)
        def wrapper(*children, **props) -> rx.Component:
            """The template component.

            Args:
                children: The children components.
                props: The props to apply to the component.

            Returns:
                The component with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.docpage.navbar import navbar
            from pcweb.pages.customers.views.footer import footer_customer
            from pcweb.components.webpage.badge import badge
            from pcweb.views.bottom_section.bottom_section import bottom_section

            # Wrap the component in the template.
            return rx.box(
                rx.box(
                    index_colors(),
                    navbar(),
                    company_card(company, founded, investors, domain),
                    rx.el.main(
                        hero(company, description, stats),
                        contents(*children, **props),
                        more_customers(company),
                        rx.box(class_name="flex-grow"),
                        class_name="w-full z-[1] relative flex flex-col justify-center mx-auto max-w-[640px] lg:px-0 px-4 pb-20",
                    ),
                    rx.box(class_name="h-[1px] bg-slate-3 w-full"),
                    bottom_section(),
                    footer_customer(),
                    class_name="relative flex flex-col justify-start items-center w-full h-full min-h-screen font-instrument-sans gap-4 mx-auto max-w-[64.19rem] lg:border-x border-slate-3 pt-24 lg:pt-48",
                ),
                class_name="relative overflow-hidden",
                **props,
            )

        return Route(
            path=path,
            title=company + " · Reflex Customer Story",
            description=description,
            meta=meta,
            component=wrapper,
            add_as_page=add_as_page,
        )

    return storypage
