import reflex as rx
from pcweb.components.button import button, icon_button


class FormState(rx.State):

    def submit(self, form_data):
        return rx.toast(form_data)


def form() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.image(
                    src="/logo.jpg",
                    loading="lazy",
                    class_name="rounded-[25%] w-9 h-auto",
                ),
                rx.el.h2(
                    "Create an account",
                    class_name="font-base font-semibold text-[1.5rem] text-center text-slate-12",
                ),
                class_name="flex flex-col items-center gap-4",
            ),
            rx.box(
                rx.text(
                    "Email address", class_name="font-medium font-small text-slate-11"
                ),
                rx.el.input(
                    placeholder="user@reflex.dev",
                    name="email",
                    type="email",
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 shadow-small p-[0.5rem_0.75rem] border rounded-[10px] w-full font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.box(
                rx.box(
                    rx.text(
                        "Password", class_name="font-medium font-small text-slate-11"
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        underline="none",
                        class_name="font-small text-violet-9",
                    ),
                    class_name="flex flex-row justify-between w-full",
                ),
                rx.el.input(
                    placeholder="Enter your password",
                    name="password",
                    type="password",
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 shadow-small p-[0.5rem_0.75rem] border rounded-[10px] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                ),
                class_name="flex flex-col gap-2",
            ),
            button("Sign In", type="submit", class_name="-mt-2"),
            rx.box(
                rx.divider(margin="0", class_name="bg-slate-4"),
                rx.text(
                    "OR CONTINUE WITH",
                    class_name="text-slate-9 font-small !text-xs whitespace-nowrap",
                ),
                rx.divider(margin="0", class_name="bg-slate-4"),
                class_name="flex flex-row gap-2 items-center",
            ),
            icon_button("GitHub", "github", variant="secondary"),
            on_submit=FormState.submit,
            class_name="flex flex-col gap-6 border-slate-5 bg-white-1 shadow-small p-8 border rounded-[1.125rem] w-full",
        ),
        class_name="flex items-center px-12 py-8 h-full overflow-hidden",
    )


form_code = """class FormState(rx.State):

    def submit(self, form_data):
        return rx.toast(form_data)

def form() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.image(
                    src="/logo.jpg",
                    class_name="image",
                ),
                rx.heading(
                    "Create an account",
                    class_name="heading",
                ),
                class_name="vstack",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    class_name="text",
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    name="email",
                    type="email",
                    class_name="input",
                ),
                class_name="vstack",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        class_name="text",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        class_name="link",
                    ),
                    class_name="hstack-password",
                ),
                rx.input(
                    placeholder="Enter your password",
                    name="password",
                    type="password",
                    class_name="input",
                ),
                class_name="vstack",
            ),
            rx.button("Sign In", type="submit", class_name="button"),
            rx.hstack(
                rx.divider(),
                rx.text(
                    "OR CONTINUE WITH",
                    class_name="text-small",
                ),
                rx.divider(),
                class_name="hstack",
            ),
            rx.button(
                rx.icon(tag="github"),
                "GitHub",
                class_name="button-secondary",
            ),
            class_name="form",
            on_submit=FormState.submit,
        ),
        class_name="card",
    )
"""
