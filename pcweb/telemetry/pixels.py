from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

from pcweb.telemetry import pixels_clearbit, pixels_google, pixels_koala, pixels_posthog, pixels_rb2b

if TYPE_CHECKING:
    import reflex as rx



def get_pixel_website_trackers() -> list[rx.Component]:
    return list(
        itertools.chain(
            pixels_google.get_pixel_website_trackers(),
            pixels_koala.get_pixel_website_trackers(),
            pixels_posthog.get_pixel_website_trackers(),
            pixels_clearbit.get_pixel_website_trackers(),
            pixels_rb2b.get_pixel_rb2b_website_trackers(),
        ),
    )
