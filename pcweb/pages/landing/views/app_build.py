import reflex as rx
import reflex_ui as ui
from pcweb.components.icons.icons import get_icon
from pcweb.components.progressive_blur import progressive_blur


# Animation delays (in ms)
DELAY_USER_PROFILE = 250
DURATION_USER_PROFILE = 900
DELAY_OKTA = 1050
DURATION_OKTA = 300
DELAY_DIVIDER = 1200
DURATION_DIVIDER = 200
DELAY_GRAPH_OVERVIEW = 1350
DURATION_GRAPH_OVERVIEW = 700
DELAY_GRAPH_Y_AXIS = 1550
DURATION_GRAPH_Y_AXIS = 700
DELAY_DATABRICKS = 2100
DURATION_DATABRICKS = 300
DELAY_GRAPH_BARS = 1950
DURATION_GRAPH_BARS = 300
DELAY_METRICS_HEADER = 2250
DURATION_METRICS_HEADER = 800
DELAY_METRICS_BADGE = 2500
DURATION_METRICS_BADGE = 700
DELAY_METRICS_TABS = 2350
DURATION_METRICS_TABS = 700
DELAY_METRICS_CONTENT = 2450
DURATION_METRICS_CONTENT = 600
DELAY_SLACK = 3050
DURATION_SLACK = 300


def integration_card(icon: str, class_name: str = ""):
    return rx.el.div(
        rx.image(
            src=f"/landing/integrations/light/{icon}.svg",
            class_name="size-7 pointer-events-none shrink-0",
        ),
        class_name=ui.cn(
            "z-100 flex justify-center items-center size-12 bg-white-1/88 backdrop-blur-[6px] border border-slate-6 shadow-large",
            class_name,
        ),
    )


def okta_card():
    return integration_card(
        "okta",
        class_name=f"rounded-t-[14px] rounded-bl-[14px] rounded-br-[4px] absolute top-2 left-2 animate-scale-rotate-in animate-duration-{DURATION_OKTA} animate-ease-out animate-delay-{DELAY_OKTA}",
    )


def databricks_card():
    return integration_card(
        "databricks",
        class_name=f"rounded-t-[14px] rounded-br-[14px] rounded-bl-[4px] absolute top-[5.25rem] right-[11rem] animate-scale-rotate-in animate-duration-{DURATION_DATABRICKS} animate-ease-out animate-delay-{DELAY_DATABRICKS}",
    )


def user_profile():
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="/landing/app_build/user.webp",
                class_name="object-cover pointer-events-none",
            ),
            class_name="size-10 bg-violet-5 rounded-full border border-violet-7 overflow-hidden",
        ),
        rx.el.span(
            "Amelia Wong",
            class_name="text-slate-12 text-sm font-semibold",
        ),
        get_icon("arrow-fill-down", class_name="size-4 text-slate-9 -ml-2"),
        class_name=f"flex flex-row items-center gap-4 animate-slide-in-left animate-duration-{DURATION_USER_PROFILE} animate-ease-out animate-delay-{DELAY_USER_PROFILE}",
    )


def slack_alert():
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"/landing/integrations/light/slack.svg",
                class_name="size-full pointer-events-none shrink-0 object-cover",
            ),
            class_name="size-9 bg-white-1 rounded-[8px] border-[0.5px] border-slate-6 overflow-hidden flex justify-center items-center p-1 shadow-small shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                "New message from Reflex",
                class_name="text-slate-12 text-sm font-semibold",
            ),
            rx.el.p(
                "Metrics reached critical level of 93%",
                rx.el.br(),
                "Please, check it.",
                class_name="text-slate-11 text-xs font-medium word-wrap",
            ),
            class_name="flex flex-col",
        ),
        rx.el.span(
            "now",
            class_name="absolute top-3 right-2 text-xs text-slate-7 font-medium",
        ),
        class_name=f"flex flex-row items-center gap-3.5 border border-slate-6 h-[72px] w-[326px] rounded-[14px] px-3 shadow-large absolute top-2 right-2 z-[10] bg-white/88 backdrop-blur-[6px] animate-scale-in-top-right animate-duration-{DURATION_SLACK} animate-ease-out animate-delay-{DELAY_SLACK}",
    )


