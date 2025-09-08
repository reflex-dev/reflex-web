import reflex as rx

from pcweb.components.dialog import dialog
from pcweb.components.icons.icons import get_icon
from pcweb.components.new_button import button
from pcweb.constants import DEMO_VIDEO_URL


def video_demo() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.span(
                "Get one month free",
                class_name="rounded-full border border-slate-6 text-slate-11 text-xs px-2 py-0.5 w-fit font-medium -mb-1.5",
            ),
            rx.el.span(
                rx.el.span(
                    "Reflex Build ",
                    class_name="inline text-slate-12 font-semibold text-2xl",
                ),
                rx.el.span(
                    "The first AI agent to build internal Python enterprise apps.",
                    class_name="inline text-slate-9 font-medium text-xl",
                ),
                class_name="flex flex-col gap-1.5",
            ),
            rx.link(
                button("Get Access", size="lg", class_name="w-fit"),
                href="/pricing",
            ),
            class_name="flex flex-col gap-4 max-lg:items-center max-lg:justify-center max-lg:text-center",
        ),
        dialog(
            trigger=rx.box(
                get_icon(
                    "play_video",
                    class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 scale-110 z-[2] group-hover:scale-125 transition-transform duration-300 backdrop",
                ),
                rx.image(
                    "/landing/video/dark/video_placeholder.webp",
                    class_name="object-cover size-full dark:block hidden scale-110",
                ),
                rx.image(
                    "/landing/video/light/video_placeholder.webp",
                    class_name="object-cover size-full dark:hidden block scale-110",
                ),
                rx.el.span(
                    class_name="inset-0 size-full absolute z-[1] bg-[#0000001f] backdrop-blur-[1.5px] rounded-lg",
                ),
                class_name="aspect-video rounded-lg overflow-hidden cursor-pointer relative isolate group border border-slate-4",
            ),
            content=rx.box(
                rx.image(
                    "/logo.jpg",
                    class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 z-[-1] rounded-md",
                ),
                rx.video(
                    url=DEMO_VIDEO_URL,
                    playing=True,
                    controls=False,
                    class_name="size-full z-[1]",
                ),
                class_name="relative isolate aspect-video bg-slate-1 rounded-2xl overflow-hidden",
            ),
            class_name="!max-w-[70rem] !p-0 !bg-transparent overflow-hidden",
        ),
        class_name="h-full overflow-hidden grid grid-cols-1 lg:grid-cols-2 gap-12 relative isolate items-center",
    )


def watch_preview() -> rx.Component:
    return dialog(
        trigger=button(
            "Watch Preview",
            variant="secondary",
            size="xl",
            class_name="w-fit flex flex-row-reverse gap-2 mt-10 -mb-10",
            icon=rx.icon("chevron-right", size=16),
        ),
        content=rx.box(
            rx.image(
                "/logo.jpg",
                class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 z-[-1] rounded-md",
            ),
            rx.video(
                url=DEMO_VIDEO_URL,
                playing=True,
                controls=False,
                class_name="size-full z-[1]",
            ),
            class_name="relative isolate aspect-video bg-slate-1 rounded-2xl overflow-hidden",
        ),
        class_name="!max-w-[70rem] !p-0 !bg-transparent overflow-hidden",
    )
