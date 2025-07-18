import reflex as rx

from pcweb.components.new_button import button


def start_building() -> rx.Component:
    return rx.el.section(
        # Glowing
        rx.box(
            class_name="top-[-4.25rem] z-[-1] blur-[28px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[64.25rem] h-[13rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
        ),
        rx.box(
            class_name="bottom-[-16.5rem] z-[-1] blur-[28px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[64.25rem] h-[13rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
        ),
        # Headings
        rx.el.h2(
            "Ready to get started?",
            class_name="text-slate-12 text-2xl lg:text-4xl font-semibold text-center",
        ),
        rx.el.h3(
            "Start building with Reflex",
            class_name="text-slate-9 text-2xl lg:text-4xl font-semibold text-center",
        ),
        rx.link(
            button(
                "Contact sales",
                size="xl",
            ),
            underline="none",
            href="/pricing",
            class_name="mt-6",
        ),
        class_name="flex flex-col justify-center items-center lg:mx-auto md:w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[6.31rem] border-t border-slate-3 py-[6rem] relative z-[1] overflow-hidden isolate w-screen -mx-4",
    )
