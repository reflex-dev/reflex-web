from typing import Generator

import reflex as rx

PIXEL_SCRIPT_URL_CLEARBIT: str = (
    "https://tag.clearbitscripts.com/v1/pk_3d711a6e26de5ddb47443d8db170d506/tags.js"
)


def get_pixel_website_trackers() -> Generator[rx.Component, None, None]:
    yield rx.el.script(
        src=PIXEL_SCRIPT_URL_CLEARBIT,
        referrer_policy="strict-origin-when-cross-origin",
    )
