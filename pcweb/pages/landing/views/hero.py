import reflex as rx
from reflex.experimental import ClientStateVar

from pcweb.components.new_button import button

from .video_demo import video_demo, watch_preview

textarea_x_pos = ClientStateVar.create(var_name="textarea_x_pos", default=0)
textarea_y_pos = ClientStateVar.create(var_name="textarea_y_pos", default=0)
textarea_opacity = ClientStateVar.create(var_name="textarea_opacity", default=0)


def hero_box() -> rx.Component:
    return rx.box(
        video_demo(),
        rx.box(
            aria_hidden=True,
            style={
                "border": "1.5px solid var(--c-violet-6)",
                "opacity": textarea_opacity.value,
                "WebkitMaskImage": f"radial-gradient(45% 40px at {textarea_x_pos.value}px {textarea_y_pos.value}px, black 45%, transparent)",
            },
            class_name="pointer-events-none absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-10 h-[calc(100%+2px)] w-[calc(100%+2px)] rounded-[1.5rem] border bg-[transparent] opacity-0 transition-opacity duration-500 bg-clip-padding",
        ),
        on_mouse_enter=textarea_opacity.set_value(1),
        on_mouse_leave=textarea_opacity.set_value(0),
        on_mouse_move=[
            rx.call_function(
                textarea_x_pos.set_value(
                    rx.Var(
                        "event.clientX - document.getElementById('landing-input-box').getBoundingClientRect().left"
                    )
                )
            ),
            rx.call_function(
                textarea_y_pos.set_value(
                    rx.Var(
                        "event.clientY - document.getElementById('landing-input-box').getBoundingClientRect().top"
                    )
                )
            ),
        ],
        id="landing-input-box",
        class_name="bg-clip-border border max-w-[42rem] rounded-[1.5rem] p-4 flex flex-col gap-4 w-full mt-[2rem] bg-[linear-gradient(180deg,_rgba(252,_252,_253,_0.82)_0%,_rgba(252,_252,_253,_0.80)_88%)] border-[rgba(190,_190,_210,_0.40)] dark:bg-[linear-gradient(180deg,_rgba(21,_22,_24,_0.82)_0%,_rgba(21,_22,_24,_0.80)_88%)] dark:border-[rgba(255,_255,_255,_0.06)] backdrop-blur-[6px] z-[1]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        # Dark Waves
        rx.image(
            src="/landing/patterns/dark/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:right-0 right-[-150px] z-[-1] pointer-events-none hidden dark:lg:block w-[514px] lg:h-[406px] h-[506px] dark:block",
        ),
        rx.image(
            src="/landing/patterns/dark/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:left-0 left-[-150px] z-[-1] pointer-events-none hidden dark:lg:block scale-x-[-1] w-[514px] lg:h-[406px] h-[506px] dark:block",
        ),
        # Light Waves
        rx.image(
            src="/landing/patterns/light/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:right-0 right-[-150px] z-[-1] pointer-events-none hidden lg:block w-[514px] lg:h-[406px] h-[506px] dark:hidden dark:lg:hidden",
        ),
        rx.image(
            src="/landing/patterns/light/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:left-0 left-[-150px] z-[-1] pointer-events-none hidden lg:block scale-x-[-1] w-[514px] lg:h-[406px] h-[506px] dark:hidden dark:lg:hidden",
        ),
        # Triangle
        rx.box(
            rx.image(
                src="/landing/patterns/dark/triangle.webp",
                class_name="size-full bg-transparent",
            ),
            class_name="absolute top-[232px] left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover z-[1] pointer-events-none w-[31rem] h-[20.875rem] hidden lg:block bg-transparent mix-blend-overlay",
        ),
        # Small gradient
        # rx.box(
        #     class_name="z-[-1] blur-[16px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[37rem] lg:h-[9.5rem] h-[6.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 lg:top-[21.5rem] top-[25.5rem] saturate-[1.25] lg:-mx-0 -mx-8 opacity-80 md:opacity-100 max-lg:opacity-50"
        # ),
        # Big gradient
        rx.box(
            class_name="z-[-1] blur-[28px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_#D4CAFE_0%,_rgba(21,_22,_24,_0)_100%)] dark:bg-[radial-gradient(50%_50%_at_50%_50%,_#4329AC_0%,_rgba(21,_22,_24,_0)_100%)] w-[40rem] lg:h-[10.25rem] h-[18.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-[28.25rem] saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100 max-lg:hidden"
        ),
        # New Ellipse gradient
        rx.box(
            class_name="absolute w-[1076px] h-[676px] lg:top-[-369px] top-[-26rem] bg-[radial-gradient(37.87%_37.87%_at_50%_50%,_#F4F0FE_0%,_rgba(21,_22,_24,_0)_100%)] dark:bg-[radial-gradient(37.87%_37.87%_at_50%_50%,_#261958_0%,_rgba(21,_22,_24,_0)_100%)] z-[-1] pointer-events-none saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100"
        ),
        # Headings
        rx.el.h1(
            "Prompt to production app, in seconds",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-5xl lg:text-6xl font-semibold text-center text-transparent text-balance mx-auto break-words z-[1]",
        ),
        rx.el.h2(
            "A unified platform to build and deploy all in Python.",
            class_name="max-w-full w-full text-lg lg:text-xl text-center text-slate-9 font-medium mx-auto text-balance word-wrap break-words md:whitespace-pre z-[1]",
        ),
        rx.box(
            rx.link(
                button(
                    "Get Access",
                    size="xl",
                    class_name="w-fit flex flex-row-reverse gap-2",
                    icon=rx.icon("chevron-right", size=16),
                ),
                underline="none",
                href="/pricing",
            ),
            watch_preview(),
            class_name="flex flex-row gap-4 items-center z-[10] mt-2",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[6.31rem] pt-28 lg:pt-[10rem] relative lg:overflow-hidden overflow-visible z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
