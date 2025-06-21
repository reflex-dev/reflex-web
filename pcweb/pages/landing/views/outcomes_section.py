from typing import List

import reflex as rx

from pcweb.components.icons import get_icon
from pcweb.components.new_button import button

# Outcomes features data
OUTCOMES_FEATURES = [
    {
        "title": "Dedicated Engineer",
        "description": "An expert engineer is assigned to your team to build your first app.",
        "icon": "backend_auth",
    },
    {
        "title": "Fast Time to Launch",
        "description": "Get your first app up and running quickly with expert guidance.",
        "icon": "zap",
    },
    {
        "title": "Guaranteed Success",
        "description": "We ensure your app reaches a successful state before handoff.",
        "icon": "star",
    },
    {
        "title": "Training and Enablement",
        "description": "Hands-on training so your team can maintain and extend your app.",
        "icon": "document_code",
    },
]


def header() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Deliver Outcomes",
            class_name="lg:text-3xl text-xl font-semibold text-slate-12 text-balance",
        ),
        rx.el.p(
            "Your success, guaranteed. Real outcomes, real support",
            class_name="lg:text-3xl text-xl font-semibold text-slate-9 text-balance",
        ),
        class_name="flex text-center flex-col py-[3.5rem] 2xl:border-x border-t border-slate-3 max-w-[64.19rem] mx-auto w-full max-lg:border-b",
    )


