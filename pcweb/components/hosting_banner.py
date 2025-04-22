import reflex as rx

from pcweb.constants import REFLEX_AI_BUILDER


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
        rx.hstack(
            rx.link(
                rx.box(
                    rx.box(
                        rx.text(
                            "Reflex Build - ",
                            rx.el.span(
                                "Build internal apps with AI.",
                                # class_name="text-slate-12 font-medium text-sm",
                                class_name="hidden md:inline-block text-slate-12 font-medium text-sm",
                            ),
                            # ... keep this for mobile view if/when needed
                            rx.el.span(
                                "Build internal apps with AI.",
                                # class_name="text-slate-12 font-medium text-sm",
                                class_name="inline-block md:hidden text-slate-12 font-medium text-sm",
                            ),
                            class_name="text-slate-12 font-semibold text-sm z-[1]",
                        ),
                        # ... keep this for mobile view if/when needed
                        rx.el.button(
                            "Try for Free!",
                            class_name="hidden md:inline-block text-green-11 h-[1.5rem] rounded-md bg-green-4 px-1.5 text-sm font-semibold z-[1] items-center justify-center shrink-0",
                        ),
                        class_name="flex items-center gap-4",
                    ),
                ),
                glow(),
                href=REFLEX_AI_BUILDER,
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
