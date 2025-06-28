"""Grid section for security page featuring trust services criteria."""

import reflex as rx
from pcweb.components.icons import get_icon
from ..data import PAGE_CONTENT, TRUST_SERVICES_CRITERIA


def security_card(
    title: str,
    description: str,
    icon: str,
    cols: str = "1",
    class_name: str = "",
) -> rx.Component:
    """Individual security feature card component."""
    return rx.box(
        rx.box(
            _card_header(title, icon),
            _card_description(description),
            class_name="flex flex-col gap-[0.875rem]",
        ),
        class_name=f"overflow-hidden p-8 w-full {class_name} lg:col-span-{cols} h-[13rem] lg:h-[11rem] border-slate-3",
    )


def _card_header(title: str, icon: str) -> rx.Component:
    """Card header with icon and title."""
    return rx.box(
        get_icon(icon, class_name="!text-slate-9"),
        rx.el.h3(title, class_name="text-slate-12 text-base font-semibold"),
        class_name="flex flex-row items-center gap-2",
    )


def _card_description(description: str) -> rx.Component:
    """Card description text."""
    return rx.el.p(
        description, class_name="text-slate-9 font-medium text-sm text-start"
    )


def outcomes_showcase() -> rx.Component:
    """Central outcomes showcase component with prominent display."""
    showcase = PAGE_CONTENT["showcase"]

    return rx.box(
        rx.box(
            rx.box(
                rx.el.h2(
                    showcase["title"],
                    class_name="text-slate-12 text-lg lg:text-2xl font-semibold text-center",
                ),
                rx.el.h3(
                    showcase["subtitle"],
                    class_name="text-slate-9 text-md lg:text-xl font-semibold text-center",
                ),
                class_name="flex flex-col gap-2 p-10 items-center justify-center",
            ),
            rx.box(
                rx.box(
                    *[
                        rx.image(
                            src=logo["src"],
                            alt=logo["alt"],
                            class_name="h-24 w-auto"
                        )
                        for logo in showcase["logos"]
                    ],
                    class_name="flex flex-row gap-10 items-center justify-center",
                ),
                class_name="p-10 flex items-center justify-center",
            ),
            class_name="flex flex-col justify-center items-center h-full",
        ),
        class_name="h-full w-full flex flex-col justify-center items-center relative overflow-hidden lg:row-span-3 lg:col-span-1 lg:border-l lg:border-r border-slate-3 p-8 lg:p-1",
    )


def security_grid() -> rx.Component:
    """Main security features grid component with responsive layout."""
    criteria = TRUST_SERVICES_CRITERIA

    # Mobile layout - simple single column stack
    mobile_layout = rx.box(
        *[security_card(**criterion) for criterion in criteria],
        class_name="lg:hidden flex flex-col divide-y divide-slate-3 border border-slate-3"
    )

    # Desktop layout - complex grid with showcase
    desktop_layout = rx.box(
        # Last card (spans 2 columns) -> moved to top
        security_card(
            **criteria[4],
            cols="2",
            class_name="lg:col-span-2"
        ),

        # Center showcase (spans 3 rows, 1 column)
        outcomes_showcase(),

        # First 2 cards
        *[security_card(**criterion) for criterion in criteria[:2]],

        # Next 2 cards
        *[security_card(**criterion) for criterion in criteria[2:4]],

        class_name=(
            "hidden lg:grid lg:grid-cols-3 lg:grid-rows-3 "
            "w-full border border-slate-3"
        )
    )

    return rx.box(
        mobile_layout,
        desktop_layout,
        class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
    )
