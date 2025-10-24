import datetime

import reflex as rx


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute w-[120rem] h-[23.75rem] flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[0] top-[-16rem] dark:[background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(58,45,118,1)_0%,_rgba(21,22,24,0.00)_100%)] [background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(235,228,255,0.95)_0%,_rgba(252,252,253,0.00)_100%)] saturate-200 dark:saturate-100 group-hover:saturate-300 transition-[saturate] dark:group-hover:saturate-100",
    )


POST_LINK = "https://www.producthunt.com/products/reflex-5?launch=reflex-7"

# October 25, 2025 12:01 AM PDT (UTC-7) = October 25, 2025 07:01 AM UTC
DEADLINE = datetime.datetime(2025, 10, 25, 7, 1, tzinfo=datetime.UTC)


class HostingBannerState(rx.State):
    show_banner: rx.Field[bool] = rx.field(False)
    force_hide_banner: rx.Field[bool] = rx.field(False)

    @rx.event
    def hide_banner(self):
        self.force_hide_banner = True

    @rx.event
    def check_deadline(self):
        if datetime.datetime.now(datetime.UTC) < DEADLINE:
            self.show_banner = True

    @rx.var
    def is_banner_visible(self) -> bool:
        return self.show_banner and not self.force_hide_banner


def timer():
    remove_negative_sign = rx.vars.function.ArgsFunctionOperation.create(
        args_names=("t",),
        return_expr=rx.vars.sequence.string_replace_operation(
            rx.Var("t").to(str), "-", ""
        ),
    )

    return rx.el.div(
        rx.moment(
            date=DEADLINE,
            duration_from_now=True,
            format="DD[d] HH[h] mm[m] ss[s]",
            custom_attrs={"filter": remove_negative_sign},
            interval=1000,
            class_name="font-medium text-sm",
        ),
        class_name="items-center gap-1 z-[1] bg-orange-4 border border-orange-5 rounded-md px-1.5 py-0.5 text-orange-11 font-medium text-sm md:flex hidden",
    )


def hosting_banner() -> rx.Component:
    return rx.el.div(
        rx.cond(
            HostingBannerState.is_banner_visible,
            rx.hstack(
                rx.el.a(
                    rx.box(
                        rx.box(
                            # Header text with responsive spans
                            rx.el.span(
                                "Launch",
                                class_name="items-center font-medium px-1.5 h-5 rounded-md text-xs bg-violet-9 text-slate-1 z-[1] inline-flex",
                            ),
                            rx.text(
                                rx.el.span(
                                    "We're live on Product Hunt - ",
                                    class_name="inline-block text-slate-12 font-semibold text-sm",
                                ),
                                # Mobile CTA: inline on small, hidden on md+
                                rx.el.span(
                                    " 50% ",
                                    class_name="text-slate-12 font-semibold text-sm underline decoration-slate-11",
                                ),
                                rx.el.span(
                                    " launch",
                                    class_name="text-slate-12 font-semibold text-sm underline decoration-slate-11 hidden md:inline-block",
                                ),
                                rx.el.span(
                                    " discount!",
                                    class_name="text-slate-12 font-semibold text-sm underline decoration-slate-11",
                                ),
                                class_name="text-slate-12 font-semibold text-sm z-[1]",
                            ),
                            # Standalone CTA button: hidden on small, inline on md+
                            timer(),
                            class_name="flex items-center md:gap-3.5 gap-2",
                        )
                    ),
                    glow(),
                    to=POST_LINK,
                    target="_blank",
                ),
                rx.icon(
                    "x",
                    on_click=HostingBannerState.hide_banner,
                    size=16,
                    class_name="cursor-pointer hover:!text-slate-11 transition-color !text-slate-9 absolute right-4 z-10",
                ),
                class_name="px-4 lg:px-6 w-screen h-[2rem] lg:h-[3.5rem] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex items-center justify-between md:justify-center bg-slate-1 flex-row gap-4 overflow-hidden relative lg:py-0 py-2 max-w-full group",
            ),
        ),
        on_mount=HostingBannerState.check_deadline,
    )
