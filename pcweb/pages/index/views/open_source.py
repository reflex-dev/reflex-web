import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.components.button import button
from pcweb.constants import GITHUB_URL, GITHUB_STARS

contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
bugs_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"


def stat(icon: str, stat: str, text: str) -> rx.Component:
    return rx.box(
        get_icon(icon),
        rx.box(
            rx.text(
                stat,
                class_name="font-semibold text-[2.5rem] text-slate-9 leading-[3rem] tracking-[-0.0375rem]",
            ),
            rx.text(text, class_name="font-small text-slate-9"),
            class_name="flex flex-col text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4",
    )


def stats() -> rx.Component:
    return rx.box(
        stat("star", f"{GITHUB_STARS:,}+", "stars"),
        stat("fork", "1,100+", "forks"),
        stat("eye_big", "145+", "watch"),
        class_name="justify-center gap-10 grid grid-cols-3",
    )


def github_links() -> rx.Component:
    return rx.box(
        rx.link(
            button("Open GitHub", class_name="!w-full"),
            href=GITHUB_URL,
            is_external=True,
            class_name="w-full",
        ),
        rx.box(
            rx.link(
                button("Bugs", variant="secondary", class_name="!w-full"),
                href=bugs_url,
                is_external=True,
                class_name="w-full",
            ),
            rx.link(
                button("Good first issues", variant="secondary", class_name="!w-full"),
                href=contribution_url,
                is_external=True,
                class_name="w-full",
            ),
            class_name="flex flex-row items-center gap-4",
        ),
        class_name="flex flex-col gap-4 border-slate-4 bg-slate-2 shadow-large mx-auto p-4 border rounded-[1.125rem] w-full max-w-[25rem]",
    )


def open_source() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Join our open source community",
                class_name="font-x-large gradient-heading",
            ),
            rx.text(
                "Get help and contribute on GitHub.",
                class_name="font-base text-slate-9",
            ),
            class_name="flex flex-col gap-4 text-center",
        ),
        # Stats
        stats(),
        # Github links
        github_links(),
        class_name="flex flex-col gap-10 w-full",
    )
