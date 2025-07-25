from datetime import datetime

import reflex as rx

from pcweb.components.icons.icons import get_icon
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
from pcweb.pages.use_cases.use_cases import use_cases_page
from pcweb.pages.gallery import gallery
from pcweb.signup import IndexState


def footer_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        class_name="font-small text-slate-9 hover:!text-slate-11 no-underline transition-color",
    )


def footer_link_flex(heading: str, links: list[rx.Component]) -> rx.Component:
    return rx.box(
        rx.el.h4(
            heading,
            class_name="font-smbold text-slate-12",
        ),
        *links,
        class_name="flex flex-col gap-4",
    )


def social_menu_item(icon: str, url: str = "/", class_name: str = "") -> rx.Component:
    return rx.link(
        get_icon(icon=icon),
        class_name="flex justify-center items-center gap-2 bg-slate-1 hover:bg-slate-3 p-[0.125rem_0.75rem] text-slate-9 hover:!text-slate-9 transition-bg cursor-pointer overflow-hidden"
        + " "
        + class_name,
        href=url,
        is_external=True,
    )


def menu_socials() -> rx.Component:
    return rx.box(
        rx.box(
            social_menu_item("github", GITHUB_URL),
            social_menu_item(
                "twitter",
                TWITTER_URL,
                class_name="border-l border-slate-5 border-solid border-y-0 border-r-0",
            ),
            social_menu_item(
                "forum",
                FORUM_URL,
                class_name="!border-l !border-r border-slate-5 border-solid border-y-0",
            ),
            social_menu_item("discord", DISCORD_URL),
            social_menu_item(
                "linkedin",
                LINKEDIN_URL,
                class_name="!border-l !border-r border-slate-5 border-solid border-y-0",
            ),
            class_name="flex flex-row h-full align-center divide-x divide-slate-5 border-solid",
        ),
        class_name="border-slate-5 bg-slate-1 shadow-large border rounded-full h-6 overflow-hidden",
    )


def newsletter_form() -> rx.Component:
    return (
        rx.box(
            rx.el.h4(
                "Join Newsletter",
                class_name="font-instrument-sans font-semibold text-slate-12 text-sm leading-tight",
            ),
            rx.text(
                "Get the latest updates and news about Reflex",
                class_name="font-small text-slate-9",
            ),
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
                            class_name="font-smbold text-slate-11",
                        ),
                        class_name="flex flex-row items-center gap-2",
                    ),
                    rx.el.button(
                        "Sign up for another email",
                        class_name="bg-slate-3 hover:bg-slate-4 px-3 py-2 rounded-[10px] font-small text-slate-9 cursor-pointer",
                        on_click=IndexState.signup_for_another_user,
                    ),
                    class_name="flex flex-col flex-wrap gap-2",
                ),
                rx.form(
                    rx.box(
                        rx.el.input(
                            placeholder="Your email",
                            name="input_email",
                            type="email",
                            class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 p-[0.5rem_0.75rem] border rounded-[10px] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none",
                        ),
                        rx.form.submit(
                            rx.el.button(
                                "Subscribe",
                                class_name="flex justify-center items-center bg-slate-4 hover:bg-slate-5 p-[0.5rem_0.875rem] rounded-[10px] font-smbold text-slate-9 transition-bg cursor-pointer",
                            ),
                            as_child=True,
                        ),
                        class_name="flex flex-row gap-2 align-center",
                    ),
                    on_submit=IndexState.signup,
                ),
            ),
            class_name="flex flex-col gap-4 align-start",
        ),
    )


def ph_1() -> rx.Component:
    return rx.fragment(
        rx.image(
            src="/logos/dark/ph_1.svg",
            class_name="hidden dark:block h-[40px] w-fit",
            alt="1st product of the day logo",
        ),
        rx.image(
            src="/logos/light/ph_1.svg",
            class_name="dark:hidden block h-[40px] w-fit",
            alt="1st product of the day logo",
        ),
    )


@rx.memo
def footer() -> rx.Component:
    from pcweb.pages.framework.views.footer_index import dark_mode_toggle

    return rx.el.footer(
        rx.box(
            rx.box(
                rx.box(
                    menu_socials(),
                    ph_1(),
                    class_name="flex flex-col gap-6",
                ),
                rx.text(
                    f"© {datetime.now().year} Pynecone, Inc.",
                    class_name="font-small text-slate-9",
                ),
                class_name="flex flex-col justify-between items-start gap-4 self-stretch",
            ),
            footer_link_flex(
                "Links",
                [
                    footer_link("Home", "/"),
                    footer_link("Templates", gallery.path),
                    footer_link("Blog", blogs.path),
                    footer_link(
                        "Changelog", "https://github.com/reflex-dev/reflex/releases"
                    ),
                ],
            ),
            footer_link_flex(
                "Documentation",
                [
                    footer_link("Introduction", getting_started.introduction.path),
                    footer_link("Installation", getting_started.installation.path),
                    footer_link("Components", library.path),
                    footer_link("Hosting", hosting.deploy_quick_start.path),
                ],
            ),
            footer_link_flex(
                "Resources",
                [
                    footer_link("FAQ", faq.path),
                    footer_link("Common Errors", errors.path),
                    footer_link("Roadmap", ROADMAP_URL),
                    footer_link("Forum", FORUM_URL),
                    footer_link("Affiliates", "/affiliates"),
                    footer_link("Use Cases", use_cases_page.path),
                    rx.box(class_name="grow"),
                    dark_mode_toggle(),
                ],
            ),
            newsletter_form(),
            class_name="flex flex-row flex-wrap justify-between gap-[4.5rem] p-[3rem_1rem_3rem_1.5rem] w-full max-w-[94.5rem]",
        ),
        class_name="flex justify-center border-slate-3 border-t w-full",
    )
