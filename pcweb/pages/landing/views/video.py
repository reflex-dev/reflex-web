import reflex as rx
import reflex_ui as ui

import reflex as rx

from pcweb.components.dialog import dialog
from pcweb.constants import DEMO_VIDEO_URL, REFLEX_BUILD_URL


def video_demo() -> rx.Component:
    return rx.el.div(
        dialog(
            trigger=rx.el.div(
                rx.el.div(
                    ui.icon("PlayIcon", class_name="text-slate-1 fill-slate-1 size-5"),
                    class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 scale-100 z-[2] group-hover:scale-110 transition-transform duration-300 backdrop rounded-full bg-slate-10 size-10 flex items-center justify-center",
                ),
                rx.image(
                    "/landing/video/dark/video_demo_dark.webp",
                    class_name="object-cover size-full dark:block hidden scale-110",
                ),
                rx.image(
                    "/landing/video/light/video_demo_light.webp",
                    class_name="object-cover size-full dark:hidden block scale-110",
                ),
                rx.el.span(
                    class_name="inset-0 size-full absolute z-[1] dark:bg-[#0000001f] backdrop-blur-[0.1px] rounded-lg",
                ),
                class_name="shadow-small aspect-video rounded-xl overflow-hidden cursor-pointer relative isolate group border border-slate-4",
            ),
            content=rx.el.div(
                rx.image(
                    "/logo.jpg",
                    class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 z-[-1] rounded-md",
                ),
                rx.video(
                    src=DEMO_VIDEO_URL,
                    playing=True,
                    controls=False,
                    class_name="size-full z-[1]",
                ),
                class_name="relative isolate aspect-video bg-slate-1 rounded-2xl overflow-hidden",
            ),
            class_name="!max-w-[70rem] !p-0 !bg-transparent overflow-hidden",
        ),
        class_name="p-10",
    )


def text() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Build With Reflex. ",
            rx.el.span(
                "A Single Platform to Build With AI And Iterate in Python",
                class_name="text-slate-10 text-2xl font-semibold",
            ),
            class_name="text-slate-12 text-2xl font-semibold max-w-[57rem]",
        ),
        ui.link(
            render_=ui.button(
                "Get Started with Reflex",
                size="lg",
                class_name="w-fit font-semibold mr-auto rounded-[0.625rem]",
            ),
            to=REFLEX_BUILD_URL,
            target="_blank",
        ),
        class_name="flex flex-col gap-6 items-start justify-center py-20 px-10",
    )


def video() -> rx.Component:
    return rx.el.section(
        text(),
        video_demo(),
        class_name="grid grid-cols-1 lg:grid-cols-2 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden lg:border-y",
    )
