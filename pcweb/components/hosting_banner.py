import reflex as rx


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute w-[120rem] h-[23.75rem] flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[0] top-[-16rem]",
        background_image=rx.color_mode_cond(
            "radial-gradient(50% 50% at 50% 50%, rgba(235, 228, 255, 0.80) 0%, rgba(252, 252, 253, 0.00) 100%)",
            "radial-gradient(50% 50% at 50% 50%, rgba(38, 25, 88, 1) 0%, rgba(21, 22, 24, 0.00) 100%)",
        ),
    )


def hosting_banner() -> rx.Component:
    return rx.box(
        rx.text(
            "Meet Hosting. ",
            rx.el.span(
                "Deploy your app with a single command. Performant, secure, and scalable.",
                class_name="text-slate-12 font-medium text-sm",
            ),
            class_name="text-slate-12 font-semibold text-sm z-[1]",
        ),
        rx.link(
            rx.el.button(
                "Learn More",
                class_name="text-slate-12 h-[1.75rem] rounded-md bg-slate-4 px-1.5 text-sm font-semibold",
            ),
            href="/hosting",
            class_name="z-[1] shrink-0",
        ),
        glow(),
        class_name="px-4 lg:px-6 w-screen h-auto lg:h-[65px] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex items-center justify-center bg-slate-1 flex-row gap-4 overflow-hidden relative lg:py-0 py-2 max-w-full",
    )
