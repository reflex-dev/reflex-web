import reflex as rx
from pcweb.components.icons.patterns import get_icon


def pip_install_card() -> rx.Component:
    return rx.box(
        # Glow
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="320" height="120" viewBox="0 0 320 120" fill="none">
  <path d="M320 60C320 93.1371 248.366 120 160 120C71.6344 120 0 93.1371 0 60C0 26.8629 71.6344 0 160 0C248.366 0 320 26.8629 320 60Z" fill="url(#paint0_radial_10744_8990)"/>
  <defs>
    <radialGradient id="paint0_radial_10744_8990" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(160 60) rotate(90) scale(60 160)">
      <stop stop-color="var(--c-violet-3)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>""",
            class_name="w-[20rem] h-[7.5rem] shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-1]",
        ),
        # Pip install
        rx.el.button(
            get_icon("copy_pip", class_name="!text-violet-9"),
            rx.el.p(
                "$ pip install reflex",
                class_name="font-['JetBrains_Mono'] font-bold text-[0.8125rem] text-center text-slate-9 leading-5 tracking-[-0.01219rem]",
            ),
            on_click=rx.set_clipboard("pip install reflex"),
            class_name="flex flex-row items-center gap-1.5 px-1.5 py-1 rounded-lg cursor-pointer transition-bg border border-solid border-slate-4 bg-[rgba(249,249,251,0.48)] dark:bg-[rgba(26,27,29,0.48)] hover:bg-[rgba(249,249,251,0.48)] dark:hover:bg-[rgba(26,27,29,0.48)] backdrop-filter backdrop-blur-[6px]",
        ),
        class_name="flex h-full w-full justify-center items-center relative overflow-hidden row-span-2 lg:!border-r !border-slate-3 !border-t-0",
    )


def backend_card(
    title: str,
    description: str,
    icon: str,
    cols: str = "1",
    rows: str = "1",
    class_name: str = "",
) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                get_icon(icon, class_name="!text-slate-9"),
                rx.el.h3(title, class_name="font-base text-slate-9"),
                class_name="flex flex-row items-center gap-2",
            ),
            rx.el.p(description, class_name="font-md-smbold text-slate-11"),
            class_name="flex flex-col gap-[0.875rem]",
        ),
        class_name=f"col-span-{cols} h-[15rem] overflow-hidden p-8 w-full"
        + " "
        + class_name,
    )


def backend_grid() -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2(
                "Get server-side logic of your app.",
                class_name="font-x-large text-slate-12",
            ),
            rx.el.p(
                "Back-end is handled",
                class_name="font-x-large text-slate-9 z-[1]",
            ),
            class_name="lg:flex flex-col p-[5rem_6.5rem_5rem_2.5rem] text-nowrap hidden col-span-2 lg:border-l border-slate-3",
        ),
        pip_install_card(),
        backend_card(
            title="Integrated front and back-end",
            description="Skip the boilerplate and get started faster. No need to write API endpoints.",
            icon="backend_db",
        ),
        backend_card(
            title="Jobs and async events",
            description="Back-end jobs and asynchronous events...",
            icon="backend_async",
        ),
        backend_card(
            title="DB ORM",
            description="Integrate with existing databases with a single line of code. Or use our built in SQLite database.",
            icon="backend_db",
        ),
        backend_card(
            title="Compatible",
            description="Use any Python library with Reflex.",
            icon="backend_compatible",
        ),
        backend_card(
            title="Authorization",
            description="Temporary placeholder for authorization.",
            icon="backend_auth",
            class_name="lg:!border-r !border-slate-3",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-3 w-full lg:divide-y divide-slate-3 lg:divide-x",
    )


def backend_features() -> rx.Component:
    return rx.el.section(
        rx.box(
            backend_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col justify-center items-center",
    )
