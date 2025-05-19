import uuid
import httpx
import reflex as rx
from pcweb.components.icons.icons import get_icon_var
from pcweb.constants import REFLEX_BUILD_URL, RX_BUILD_BACKEND
from reflex.experimental import ClientStateVar

textarea_x_pos = ClientStateVar.create(var_name="textarea_x_pos", default=0)
textarea_y_pos = ClientStateVar.create(var_name="textarea_y_pos", default=0)
textarea_opacity = ClientStateVar.create(var_name="textarea_opacity", default=0)


class SubmitPromptState(rx.State):
    @rx.event(background=True)
    async def redirect_to_ai_builder(self, form_data: dict):
        if prompt := form_data.get("prompt"):
            random_uuid = uuid.uuid4()

            async with httpx.AsyncClient() as client:
                await client.post(
                    RX_BUILD_BACKEND.rstrip("/") + "/prompt",
                    json={
                        "prompt": prompt,
                        "token": str(random_uuid),
                    },
                )

            return rx.redirect(
                REFLEX_BUILD_URL.strip("/") + "/prompt?token={random_uuid!s}"
            )


@rx.memo
def preset_cards(text: str, id: str, icon: str) -> rx.Component:
    textarea_x_pos = ClientStateVar.create(
        var_name="textarea_x_pos", default=0, global_ref=False
    )
    textarea_y_pos = ClientStateVar.create(
        var_name="textarea_y_pos", default=0, global_ref=False
    )
    textarea_opacity = ClientStateVar.create(
        var_name="textarea_opacity", default=0, global_ref=False
    )
    return rx.box(
        rx.el.button(
            get_icon_var(icon, class_name="shrink-0"),
            text,
            on_click=SubmitPromptState.redirect_to_ai_builder({"prompt": text}),
            on_mouse_enter=rx.call_function(textarea_opacity.set_value(1)),
            on_mouse_leave=rx.call_function(textarea_opacity.set_value(0)),
            id=id,
            on_mouse_move=[
                rx.call_function(
                    textarea_x_pos.set_value(
                        rx.Var(
                            f"event.clientX - document.getElementById({id}).getBoundingClientRect().left"
                        )
                    )
                ),
                rx.call_function(
                    textarea_y_pos.set_value(
                        rx.Var(
                            f"event.clientY - document.getElementById({id}).getBoundingClientRect().top"
                        )
                    )
                ),
            ],
            class_name="flex flex-row gap-2.5 p-2.5 rounded-[0.625rem] transition-bg cursor-pointer flex-1 text-sm font-medium text-slate-9 border-[rgba(190,_190,_210,_0.40)] dark:border-[rgba(255,_255,_255,_0.06)] hover:bg-[#fdfdfd78] dark:hover:bg-[#15161863] border-[1.5px] items-center justify-start w-full",
        ),
        rx.box(
            aria_hidden=True,
            style={
                "border": "2px solid var(--c-violet-6)",
                "opacity": textarea_opacity.value,
                "WebkitMaskImage": f"radial-gradient(50% 40px at {textarea_x_pos.value}px {textarea_y_pos.value}px, black 45%, transparent)",
            },
            class_name="pointer-events-none absolute left-0 top-0 z-10 h-full w-full rounded-[0.625rem] border-[1.5px] bg-[transparent] opacity-0 transition-opacity duration-500 box-border",
        ),
        class_name="relative w-full",
    )