def metrics_tabs():
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                "All",
                class_name="text-slate-10 text-xs font-medium size-full text-center bg-slate-2 overflow-hidden flex items-center justify-center",
            ),
            rx.el.span(
                "Critical",
                class_name="text-slate-10 text-xs font-medium size-full text-center overflow-hidden flex items-center justify-center",
            ),
            rx.el.span(
                "Normal",
                class_name="text-slate-10 text-xs font-medium size-full text-center overflow-hidden flex items-center justify-center",
            ),
            class_name="flex flex-row items-center w-[246px] h-[32px] rounded-[8px] bg-white-1 border border-slate-4 divide-x divide-slate-4 overflow-hidden",
        ),
        class_name=f"w-full h-[32px] animate-slide-in-right animate-duration-{DURATION_METRICS_TABS} animate-ease-out animate-delay-{DELAY_METRICS_TABS} pl-6",
    )


def metrics_header():
    return rx.el.div(
        rx.el.div(
            rx.html(
                """<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M64 32C64 49.6731 49.6731 64 32 64C14.3269 64 0 49.6731 0 32C0 14.3269 14.3269 0 32 0C49.6731 0 64 14.3269 64 32ZM5.36 32C5.36 46.7129 17.2871 58.64 32 58.64C46.7129 58.64 58.64 46.7129 58.64 32C58.64 17.2871 46.7129 5.36 32 5.36C17.2871 5.36 5.36 17.2871 5.36 32Z" fill="#E8E8EC"/>
<g clip-path="url(#paint0_angular_17892_9711_clip_path)" data-figma-skip-parse="true"><g transform="matrix(0 -0.032 -0.032 0 32 32)"><foreignObject x="-1031.25" y="-1031.25" width="2062.5" height="2062.5"><div xmlns="http://www.w3.org/1999/xhtml" style="background:conic-gradient(from 90deg,rgba(220, 62, 66, 1) 0deg,rgba(229, 72, 77, 1) 90deg,rgba(170, 153, 236, 1) 180deg,rgba(170, 153, 236, 1) 360deg);height:100%;width:100%;opacity:1"></div></foreignObject></g></g><path d="M32 2.68C32 1.19988 33.2021 -0.0116695 34.6771 0.112117C41.629 0.695569 48.2278 3.53931 53.4426 8.24679C59.3229 13.5551 63.0253 20.8559 63.8332 28.7366C64.6411 36.6172 62.4971 44.5173 57.8161 50.9084C53.1352 57.2994 46.25 61.727 38.4929 63.3344C30.7357 64.9417 22.6581 63.6146 15.823 59.6099C8.98791 55.6051 3.88125 49.2073 1.49116 41.6546C-0.898926 34.1018 -0.402527 25.931 2.88431 18.7231C5.79911 12.3311 10.7246 7.09933 16.8723 3.80148C18.1766 3.1018 19.7612 3.73591 20.3493 5.09416C20.9375 6.45241 20.3047 8.0187 19.0124 8.74026C14.078 11.4954 10.1252 15.7628 7.76119 20.947C5.0249 26.9475 4.61164 33.7498 6.60139 40.0374C8.59114 46.3251 12.8424 51.6512 18.5326 54.9852C24.2229 58.3192 30.9475 59.424 37.4053 58.0859C43.8631 56.7477 49.595 53.0618 53.4919 47.7412C57.3888 42.4207 59.1737 35.8438 58.5011 29.2832C57.8285 22.7226 54.7463 16.6446 49.851 12.2255C45.6216 8.4075 40.2986 6.06215 34.6756 5.49465C33.203 5.34602 32 4.16012 32 2.68Z" data-figma-gradient-fill="{&#34;type&#34;:&#34;GRADIENT_ANGULAR&#34;,&#34;stops&#34;:[{&#34;color&#34;:{&#34;r&#34;:0.86274510622024536,&#34;g&#34;:0.24313725531101227,&#34;b&#34;:0.25882354378700256,&#34;a&#34;:1.0},&#34;position&#34;:0.0},{&#34;color&#34;:{&#34;r&#34;:0.89803922176361084,&#34;g&#34;:0.28235295414924622,&#34;b&#34;:0.30196079611778259,&#34;a&#34;:1.0},&#34;position&#34;:0.250},{&#34;color&#34;:{&#34;r&#34;:0.66666668653488159,&#34;g&#34;:0.60000002384185791,&#34;b&#34;:0.92549020051956177,&#34;a&#34;:1.0},&#34;position&#34;:0.50},{&#34;color&#34;:{&#34;r&#34;:0.66666668653488159,&#34;g&#34;:0.60000002384185791,&#34;b&#34;:0.92549020051956177,&#34;a&#34;:1.0},&#34;position&#34;:1.0}],&#34;stopsVar&#34;:[{&#34;color&#34;:{&#34;r&#34;:0.86274510622024536,&#34;g&#34;:0.24313725531101227,&#34;b&#34;:0.25882354378700256,&#34;a&#34;:1.0},&#34;position&#34;:0.0},{&#34;color&#34;:{&#34;r&#34;:0.89803922176361084,&#34;g&#34;:0.28235295414924622,&#34;b&#34;:0.30196079611778259,&#34;a&#34;:1.0},&#34;position&#34;:0.250},{&#34;color&#34;:{&#34;r&#34;:0.66666668653488159,&#34;g&#34;:0.60000002384185791,&#34;b&#34;:0.92549020051956177,&#34;a&#34;:1.0},&#34;position&#34;:0.50},{&#34;color&#34;:{&#34;r&#34;:0.66666668653488159,&#34;g&#34;:0.60000002384185791,&#34;b&#34;:0.92549020051956177,&#34;a&#34;:1.0},&#34;position&#34;:1.0}],&#34;transform&#34;:{&#34;m00&#34;:2.4542457774173396e-15,&#34;m01&#34;:-64.0,&#34;m02&#34;:64.0,&#34;m10&#34;:-64.0,&#34;m11&#34;:-1.6665100492619343e-14,&#34;m12&#34;:64.0},&#34;opacity&#34;:1.0,&#34;blendMode&#34;:&#34;NORMAL&#34;,&#34;visible&#34;:true}"/>
<defs>
<clipPath id="paint0_angular_17892_9711_clip_path"><path d="M32 2.68C32 1.19988 33.2021 -0.0116695 34.6771 0.112117C41.629 0.695569 48.2278 3.53931 53.4426 8.24679C59.3229 13.5551 63.0253 20.8559 63.8332 28.7366C64.6411 36.6172 62.4971 44.5173 57.8161 50.9084C53.1352 57.2994 46.25 61.727 38.4929 63.3344C30.7357 64.9417 22.6581 63.6146 15.823 59.6099C8.98791 55.6051 3.88125 49.2073 1.49116 41.6546C-0.898926 34.1018 -0.402527 25.931 2.88431 18.7231C5.79911 12.3311 10.7246 7.09933 16.8723 3.80148C18.1766 3.1018 19.7612 3.73591 20.3493 5.09416C20.9375 6.45241 20.3047 8.0187 19.0124 8.74026C14.078 11.4954 10.1252 15.7628 7.76119 20.947C5.0249 26.9475 4.61164 33.7498 6.60139 40.0374C8.59114 46.3251 12.8424 51.6512 18.5326 54.9852C24.2229 58.3192 30.9475 59.424 37.4053 58.0859C43.8631 56.7477 49.595 53.0618 53.4919 47.7412C57.3888 42.4207 59.1737 35.8438 58.5011 29.2832C57.8285 22.7226 54.7463 16.6446 49.851 12.2255C45.6216 8.4075 40.2986 6.06215 34.6756 5.49465C33.203 5.34602 32 4.16012 32 2.68Z"/></clipPath></defs>
</svg>
"""
            ),
            # Text
            rx.el.div(
                "93%",
                class_name="absolute size-16 left-0 top-0 flex items-center justify-center text-center text-red-10 text-base font-[565] leading-[21px] font-mono z-10",
            ),
            class_name="relative size-16 flex-none",
        ),
        rx.el.div(
            rx.el.span(
                "Metrics",
                class_name="text-slate-12 text-lg font-semibold",
            ),
            rx.el.div(
                get_icon("alert"),
                "Critical Level",
                class_name=f"text-red-10 bg-red-2 border-red-6 border flex flex-row items-center gap-1.5 text-xs font-medium rounded-md px-1.5 h-[24px] animate-delay-{DELAY_METRICS_BADGE} animate-duration-{DURATION_METRICS_BADGE} animate-slide-in-right animate-ease-out",
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name=f"flex flex-row gap-6 w-full justify-start relative animate-slide-in-right animate-duration-{DURATION_METRICS_HEADER} animate-ease-out animate-delay-{DELAY_METRICS_HEADER} pl-6",
    )


def metrics_content():
    def metrics_row(name: str, value: str, time: str):
        return rx.el.div(
            rx.el.span(name, class_name="text-slate-9 text-sm font-medium w-[72px]"),
            rx.el.span(value, class_name="text-slate-9 text-sm font-medium w-[46px]"),
            rx.el.span(
                time, class_name="text-slate-9 text-sm font-medium text-end ml-auto"
            ),
            class_name="flex flex-row items-center h-[48px] px-6 py-4 gap-4",
        )

    return rx.el.div(
        metrics_row("Critical", "93%", "Now"),
        metrics_row("Normal", "32%", "12:42"),
        metrics_row("Critical", "89%", "09:41"),
        metrics_row("Normal", "34%", "08:14"),
        metrics_row("Normal", "12%", "05:36"),
        class_name=f"flex flex-col w-[294px] divide-y divide-slate-4 border-t border-slate-3 animate-slide-in-up animate-delay-{DELAY_METRICS_CONTENT} animate-ease-out animate-duration-{DURATION_METRICS_CONTENT}",
    )


def metrics_card():
    return rx.el.div(
        rx.el.div(
            progressive_blur(
                steps=16,
                strength=6,
                side="right",
                fall_of_percentage=100,
                class_name="w-[1.45rem] inset-y-0 absolute right-0 z-50 pointer-events-none",
            ),
            metrics_header(),
            metrics_tabs(),
            class_name="flex flex-col gap-6 relative items-center w-full justify-start",
        ),
        metrics_content(),
        class_name="flex flex-col gap-6 justify-start items-center min-w-[18.375rem] pt-6 overflow-hidden",
    )


def graph_y_axis():
    return rx.el.div(
        *[
            rx.el.div(
                rx.el.span(
                    f"{i}",
                    class_name="text-slate-9 text-xs font-medium",
                ),
                rx.el.div(
                    class_name="h-[0.5px] bg-slate-3 w-[524px] absolute left-10 top-1/2 -translate-y-1/2",
                ),
                class_name="relative",
            )
            for i in [64, 48, 32, 24, 16, 8, 4]
        ],
        class_name=f"flex flex-col items-end gap-7 w-4 pt-9 animate-slide-in-up animate-duration-{DURATION_GRAPH_Y_AXIS} animate-ease-out animate-delay-{DELAY_GRAPH_Y_AXIS}",
    )


def stacked_bar_chart(primary_height: int = 8, secondary_height: int = 16):
    return rx.el.div(
        rx.el.div(
            height=f"{primary_height}rem",
            class_name="w-4 rounded-t-sm bg-violet-8 absolute bottom-0 left-0 z-20",
        ),
        rx.el.div(
            height=f"{secondary_height}rem",
            class_name="w-4 rounded-t-sm bg-violet-3 absolute bottom-0 left-0 z-10",
        ),
        class_name="relative h-full w-4",
    )


def graph_chart():
    return rx.el.div(
        graph_y_axis(),
        rx.el.div(
            stacked_bar_chart(primary_height=8.4375, secondary_height=16),
            stacked_bar_chart(primary_height=13.25, secondary_height=16),
            stacked_bar_chart(primary_height=14.75, secondary_height=16),
            stacked_bar_chart(primary_height=11.25, secondary_height=15.0625),
            stacked_bar_chart(primary_height=12.9375, secondary_height=16),
            stacked_bar_chart(primary_height=14.375, secondary_height=16),
            stacked_bar_chart(primary_height=8.625, secondary_height=12.3125),
            stacked_bar_chart(primary_height=10.75, secondary_height=13.3125),
            stacked_bar_chart(primary_height=7.3125, secondary_height=12.3125),
            stacked_bar_chart(primary_height=13.25, secondary_height=16),
            stacked_bar_chart(primary_height=9.875, secondary_height=15.0625),
            stacked_bar_chart(primary_height=6.75, secondary_height=16),
            class_name=f"flex flex-row justify-between w-full animate-slide-in-up animate-duration-{DURATION_GRAPH_BARS} animate-ease-out animate-delay-{DELAY_GRAPH_BARS}",
        ),
        class_name="flex flex-row gap-6 w-full px-8 pt-8 border border-slate-4 rounded-t-lg overflow-hidden h-[408px]",
    )


def graph_overview():
    return rx.el.div(
        databricks_card(),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Overview",
                    class_name="text-slate-12 text-2xl font-semibold",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(class_name="size-4 rounded-sm bg-violet-8"),
                        "Peak Performance",
                        class_name="flex flex-row items-center gap-2 text-xs font-medium text-slate-10",
                    ),
                    rx.el.div(
                        rx.el.span(class_name="size-4 rounded-sm bg-violet-4"),
                        "Capacity Per Day",
                        class_name="flex flex-row items-center gap-2 text-xs font-medium text-slate-10",
                    ),
                    class_name="flex flex-row items-center gap-4",
                ),
                class_name="flex flex-col gap-6",
            ),
            rx.el.div(
                "24 June ",
                rx.el.span(" - ", class_name="text-slate-8 ml-0.5"),
                " Today",
                class_name="text-slate-10 text-sm font-medium rounded-lg px-3.5 h-8 border border-slate-4 bg-white-1 flex items-center",
            ),
            class_name="flex flex-row justify-between items-baseline w-full",
        ),
        graph_chart(),
        class_name=f"flex flex-col gap-6 size-full border-r border-slate-4 px-6 pt-6 animate-slide-in-up animate-duration-{DURATION_GRAPH_OVERVIEW} animate-ease-out animate-delay-{DELAY_GRAPH_OVERVIEW} h-[408px] relative",
    )


