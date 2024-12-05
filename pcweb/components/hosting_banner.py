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
        self.show_banner = False


def hosting_banner() -> rx.Component:
    return rx.cond(
        HostingBannerState.show_banner,
        rx.box(
            rx.link(
                rx.box(
                    rx.text(
                        "Reflex Cloud - ",
                        rx.el.span(
                            "Fast, secure & scalable hosting. One command to deploy.",
                            class_name="text-slate-12 font-medium text-sm",
                        ),
                        class_name="text-slate-12 font-semibold text-sm z-[1]",
                    ),
                    rx.el.button(
                        "Live on Product Hunt Now! 🚀",
                        class_name="text-orange-11 h-[1.5rem] rounded-md bg-orange-4 px-1.5 text-sm font-semibold z-[1] items-center justify-center shrink-0",
                    ),
                    class_name="flex items-center gap-4",
                ),
                href="https://www.producthunt.com/posts/reflex-cloud",
                underline="none",
                class_name="mr-7 lg:mr-0",
            ),
            rx.icon(
                "x",
                on_click=HostingBannerState.hide_banner,
                size=16,
                class_name="z-[1] cursor-pointer hover:!text-slate-11 transition-color !text-slate-9 absolute right-4",
            ),
            glow(),
            class_name="px-4 lg:px-6 w-screen h-auto lg:h-[3.5rem] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex items-center justify-center bg-slate-1 flex-row gap-4 overflow-hidden relative lg:py-0 py-2 max-w-full",
        ),
    )
