from __future__ import annotations

from typing import Generator

import reflex as rx

PIXEL_SCRIPT_GOOGLE_TAG: str = """
window.dataLayer = window.dataLayer || [];
function gtag() {
    window.dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', 'reflex_pixel_id');
"""
PIXEL_SCRIPT_URL_GOOGLE_TAG: str = (
    "https://www.googletagmanager.com/gtag/js?id=reflex_pixel_id"
)
REFLEX_PIXEL_ID: str = "G-4T7C8ZD9TR"


def get_pixel_script_url_google_tag(
    reflex_pixel_id: str,
) -> str:
    return PIXEL_SCRIPT_URL_GOOGLE_TAG.replace(
        "reflex_pixel_id",
        reflex_pixel_id,
    )


def get_pixel_script_google_tag(
    reflex_pixel_id: str,
) -> str:
    return PIXEL_SCRIPT_GOOGLE_TAG.replace(
        "reflex_pixel_id",
        reflex_pixel_id,
    )


def get_pixel_website_trackers() -> Generator[rx.Component, None, None]:
    yield rx.script(
        src=get_pixel_script_url_google_tag(
            reflex_pixel_id=REFLEX_PIXEL_ID,
        ),
    )
    yield rx.script(
        get_pixel_script_google_tag(
            reflex_pixel_id=REFLEX_PIXEL_ID,
        ),
    )
