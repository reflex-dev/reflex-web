import reflex as rx
from pcweb import constants, styles
from pcweb.templates.webpage import webpage
from pcweb.components.logo import logo


def change(date, title, description, points, link):
    return rx.vstack(
        rx.vstack(
            logo(
                width=["10em", "12em", "14em"],
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon(tag="copy", size=18, color="#6C6C81"),
                    rx.text(title, font_weight=styles.BOLD_WEIGHT, color="#D6D6ED"),
                ),
                rx.tablet_and_desktop(
                    rx.divider(margin_x="1em", size="4"),
                    width="100%",
                ),
                rx.link(
                    rx.button(
                        rx.icon(tag="github", size=18),
                        "Full Notes ->",
                        color="#A2A2B9",
                        padding_x="1em",
                        border_radius="7px;",
                        border="1px solid rgba(107, 107, 127, 0.50);",
                        background="rgba(107, 107, 127, 0.10);",
                        box_shadow="0px 3px 4px -1px rgba(23, 26, 43, 0.40);",
                        backdrop_filter="blur(2px);",
                        text_wrap="nowrap",
                    ),
                    href=link,
                ),
                width="100%",
                padding_top=["1em", "1em", "0", "0", "0", "0"],
                justify="between",
            ),
            padding_right="1em",
            border_radius="10px",
            border="1px solid #3C3646",
            background="linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%)",
            box_shadow="0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
            padding="1em",
            padding_top="2em",
            width="100%",
        ),
        rx.text(description, color="#D6D6ED", font_family=styles.MONO),
        rx.chakra.unordered_list(
            *[
                rx.list_item(
                    d, font_size=".8em", color="#6C6C81", font_family=styles.MONO
                )
                for d in points
            ],
            padding_left="1.5em",
        ),
        align_items="flex-start",
        width="100%",
        padding_bottom="3em",
        padding_left=["0", "0", "1em", "1em", "1em", "1em"],
        border_left="1px solid #23222B",
    )