def outcomes_showcase() -> rx.Component:
    """Central outcomes showcase component with prominent display."""
    return rx.box(
        # Radial background
        rx.html(
            """<svg width="338" height="478" viewBox="0 0 338 478" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="23.824" y="210.094" width="275" height="107" rx="53.5" transform="rotate(-9 23.824 210.094)" stroke="var(--c-slate-5)"/>
<rect x="8.14869" y="208.44" width="299" height="131" rx="65.5" transform="rotate(-12 8.14869 208.44)" stroke="var(--c-slate-5)"/>
<rect x="-8.05511" y="208.366" width="323" height="155" rx="77.5" transform="rotate(-15 -8.05511 208.366)" stroke="var(--c-slate-5)"/>
<rect x="-24.6649" y="209.92" width="347" height="179" rx="89.5" transform="rotate(-18 -24.6649 209.92)" stroke="var(--c-slate-5)"/>
<rect x="-41.5532" y="213.144" width="371" height="203" rx="101.5" transform="rotate(-21 -41.5532 213.144)" stroke="var(--c-slate-5)"/>
<rect x="-58.5899" y="218.069" width="395" height="227" rx="113.5" transform="rotate(-24 -58.5899 218.069)" stroke="var(--c-slate-5)"/>
<rect x="-75.6415" y="224.715" width="419" height="251" rx="125.5" transform="rotate(-27 -75.6415 224.715)" stroke="var(--c-slate-5)"/>
<rect x="-92.5743" y="233.097" width="443" height="275" rx="137.5" transform="rotate(-30 -92.5743 233.097)" stroke="var(--c-slate-5)"/>
<rect x="-109.253" y="243.217" width="467" height="299" rx="149.5" transform="rotate(-33 -109.253 243.217)" stroke="var(--c-slate-5)"/>
<rect x="-125.541" y="255.071" width="491" height="323" rx="161.5" transform="rotate(-36 -125.541 255.071)" stroke="var(--c-slate-5)"/>
<rect x="-141.302" y="268.641" width="515" height="347" rx="173.5" transform="rotate(-39 -141.302 268.641)" stroke="var(--c-slate-5)"/>
<rect x="-156.401" y="283.903" width="539" height="371" rx="185.5" transform="rotate(-42 -156.401 283.903)" stroke="var(--c-slate-5)"/>
<rect x="-170.704" y="300.823" width="563" height="395" rx="197.5" transform="rotate(-45 -170.704 300.823)" stroke="var(--c-slate-5)"/>
<rect x="-184.079" y="319.356" width="587" height="419" rx="209.5" transform="rotate(-48 -184.079 319.356)" stroke="var(--c-slate-5)"/>
<rect x="-196.395" y="339.449" width="611" height="443" rx="221.5" transform="rotate(-51 -196.395 339.449)" stroke="var(--c-slate-5)"/>
<rect x="-207.527" y="361.041" width="635" height="467" rx="233.5" transform="rotate(-54 -207.527 361.041)" stroke="var(--c-slate-5)"/>
<rect x="-217.352" y="384.059" width="659" height="491" rx="245.5" transform="rotate(-57 -217.352 384.059)" stroke="var(--c-slate-5)"/>
<rect x="-225.752" y="408.423" width="683" height="515" rx="257.5" transform="rotate(-60 -225.752 408.423)" stroke="var(--c-slate-5)"/>
<rect x="-232.612" y="434.046" width="707" height="539" rx="269.5" transform="rotate(-63 -232.612 434.046)" stroke="var(--c-slate-5)"/>
<rect x="-237.825" y="460.83" width="731" height="563" rx="281.5" transform="rotate(-66 -237.825 460.83)" stroke="var(--c-slate-5)"/>
<rect x="-241.29" y="488.671" width="755" height="587" rx="293.5" transform="rotate(-69 -241.29 488.671)" stroke="var(--c-slate-5)"/>
<rect x="-242.91" y="517.457" width="779" height="611" rx="305.5" transform="rotate(-72 -242.91 517.457)" stroke="var(--c-slate-5)"/>
<rect x="-242.597" y="547.07" width="803" height="635" rx="317.5" transform="rotate(-75 -242.597 547.07)" stroke="var(--c-slate-5)"/>
<rect x="-240.271" y="577.383" width="827" height="659" rx="329.5" transform="rotate(-78 -240.271 577.383)" stroke="var(--c-slate-5)"/>
<rect x="-235.858" y="608.265" width="851" height="683" rx="341.5" transform="rotate(-81 -235.858 608.265)" stroke="var(--c-slate-5)"/>
<rect x="-229.295" y="639.578" width="875" height="707" rx="353.5" transform="rotate(-84 -229.295 639.578)" stroke="var(--c-slate-5)"/>
<rect x="-220.524" y="671.181" width="899" height="731" rx="365.5" transform="rotate(-87 -220.524 671.181)" stroke="var(--c-slate-5)"/>
<rect x="-209.5" y="702.926" width="923" height="755" rx="377.5" transform="rotate(-90 -209.5 702.926)" stroke="var(--c-slate-5)"/>
<rect x="-196.185" y="734.662" width="947" height="779" rx="389.5" transform="rotate(-93 -196.185 734.662)" stroke="var(--c-slate-5)"/>
<rect x="-180.552" y="766.234" width="971" height="803" rx="401.5" transform="rotate(-96 -180.552 766.234)" stroke="var(--c-slate-5)"/>
<rect x="-162.583" y="797.486" width="995" height="827" rx="413.5" transform="rotate(-99 -162.583 797.486)" stroke="var(--c-slate-5)"/>
<rect x="-142.271" y="828.258" width="1019" height="851" rx="425.5" transform="rotate(-102 -142.271 828.258)" stroke="var(--c-slate-5)"/>
<rect x="38.8498" y="213.271" width="251" height="83" rx="41.5" transform="rotate(-6 38.8498 213.271)" stroke="var(--c-slate-5)"/>
<rect x="23.824" y="210.094" width="275" height="107" rx="53.5" transform="rotate(-9 23.824 210.094)" stroke="var(--c-slate-5)"/>
<rect x="8.14869" y="208.44" width="299" height="131" rx="65.5" transform="rotate(-12 8.14869 208.44)" stroke="var(--c-slate-5)"/>
<rect x="-8.05511" y="208.366" width="323" height="155" rx="77.5" transform="rotate(-15 -8.05511 208.366)" stroke="var(--c-slate-5)"/>
<rect x="-24.6649" y="209.92" width="347" height="179" rx="89.5" transform="rotate(-18 -24.6649 209.92)" stroke="var(--c-slate-5)"/>
<rect x="-41.5532" y="213.144" width="371" height="203" rx="101.5" transform="rotate(-21 -41.5532 213.144)" stroke="var(--c-slate-5)"/>
<rect x="-58.5899" y="218.069" width="395" height="227" rx="113.5" transform="rotate(-24 -58.5899 218.069)" stroke="var(--c-slate-5)"/>
<rect x="-75.6415" y="224.715" width="419" height="251" rx="125.5" transform="rotate(-27 -75.6415 224.715)" stroke="var(--c-slate-5)"/>
<rect x="-92.5743" y="233.097" width="443" height="275" rx="137.5" transform="rotate(-30 -92.5743 233.097)" stroke="var(--c-slate-5)"/>
<rect x="-109.253" y="243.217" width="467" height="299" rx="149.5" transform="rotate(-33 -109.253 243.217)" stroke="var(--c-slate-5)"/>
<rect x="-125.541" y="255.071" width="491" height="323" rx="161.5" transform="rotate(-36 -125.541 255.071)" stroke="var(--c-slate-5)"/>
<rect x="-141.302" y="268.641" width="515" height="347" rx="173.5" transform="rotate(-39 -141.302 268.641)" stroke="var(--c-slate-5)"/>
<rect x="-156.401" y="283.903" width="539" height="371" rx="185.5" transform="rotate(-42 -156.401 283.903)" stroke="var(--c-slate-5)"/>
<rect x="-170.704" y="300.823" width="563" height="395" rx="197.5" transform="rotate(-45 -170.704 300.823)" stroke="var(--c-slate-5)"/>
<rect x="-184.079" y="319.356" width="587" height="419" rx="209.5" transform="rotate(-48 -184.079 319.356)" stroke="var(--c-slate-5)"/>
<rect x="-196.395" y="339.449" width="611" height="443" rx="221.5" transform="rotate(-51 -196.395 339.449)" stroke="var(--c-slate-5)"/>
<rect x="-207.527" y="361.041" width="635" height="467" rx="233.5" transform="rotate(-54 -207.527 361.041)" stroke="var(--c-slate-5)"/>
<rect x="-217.352" y="384.059" width="659" height="491" rx="245.5" transform="rotate(-57 -217.352 384.059)" stroke="var(--c-slate-5)"/>
<rect x="-225.752" y="408.423" width="683" height="515" rx="257.5" transform="rotate(-60 -225.752 408.423)" stroke="var(--c-slate-5)"/>
<rect x="-232.612" y="434.046" width="707" height="539" rx="269.5" transform="rotate(-63 -232.612 434.046)" stroke="var(--c-slate-5)"/>
<rect x="-237.825" y="460.83" width="731" height="563" rx="281.5" transform="rotate(-66 -237.825 460.83)" stroke="var(--c-slate-5)"/>
<rect x="-241.29" y="488.671" width="755" height="587" rx="293.5" transform="rotate(-69 -241.29 488.671)" stroke="var(--c-slate-5)"/>
<rect x="-242.91" y="517.457" width="779" height="611" rx="305.5" transform="rotate(-72 -242.91 517.457)" stroke="var(--c-slate-5)"/>
<rect x="-242.597" y="547.07" width="803" height="635" rx="317.5" transform="rotate(-75 -242.597 547.07)" stroke="var(--c-slate-5)"/>
<rect x="-240.271" y="577.383" width="827" height="659" rx="329.5" transform="rotate(-78 -240.271 577.383)" stroke="var(--c-slate-5)"/>
<rect x="-235.858" y="608.265" width="851" height="683" rx="341.5" transform="rotate(-81 -235.858 608.265)" stroke="var(--c-slate-5)"/>
<rect x="-229.295" y="639.578" width="875" height="707" rx="353.5" transform="rotate(-84 -229.295 639.578)" stroke="var(--c-slate-5)"/>
<rect x="-220.524" y="671.181" width="899" height="731" rx="365.5" transform="rotate(-87 -220.524 671.181)" stroke="var(--c-slate-5)"/>
<rect x="-209.5" y="702.926" width="923" height="755" rx="377.5" transform="rotate(-90 -209.5 702.926)" stroke="var(--c-slate-5)"/>
<rect x="-196.185" y="734.662" width="947" height="779" rx="389.5" transform="rotate(-93 -196.185 734.662)" stroke="var(--c-slate-5)"/>
<rect x="-180.552" y="766.234" width="971" height="803" rx="401.5" transform="rotate(-96 -180.552 766.234)" stroke="var(--c-slate-5)"/>
<rect x="-162.583" y="797.486" width="995" height="827" rx="413.5" transform="rotate(-99 -162.583 797.486)" stroke="var(--c-slate-5)"/>
<rect x="-142.271" y="828.258" width="1019" height="851" rx="425.5" transform="rotate(-102 -142.271 828.258)" stroke="var(--c-slate-5)"/>
</svg>""",
            class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-3] pointer-events-none hidden lg:flex dark:opacity-60",
        ),
        # Gradial blur
        rx.html(
            """<svg width="338" height="478" viewBox="0 0 338 478" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="480" transform="translate(-1)" fill="url(#paint0_radial_10857_13090)"/>
<defs>
<radialGradient id="paint0_radial_10857_13090" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(170.501 240) rotate(-17.9215) scale(476.451 427.42)">
<stop offset="0.005434" stop-color="var(--c-slate-1)"/>
<stop offset="1" stop-color="var(--c-slate-1)" stop-opacity="0"/>
</radialGradient>
</defs>
</svg>
""",
            class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none",
        ),
        rx.box(
            rx.el.h2(
                "Powerful Outcomes",
                class_name="text-2xl font-semibold text-slate-12 text-center",
            ),
            rx.el.p(
                "Everything you need to achieve your goals",
                class_name="font-medium text-slate-9 text-center mt-2 text-base",
            ),
            rx.link(
                button(
                    "Book a demo",
                    size="xl",
                ),
                underline="none",
                is_external=True,
                href="/pricing",
                class_name="mt-6",
            ),
            class_name="flex flex-col justify-center items-center h-full",
        ),
        class_name="desktop-only h-full w-full flex flex-col justify-center items-center relative overflow-hidden row-span-2 col-span-1 lg:border border-slate-3 max-lg:py-[3rem] lg:p-1 lg:border-t-0 lg:border-b-0",
    )