def prompt_box() -> rx.Component:
    return rx.box(
        rx.el.form(
            rx.box(
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
                    on_mouse_enter=textarea_opacity.set_value(1),
                    on_mouse_leave=textarea_opacity.set_value(0),
                    on_mouse_move=[
                        rx.call_function(
                            textarea_x_pos.set_value(
                                rx.Var(
                                    "event.clientX - document.getElementById('landing-input-box').getBoundingClientRect().left"
                                )
                            )
                        ),
                        rx.call_function(
                            textarea_y_pos.set_value(
                                rx.Var(
                                    "event.clientY - document.getElementById('landing-input-box').getBoundingClientRect().top"
                                )
                            )
                        ),
                    ],
                    id="landing-input-box",
                    class_name="bg-[#fdfdfd78] dark:bg-[#16161ac2] border-[rgba(190,_190,_210,_0.40)] dark:border-[rgba(255,_255,_255,_0.06)] overflow-hidden border-[1.5px] rounded-xl px-3 py-2.5 w-full flex flex-row items-center gap-3",
                ),
                rx.box(
                    aria_hidden=True,
                    style={
                        "border": "2px solid var(--c-violet-6)",
                        "opacity": textarea_opacity.value,
                        "WebkitMaskImage": f"radial-gradient(45% 40px at {textarea_x_pos.value}px {textarea_y_pos.value}px, black 45%, transparent)",
                    },
                    class_name="pointer-events-none absolute left-0 top-0 z-10 h-full w-full rounded-xl border bg-[transparent] opacity-0 transition-opacity duration-500 box-border",
                ),
                class_name="relative w-full",
            ),
            rx.box(
                preset_cards(text="Pricing page", id="pricing-page", icon="dollar"),
                preset_cards(text="Chat App", id="chat-app", icon="ai-chat-02"),
                preset_cards(text="Dashboard UI", id="dashboard-ui", icon="webpage"),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-2",
            ),
            class_name="flex flex-col gap-4 w-full",
            on_submit=SubmitPromptState.redirect_to_ai_builder,
        ),
        class_name="max-w-[34.125rem] rounded-[1.75rem] p-4 flex flex-col gap-4 w-full mt-[2rem] bg-[linear-gradient(180deg,_rgba(252,_252,_253,_0.82)_0%,_rgba(252,_252,_253,_0.80)_88%)] shadow-[0px_0px_0px_1px_rgba(190,_190,_210,_0.40)] dark:bg-[linear-gradient(180deg,_rgba(21,_22,_24,_0.82)_0%,_rgba(21,_22,_24,_0.80)_88%)] dark:shadow-[0px_0px_0px_1px_rgba(255,_255,_255,_0.06)] backdrop-blur-[6px] z-[1]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        # Dark Waves
        rx.image(
            src="/landing/patterns/dark/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:right-0 right-[-150px] z-[-1] pointer-events-none hidden dark:lg:block w-[514px] lg:h-[406px] h-[506px] dark:block",
        ),
        rx.image(
            src="/landing/patterns/dark/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:left-0 left-[-150px] z-[-1] pointer-events-none hidden dark:lg:block scale-x-[-1] w-[514px] lg:h-[406px] h-[506px] dark:block",
        ),
        # Light Waves
        rx.image(
            src="/landing/patterns/light/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:right-0 right-[-150px] z-[-1] pointer-events-none hidden lg:block w-[514px] lg:h-[406px] h-[506px] dark:hidden dark:lg:hidden",
        ),
        rx.image(
            src="/landing/patterns/light/wave.webp",
            class_name="absolute lg:top-[65px] top-[45px] lg:left-0 left-[-150px] z-[-1] pointer-events-none hidden lg:block scale-x-[-1] w-[514px] lg:h-[406px] h-[506px] dark:hidden dark:lg:hidden",
        ),
        # Triangle
        rx.box(
            rx.image(
                src=f"/landing/patterns/dark/triangle.webp",
                class_name="size-full bg-transparent",
            ),
            class_name="absolute top-[232px] left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover z-[1] pointer-events-none w-[31rem] h-[20.875rem] hidden lg:block bg-transparent mix-blend-overlay",
        ),
        # Small gradient
        rx.box(
            class_name="z-[-1] blur-[16px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[37rem] lg:h-[9.5rem] h-[6.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-[21.5rem] saturate-[1.25] lg:-mx-0 -mx-8 opacity-80 md:opacity-100"
        ),
        # Big gradient
        rx.box(
            class_name="z-[-1] blur-[28px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[56rem] lg:h-[6.5rem] h-[18.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-[28.25rem] saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100"
        ),
        # New Ellipse gradient
        rx.box(
            class_name="absolute w-[1076px] h-[676px] lg:top-[-369px] top-[-26rem] bg-[radial-gradient(37.87%_37.87%_at_50%_50%,_light-dark(#F4F0FE,#261958)_0%,_rgba(21,_22,_24,_0)_100%)] z-[-1] pointer-events-none saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100"
        ),
        # Headings
        rx.el.h1(
            "Build Internal Tools With AI",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-5xl lg:text-6xl font-semibold text-center text-transparent text-balance mx-auto break-words z-[1]",
        ),
        rx.el.h2(
            "A unified platform to build and deploy all in Python.",
            class_name="max-w-full w-full text-lg lg:text-xl text-center text-slate-9 -mt-2 font-medium mx-auto text-balance word-wrap break-words md:whitespace-pre z-[1]",
        ),
        prompt_box(),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[6.31rem] pt-28 lg:pt-[9.65rem] relative lg:overflow-hidden overflow-visible z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
