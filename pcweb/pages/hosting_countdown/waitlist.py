import reflex as rx


class WaitlistState(rx.State):
    loading = False
    success = False


def waitlist():
    return rx.box(
        rx.box(
            rx.el.h2(
                "Claim your spot!",
                class_name="lg:text-5xl text-3xl gradient-heading font-semibold leading-[3.5rem] mb-4",
            ),
            rx.text(
                """Deploy your app with a single command.
            Performant, secure, and scalable.""",
                class_name="text-slate-9 lg:text-lg text-base mb-8 whitespace-pre-line font-medium text-center",
            ),
            rx.form(
                rx.cond(
                    WaitlistState.success,
                    rx.badge(
                        "Thank you for joining the waitlist!",
                        color_scheme="green",
                        size="3",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.el.input(
                                placeholder="Email",
                                name="email",
                                type="email",
                                required=True,
                                class_name="box-border flex flex-row gap-2 border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] px-3.5 border rounded-[8px] h-[2rem] font-medium text-slate-12 placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 max-w-[17.4rem] text-base",
                            ),
                            rx.button(
                                "Join Waitlist",
                                background="linear-gradient(180deg, #6E56CF 0%, #654DC4 100%)",
                                _hover={
                                    "background": "linear-gradient(180deg, #6E56CF 0%, #6E56CF 100%)"
                                },
                                class_name="w-fit h-[2rem] px-3.5 rounded-[8px] cursor-pointer text-[#FCFCFD] font-medium text-base transition-bg",
                            ),
                            is_loading=WaitlistState.loading,
                        ),
                        rx.text(
                            "Join the waitlist to get access.",
                            class_name="text-slate-8 lg:text-md text-base mb-8 whitespace-pre-line font-medium text-center",
                        ),
                        align_items="center",
                    ),
                ),
                class_name="flex lg:flex-row flex-col gap-2 justify-center items-center",
            ),
            class_name="flex flex-col items-center max-w-[40rem]bg-slate-1 self-center w-full",
        ),
        class_name="flex flex-col items-center h-[20rem] bg-slate-1 self-center mt-2 z-10 py-20 lg:mb-[20rem] mb-[10rem] border-t border-slate-4 w-full",
    )
