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
        class_name=f"col-span-{cols} h-96 rounded-[1.125rem] bg-slate-2 border-t border-slate-3 overflow-hidden relative",
    )


def frontend_grid() -> rx.Component:
    return rx.box(
        frontend_card(
            title="Ship with 60+ components",
            description="Build your project faster with Reflex UI library.",
            image="components.svg",
            cols="2",
            height="17.5rem",
            top="6.5rem",
        ),
        frontend_card(
            title="Get right colors",
            description="Design with built-in themes.",
            image="colors.svg",
            height="15rem",
            top="9rem",
        ),
        frontend_card(
            title="Customize UI",
            description="Style components with props.",
            image="ui.svg",
            height="17.5rem",
            top="6.5rem",
        ),
        frontend_card(
            title="Turn on the lights",
            description="Auto dark/light mode included.",
            image="dark_light_mode.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card(
            title="Adapt with ease",
            description="Enjoy responsive components.",
            image="responsive.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card(
            title="Ship with 60+ components",
            description="Build your project faster with Reflex UI library.",
            image="components.svg",
            cols="2",
            height="17.5rem",
            top="6.5rem",
        ),
        class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 grid-rows-2 max-w-[84.5rem]",
    )


def frontend_features() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Save time on the front-end.",
                    class_name="font-x-large text-slate-12",
                ),
                rx.el.p(
                    "Turn your ideas into apps lightning fast",
                    class_name="font-x-large text-slate-9 z-[1]",
                ),
                class_name="lg:flex flex-col border-r border-slate-3 p-[6rem_6.5rem_6rem_2.5rem] text-nowrap hidden",
            ),
            rx.box(
                stat(stat="100K+", text="Apps built with Reflex"),
                class_name="px-10 py-24",
            ),
            class_name="flex flex-row lg:border-t border-slate-3 max-w-[64.19rem] justify-center lg:border-x",
        ),
        frontend_grid(),
        class_name="flex flex-col justify-center items-center",
    )
