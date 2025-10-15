import reflex as rx

from pcweb.components.button import button
from pcweb.constants import GITHUB_URL
from pcweb.signup import IndexState


def os_card() -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2("Open source", class_name="font-large text-slate-12"),
            rx.el.p(
                """Apache 2.0 license--view the source code,
contribute, self-host, and more""",
                class_name="font-base text-slate-9 whitespace-pre",
            ),
            class_name="flex flex-col gap-2",
        ),
        rx.link(
            # Glow
            rx.html(
                """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="89" viewBox="0 0 300 89" fill="none"><path d="M300 44.5C300 69.077 232.978 89 150 89S0 69.077 0 44.5 67.022 0 150 0s150 19.923 150 44.5" fill="url(#a)"/><defs><radialGradient id="a" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="scale(150 44.5)rotate(90 0 1)"><stop stop-color="var(--c-violet-3)"/><stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/></radialGradient></defs></svg>""",
                class_name="lg:flex hidden shrink-0 absolute w-[18.75rem] h-[5.5625rem] -translate-y-1/2 left-[-3.5rem] top-1/2",
            ),
            button(
                "Contribute on GitHub",
                variant="muted",
                class_name="self-start shrink-0 w-full lg:w-auto lg:max-w-full max-w-[24rem]",
            ),
            href=GITHUB_URL,
            class_name="relative w-full lg:w-auto",
        ),
        class_name="lg:!border-b-0 flex flex-col gap-8 w-full p-10 pb-12 lg:!border-l !border-slate-3 items-center lg:items-start text-center lg:text-start",
    )


def newletter_input() -> rx.Component:
    return rx.box(
        rx.cond(
            IndexState.signed_up,
            rx.box(
                rx.box(
                    rx.icon(
                        tag="circle-check",
                        size=16,
                        class_name="!text-violet-9",
                    ),
                    rx.text(
                        "Thanks for subscribing!",
                        class_name="font-base text-slate-11",
                    ),
                    class_name="flex flex-row items-center gap-2",
                ),
                button(
                    "Sign up for another email",
                    variant="muted",
                    on_click=IndexState.signup_for_another_user,
                ),
                class_name="flex flex-col flex-wrap gap-2",
            ),
            rx.form(
                # Glow
                rx.box(
                    # Glow
                    rx.html(
                        """<svg xmlns="http://www.w3.org/2000/svg" width="403" height="89" viewBox="0 0 403 89" fill="none">
  <path d="M0 44.5C0 69.0767 90.2146 89 201.5 89C312.785 89 403 69.0767 403 44.5C403 19.9233 312.785 0 201.5 0C90.2146 0 0 19.9233 0 44.5Z" fill="url(#paint0_radial_10744_8734)"/>
  <defs>
    <radialGradient id="paint0_radial_10744_8734" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(201.5 44.5) rotate(90) scale(44.5 201.5)">
      <stop stop-color="var(--c-violet-3)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>""",
                        class_name="lg:flex hidden shrink-0 absolute -translate-y-1/2 left-[-2.5rem] top-1/2 h-[5.5625rem] w-[25.1875rem] z-[-1]",
                    ),
                    rx.el.input(
                        placeholder="Your email",
                        name="input_email",
                        type="email",
                        class_name="relative box-border border-slate-4 focus:border-violet-9 focus:border-1 bg-slate-2 p-[0.5rem_0.75rem] border rounded-xl font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full max-w-[24rem]",
                    ),
                    class_name="relative w-full flex items-center justify-center lg:justify-start",
                ),
                rx.box(
                    # Glow
                    rx.html(
                        """<svg xmlns="http://www.w3.org/2000/svg" width="183" height="89" viewBox="0 0 183 89" fill="none">
  <path d="M183 44.5C183 69.0767 142.034 89 91.5 89C40.9659 89 0 69.0767 0 44.5C0 19.9233 40.9659 0 91.5 0C142.034 0 183 19.9233 183 44.5Z" fill="url(#paint0_radial_10744_8733)"/>
  <defs>
    <radialGradient id="paint0_radial_10744_8733" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(91.5 44.5) rotate(90) scale(44.5 91.5)">
      <stop stop-color="var(--c-violet-3)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>""",
                        class_name="lg:flex hidden shrink-0 absolute w-[11.4375rem] h-[5.5625rem] -translate-y-1/2 right-[-2.5rem] top-1/2 z-[-1]",
                    ),
                    button(
                        "Subscribe",
                        type="submit",
                        variant="muted",
                        class_name="w-full lg:w-auto lg:max-w-full max-w-[24rem]",
                    ),
                    class_name="relative",
                ),
                class_name="flex flex-col lg:flex-row gap-2 align-center",
                on_submit=IndexState.signup,
            ),
        ),
        class_name="w-full lg:w-auto",
    )


def newsletter_card() -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2("Newsletter", class_name="font-large text-slate-12"),
            rx.el.p(
                """Stay up to date with the latest Reflex news
and updates""",
                class_name="font-medium text-slate-9 whitespace-pre",
            ),
            class_name="flex flex-col gap-2",
        ),
        newletter_input(),
        id="newsletter",
        class_name="flex flex-col gap-8 w-full p-10 pb-12 lg:!border-r !border-slate-3 items-center lg:items-start text-center lg:text-start scroll-mt-72",
    )


def os_newsletter_grid() -> rx.Component:
    return rx.box(
        os_card(),
        newsletter_card(),
        class_name="grid grid-cols-1 lg:grid-cols-2 gap-0 grid-rows-1 w-full lg:divide-y divide-slate-3 lg:divide-x",
    )


def os_newsletter() -> rx.Component:
    return rx.el.section(
        rx.box(
            os_newsletter_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col justify-center items-center w-full border-y border-slate-3 lg:border-y-0",
    )
