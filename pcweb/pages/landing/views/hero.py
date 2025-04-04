import reflex as rx
from pcweb.components.icons.hugeicons import hi
from pcweb.constants import REFLEX_BUILD_URL


class SubmitPromptState(rx.State):

    @rx.event
    def redirect_to_ai_builder(self, form_data: dict):
        if prompt := form_data.get("prompt"):
            return rx.redirect(f"{REFLEX_BUILD_URL.strip('/')}/?prompt={prompt}")


def preset_cards(text: str) -> rx.Component:
    return rx.el.button(
        hi("magic-wand-01", class_name="shrink-0"),
        text,
        on_click=SubmitPromptState.redirect_to_ai_builder({"prompt": text}),
        class_name="flex flex-row gap-2.5 p-2.5 rounded-[0.625rem] bg-slate-1 hover:bg-slate-3 transition-bg cursor-pointer flex-1 text-sm font-medium text-slate-9 shadow-[0px_0px_0px_1px_rgba(190,_190,_210,_0.40)] dark:shadow-[0px_0px_0px_1px_rgba(255,_255,_255,_0.06)] items-center justify-start",
    )


def prompt_box() -> rx.Component:
    return rx.box(
        rx.el.form(
            rx.box(
                rx.el.input(
                    placeholder="What do you want to build?",
                    id="prompt",
                    class_name="font-medium text-slate-12 text-base placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 w-full bg-transparent",
                ),
                rx.el.button(
                    rx.html(
                        """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
  <path d="M8 13V3M8 3L3 8M8 3L13 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
                    ),
                    class_name="bg-[#6E56CF] hover:bg-[#654DC4] text-white rounded-full size-6 shrink-0 flex items-center justify-center cursor-pointer",
                ),
                class_name="shadow-[0px_0px_0px_1px_rgba(190,_190,_210,_0.40)] dark:shadow-[0px_0px_0px_1px_rgba(255,_255,_255,_0.06)] rounded-xl px-3 py-2.5 w-full flex flex-row items-center gap-3",
            ),
            rx.box(
                preset_cards("Dashboard UI"),
                preset_cards("Pricing section"),
                preset_cards("Settings page"),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-2",
            ),
            class_name="flex flex-col gap-4 w-full",
            on_submit=SubmitPromptState.redirect_to_ai_builder,
        ),
        class_name="max-w-[34.125rem] rounded-[1.75rem] p-4 flex flex-col gap-4 w-full mt-[2rem] bg-[linear-gradient(180deg,_rgba(252,_252,_253,_0.82)_0%,_rgba(252,_252,_253,_0.80)_88%)] shadow-[0px_0px_0px_1px_rgba(190,_190,_210,_0.40)] dark:bg-[linear-gradient(180deg,_rgba(21,_22,_24,_0.82)_0%,_rgba(21,_22,_24,_0.80)_88%)] dark:shadow-[0px_0px_0px_1px_rgba(255,_255,_255,_0.06)] backdrop-blur-[6px]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.image(
            src=f"/landing/patterns/{rx.color_mode_cond(light='light', dark='dark')}/hero.svg",
            class_name="absolute top-0 left-0 w-full h-full object-cover z-[-2] pointer-events-none dark:mt-6 mt-9 opacity-50 dark:opacity-100 lg:block hidden",
        ),
        rx.box(
            rx.image(
                src=f"/landing/patterns/{rx.color_mode_cond(light='light', dark='dark')}/triangle.svg",
                class_name="w-[34.125rem] h-[20.875rem]",
            ),
            class_name="absolute top-[232px] left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover z-[-1] pointer-events-none w-[34.125rem] h-[20.875rem] blur-[36px] opacity-[0.35] hidden lg:block bg-violet-6 mix-blend-overlay",
        ),
        # Headings
        rx.el.h1(
            "Build Internal Tools With AI",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-4xl lg:text-6xl font-semibold text-center text-transparent text-balance mx-auto break-words",
        ),
        rx.el.h2(
            "A unified platform to build and deploy all in Python.",
            class_name="max-w-full w-full text-lg lg:text-xl text-center text-slate-11 -mt-2 font-medium mx-auto text-balance word-wrap break-words md:whitespace-pre",
        ),
        prompt_box(),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[6.31rem] pt-32 lg:pt-48 relative overflow-hidden z-[1] bg-transparent lg:bg-slate-1 px-4",
    )
