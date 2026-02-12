import reflex as rx
import reflex_ui as ui

from pcweb.components.hosting_banner import HostingBannerState


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.p("About Reflex", class_name="text-sm font-[525] text-primary-10"),
            rx.el.h1(
                "The Operating System ",
                rx.el.br(class_name="max-lg:hidden"),
                " for Most Critical ",
                rx.el.br(class_name="max-lg:hidden"),
                " Enterprise ",
                rx.el.br(class_name="max-lg:hidden"),
                " Applications ",
                class_name="text-secondary-12 lg:text-5xl text-3xl font-[575]",
            ),
            rx.el.div(
                class_name="absolute -bottom-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-secondary-4"
            ),
            class_name="flex flex-col gap-6 border-b border-secondary-4 max-lg:pb-10 xl:pr-16 max-lg:text-center relative",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Right now, the ",
                    rx.el.b(
                        "enterprise stack is fragmented and requires multiple tools and roles to ship an app. ",
                        class_name="font-semibold text-secondary-12",
                    ),
                    "Teams face organizational bottlenecks at every turn—waiting on infrastructure, coordinating between specialists, juggling disconnected platforms. ",
                    rx.el.b(
                        " This slows everything down ",
                        class_name="font-semibold text-secondary-12",
                    ),
                    " and makes building production apps unnecessarily complex.",
                ),
                rx.el.p(
                    rx.el.b(
                        "Reflex is the operating system on which enterprises build mission-critical applications. ",
                        class_name="font-semibold text-secondary-12",
                    ),
                    "We're the only platform that owns the underlying framework and handles the full lifecycle of your app. Our platform lets teams connect securely with company data, use AI to build standardized apps powered by our open source framework, and deploy with a single click to share with their company.",
                ),
                rx.el.p(
                    "We're empowering teams to finish the whole production app themselves, without needing to get multiple roles and tools involved. We do this by building solid reusable abstractions at both the framework and infrastructure level. Reflex replaces the fragmented stack, letting teams build, deploy, and manage their apps in a unified platform.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="/about/alek.avif",
                            alt="Alek",
                            custom_attrs={"fetchPriority": "high"},
                            class_name="size-8 rounded-full pointer-events-none",
                        ),
                        rx.image(
                            src="/about/nikhil.avif",
                            alt="Nikhil",
                            custom_attrs={"fetchPriority": "high"},
                            class_name="size-8 rounded-full pointer-events-none",
                        ),
                        class_name="flex flex-row items-center -space-x-1",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Alek Petuskey & Nikhil Rao",
                            class_name="text-sm font-semibold text-secondary-12",
                        ),
                        rx.el.span(
                            "Founders",
                            class_name="text-sm font-[475] text-secondary-11",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex flex-row gap-4",
                ),
                class_name="flex flex-col gap-4 text-base text-secondary-11 font-[475]",
            ),
            rx.el.div(
                class_name="absolute -top-24 -right-px w-px h-24 bg-gradient-to-b from-transparent to-current text-secondary-4"
            ),
            rx.el.div(
                class_name="absolute -top-24 -left-px w-px h-24 bg-gradient-to-b from-transparent to-current text-secondary-4"
            ),
            rx.el.div(
                class_name="absolute -bottom-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-secondary-4"
            ),
            class_name="flex flex-col gap-8 lg:p-12 p-6 border border-secondary-4 shadow-[0_6px_16px_0_rgba(0,0,0,0.04)_inset] lg:max-w-[34.5rem] w-full relative",
        ),
        class_name=ui.cn(
            "flex lg:flex-row flex-col max-w-(--layout-max-width) mx-auto lg:px-24 px-6 overflow-hidden",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "lg:pt-[14.5rem] pt-[12.5rem]",
                "lg:pt-[10.5rem] pt-[7.5rem]",
            ),
        ),
    )
