"""This module contains the pixel trackers for the website."""

import reflex as rx
from reflex_ui.blocks.telemetry import (
    get_default_telemetry_script,
    get_google_analytics_trackers,
    get_unify_trackers,
    gtag_report_conversion,
)


def get_pixel_website_trackers() -> list[rx.Component]:
    """Get the pixel trackers for the website."""
    return [
        *get_google_analytics_trackers(tracking_id="G-4T7C8ZD9TR"),
        gtag_report_conversion(
            conversion_id_and_label="AW-11360851250/ASB4COvpisIbELKqo6kq"
        ),
        get_unify_trackers(),
        get_default_telemetry_script(),
    ]
