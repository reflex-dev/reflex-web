import reflex as rx
from pcweb.pages.index.components.stat import stat


def frontend_card(
    title: str,
    description: str,
    image: str,
    height: str = "auto",
    top: str = "5rem",
    cols: str = "1",
) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2(title, class_name="font-large text-slate-12 z-[1]"),
            rx.el.p(description, class_name="font-base text-slate-9 z-[1]"),
            class_name="flex flex-col gap-2 px-10 pt-10",
        ),
        rx.image(
            src=rx.color_mode_cond(
                light=f"/landing/frontend_features/light/{image}",
                dark=f"/landing/frontend_features/dark/{image}",
            ),
            class_name="w-full absolute shrink-0",
            top=top,
            height=height,
            loading="lazy",
        ),
        class_name=f"col-span-{cols} h-96 rounded-[1.125rem] bg-slate-2 border border-slate-3 overflow-hidden relative shadow-large max-h-full pointer-events-none",
    )


def frontend_grid() -> rx.Component:
    return rx.box(
        frontend_card(
            title="60+ built-in components",
            description="Exensible by design. Wrap and use any React component",
            image="components.svg",
            cols="2",
            height="17.5rem",
            top="6.5rem",
        ),
        frontend_card(
            title="Theming system",
            description="Give your app a unified look and feel",
            image="colors.svg",
            height="15rem",
            top="9rem",
        ),
        frontend_card(
            title="Customizable UI",
            description="Tweak and style components to your liking",
            image="ui.svg",
            height="17.5rem",
            top="6.5rem",
        ),
        frontend_card(
            title="Turn off the lights",
            description="Toggle between light and dark mode",
            image="dark_light_mode.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card( 
            title="Fully responsive",
            description="Your app looks good on every device",
            image="responsive.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card(
            title="Reusable components",
            description="Keep your code clean as your app grows",
            image="reusable.svg",
            cols="2",
            height="20rem",
            top="4rem",
        ),
        class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 grid-rows-2 max-w-[84.5rem]",
    )


def frontend_features() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Build your entire app in Python",
                    class_name="font-x-large text-slate-12",
                ),
                rx.el.p(
                    "Turn your ideas into apps lightning fast",
                    class_name="font-x-large text-slate-9 z-[1]",
                ),
                class_name="lg:flex flex-col lg:border-r border-slate-3 p-[5rem_6.5rem_5rem_2.5rem] text-nowrap hidden",
            ),
            rx.box(
                stat(stat="100K+", text="Apps built with Reflex"),
                class_name="px-10 py-[5.5rem] w-auto",
            ),
            class_name="flex flex-row lg:border-t border-slate-3 max-w-[64.19rem] justify-center lg:border-x w-full",
        ),
        frontend_grid(),
        class_name="flex flex-col justify-center items-center",
    )
