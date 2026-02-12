import reflex as rx

COMPANIES = [
    {
        "src": "/about/companies/y_combinator.svg",
        "alt": "Y Combinator",
    },
    {
        "src": "/about/companies/abstract.svg",
        "alt": "Abstract",
    },
    {
        "src": "/about/companies/outset.svg",
        "alt": "Outset",
    },
    {
        "src": "/about/companies/picus.svg",
        "alt": "Picus Capital",
    },
    {
        "src": "/about/companies/box_group.svg",
        "alt": "Box Group",
    },
    {
        "src": "/about/companies/lux.svg",
        "alt": "Lux Capital",
    },
]


def company_image(src: str, alt: str) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=src,
            alt=alt,
            loading="lazy",
            class_name="pointer-events-none",
        ),
        class_name="flex justify-center items-center h-12 w-auto",
    )


def companies() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            *[company_image(company["src"], company["alt"]) for company in COMPANIES],
            class_name="flex flex-row lg:gap-18 max-lg:gap-x-6 max-lg:gap-y-4 flex-wrap justify-center items-center",
        ),
        rx.el.p(
            "Reflex is backed by YC, venture capital firms, and angel investors, including ",
            rx.el.br(class_name="max-lg:hidden"),
            rx.el.b(" Qasar Younis", class_name="text-secondary-12 font-semibold"),
            " (Applied Intuition), ",
            rx.el.b(" Jack Altman ", class_name="text-secondary-12 font-semibold"),
            " (Lattice), ",
            rx.el.b(" Paul Copplestone ", class_name="text-secondary-12 font-semibold"),
            " (Supabase), ",
            rx.el.b(" Matt Kraning", class_name="text-secondary-12 font-semibold"),
            " (Palo ",
            rx.el.br(class_name="max-lg:hidden"),
            " Alto Networks, ",
            rx.el.b(" Alfredo Andere ", class_name="text-secondary-12 font-semibold"),
            " (Latch Bio), and others.",
            class_name="text-secondary-11 font-medium text-sm max-w-[45.125rem] text-balance text-center leading-6",
        ),
        class_name="flex flex-col gap-8 max-w-[69rem] mx-auto pt-24 justify-center items-center max-lg:px-6",
    )
