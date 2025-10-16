import reflex as rx


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute w-[120rem] h-[23.75rem] flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[0] top-[-16rem] dark:[background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(58,45,118,1)_0%,_rgba(21,22,24,0.00)_100%)] [background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(235,228,255,0.95)_0%,_rgba(252,252,253,0.00)_100%)]",
    )


class HostingBannerState(rx.State):
    show_banner: bool = False

    def hide_banner(self):
        self.show_banner = False


def hosting_banner() -> rx.Component:
    return rx.cond(
        HostingBannerState.show_banner,
        rx.hstack(
            rx.link(
                rx.box(
                    rx.box(
                        # Header text with responsive spans
                        rx.el.span(
                            "New",
                            class_name="inline-flex items-center font-medium px-1.5 h-5 rounded-md text-xs bg-violet-9 text-slate-1 z-[1]",
                        ),
                        rx.text(
                            "Reflex Build – ",  # noqa: RUF001
                            # Descriptive text: hidden on small, inline on md+
                            rx.el.span(
                                "The first AI agent to build internal Python enterprise apps",
                                class_name="hidden md:inline-block text-slate-12 font-medium text-sm",
                            ),
                            # Mobile CTA: inline on small, hidden on md+
                            rx.el.span(
                                "Early Access",
                                class_name="inline-block md:hidden text-slate-12 font-medium text-sm",
                            ),
                            class_name="text-slate-12 font-semibold text-sm z-[1]",
                        ),
                        # Standalone CTA button: hidden on small, inline on md+
                        rx.el.button(
                            "Get Access",
                            class_name=(
                                "hidden md:inline-block "
                                "text-green-11 h-[1.65rem] rounded-md bg-green-4 "
                                "px-1.5 text-sm font-semibold z-[1] items-center "
                                "justify-center shrink-0 border border-green-5 hover:bg-green-5 transition-colors"
                            ),
                        ),
                        class_name="flex items-center gap-4",
                    )
                ),
                glow(),
                href="https://build.reflex.dev/",
                underline="none",
                is_external=True,
            ),
            rx.icon(
                "x",
                on_click=HostingBannerState.hide_banner,
                size=16,
                class_name="cursor-pointer hover:!text-slate-11 transition-color !text-slate-9 absolute right-4 z-10",
            ),
            class_name="px-4 lg:px-6 w-screen h-auto lg:h-[3.5rem] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex items-center justify-between md:justify-center bg-slate-1 flex-row gap-4 overflow-hidden relative lg:py-0 py-2 max-w-full",
        ),
    )
