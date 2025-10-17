import reflex as rx
import reflex_ui as ui

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
                    class_name="inset-0 size-full absolute z-[1] bg-[#00000008] backdrop-blur-[0.1px] rounded-lg",
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
                class_name="text-slate-10 text-3xl font-semibold",
            ),
            class_name="text-slate-12 text-3xl font-semibold max-w-[57rem]",
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
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="1319" height="561" viewBox="0 0 1319 561" fill="none">
          <g opacity="0.48" filter="url(#filter0_f_18083_222594)">
            <path d="M178.56 223.585C69.0001 74.636 -27.8842 31.9438 647.928 112.695C910.498 144.068 1430.13 -8.92554 1175 174.327C999.595 300.313 1180 239.557 1234 349.094C1255.21 392.116 1279 555.245 1022 458.015C962.219 435.399 591.448 442.522 392.794 475.504C194.14 508.487 103.578 462.994 75.3378 380.537C47.0978 298.08 254.184 326.398 178.56 223.585Z" stroke="#C2B5F5" stroke-width="16"/>
          </g>
          <defs>
            <filter id="filter0_f_18083_222594" x="0.671143" y="0.454102" width="1317.53" height="559.985" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
              <feFlood flood-opacity="0" result="BackgroundImageFix"/>
              <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
              <feGaussianBlur stdDeviation="32" result="effect1_foregroundBlur_18083_222594"/>
            </filter>
          </defs>
        </svg>""",
            class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-1 pointer-events-none dark:hidden block",
        ),
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="1298" height="560" viewBox="0 0 1298 560" fill="none">
  <g opacity="0.48" filter="url(#filter0_f_18310_74204)">
    <path d="M176.126 223.136C68.3898 74.182 -26.8819 31.4882 637.681 112.242C895.881 143.617 1406.87 -9.38262 1155.98 173.877C983.495 299.868 1160.9 239.109 1214 348.65C1234.85 391.673 1258.25 554.808 1005.53 457.575C946.741 434.958 582.142 442.081 386.794 475.065C191.447 508.049 102.392 462.554 74.622 380.094C46.8521 297.634 250.491 325.953 176.126 223.136Z" stroke="#2F265F" stroke-width="16"/>
  </g>
  <defs>
    <filter id="filter0_f_18310_74204" x="0" y="0" width="1298" height="560" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="32" result="effect1_foregroundBlur_18310_74204"/>
    </filter>
  </defs>
</svg>""",
            class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none hidden dark:block",
        ),
        rx.el.div(
            text(),
            video_demo(),
            class_name="grid grid-cols-1 lg:grid-cols-2 w-full rounded-2xl border border-slate-4 bg-white-1 z-5",
        ),
        class_name="mx-auto w-full max-w-[71.125rem] relative rounded-4xl border border-slate-4 backdrop-blur-[6px] bg-slate-2/48 p-4 flex z-1",
    )