def app_build():
    return rx.el.section(
        slack_alert(),
        okta_card(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="w-[0.95rem] inset-y-0 absolute left-0 z-50 pointer-events-none backdrop-blur-[1px]",
                    ),
                    user_profile(),
                    class_name="h-[4.5rem] shrink-0 w-full",
                ),
                class_name="w-full h-[4.5rem] shrink-0 relative p-4 overflow-hidden rounded-t-[32px]",
            ),
            rx.el.div(
                height="0.5px",
                class_name=f"w-full bg-slate-4 animate-fade animate-duration-{DURATION_DIVIDER} animate-ease-out animate-delay-{DELAY_DIVIDER} shrink-0",
            ),
            rx.el.div(
                graph_overview(),
                metrics_card(),
                class_name="flex flex-row size-full",
            ),
            progressive_blur(
                steps=16,
                strength=6,
                side="bottom",
                fall_of_percentage=100,
                class_name="h-[9rem] inset-x-0 absolute bottom-0 z-50 pointer-events-none -mb-1",
            ),
            class_name="border-t border-x border-slate-4 rounded-t-[32px] bg-white-1 relative size-full shadow-[0px_2px_16px_0px_rgba(28,32,36,0.04)] flex flex-col",
        ),
        class_name="flex flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t px-6 pt-6 h-[504px]",
    )
