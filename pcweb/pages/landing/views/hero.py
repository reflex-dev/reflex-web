import reflex as rx
from reflex.experimental import ClientStateVar
from pcweb.constants import REFLEX_BUILD_URL
from pcweb.components.new_button import button
from pcweb.components.icons.icons import get_icon_var
from .video_demo import video_demo, watch_preview


import uuid
import httpx
import base64
import reflex as rx
from pcweb.components.icons.icons import get_icon_var
from pcweb.components.icons.hugeicons import hi
from pcweb.constants import (
    REFLEX_BUILD_URL,
    RX_BUILD_BACKEND,
    MAX_FILE_SIZE_MB,
    MAX_FILE_SIZE_BYTES,
    MAX_IMAGES_COUNT,
    PROMPT_MAP,
)
from reflex.experimental import ClientStateVar
from typing import TypedDict


def is_content_type_valid(content_type: str) -> bool:
    """Check if the content type is valid."""
    return content_type.startswith("image/")


textarea_x_pos = ClientStateVar.create(var_name="textarea_x_pos", default=0)
textarea_y_pos = ClientStateVar.create(var_name="textarea_y_pos", default=0)
textarea_opacity = ClientStateVar.create(var_name="textarea_opacity", default=0)


class ImageData(TypedDict):
    data: bytes
    mime_type: str


