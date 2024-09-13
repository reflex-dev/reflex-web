import reflex as rx
from pcweb.components.icons.patterns import get_icon
from pcweb.components.button import button
from pcweb.pages.docs import hosting


def graphic_card() -> rx.Component:
    return rx.box(
        # Glow
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="342" height="322" viewBox="0 0 342 322" fill="none">
  <g filter="url(#filter0_f_10744_8736)">
    <path d="M229.949 96.5486C278.245 98.9569 202.581 123.44 198.154 159.563C193.726 195.686 216.25 229 176.018 229C135.785 229 165.151 137.087 98.7436 118.222C32.3361 99.3581 181.652 94.1404 229.949 96.5486Z" fill="var(--c-violet-3)"/>
  </g>
  <defs>
    <filter id="filter0_f_10744_8736" x="-14" y="0" width="356" height="325" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="48" result="effect1_foregroundBlur_10744_8736"/>
    </filter>
  </defs>
</svg>""",
            class_name="w-auto h-auto -rotate-90 shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-1]",
        ),
        rx.image(
            src=rx.color_mode_cond(
                light="/landing/hosting_features/light/deploy.svg",
                dark="/landing/hosting_features/dark/deploy.svg",
            ),
            alt="Hosting graphic",
            loading="lazy",
            class_name="w-[7.875rem] h-[8.5rem] shrink-0",
        ),
        class_name="flex justify-center items-center relative overflow-hidden pointer-events-none lg:!border-l !border-slate-3 lg:!border-t h-full w-full",
    )


def reflex_deploy_card() -> rx.Component:
    return rx.box(
        # Pip install
        rx.el.button(
            get_icon("copy_pip", class_name="!text-violet-9"),
            rx.el.p(
                "$ reflex deploy",
                class_name="font-['JetBrains_Mono'] font-bold text-[0.8125rem] text-center text-slate-9 leading-5 tracking-[-0.01219rem]",
            ),
            on_click=rx.set_clipboard("reflex deploy"),
            class_name="flex flex-row items-center gap-1.5 px-1.5 py-1 rounded-lg cursor-pointer transition-bg border border-solid border-slate-4 bg-[rgba(249,249,251,0.48)] dark:bg-[rgba(26,27,29,0.48)] hover:bg-[rgba(249,249,251,0.48)] dark:hover:bg-[rgba(26,27,29,0.48)] backdrop-filter backdrop-blur-[6px]",
        ),
        class_name="flex h-full w-full justify-end items-end relative overflow-hidden row-span-2",
    )

def hosting_grid() -> rx.Component:
    return rx.box(
        graphic_card(),
        rx.box(
            rx.box(
                rx.el.h3(
                    "Deploy your app with a single command.",
                    class_name="font-x-large text-slate-12 text-right",
                ),
                rx.el.p(
                    "Performant, secure, and scalable",
                    class_name="font-x-large text-slate-9 text-right",
                ),
                class_name="flex flex-col items-end",
            ),
            reflex_deploy_card(),
            class_name="lg:flex flex-col p-[5rem_2.5rem_5rem_6.5rem] text-nowrap hidden col-span-2 gap-6 lg:!border-r !border-slate-3 items-end",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full lg:divide-y divide-slate-3 lg:divide-x",
    )

def hosting_features() -> rx.Component:
    return rx.el.section(
        rx.box(
            hosting_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col justify-center items-center w-full",
    )
