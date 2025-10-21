from dataclasses import dataclass

import reflex as rx
import reflex_ui as ui

from pcweb.components.marquee import marquee


def get_highlight(text: str) -> rx.Component:
    return rx.el.span(text, class_name="text-primary-11")


def get_normal_text(*children) -> rx.Component:
    return rx.el.span(
        *children, class_name="text-secondary-12 text-sm font-medium text-wrap flex-1"
    )


@dataclass
class Social:
    name: str
    role: str
    text: str | rx.Component
    url: str | None = None
    avatar: str | None = None


SOCIALS_1 = [
    Social(
        name="vishnudeva",
        role="Hacker News",
        text=get_normal_text(
            "Been a lurker on Hacker News for years but I created an account just so I could say how excited I am! Love the effort you're putting into ",
            get_highlight("Reflex"),
            ". Streamlit felt really painful to use whenever you want to do anything slightly out of the main path.",
        ),
        url="https://news.ycombinator.com/item?id=35140025",
    ),
    Social(
        name="Alex",
        role="OpenSea Co-founder",
        text=get_normal_text(
            "Have been playing with ",
            get_highlight("Reflex"),
            " since Jan and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making! ❤️",
        ),
        avatar="/landing/social/alex_opensea.webp",
    ),
    Social(
        name="Andrew",
        role="Discord",
        text=get_normal_text(
            "I've recently started using ",
            get_highlight("Reflex"),
            " and love it. My developer productivity is through the roof. Built a full-stack web app with stripe integration, firebase user authentication all built and looking quite nice and all done in about 2 nights of work.",
        ),
    ),
]

SOCIALS_2 = [
    Social(
        name="PoshoDev",
        role="Discord",
        text=get_normal_text(
            "I'm experimenting with ",
            get_highlight("Reflex"),
            " for the first time and I have to say that I really love the experience so far. Not needing to create frontend and backend individually for small web projects is a huge advantage. 😊",
        ),
    ),
    Social(
        name="vikinghckr",
        role="Hacker News",
        text=get_normal_text(
            "I'm not exaggerating but this might just be the highest impact library I've seen. As a backend developer who has lots of great project ideas but bail at the thought of having to use JavaScript and HTML, ",
            get_highlight("Reflex"),
            " is a godsend!",
        ),
        url="https://news.ycombinator.com/item?id=35140025",
    ),
    Social(
        name="Chaumy",
        role="Discord",
        text=get_normal_text(
            "Finally managed to work through the docs - ",
            get_highlight("Reflex"),
            " looks like an awesome framework to build webapps with - I just can't get used to the whole javascript ecosystem",
        ),
    ),
]


def social_card(social: Social) -> rx.Component:
    return rx.el.div(
        social.text,
        rx.el.div(
            ui.gradient_profile(
                seed=social.name,
                class_name="size-9 rounded-full",
            )
            if not social.avatar
            else rx.image(
                src=social.avatar,
                class_name="size-9 rounded-full",
            ),
            rx.el.div(
                rx.el.span(
                    social.name, class_name="text-secondary-12 font-medium text-sm"
                ),
                rx.el.span(
                    social.role, class_name="text-secondary-11 text-sm font-medium"
                ),
                class_name="flex flex-col",
            ),
            class_name="flex flex-row gap-4 mt-auto",
        ),
        rx.fragment(
            rx.el.a(
                to=social.url,
                target="_blank",
                class_name="absolute inset-0",
            ),
            ui.icon(
                "ArrowUpRight01Icon",
                class_name="group-hover:opacity-100 opacity-0 scale-50 group-hover:scale-100 transition-all duration-100 absolute bottom-4 right-4 size-5 text-primary-11 origin-bottom-left ease-in-out",
            ),
        )
        if social.url
        else None,
        class_name="flex flex-col gap-4 bg-slate-1 hover:bg-slate-2 transition-colors relative w-[22.5rem] h-[15rem] flex-shrink-0 p-6 group border-slate-4 py-10",
    )


def social_marquee() -> rx.Component:
    return rx.el.section(
        marquee(
            *[social_card(social) for social in SOCIALS_1],
            direction="left",
        ),
        marquee(
            *[social_card(social) for social in SOCIALS_2],
            direction="right",
        ),
        class_name="flex flex-col mx-auto w-full max-w-[64.19rem] lg:border-x justify-center items-center relative overflow-hidden border-slate-3 border-b",
    )
