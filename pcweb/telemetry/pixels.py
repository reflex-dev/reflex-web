"""This module contains the pixel trackers for the website."""

import reflex as rx
from reflex_ui.blocks.telemetry import (
    get_clearbit_trackers,
    get_common_room_trackers,
    get_google_analytics_trackers,
    get_posthog_trackers,
    get_rb2b_trackers,
    get_unify_trackers,
    gtag_report_conversion,
)


def get_pixel_website_trackers() -> list[rx.Component]:
    """Get the pixel trackers for the website."""
    return [
        get_common_room_trackers(site_id="b608b3c3-5dea-4365-b685-6b6635c7fda5"),
        *get_google_analytics_trackers(tracking_id="G-4T7C8ZD9TR"),
        gtag_report_conversion(
            conversion_id_and_label="AW-11360851250/ASB4COvpisIbELKqo6kq"
        ),
        get_clearbit_trackers(public_key="pk_3d711a6e26de5ddb47443d8db170d506"),
        get_posthog_trackers(
            project_id="phc_A0MAR0wCGhXrizWmowRZcYqyZ8PMhPPQW06KEwD43aC"
        ),
        *get_rb2b_trackers(),
        get_unify_trackers(),
    ]
