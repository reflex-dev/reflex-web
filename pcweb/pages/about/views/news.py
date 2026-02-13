import reflex as rx
import reflex_ui as ui

from pcweb.components.marketing_button import button
from pcweb.pages.blog import blogs
from pcweb.pages.blog.paths import blog_data


def news_item(title: str, date: str, description: str, url: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.moment(
                rx.Var.create(date).to(str),
                format="MMM DD YYYY",
                class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[415] font-mono uppercase",
            ),
            rx.image(
                src=f"/common/{rx.color_mode_cond('light', 'dark')}/squares_rectangle_xs.svg",
                class_name="pointer-events-none",
                alt="Squares Rectangle XS",
                loading="lazy",
            ),
            class_name="flex flex-row items-center lg:gap-6 gap-4 mb-6",
        ),
        rx.el.p(
            title,
            class_name="text-m-slate-12 dark:text-m-slate-3 text-2xl leading-9 font-semibold mb-4",
        ),
        rx.el.p(
            description,
            class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475] mb-6",
        ),
        rx.el.a(
            button(
                "Read More",
                ui.icon(
                    "ArrowRight01Icon",
                ),
                variant="ghost",
                size="xs",
                class_name="font-[525] w-fit text-m-slate-12 dark:text-m-slate-3 px-0",
            ),
            to=f"/blog/{url}",
            class_name="mt-auto w-fit",
        ),
        class_name="flex flex-col relative",
    )


def news() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                ui.icon(
                    "NotificationSquareIcon",
                    class_name="text-primary-10 dark:text-m-slate-6",
                ),
                rx.el.h2(
                    "What's New In Reflex",
                    class_name="text-primary-10 dark:text-m-slate-6 text-sm font-medium",
                ),
                class_name="flex flex-row items-center gap-2",
            ),
            rx.el.a(
                button(
                    "Browse All",
                    variant="outline",
                    size="sm",
                    class_name="w-fit",
                ),
                to=blogs.path,
            ),
            class_name="flex flex-row justify-between items-center",
        ),
        rx.el.div(
            *[
                news_item(
                    blog.metadata["title"],
                    blog.metadata["date"],
                    blog.metadata["description"],
                    path,
                )
                for path, blog in list(blog_data.items())[:3]
            ],
            class_name="grid lg:grid-cols-3 grid-cols-1 gap-12",
        ),
        class_name="flex flex-col gap-12 w-[69rem] max-w-[calc(100vw-3rem)] mx-auto lg:p-12 p-6 rounded-xl bg-m-slate-1 dark:bg-m-slate-11 backdrop-blur-[16px] shadow-[0_0_0_1px_rgba(0,0,0,0.04),0_12px_24px_0_rgba(0,0,0,0.08),0_1px_1px_0_rgba(0,0,0,0.01),0_4px_8px_0_rgba(0,0,0,0.03),0_0_0_1px_#FFF_inset] dark:shadow-none dark:border-t dark:border-m-slate-9 lg:mb-36 mb-24 lg:mt-24 mt-10",
    )
