import datetime

import reflex as rx


def glow() -> rx.Component:
    return rx.box(
        class_name="absolute w-[120rem] h-[23.75rem] flex-shrink-0 rounded-[120rem] left-1/2 -translate-x-1/2 z-[0] top-[-16rem] dark:[background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(58,45,118,1)_0%,_rgba(21,22,24,0.00)_100%)] [background-image:radial-gradient(50%_50%_at_50%_50%,_rgba(235,228,255,0.95)_0%,_rgba(252,252,253,0.00)_100%)] saturate-200 dark:saturate-100 group-hover:saturate-300 transition-[saturate] dark:group-hover:saturate-100",
    )


POST_LINK = "https://www.producthunt.com/products/reflex-5?launch=reflex-7"
BLOG_LINK = "/blog/2025-12-05-on-premises-deployment/"

# October 25, 2025 12:01 AM PDT (UTC-7) = October 25, 2025 07:01 AM UTC
DEADLINE = datetime.datetime(2025, 10, 25, 7, 1, tzinfo=datetime.UTC)


class HostingBannerState(rx.State):
    show_banner: rx.Field[bool] = rx.field(True)
    force_hide_banner: rx.Field[bool] = rx.field(False)

    @rx.event
    def hide_banner(self):
        self.force_hide_banner = True

    @rx.event
    def check_deadline(self):
        if datetime.datetime.now(datetime.UTC) < DEADLINE:
            self.show_banner = True

    @rx.event
    def show_blog_banner(self):
        """Show the on-premises blog banner."""
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
            rx.el.div(
                rx.el.a(
                    rx.box(
                        rx.box(
                            # Header text with responsive spans
                            rx.el.span(
                                "New",
                                class_name="items-center font-medium px-1.5 h-5 rounded-md text-xs bg-violet-9 text-slate-1 z-[1] max-lg:hidden lg:inline-flex",
                            ),
                            rx.text(
                                rx.el.span(
                                    "Reflex Build On-Prem - A secure builder running in your environment. ",
                                    rx.el.span(
                                        "Learn more",
                                        class_name="text-slate-11 font-semibold text-sm underline decoration-slate-11 lg:pl-2",
                                    ),
                                    class_name="inline-block text-slate-12 font-semibold text-sm",
                                ),
                                class_name="text-slate-12 font-semibold text-sm z-[1]",
                            ),
                            class_name="flex items-center md:gap-3.5 gap-2",
                        )
                    ),
                    glow(),
                    to=BLOG_LINK,
                    is_external=False,
                    class_name="flex justify-start md:justify-center md:col-start-2",
                ),
                rx.el.button(
                    rx.icon(
                        "x",
                        size=16,
                    ),
                    class_name="cursor-pointer hover:!text-slate-11 transition-color !text-slate-9 z-10 size-8 flex items-center justify-center shrink-0 md:col-start-3 justify-self-end ml-auto",
                    on_click=HostingBannerState.hide_banner,
                ),
                class_name="px-6 lg:px-6 w-screen min-h-[3rem] lg:h-[3.5rem] shadow-[inset_0_-1px_0_0_var(--c-slate-3)] flex md:grid md:grid-cols-[1fr_auto_1fr] items-center bg-slate-1 gap-4 overflow-hidden relative lg:py-0 py-3 max-w-full group",
            ),
        ),
        on_mount=HostingBannerState.show_blog_banner,
    )
