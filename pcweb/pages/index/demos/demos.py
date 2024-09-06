import reflex as rx

from .forms.forms import form, form_code
from pcweb.pages.gallery import gallery
from .image_gen.image_gen import image_gen, image_gen_code
from .charts.charts import charts, charts_code

# from .auth.auth import auth, auth_code
from .react.react import react, react_code


class DemoState(rx.State):

    demo = "Image Gen"

    def set_demo(self, demo):
        self.demo = demo


def tab(name: str, icon: str) -> rx.Component:
    is_selected = DemoState.demo == name
    return rx.box(
        rx.icon(tag=icon, size=16),
        name,
        class_name="box-border flex flex-row justify-center items-center gap-2 hover:bg-slate-3 px-3 py-0.5 rounded-[0.625rem] h-8 font-small text-slate-9 transition-bg cursor-pointer"
        + rx.cond(is_selected, " border border-slate-5 bg-slate-1", ""),
        on_click=DemoState.set_demo(name),
    )


def code_block(code: str) -> rx.Component:
    return rx.code_block(
        code,
        language="python",
        # wrap_long_lines=True,
        class_name="demo-code-block border-slate-4 !p-8 border-r !rounded-none",
    )


def preview_block() -> rx.Component:
    return rx.box(
        rx.text("Preview"),
        class_name="flex justify-center items-center p-8 w-full h-full",
    )

def demo_section() -> rx.Component:
    return rx.box(
        # Tabs
        rx.box(
            tab("Image Gen", "wand-sparkles"),
            tab("Forms", "scan-text"),
            tab("Charts", "area-chart"),
            # tab("Chatbot", "bot-message-square"),
            tab("Custom", "atom"),
            rx.link(
                rx.box(
                    rx.icon(tag="layers", size=16),
                    "More",
                    class_name="box-border flex flex-row justify-center items-center gap-2 hover:bg-slate-3 px-3 py-0.5 rounded-[0.625rem] h-8 font-small text-slate-9 transition-bg cursor-pointer",
                ),
                href=gallery.path,
                underline="none",
            ),
            class_name="flex flex-row items-center gap-2 border-slate-4 p-2 border-b flex-wrap",
        ),
        # Previews
        rx.box(
            rx.box(
                rx.match(
                    DemoState.demo,
                    ("Image Gen", image_gen()),
                    ("Forms", form()),
                    ("Charts", charts()),
                    # ("Chatbot", charts()),
                    ("Custom", react()),
                    image_gen(),
                ),
                class_name="border-slate-4 border-r w-full lg:w-1/2 h-auto",
            ),
            rx.box(
                rx.match(
                    DemoState.demo,
                    ("Image Gen", code_block(image_gen_code)),
                    ("Forms", code_block(form_code)),
                    ("Charts", code_block(charts_code)),
                    ("Chatbot", code_block(charts_code)),
                    ("Custom", code_block(react_code)),
                    image_gen(),
                ),
                class_name="desktop-only w-1/2 overflow-auto",
            ),
            class_name="flex flex-row w-full h-full max-h-[34rem] overflow-hidden",
        ),
        class_name="flex flex-col border-slate-4 bg-slate-2 shadow-large border rounded-[1.125rem] w-full max-w-[67rem] h-full overflow-hidden",
    )
