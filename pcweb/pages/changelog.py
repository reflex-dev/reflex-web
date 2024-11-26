import reflex as rx
from pcweb import constants
from pcweb.templates.webpage import webpage
from pcweb.components.icons.icons import get_icon
from pcweb.components.webpage.comps import h1_title
from pcweb.flexdown import markdown_with_shiki

def change(
    date: str, version: str, description: str, points: list[str], link: str
) -> rx.Component:
    return rx.el.li(
        rx.box(
            rx.box(
                rx.code(version, class_name="max-w-fit text-xl code-style"),
                rx.moment(date, from_now=True, class_name="font-small text-slate-10"),
                class_name="flex flex-col gap-2",
            ),
            rx.link(
                rx.el.button(
                    "Full Notes",
                    get_icon(icon="new_tab"),
                    class_name="flex flex-row items-center gap-2 border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small p-[0.3125rem] border rounded-md h-6 font-small text-slate-9 transition-background",
                ),
                underline="none",
                href=link,
            ),
            class_name="flex flex-row justify-between items-start border-slate-5 pb-3 lg:pb-4 border-b w-full",
        ),
        rx.el.h3(
            description,
            class_name="pt-3 lg:pt-4 pb-2 lg:pb-3 font-md text-balance text-slate-12",
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    markdown_with_shiki(d, class_name="markdown-code"),
                    class_name="font-small text-slate-11",
                )
                for d in points
            ],
            list_style_type="disc",
            class_name="space-y-2 pl-4 w-full",
        ),
        class_name="flex flex-col gap-0 border-slate-5 bg-slate-2 shadow-large p-4 lg:p-6 border rounded-xl w-full",
    )


