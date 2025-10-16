"""Github stars count for the reflex repository."""

import reflex as rx

REFLEX_STAR_COUNT = 26000


class GithubStarState(rx.State):
    @rx.var(cache=True, interval=60)
    def stars(self) -> str:
        return f"{REFLEX_STAR_COUNT}"

    @rx.var(cache=True, interval=60)
    def stars_short(self) -> str:
        return f"{round(REFLEX_STAR_COUNT / 1000)}K"
