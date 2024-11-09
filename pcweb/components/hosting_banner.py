import reflex as rx


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute w-[120rem] h-[23.75rem] flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[0] top-[-16rem]",
        background_image=rx.color_mode_cond(
            "radial-gradient(50% 50% at 50% 50%, rgba(235, 228, 255, 0.95) 0%, rgba(252, 252, 253, 0.00) 100%)",
            "radial-gradient(50% 50% at 50% 50%, rgba(58, 45, 118, 1) 0%, rgba(21, 22, 24, 0.00) 100%)",
        ),
    )


class HostingBannerState(rx.State):
    show_banner: bool = True

    def hide_banner(self):
        print("hide_banner")
        self.show_banner = False

def hosting_banner() -> rx.Component:
    return rx.cond(
        HostingBannerState.show_banner,
        rx.desktop_only(rx.box(
            rx.link(
                rx.box(
                    rx.text(""),
                    rx.text(
                        "Reflex Cloud - ",
                        rx.el.span(
                            "Fast, secure & scalable hosting. One command to deploy.",
                            class_name="text-slate-12 font-medium text-sm",
                        ),
                        class_name="text-slate-12 font-semibold text-sm z-[1]",
                    ),
                    rx.el.button(
                        "Launching Soon",
                        class_name="text-slate-11 h-[1.5rem] rounded-md bg-slate-4 px-1.5 text-sm font-semibold z-[1]",
                    ),
                    class_name="flex items-center gap-4",
                ),
                href="/hosting",
            ),
            rx.icon("x", on_click=HostingBannerState.hide_banner, size=16, color=rx.color("slate", 9), class_name="absolute right-4 z-[1]"),
            glow(),
            class_name="px-4 lg:px-6 w-screen h-auto lg:h-[40px] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex items-center justify-center bg-slate-1 flex-row gap-4 overflow-hidden relative lg:py-0 py-2 max-w-full",
        ))
    )
