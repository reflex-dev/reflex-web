import reflex as rx

from pcweb.components.dialog import dialog
from pcweb.components.icons.icons import get_icon
from pcweb.components.new_button import button
from pcweb.constants import DEMO_VIDEO_URL


def icon_svg() -> rx.Component:
    return rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 16 16" fill="none">
            <rect width="16" height="16" rx="2" fill="#6E56CF"/>
            <path d="M10 9V13H12V9H10Z" fill="white"/>
            <path d="M4 3V13H6V9H10V7H6V5H10V7H12V3H4Z" fill="white"/>
        </svg>""",
        class_name="flex justify-center items-center",
    )


def video_demo() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.span(
                rx.box(
                    icon_svg(),
                    rx.el.span(
                        "Reflex Build ",
                        class_name="inline text-slate-12 font-semibold text-2xl",
                    ),
                    class_name="flex flex-row items-center gap-x-2 justify-center lg:justify-start",
                ),
                rx.el.span(
                    "The first AI agent to build internal Python enterprise apps.",
                    class_name="inline text-secondary-11 font-medium text-xl",
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
                    "/landing/video/dark/video_demo_dark.webp",
                    loading="lazy",
                    class_name="object-cover size-full dark:block hidden scale-110",
                ),
                rx.image(
                    "/landing/video/light/video_demo_light.webp",
                    loading="lazy",
                    class_name="object-cover size-full dark:hidden block scale-110",
                ),
                rx.el.span(
                    class_name="inset-0 size-full absolute z-[1] dark:bg-[#0000001f] backdrop-blur-[0.1px] rounded-lg",
                ),
                class_name="aspect-video rounded-lg overflow-hidden cursor-pointer relative isolate group border border-slate-4",
            ),
            content=rx.box(
                rx.image(
                    "/logo.jpg",
                    loading="lazy",
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
        class_name="h-full overflow-hidden grid grid-cols-1 lg:grid-cols-2 gap-12 relative isolate items-center md:px-8 py-4 mt-10 scale-90",
    )


def watch_preview() -> rx.Component:
    return video_demo()