def changelog_content():
    return rx.el.ul(
        change(
            "2024-11-25",
            "v0.6.6",
            "Support Pydantic BaseModel (v1 & v2) objects in state",
            [
                "`reflex init` now links to templates on the web",
                "New `.temporal` event action drops event when backend is down",
                "Improved type checking",
                "`rx.asset` promoted from experimental",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.6",
        ),
        change(
            "2024-11-12",
            "v0.6.5",
            "New Hosting Service CLI",
            [
                "Additional static and runtime typing improvements",
                "`rx.get_state` API for accessing state outside of event handlers",
                "Support custom `bunfig.toml`",
                "Direct encoding of State vars to JSON (without `get_value`)",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.5",
        ),
        change(
            "2024-10-29",
            "v0.6.4",
            "Make Var System Expandable",
            [
                "Set default gunicorn max_requests to avoid memory leak",
                "Support for dotenv `env_file` when `python-dotenv` is installed",
                "New `rx.dynamic` decorator for component functions using state",
                "More event typing improvements",
                "Experimental support for Shiki code block",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.4",
        ),
        change(
            "2024-10-18",
            "v0.6.3",
            "Improved Static Typing for Var and Event",
            [
                "Support `aria_` and `data_` props passed to all components",
                "Optimize state manager and state serialization",
                "Graphing doc improvements",
                "Bug fixes",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.3",
        ),
        change(
            "2024-10-07",
            "v0.6.2",
            "Improve Event Processing Time",
            [
                "`rx.cond` can now be used with event triggers, like `on_click`",
                "Replace dill with standard pickle for faster serialization",
                "All `rx.el.svg` elements are now supported",
                "Fix styling in dynamic components",
                "Fix bug when using `rx.call_script` with f-strings and vars",
            ],
            "https://github.com/reflex-dev/reflex/releases/v0.6.2",
        ),
        change(
            "2024-09-30",
            "v0.6.1",
            "Experimental Dynamic Components",
            [
                "Fix various regressions from v0.5.10",
                "Optionally run app using Granian instead of Uvicorn",
                "Set `REFLEX_USE_SYSTEM_BUN=1` and `REFLEX_USE_SYSTEM_NODE=1` to use already-installed runtimes on the `PATH`",
                "Bump nextjs to 14.2.13",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.1",
        ),
        change(
            "2024-09-24",
            "v0.6.0",
            "Improved Javascript Interop with updated rx.Var API",
            [
                "Maintain state across hot reloads",
                "Added backend `/_health` endpoint to get server status",
                "Better validation of dynamic route args, computed vars, and dependency tracking.",
                "Drop support for Python 3.8",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.6.0",
        ),
        change(
            "2024-08-27",
            "v0.5.10",
            "Bug Fixes",
            [
                "Move chakra components into its repo (reflex-chakra)",
                "Fix import clash between connectionToaster and hooks.useState",
                "Fix various line_chart issues",
                "Validate Toast Props",
                "Use different registry when in china",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.10",
        ),
        change(
            "2024-08-06",
            "v0.5.9",
            "Bug Fixes",
            [
                "Properly set `is_hydrated` to `false` on page navigation events",
                "`@rx.var(cache=True)` now correctly gets the initial value",
                "Accessing /404 now shows the 404 page content",
                "Fix event actions for Recharts event triggers",
                "Allow setting `rx.breakpoints` in the `style` prop",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.9",
        ),
        change(
            "2024-07-29",
            "v0.5.8",
            "Use templates from reflex-dev/templates",
            [
                "Nicer looking default style for charts and graphs",
                "Support `rx.svg` circle, polygon and rect components",
                "Bug fixes for background tasks, class_name prop, fully controlled inputs and more",
                "Progress on Var Operations refactor",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.8",
        ),
        change(
            "2024-07-16",
            "v0.5.7",
            "Specify frontend and backend exception handlers",
            [
                "Recharts improvements",
                "Fix for 404 error on dynamic route after hot reload",
                "Fix deprecation warnings",
                "Support mutation tracking for SQLAlchemy models",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.7",
        ),
        change(
            "2024-07-08",
            "v0.5.6",
            "Fix hot-reload issues on Windows",
            [
                "rx.clipboard component for handling on_paste event",
                "rx.breakpoints API for passing responsive CSS props",
                "Fix ComponentState with backend vars issue",
                "Fix sqlmodel metaclass conflict issue",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.5.6",
        ),
        change(
            "2024-06-24",
            "v0.5.5",
            "Support rx.SessionStorage as State Var",
            [
                "More Recharts improvements",
                "Better support for interactive stateless apps",
                "Fix websocket disconnect when navigating to another domain",
                "Make .web folder location configurable with `REFLEX_WEB_WORKDIR`",
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
                "Better customizability for `rx.accordion`",
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
                "Use Alembic batch mode for `db makemigrations`",
                "Experimental toast component in `rx._x.toast`",
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
                "`reflex run` will automatically init the app when required",
                "Reflex Experimental Namespace: `rx._x`",
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
                "Allow `rx.download` to resolve `rx.get_upload_url` links",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.5",
        ),
        change(
            "2024-03-11",
            "v0.4.4",
            "Fix missing on_load and /_upload in prod deployments",
            [
                "`rx.upload` exposes `on_drop` event trigger",
                "`rx.el.form` supports `on_submit` event trigger",
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
                "`app.compile()` is no longer required",
                "Add `time_picker` component",
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
                "`stop_propagation` and `prevent_default` for all events",
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
            "2023-09-08",
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
            "2023-08-14",
            "v0.2.6",
            "Bug fix to connect to no sql databases.",
            [
                "Added the step prop to Slider.",
                "Added support for limits in pagination",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.6",
        ),
        change(
            "2023-08-01",
            "v0.2.5",
            "Performance improvements + bug fixes.",
            [
                "Removing the Node dependency on Windows",
                "3x performance improvement on the frontend (dev mode should be much snappier now!)",
                "f-string support for vars",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.2.5",
        ),
        class_name="flex flex-col gap-6 w-full",
    )


@webpage(path="/changelog", title="Changelog · Reflex")
def changelog():
    return rx.el.section(
        rx.box(
            h1_title(title="Changelog"),
            rx.box(
                rx.el.h2(
                    "Reflex has new releases and features coming every week! Make sure to star and watch on ",
                    rx.link(
                        "GitHub",
                        underline="always",
                        href=constants.GITHUB_URL,
                        class_name="text-violet-9",
                    ),
                    " to stay up to date.",
                ),
                class_name="font-md text-balance text-slate-10",
            ),
            class_name="section-header",
        ),
        changelog_content(),
        id="changelog",
        class_name="section-content",
    )