class SubmitPromptState(rx.State):
    _images: list[ImageData] | None = None
    is_uploading: bool = False

    @rx.event(background=True, temporal=True)
    async def redirect_to_ai_builder(self, form_data: dict):
        if prompt := form_data.get("prompt"):
            random_uuid = uuid.uuid4()
            print(prompt)
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    RX_BUILD_BACKEND.rstrip("/") + "/prompt",
                    json={
                        "prompt": PROMPT_MAP.get(prompt, prompt),
                        "token": str(random_uuid),
                        "images": self.image_data_uris,
                    },
                )
            async with self:
                self.reset()
            return (
                rx.redirect("/")
                if not response.is_success
                else rx.redirect(REFLEX_BUILD_URL.strip("/"))
            )

    @rx.event(temporal=True)
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of an image."""
        if not files:
            yield rx.toast.error("No files selected")
            yield rx.cancel_upload("upload-image-button")
            return
        self.is_uploading = True
        self._images = self._images or []
        yield
        for first_file in files:
            if len(self._images) >= MAX_IMAGES_COUNT:
                yield rx.toast.error("Maximum of 5 images allowed")
                yield rx.cancel_upload("upload-image-button")
                self.is_uploading = False
                return
            if not first_file.content_type:
                yield rx.toast.error("No content type")
                yield rx.cancel_upload("upload-image-button")
                self.is_uploading = False
                self._images = None
                return
            if not first_file.content_type.startswith("image/"):
                yield rx.toast.error(f"Invalid content type {first_file.content_type}")
                yield rx.cancel_upload("upload-image-button")
                self.is_uploading = False
                self._images = None
                return
            upload_data = await first_file.read()
            if len(upload_data) > MAX_FILE_SIZE_BYTES:
                yield rx.toast.error(
                    f"File too large, maximum size is {MAX_FILE_SIZE_MB}MB"
                )
                yield rx.cancel_upload("upload-image-button")
                self.is_uploading = False
                self._images = None
                return
            self._images.append(
                ImageData(
                    data=upload_data,
                    mime_type=first_file.content_type,
                )
            )
            self.is_uploading = False

    @rx.event
    def cancel_upload(self, index: int):
        if self.is_uploading or index < 0:
            self.is_uploading = False
            self._images = None
            return rx.cancel_upload("upload-image-button")
        elif self._images is not None:
            if index < len(self._images):
                self._images.pop(index)

    @rx.var
    def image_data_uris(self) -> list[str]:
        """Return the image data."""
        if self._images is None:
            return []
        return [
            f"data:{image['mime_type']};base64,{base64.b64encode(image['data']).decode('ascii')}"
            for image in self._images
        ]


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


@rx.memo
def preset_image_card(text: str, id: str):
    textarea_x_pos = ClientStateVar.create(
        var_name="textarea_x_pos", default=0, global_ref=False
    )
    textarea_y_pos = ClientStateVar.create(
        var_name="textarea_y_pos", default=0, global_ref=False
    )
    textarea_opacity = ClientStateVar.create(
        var_name="textarea_opacity", default=0, global_ref=False
    )
    return rx.upload.root(
        rx.box(
            rx.el.button(
                get_icon_var("image-03", class_name="shrink-0"),
                text,
                on_click=rx.set_value("prompt", text),
                class_name="flex flex-row gap-2 p-2.5 rounded-xl transition-bg cursor-pointer flex-1 text-sm font-medium text-slate-9 text-start border-[rgba(190,_190,_210,_0.40)] dark:border-[rgba(255,_255,_255,_0.06)] hover:bg-[#fdfdfd78] dark:hover:bg-[#15161863] border-[1.5px] w-full items-center",
                on_mouse_enter=textarea_opacity.set_value(1),
                on_mouse_leave=textarea_opacity.set_value(0),
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
                type="button",
            ),
            rx.box(
                aria_hidden=True,
                style={
                    "border": "2px solid var(--c-violet-6)",
                    "opacity": textarea_opacity.value,
                    "WebkitMaskImage": f"radial-gradient(50% 40px at {textarea_x_pos.value}px {textarea_y_pos.value}px, black 45%, transparent)",
                },
                class_name="pointer-events-none absolute left-0 top-0 z-10 h-full w-full rounded-xl border bg-[transparent] opacity-0 transition-opacity duration-500 box-border",
            ),
            id=id,
            class_name="relative w-full",
        ),
        on_drop=SubmitPromptState.handle_upload(
            rx.upload_files(
                upload_id="upload-image-button",
            )
        ),
        accept={
            "image/png": [".png"],
            "image/jpeg": [".jpg", ".jpeg"],
            "image/webp": [".webp"],
        },
        multiple=True,
        id="upload-image-button",
    )


@rx.memo
def one_upload_image_display(image_data_uri: str, index: int):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.box(
                rx.el.button(
                    hi(
                        "multiplication-sign",
                        size=11,
                        stroke_width=3.5,
                    ),
                    type="button",
                    on_click=SubmitPromptState.cancel_upload(index),
                    class_name="absolute top-1 right-1 -translate-y-1/2 translate-x-1/2 rounded-full transition-colors dark:border-token-main-surface-secondary border-[3px] border-slate-2 bg-slate-12 p-[2px] text-slate-1 flex justify-center items-center",
                ),
                rx.image(
                    src=image_data_uri,
                    class_name="rounded-lg object-cover h-full w-full aspect-square",
                ),
                class_name="flex items-center gap-2 relative size-12",
            ),
        ),
        rx.hover_card.content(
            rx.image(
                src=image_data_uri,
                class_name="rounded-lg object-cover h-full w-full",
            ),
            side="top",
            align="center",
            class_name="bg-slate-1 p-2 rounded-xl shadow-large border border-slate-5",
        ),
    )


def uploaded_image_display():
    return rx.foreach(
        SubmitPromptState.image_data_uris,
        lambda image_data_uri, index: one_upload_image_display(
            image_data_uri=image_data_uri,
            index=index,
        ),
    )


def uploading_image_display():
    return rx.box(
        rx.el.button(
            hi(
                "multiplication-sign",
                size=11,
                stroke_width=3.5,
            ),
            type="button",
            on_click=SubmitPromptState.cancel_upload(-1),
            class_name="absolute top-1 right-1 -translate-y-1/2 translate-x-1/2 rounded-full transition-colors dark:border-token-main-surface-secondary border-[3px] border-slate-2 bg-slate-12 p-[2px] text-slate-1 flex justify-center items-center",
        ),
        rx.skeleton(
            class_name="rounded-lg object-cover h-full w-full aspect-square",
        ),
        class_name="flex items-center gap-2 relative size-12",
    )


def prompt_box() -> rx.Component:
    return rx.box(
        rx.el.form(
            rx.cond(
                SubmitPromptState.image_data_uris | SubmitPromptState.is_uploading,
                rx.box(
                    rx.cond(
                        SubmitPromptState.is_uploading,
                        uploading_image_display(),
                        uploaded_image_display(),
                    ),
                    class_name="h-auto flex flex-row items-center gap-2 overflow-x-auto scrollbar-thin scrollbar-thumb-slate-4 scrollbar-track-transparent overflow-y-visible pt-2",
                ),
            ),
            rx.box(
                rx.upload.root(
                    rx.box(
                        rx.el.input(
                            placeholder="What do you want to build?",
                            id="prompt",
                            class_name="font-medium text-slate-12 text-base placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 w-full bg-transparent",
                        ),
                        rx.box(
                            rx.upload.root(
                                rx.el.button(
                                    hi("image-add-02"),
                                    type="button",
                                    title="Upload images",
                                    class_name="w-full [background:linear-gradient(45deg,var(--c-violet-2),var(--c-violet-2)_50%,var(--c-violet-2))_padding-box,conic-gradient(from_var(--border-angle),#9a79fd7a_60%,#8b5cf680_70%,#745dd1db_85%,#8b5cf680_90%,#9a79fd7a)_border-box] dark:[background:linear-gradient(45deg,var(--c-violet-3),var(--c-violet-3)_50%,var(--c-violet-3))_padding-box,conic-gradient(from_var(--border-angle),#5F43D0CC_60%,#7c57f8e3_72%,#926bfee6_85%,#7c57f8e3_95%,#5F43D0CC)_border-box] border-[1.5px] border-transparent animate-border text-violet-9 text-sm cursor-pointer inline-flex items-center justify-center relative transition-bg shrink-0 font-sans disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 transition-bg outline-none peer-placeholder-shown:!bg-slate-3 peer-placeholder-shown:!bg-none peer-placeholder-shown:cursor-not-allowed peer-placeholder-shown:border peer-placeholder-shown:border-slate-5 peer-placeholder-shown:!text-slate-8 text-nowrap px-1.5 h-7 rounded-md gap-1.5 bg-transparent hover:bg-slate-3 font-medium",
                                ),
                                on_drop=SubmitPromptState.handle_upload(
                                    rx.upload_files(
                                        upload_id="upload-image-button",
                                    )
                                ),
                                accept={
                                    "image/png": [".png"],
                                    "image/jpeg": [".jpg", ".jpeg"],
                                    "image/webp": [".webp"],
                                },
                                no_drag=True,
                                multiple=True,
                                max_files=MAX_IMAGES_COUNT,
                                id="upload-image-button",
                            ),
                            rx.el.button(
                                rx.html(
                                    """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
  <path d="M8 13V3M8 3L3 8M8 3L13 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
                                ),
                                class_name="bg-[#6E56CF] hover:bg-[#654DC4] text-white rounded-full size-6 shrink-0 flex items-center justify-center cursor-pointer",
                            ),
                            class_name="flex flex-row gap-2.5 items-center",
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
                    accept={
                        "image/png": [".png"],
                        "image/jpeg": [".jpg", ".jpeg"],
                        "image/webp": [".webp"],
                    },
                    on_drop=SubmitPromptState.handle_upload(
                        rx.upload_files(  # pyright: ignore [reportArgumentType]
                            upload_id="upload-landing-box",
                        )
                    ),
                    no_click=True,
                    multiple=True,
                    max_files=MAX_IMAGES_COUNT,
                    id="upload-landing-box",
                    drag_active_style=rx.Style(
                        style_dict={
                            "& #landing-input-box": {
                                "border": "1.5px dashed var(--c-slate-9)"
                            }
                        }
                    ),
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
                preset_image_card(text="Use an Image", id="upload-image-box"),
                preset_cards(text="Chat App", id="chat-app", icon="ai-chat-02"),
                preset_cards(
                    text="Live Dashboard", id="live-dashboard", icon="webpage"
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-2",
            ),
            class_name="flex flex-col gap-4 w-full",
            on_submit=SubmitPromptState.redirect_to_ai_builder,
        ),
        class_name="max-w-[34.125rem] rounded-[1.75rem] p-4 flex flex-col gap-4 w-full mt-[1.5rem] bg-[linear-gradient(180deg,_rgba(252,_252,_253,_0.82)_0%,_rgba(252,_252,_253,_0.80)_88%)] shadow-[0px_0px_0px_1px_rgba(190,_190,_210,_0.40)] dark:bg-[linear-gradient(180deg,_rgba(21,_22,_24,_0.82)_0%,_rgba(21,_22,_24,_0.80)_88%)] dark:shadow-[0px_0px_0px_1px_rgba(255,_255,_255,_0.06)] backdrop-blur-[6px] z-[1]",
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
                src="/landing/patterns/dark/triangle.webp",
                class_name="size-full bg-transparent",
            ),
            class_name="absolute top-[232px] left-1/2 transform -translate-x-1/2 -translate-y-1/2 object-cover z-[1] pointer-events-none w-[31rem] h-[20.875rem] hidden lg:block bg-transparent mix-blend-overlay",
        ),
        # Small gradient
        rx.box(
            class_name="z-[-1] blur-[16px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_light-dark(#D4CAFE,#4329AC)_0%,_rgba(21,_22,_24,_0)_100%)] w-[37rem] lg:h-[9.5rem] h-[6.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 lg:top-[22.5rem] top-[25.5rem] saturate-[1.25] lg:-mx-0 -mx-8 opacity-80 md:opacity-100 max-lg:opacity-50"
        ),
        # Big gradient
        rx.box(
            class_name="z-[-1] blur-[28px] absolute rounded-[64.25rem] bg-[radial-gradient(50%_50%_at_50%_50%,_#D4CAFE_0%,_rgba(21,_22,_24,_0)_100%)] dark:bg-[radial-gradient(50%_50%_at_50%_50%,_#4329AC_0%,_rgba(21,_22,_24,_0)_100%)] w-[45rem] lg:h-[10.25rem] h-[18.5rem] overflow-hidden pointer-events-none shrink-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 top-[26.25rem] saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100 max-lg:hidden"
        ),
        # New Ellipse gradient
        rx.box(
            class_name="absolute w-[1076px] h-[676px] lg:top-[-369px] top-[-26rem] bg-[radial-gradient(37.87%_37.87%_at_50%_50%,_#F4F0FE_0%,_rgba(21,_22,_24,_0)_100%)] dark:bg-[radial-gradient(37.87%_37.87%_at_50%_50%,_#261958_0%,_rgba(21,_22,_24,_0)_100%)] z-[-1] pointer-events-none saturate-[1.5] lg:-mx-0 -mx-8 opacity-80 md:opacity-100"
        ),
        # Headings
        rx.el.h1(
            "Prompt to production app, in seconds",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-5xl lg:text-6xl font-semibold text-center text-transparent text-balance mx-auto break-words z-[1]",
        ),
        rx.el.h2(
            "A unified platform to build and deploy all in Python.",
            class_name="max-w-full w-full text-lg lg:text-xl text-center text-slate-9 font-medium mx-auto text-balance word-wrap break-words md:whitespace-pre z-[1]",
        ),
        prompt_box(),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[6.31rem] pt-28 lg:pt-[10rem] relative lg:overflow-hidden overflow-visible z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
