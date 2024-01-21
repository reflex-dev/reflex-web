import reflex as rx
from pcweb import constants, styles
from pcweb.styles import text_colors as tc
from pcweb.templates.webpage import webpage


def change(date, title, description, points, link):
    return rx.vstack(
        rx.vstack(
            rx.image(src="/changelog_icon.svg", width="5em", height="5em", opacity=1),
            rx.heading(
                "Reflex " + title,
                font_family=styles.MONO,
                font_size=styles.H3_FONT_SIZE,
                opacity=1,
            ),
            background="radial-gradient(55.39% 67.50% at 50.00% 0%, rgba(32, 17, 126, 0.05) 0%, rgba(255, 255, 255, 0.00) 100%);",
            box_shadow=" 0px 8px 12px -4px rgba(3, 3, 11, 0.02), 0px 12px 8px 0px rgba(3, 3, 11, 0.04), 0px 2px 3px 0px rgba(3, 3, 11, 0.10), 0px 0px 0px 1px rgba(52, 46, 92, 0.12);",
            align_items="center",
            width="100%",
            border_radius="lg",
            padding_y="1em",
        ),
        rx.text(description, color="#494369", font_family=styles.MONO),
        rx.unordered_list(
            *[
                rx.list_item(
                    d, font_size=".8em", color="#494369", font_family=styles.MONO
                )
                for d in points
            ],
            padding_left="1.5em",
        ),
        rx.hstack(
            rx.hstack(
                rx.image(src="/icons/copy.svg", width="1em", height="1em"),
                rx.text(
                    title,
                    font_size=styles.TEXT_FONT_SIZE,
                    font_weight=styles.BOLD_WEIGHT,
                ),
                padding_right="1em",
            ),
            rx.divider(margin_x="1em"),
            rx.link(
                rx.button(
                    "Full changelog",
                    rx.icon(tag="arrow_forward"),
                    padding_x="2em",
                    style=styles.BUTTON_LIGHT_NO_BACKGROUND,
                ),
                href=link,
            ),
            width="100%",
        ),
        align_items="flex-start",
        width="100%",
        padding_bottom="3em",
        bg="#FFFFFF",
    )


def changelog_content():
    return rx.vstack(
        change(
            "2024-01-22",
            "v0.3.9",
            "Improve hot-reload times in dev mode",
            [
                "Allow State subclasses to use mixins to define fields",
                "Improvements to Radix-UI preview components",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.9",
        )
        change(
            "2024-01-08",
            "v0.3.8",
            "New rx.match helper acts as a switch statement",
            [
                "app.compile() is no longer required",
                "Add time_picker component",
                "Support bare SQLAlchemy DeclarativeBase models",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.8",
        ),
        change(
            "2023-12-14",
            "v0.3.7",
            "Support SQLAlchemy v2",
            [
                "Preview of radix themes components",
                "Allow redis:// and rediss:// style URL",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.7",
        ),
        change(
            "2023-12-06",
            "v0.3.6",
            "rx.el components working with State",
            [],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.6",
        ),
        change(
            "2023-12-05",
            "v0.3.5",
            "Performance Improvements",
            [
                "More flexible rx.State subclassing",
                "Enhanced standard HTML elements under `rx.el`",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.5",
        ),
        change(
            "2023-11-17",
            "v0.3.4",
            "Support Dynamic Forms",
            [
                "Support python 3.12",
                "NextJS 14",
                "Fast lazy import",
                "Upload with progress and cancellation",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.4",
        ),
        change(
            "2023-11-03",
            "v0.3.2",
            "Work with Github Codespaces",
            [
                "Expose gunicorn_worker_class for extended configuration",
                "stop_propagation and prevent_default for all events",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.2",
        ),
        change(
            "2023-10-27",
            "v0.3.0",
            "New rx.data_editor Component",
            [
                "Reflex hosting alpha CLI",
                "Drop python 3.7 support",
                "Experimental support for Radix themes",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.0",
        ),
        change(
            "2023-10-09",
            "v0.2.9",
            "Core Graphing Improvements",
            [
                "Core Graphing Library is now Recharts",
                "HTML Editor Component",
                "Run Arbitrary Javascript from Event Handler",
                "Redirect into New Window",
                "rx.constants Module Refactored",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.9",
        ),
        change(
            "2023-09-22",
            "v0.2.8",
            "Background Tasks + Improved API for wrapping components.",
            [
                "Support long-running non-blocking operations",
                "Trigger file downloads",
                "Better change tracking for state vars",
                "Arbitrary args for event triggers and serializers for custom types",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.8",
        ),
        change(
            "2021-09-08",
            "v0.2.7",
            "Reduced Package Size + Client-side Storage.",
            [
                "Reduced initial package size by 60%",
                "Client-side Storage integrated with State",
                "Added on_mount and on_unmount triggers for all components",
                "Per-component prop autocompletion for IDEs and breakpoints support",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.7",
        ),
        change(
            "2021-08-14",
            "v0.2.6",
            "Bug fix to connect to no sql databases.",
            [
                "Added the step prop to Slider.",
                "Added support for limits in pagination",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.6",
        ),
        change(
            "2021-08-01",
            "v0.2.5",
            "Performance improvements + bug fixes.",
            [
                "Removing the Node dependency on Windows",
                "3x performance improvement on the frontend (dev mode should be much snappier now!)",
                "f-string support for vars",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.5",
        ),
        width="100%",
    )


@webpage(path="/changelog", title="Changelog")
def changelog():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("Changelog", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.text(
                    "Keep up to date with the latest Reflex news.",
                    color=tc["docs"]["body"],
                ),
                rx.center(
                    rx.span(
                        "Reflex has new releases and features coming every week! Make sure to star and watch on ",
                        rx.link("GitHub", href=constants.GITHUB_URL),
                        " to stay up to date.",
                        color="#494369",
                    ),
                    bg="#FAF8FB",
                    font_family=styles.MONO,
                    padding=4,
                    margin_top="2em",
                    margin_bottom="2em",
                    border="1px solid #EAE4FD",
                    border_radius=styles.DOC_BORDER_RADIUS,
                    font_size=".8em",
                ),
                changelog_content(),
                text_align="left",
                width="100%",
                spacing="2em",
            ),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        max_width="960px",
    )
