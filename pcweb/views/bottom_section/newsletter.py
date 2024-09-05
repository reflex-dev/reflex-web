import reflex as rx
from pcweb.components.button import button
from pcweb.signup import IndexState


def newsletter() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Join our newsletter",
                class_name="gradient-heading font-x-large",
            ),
            rx.el.h3(
                "Get the latest updates and news about Reflex.",
                class_name="font-base text-slate-9",
            ),
            class_name="flex flex-col gap-4 text-center self-stretch",
        ),
        rx.cond(
            IndexState.signed_up,
            rx.box(
                rx.box(
                    rx.icon(
                        tag="circle-check",
                        size=16,
                        class_name="!text-violet-9",
                    ),
                    rx.text(
                        "Thanks for subscribing!",
                        class_name="font-smbold text-slate-11",
                    ),
                    class_name="flex flex-row items-center gap-2",
                ),
                button(
                    "Sign up for another email",
                    variant="secondary",
                    on_click=IndexState.signup_for_another_user,
                ),
                class_name="flex flex-col flex-wrap gap-2",
            ),
            rx.form(
                rx.box(
                    rx.el.input(
                        placeholder="Your email",
                        name="input_email",
                        type="email",
                        class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 p-[0.5rem_0.75rem] border rounded-[10px] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                    ),
                    rx.form.submit(
                        rx.el.button(
                            "Subscribe",
                            class_name="flex justify-center items-center bg-slate-4 hover:bg-slate-5 p-[0.5rem_0.875rem] rounded-[10px] font-smbold text-slate-9 transition-bg cursor-pointer",
                        ),
                        as_child=True,
                    ),
                    class_name="flex flex-row gap-2 border-slate-4 bg-slate-2 shadow-large p-4 border rounded-[1.125rem] align-center",
                ),
                on_submit=IndexState.signup,
            ),
        ),
        id="newsletter",
        class_name="flex flex-col justify-center items-center gap-10 pb-2 w-[25rem]",
    )
