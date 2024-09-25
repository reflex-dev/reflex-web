from typing import Generator

import reflex as rx

PIXEL_SCRIPT_URL_INSTANTLY: str = "https://r2.leadsy.ai/tag.js"


def get_pixel_website_trackers()-> Generator[rx.Component, None, None]:
    yield rx.script(
        src=PIXEL_SCRIPT_URL_INSTANTLY,
        custom_attrs={
            "id": "vtag-ai-js",
            "data-pid": "1lyr4f7pDa9XKwTjr",
            "data-version": "062024",
        },
    )
