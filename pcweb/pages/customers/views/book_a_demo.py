import reflex as rx
from reflex_ui.blocks.demo_form import demo_form


def book_a_demo() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Contact Us",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-primary-9",
                ),
                rx.el.h1(
                    "Book a demo",
                    class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-5xl text-3xl font-[575]",
                ),
                rx.el.h2(
                    "Book a demo to see how you can build powerful Python web apps for your team with Reflex AI.",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
                ),
                class_name="flex flex-col gap-6 lg:max-w-[21rem] lg:self-start max-lg:self-center max-lg:items-center max-lg:text-center",
            ),
            rx.el.div(
                demo_form(),
                class_name="relative bg-white/96 dark:bg-m-slate-11 rounded-xl dark:border dark:border-m-slate-9 shadow-[0_0_0_1px_rgba(0,_0,_0,_0.12)_inset,_0_12px_24px_0_rgba(0,0,0,0.08),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_8px_0_rgba(0,_0,_0,_0.03),_0_0_0_1px_#FFF_inset] dark:shadow-none w-full lg:mx-0 overflow-hidden xl:ml-12 mx-auto max-w-[42rem]",
            ),
            class_name="flex lg:flex-row lg:justify-between gap-12 flex-col max-lg:gap-6 max-w-(--docs-layout-max-width) mx-auto relative pb-24 max-xl:px-6",
        ),
        class_name="w-full relative lg:mt-24 mt-12",
    )