def changelog_content():
    return rx.chakra.vstack(
        change(
            "2024-06-24",
            "v0.5.5",
            "Support rx.SessionStorage as State Var",
            [
                "More Recharts improvements",
                "Better support for interactive stateless apps",
                "Fix websocket disconnect when navigating to another domain",
                "Make .web folder location configurable with REFLEX_WEB_WORKDIR",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.5",
        ),
        change(
            "2024-06-11",
            "v0.5.4",
            "Better support for serializing datetime, Color, Path, and others to string",
            [
                "Default theme appearance to system light/dark setting",
                "Toast component is now promoted to `rx.toast`",
                "Recharts props accept `rx.color` values",
                "Avoid hang when backend disconnects while processing an event",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.4",
        ),
        change(
            "2024-06-05",
            "v0.5.3",
            "Plotly Improvements",
            [
                "More granular lazy imports",
                "External asset support",
                "Numerous bug fixes (see release notes)",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.3",
        ),
        change(
            "2024-05-30",
            "v0.5.2",
            "Support for Lifespan tasks",
            [
                "Vertical tabs",
                "Configurable gunicorn workers in prod mode",
                "Fix for setting global font_family style",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.2",
        ),
        change(
            "2024-05-21",
            "v0.5.1",
            "Connection Error is now a Toast",
            [
                "rx.toast supports action buttons and on_dismiss/on_auto_close",
                "Improved typing for ConnectionState and State mixins",
                "Faster CLI launch time",
                "Better customizability for rx.accordion",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.1",
        ),
        change(
            "2024-05-13",
            "v0.5.0",
            "Radix Themes 3.0",
            [
                "New public API methods for wrapping 3rd-Party Components",
                "Generic throttle and debounce for all event handlers",
                "Use Alembic batch mode for db makemigrations",
                "Experimental toast component in rx._x.toast",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.0",
        ),
        change(
            "2024-04-22",
            "v0.4.9",
            "Bug Fixes and Various Improvements",
            [
                "Fix for UnicodeDecodeError on Windows",
                "Use npm fallback when bun does not work",
                "Allow set in Var.contains",
                "Fix for light/dark dialogs not matching current theme appearance",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.9",
        ),
        change(
            "2024-04-15",
            "v0.4.8",
            "Support Bun on Windows for Faster Dependency Installation",
            [
                "Expose transpile_packages for Components that do not identify as ES6 module",
                "Enum types are serialized to their values",
                "Automatic tuple unpacking for Component children",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.8",
        ),
        change(
            "2024-04-09",
            "v0.4.7",
            "New reflex init templates",
            [
                "Use any Reflex app on Github as an initial template",
                "reflex run will automatically init the app when required",
                "Reflex Experimental Namespace: rx._x",
                "Windows support for Python 3.12",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.7",
        ),
        change(
            "2024-04-01",
            "v0.4.6",
            "rx.ComponentState provides simple per-component state",
            [
                "Use dill instead of cloudpickle",
                "More compatible package pins",
                "rx.EventHandler annotation",
                "Automatic pyi generation for published components",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.6",
        ),
        change(
            "2024-03-20",
            "v0.4.5",
            "Support SQLAlchemy Models Directly",
            [
                "Experimental Multi-process Compilation",
                "Better default titles for SEO",
                "router.session.client_ip more likely to be correct now",
                "Allow rx.download to resolve rx.get_upload_url links",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.5",
        ),
        change(
            "2024-03-11",
            "v0.4.4",
            "Fix missing on_load and /_upload in prod deployments",
            [
                "rx.upload exposes on_drop event trigger",
                "rx.el.form supports on_submit event trigger",
                "Improve 'Stateless' app detection",
                "Expose lang and other attributes on <html> tag",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.4",
        ),
        change(
            "2024-03-04",
            "v0.4.3",
            "CLI for Creating and Publishing 3rd Party Components",
            [
                "get_state() API for accessing arbitrary states",
                "Set initial_value for computed vars",
                "Less invasive backend disconnected notification",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.3",
        ),
        change(
            "2024-02-26",
            "v0.4.2",
            "Syncronize local storage between tabs",
            [
                "Tuple type annotations are now respected index-wise",
                "Substates are serialized individually",
                "Better Image Serialization",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.2",
        ),
        change(
            "2024-02-19",
            "v0.4.1",
            "Fix Windows Hot-reload Issues",
            [
                "Fix browser error when triggering upload with no files selected",
                "Fix regression: rx.link with is_external",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.1",
        ),
        change(
            "2024-02-16",
            "v0.4.0",
            "Replace Chakra with Radix components",
            [
                "Entirely new core component library based on radix-ui",
                "App-wide theming system",
                "Enhanced support for upload and download",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.0",
        ),
        change(
            "2024-02-05",
            "v0.3.10",
            "Lucide Icons now available at rx.lucide.icon",
            [
                "Custom Reflex support directory (REFLEX_DIR)",
                "Better support for native SQLAlchemy models",
                "Avoid exposing unused _upload and _event endpoints",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.10",
        ),
        change(
            "2024-01-22",
            "v0.3.9",
            "Improve hot-reload times in dev mode",
            [
                "Allow State subclasses to use mixins to define fields",
                "Improvements to Radix-UI preview components",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.3.9",
        ),
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


@webpage(path="/changelog", title="Changelog · Reflex")
def changelog():
    return rx.center(
        rx.box(
            rx.flex(
                rx.chakra.text(
                    "Timeline",
                    background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    background_clip="text",
                    padding_x="1em",
                ),
                width="7em",
                justify="center",
                border_radius="15px;",
                border="1px solid #4435D4;",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);",
            ),
            rx.chakra.text(
                "Changelog",
                font_size="44px",
                background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
            ),
            rx.center(
                rx.chakra.span(
                    "Reflex has new releases and features coming every week! Make sure to star and watch on ",
                    rx.link("GitHub", href=constants.GITHUB_URL, color="#6151F3"),
                    " to stay up to date.",
                    color="#A2A2B9",
                    width="100%",
                ),
                font_family=styles.MONO,
                padding="1em",
                margin_bottom="2em",
                border_radius="7px;",
                border="1px solid rgba(107, 107, 127, 0.50);",
                background="rgba(107, 107, 127, 0.10);",
                box_shadow="0px 3px 4px -1px rgba(23, 26, 43, 0.40);",
                backdrop_filter="blur(2px);",
                width="100%",
            ),
            changelog_content(),
            max_width=["95vw", "95vw", "100vw", "100vw", "100vw", "100vw"],
        ),
        width="100%",
    )
