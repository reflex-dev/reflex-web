import reflex as rx

from .forms.forms import form, form_code
from .image_gen.image_gen import image_gen, image_gen_code
from .charts.charts import charts, charts_code
from .chatbot.chatbot import chatbot, chatbot_code
from .react.react import react, react_code
from pcweb.components.icons.icons import get_icon


class DemoState(rx.State):
    demo = "Forms"

    @rx.event
    def set_demo(self, demo):
        self.demo = demo


def tab(name: str, icon: str) -> rx.Component:
    is_selected = DemoState.demo == name
    return rx.box(
        get_icon(icon, class_name="!text-slate-9 shrink-0"),
        name,
        class_name="box-border flex flex-row justify-center items-center gap-2 hover:bg-slate-3 px-3 py-2 h-full font-small text-slate-9 transition-bg cursor-pointer text-nowrap"
        + rx.cond(is_selected, " bg-slate-1 lg:shadow-large", ""),
        on_click=DemoState.set_demo(name),
    )


def code_block(code: str) -> rx.Component:
    return rx._x.code_block(
        code,
        language="python",
        class_name="demo-code-block !rounded-none !text-slate-12 no-scrollbar",
    )


def preview_block() -> rx.Component:
    return rx.box(
        rx.text("Preview"),
        class_name="flex justify-center items-center p-8 w-full h-full",
    )


def demo_section(color: str = "slate") -> rx.Component:
    return rx.box(
        # Tabs
        rx.box(
            tab("Forms", "send"),
            tab("Chatbot", "chat_bubble"),
            tab("Image Gen", "image_ai_small"),
            tab("Charts", "chart"),
            tab("Custom", "code_custom"),
            class_name="flex flex-row lg:items-center overflow-hidden border-slate-4 border-b lg:justify-center divide-x divide-slate-4 [&>:first-child]:border-l-slate-4 [&>:last-child]:!border-r-slate-4 lg:[&>:first-child]:!border-l lg:[&>:last-child]:!border-r flex-nowrap overflow-x-auto justify-start",
        ),
        # Previews
        rx.box(
            rx.box(
                rx.match(
                    DemoState.demo,
                    ("Forms", form(color)),
                    ("Chatbot", chatbot()),
                    ("Image Gen", image_gen()),
                    ("Charts", charts()),
                    ("Custom", react()),
                    image_gen(),
                ),
                class_name="border-slate-4 border-r w-full lg:w-1/2 h-auto",
            ),
            rx.scroll_area(
                rx.match(
                    DemoState.demo,
                    ("Forms", code_block(form_code)),
                    ("Chatbot", code_block(chatbot_code)),
                    ("Image Gen", code_block(image_gen_code)),
                    ("Charts", code_block(charts_code)),
                    ("Custom", code_block(react_code)),
                    image_gen(),
                ),
                # Bottom fade out
                rx.box(
                    class_name="absolute bottom-0 left-0 right-0 h-[5.25rem] pointer-events-none",
                    style={
                        "background": "linear-gradient(180deg, light-dark(rgba(249, 249, 251, 0.00), rgba(26, 27, 29, 0.00)) 0%, var(--c-slate-2) 79.62%)",
                    },
                ),
                # Right fade out
                rx.box(
                    class_name="absolute right-0 top-0 bottom-0 w-[5.25rem] pointer-events-none",
                    style={
                        "background": "linear-gradient(90deg, light-dark(rgba(249, 249, 251, 0.00), rgba(26, 27, 29, 0.00)) 0%, var(--c-slate-2) 79.62%)",
                    },
                ),
                class_name="desktop-only w-1/2 relative",
            ),
            class_name="flex flex-row w-full max-h-full h-[31rem] lg:h-[34rem] overflow-hidden",
        ),
        class_name="flex flex-col border-slate-3 bg-slate-2 lg:border lg:rounded-[1.125rem] w-[calc(100%+2rem)] -mx-4 h-full overflow-hidden shadow-large lg:w-full lg:-mx-0 max-w-[69.25rem]",
    )