def outcomes_card(
    title: str,
    description: str,
    icon: str,
    cols: str = "1",
    class_name: str = "",
) -> rx.Component:
    """Individual outcomes feature card component."""
    return rx.box(
        rx.box(
            _card_header(title, icon),
            _card_description(description),
            class_name="flex flex-col gap-[0.875rem]",
        ),
        class_name=f"col-span-{cols} lg:h-[11rem] overflow-hidden p-8 w-full {class_name} lg:first:border-b border-slate-3 lg:last:border-t",
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


def _create_grid_items() -> List[rx.Component]:
    """Creates the grid items with outcomes showcase in the center."""
    grid_items = []

    # Add first outcomes card
    grid_items.append(outcomes_card(**OUTCOMES_FEATURES[0]))

    # Add the central outcomes showcase
    grid_items.append(outcomes_showcase())

    # Add remaining outcomes cards
    for feature in OUTCOMES_FEATURES[1:]:
        grid_items.append(outcomes_card(**feature))

    return grid_items


def outcomes_grid() -> rx.Component:
    """Main outcomes features grid component."""
    return rx.box(
        *_create_grid_items(),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-2 lg:grid-rows-2 w-full lg:border border-b-0 border-slate-3 max-lg:divide-y divide-slate-3",
    )


def outcomes_section() -> rx.Component:
    return rx.el.section(
        header(),
        rx.box(
            outcomes_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col mx-auto w-full max-w-[84.19rem] relative justify-center items-center",
    )
