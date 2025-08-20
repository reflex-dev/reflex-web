from datetime import datetime

import reflex as rx
from reflex.style import color_mode, set_color_mode

from pcweb.components.button import button
from pcweb.components.icons import get_icon
from pcweb.components.icons.hugeicons import hi
from pcweb.constants import (
    DISCORD_URL,
    FORUM_URL,
    GITHUB_URL,
    LINKEDIN_URL,
    ROADMAP_URL,
    TWITTER_URL,
)
from pcweb.pages.blog import blogs
from pcweb.pages.docs import ai_builder, getting_started, hosting
from pcweb.pages.docs.library import library
from pcweb.pages.errors import errors
from pcweb.pages.faq import faq
from pcweb.pages.gallery import gallery
from pcweb.signup import IndexState
from pcweb.views.footer import ph_1


def tab_item(mode: str, icon: str) -> rx.Component:
    active_cn = " text-slate-9 shadow-small bg-slate-1"
    unactive_cn = " hover:text-slate-12 text-slate-9"
    return rx.el.button(
        hi(tag=icon, class_name="shrink-0"),
        on_click=set_color_mode(mode),
        class_name="flex items-center cursor-pointer justify-center rounded-md transition-color size-7 outline-none focus:outline-none "
        + rx.cond(mode == color_mode, active_cn, unactive_cn),
    )


def dark_mode_toggle() -> rx.Component:
    return rx.box(
        tab_item("system", "computer"),
        tab_item("light", "sun-01"),
        tab_item("dark", "moon-02"),
        class_name="flex flex-row items-center bg-slate-3 p-1 rounded-[0.625rem] w-fit",
    )


def footer_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        rx.icon(
            tag="chevron-right",
            size=16,
            class_name="shrink-0 lg:hidden flex",
        ),
        href=href,
        class_name="font-small text-slate-9 hover:!text-slate-11 no-underline transition-color w-full lg:w-fit flex flex-row justify-between items-center",
    )


def footer_link_flex(
    heading: str, links: list[rx.Component], class_name: str = ""
) -> rx.Component:
    return rx.box(
        rx.el.h3(
            heading,
            class_name="font-smbold text-slate-12 w-fit",
        ),
        *links,
        class_name="flex flex-col gap-4 px-8 py-10 lg:p-10" + " " + class_name,
    )


def social_menu_item(icon: str, url: str, name: str) -> rx.Component:
    return rx.link(
        get_icon(icon, class_name="!text-slate-9 shrink-0"),
        class_name="flex w-full h-8 lg:size-8 border border-slate-5 rounded-lg hover:bg-slate-3 transition-bg bg-slate-1 px-3 py-1.5 justify-center items-center border-solid",
        href=url,
        custom_attrs={"aria-label": "Social link for " + name},
        is_external=True,
    )


def menu_socials() -> rx.Component:
    return rx.box(
        social_menu_item("discord_navbar", DISCORD_URL, "Discord"),
        social_menu_item("forum", FORUM_URL, "Forum"),
        social_menu_item("twitter", TWITTER_URL, "Twitter"),
        social_menu_item("github_navbar", GITHUB_URL, "Github"),
        social_menu_item("linkedin", LINKEDIN_URL, "LinkedIn"),
        class_name="flex flex-row h-full align-center gap-2 w-full lg:w-fit max-w-[24rem]",
    )


def newletter_input() -> rx.Component:
    return rx.box(
        rx.cond(
            IndexState.signed_up,
            rx.box(
                rx.box(
                    rx.icon(
                        tag="circle-check",
                        size=16,
                        class_name="!text-violet-9",
                    ),
                    rx.text(
                        "Thanks for subscribing!",
                        class_name="font-base text-slate-11",
                    ),
                    class_name="flex flex-row items-center gap-2",
                ),
                button(
                    "Sign up for another email",
                    variant="muted",
                    on_click=IndexState.signup_for_another_user,
                ),
                class_name="flex flex-col flex-wrap gap-2",
            ),
            rx.form(
                rx.el.input(
                    placeholder="Your email",
                    name="input_email",
                    type="email",
                    class_name="relative box-border border-slate-4 focus:border-violet-9 focus:border-1 bg-slate-2 p-[0.5rem_0.75rem] border rounded-lg font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full h-8 max-w-[24rem]",
                ),
                button(
                    "Subscribe",
                    type="submit",
                    variant="muted",
                    class_name="!h-8 !rounded-lg !py-2 !px-3.5 !font-small-smbold w-full lg:w-auto lg:max-w-full max-w-[24rem]",
                ),
                class_name="w-full flex flex-col lg:flex-row gap-2 items-center",
                on_submit=IndexState.signup,
            ),
        ),
        class_name="w-full",
    )


def newsletter() -> rx.Component:
    return (
        rx.box(
            rx.text(
                "Get updates",
                class_name="font-small text-slate-9",
            ),
            newletter_input(),
            class_name="flex flex-col items-center lg:items-start gap-4 self-stretch p-10 lg:border-r border-slate-3",
        ),
    )


@rx.memo
def footer_index() -> rx.Component:
    return rx.el.footer(
        rx.box(
            footer_link_flex(
                "Reflex",
                [
                    footer_link("Home", "/"),
                    footer_link("Templates", gallery.path),
                    footer_link("Blog", blogs.path),
                    footer_link(
                        "Changelog", "https://github.com/reflex-dev/reflex/releases"
                    ),
                ],
                class_name="lg:!border-l !border-slate-3 !row-span-2",
            ),
            footer_link_flex(
                "Documentation",
                [
                    footer_link("Introduction", getting_started.introduction.path),
                    footer_link("Installation", getting_started.installation.path),
                    footer_link("Components", library.path),
                    footer_link("Hosting", hosting.deploy_quick_start.path),
                ],
                class_name="lg:!border-t-0 !row-span-2",
            ),
            footer_link_flex(
                "Resources",
                [
                    footer_link("FAQ", faq.path),
                    footer_link("Common Errors", errors.path),
                    footer_link("Roadmap", ROADMAP_URL),
                    footer_link("Forum", FORUM_URL),
                    footer_link("Affiliates", "/affiliates"),
                    footer_link("Use Cases", "/use-cases"),
                    rx.box(class_name="grow"),
                    rx.el.div(
                        ph_1(),
                        dark_mode_toggle(),
                        class_name="flex flex-row items-center gap-6",
                    ),
                ],
                class_name="!row-span-3 lg:!border-t-0 lg:!border-r !border-slate-3",
            ),
            # Socials
            rx.box(
                rx.text(
                    f"Copyright © {datetime.now().year} Pynecone, Inc.",
                    class_name="font-small text-slate-9",
                ),
                menu_socials(),
                class_name="flex flex-col items-center lg:items-start gap-4 self-stretch p-10 lg:border-l border-slate-3",
            ),
            newsletter(),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-2 w-full divide-y divide-slate-3 lg:divide-x border-t border-slate-3 lg:border-t-0",
        ),
        class_name="flex max-w-[64.19rem] justify-center items-center w-full",
    )
