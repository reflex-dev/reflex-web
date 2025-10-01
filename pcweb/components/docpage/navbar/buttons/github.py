import reflex as rx
from pcweb.constants import GITHUB_URL
from pcweb.components.icons.icons import get_icon
from pcweb.github import GithubStarState


def github() -> rx.Component:
    return rx.link(
        rx.flex(
            get_icon(icon="github_navbar", class_name="shrink-0 !text-slate-9"),
            rx.text(
                GithubStarState.stars_short,
                class_name="font-small",
            ),
            class_name="text-slate-9 flex-row gap-2 hover:bg-slate-3 flex justify-center rounded-[10px] border border-slate-5 bg-slate-1 transition-bg cursor-pointer py-0.5 px-3 items-center h-8",
        ),
        href=GITHUB_URL,
        underline="none",
    )
