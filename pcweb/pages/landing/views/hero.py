import base64
import uuid
from typing import TypedDict

import httpx
import reflex as rx
import reflex_ui as ui
from reflex.experimental import ClientStateVar

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.constants import (
    MAX_FILE_SIZE_BYTES,
    MAX_FILE_SIZE_MB,
    MAX_IMAGES_COUNT,
    PROMPT_MAP,
    REFLEX_BUILD_URL,
    RX_BUILD_BACKEND,
)


def is_content_type_valid(content_type: str) -> bool:
    """Check if the content type is valid."""
    return content_type.startswith("image/")


textarea_x_pos = ClientStateVar.create(var_name="textarea_x_pos", default=0)
textarea_y_pos = ClientStateVar.create(var_name="textarea_y_pos", default=0)
textarea_opacity = ClientStateVar.create(var_name="textarea_opacity", default=0)
show_default_prompt = ClientStateVar.create(
    var_name="show_default_prompt", default=True
)


class ImageData(TypedDict):
    data: bytes
    mime_type: str


class SubmitPromptState(rx.State):
    _images: list[ImageData] | None = None
    is_uploading: rx.Field[bool] = rx.field(False)
    is_processing: rx.Field[bool] = rx.field(False)

    @rx.event(background=True, temporal=True)
    async def redirect_to_ai_builder(self, form_data: dict):
        if prompt := form_data.get("prompt"):
            if len(prompt) < 5:
                return rx.toast.warning(
                    "Your prompt needs at least 5 characters. Please add more details.",
                )
            random_uuid = uuid.uuid4()
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
                self.is_processing = True
            return (
                rx.redirect("/")
                if not response.is_success
                else rx.redirect(
                    REFLEX_BUILD_URL.strip("/") + f"/prompt?token={random_uuid!s}"
                )
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


def integration_text(text: str, integration: str) -> rx.Component:
    return rx.el.span(
        rx.image(
            src=f"/landing/integrations/light/{integration}.svg",
            class_name="size-7 pointer-events-none shrink-0 inline-block align-text-bottom",
        ),
        rx.el.span(
            text,
            class_name="text-slate-12 text-xl leading-[2.5rem] font-semibold",
        ),
        class_name="inline-flex items-center gap-2 align-bottom mx-1",
    )


def integration_text_light_dark(text: str, integration: str) -> rx.Component:
    return rx.el.span(
        rx.image(
            src=f"/landing/integrations/light/{integration}.svg",
            class_name="size-7 pointer-events-none shrink-0 inline-block align-text-bottom dark:hidden",
        ),
        rx.image(
            src=f"/landing/integrations/dark/{integration}.svg",
            class_name="size-7 pointer-events-none shrink-0 align-text-bottom hidden dark:inline-block",
        ),
        rx.el.span(
            text,
            class_name="text-slate-12 text-xl leading-[2.5rem] font-semibold",
        ),
        class_name="inline-flex items-center gap-2 align-bottom mx-1",
    )


@rx.memo
def one_upload_file_display(file_data_uri: str, index: int) -> rx.Component:
    return ui.preview_card(
        trigger=rx.box(
            rx.el.button(
                rx.html("""<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
  <path opacity="0.64" d="M8 0.833344C11.9581 0.833344 15.1667 4.04197 15.1667 8.00001C15.1667 11.9581 11.9581 15.1667 8 15.1667C4.04196 15.1667 0.833336 11.9581 0.833336 8.00001C0.833336 4.04197 4.04196 0.833344 8 0.833344Z" fill="#1C2024"/>
  <path d="M6.4205 5.48325C6.15866 5.26969 5.77265 5.28477 5.52857 5.52882C5.28458 5.7729 5.26945 6.15893 5.483 6.42075L5.52857 6.47153L7.05719 8.00018L5.52922 9.52884C5.26897 9.78918 5.26888 10.2112 5.52922 10.4715C5.78957 10.7316 6.21164 10.7318 6.47193 10.4715L7.99992 8.94291L9.52792 10.4715L9.57872 10.5171C9.84046 10.7306 10.2265 10.7154 10.4707 10.4715C10.7147 10.2276 10.7302 9.84144 10.5169 9.57958L10.4707 9.52884L8.94199 8.00018L10.4713 6.47153L10.5169 6.42075C10.7304 6.15892 10.7153 5.7729 10.4713 5.52882C10.2272 5.28477 9.84119 5.26969 9.57932 5.48325L9.52859 5.52882L7.99992 7.05744L6.47128 5.52882L6.4205 5.48325Z" fill="white"/>
</svg>"""),
                type="button",
                on_click=SubmitPromptState.cancel_upload(index),
                class_name="absolute top-1 right-1 rounded-full transition-colors flex justify-center items-center size-[0.89581rem]",
            ),
            rx.image(
                src=file_data_uri,
                class_name="rounded-lg object-cover h-full w-full aspect-square border border-slate-3",
            ),
            class_name="flex items-center gap-2 relative size-12 shrink-0",
        ),
        content=rx.image(
            src=file_data_uri,
            class_name="rounded-lg object-cover h-full max-h-[10rem] w-auto",
        ),
    )


def uploaded_file_display() -> rx.Component:
    return rx.foreach(
        SubmitPromptState.image_data_uris,
        lambda file_data_uri, index: one_upload_file_display(
            file_data_uri=file_data_uri,
            index=index,
        ),
    )


def prompt_box() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.cond(
                show_default_prompt.value,
                rx.el.span(
                    rx.el.span(
                        "Build a dashboard with ",
                        integration_text(
                            "Databricks",
                            "databricks",
                        ),
                        "metrics,",
                        class_name="animate-[prompt-box-line] animate-duration-[200ms] animate-ease-out origin-left absolute top-3 left-5 h-10 pointer-events-none",
                    ),
                    rx.el.span(
                        "use ",
                        integration_text_light_dark(
                            "Okta",
                            "okta",
                        ),
                        "for auth, ping me on ",
                        integration_text(
                            "Slack",
                            "slack",
                        ),
                        class_name="animate-[prompt-box-line] animate-duration-[200ms] animate-ease-out origin-left absolute top-13 left-5 h-10 animate-delay-200 animate-fill-both pointer-events-none",
                    ),
                    rx.el.span(
                        "for critical metrics",
                        # Cursor
                        rx.el.span(
                            class_name="w-0.5 h-8 bg-slate-12 animate-blink inline-block align-middle animate-fill-both animate-delay-450",
                        ),
                        class_name="animate-[prompt-box-line] animate-duration-[200ms] animate-ease-out origin-left absolute top-23 left-5 h-10 animate-delay-400 animate-fill-both pointer-events-none",
                    ),
                    class_name="text-slate-11 dark:text-slate-9 text-xl leading-[2.5rem] font-medium cursor-text max-lg:hidden",
                ),
                rx.el.div(
                    rx.el.textarea(
                        placeholder="What do you want to build?",
                        auto_focus=True,
                        id="prompt",
                        custom_attrs={
                            "autoComplete": "off",
                            "autoCapitalize": "none",
                            "autoCorrect": "off",
                            "spellCheck": "false",
                        },
                        auto_height=True,
                        enter_key_submit=True,
                        class_name="text-slate-12 text-xl font-medium size-full placeholder:text-slate-9 border-none focus:border-none focus:outline-none outline-none resize-none caret-slate-12 mt-2 resize-none w-full [&::-webkit-scrollbar]:w-1 [&::-webkit-scrollbar-track]:bg-grayA-3 [&::-webkit-scrollbar-thumb]:bg-slate-7 [&::-webkit-scrollbar-track]:rounded-full [&::-webkit-scrollbar-thumb]:rounded-full bg-transparent min-h-[2.5rem] max-h-[10.5rem]",
                    ),
                    rx.el.div(
                        uploaded_file_display(),
                        class_name="flex flex-row gap-2 items-center overflow-x-auto mb-2",
                    ),
                    class_name="flex flex-col gap-2",
                ),
            ),
            rx.cond(
                show_default_prompt.value,
                rx.el.span(
                    class_name="absolute inset-0 cursor-text z-10",
                    on_click=show_default_prompt.set_value(False),
                ),
                None,
            ),
            on_click=rx.set_focus("prompt"),
            class_name="min-h-[9rem] h-full lg:w-[29rem] max-w-[29rem] max-lg:w-full rounded-2xl bg-white-1 dark:bg-[#151618] border border-slate-4 px-5 py-3 relative overflow-hidden dark:!shadow-none",
            style={
                "box-shadow": "0 2px 0 0 #FFF inset, 0 2px 6px 0 light-dark(rgba(28, 32, 36, 0.08), rgba(0, 0, 0, 0)) inset, 0 1px 5px 0 light-dark(rgba(28, 32, 36, 0.03), rgba(0, 0, 0, 0)) inset;",
            },
        ),
        rx.el.div(
            rx.upload.root(
                ui.button(
                    ui.icon(icon="AttachmentIcon"),
                    "Attach",
                    size="lg",
                    type="button",
                    variant="ghost",
                    on_click=show_default_prompt.set_value(False),
                    class_name="rounded-[10px] font-semibold text-slate-10 dark:text-slate-9",
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
                on_drop_rejected=rx.toast.error(
                    f"Unsupported file type or file too large (Max {MAX_FILE_SIZE_MB}MB, up to {MAX_IMAGES_COUNT} files)."
                ),
                max_files=MAX_IMAGES_COUNT,
                max_size=MAX_FILE_SIZE_BYTES,
                multiple=True,
                id="upload-image-button",
            ),
            ui.button(
                "Build Your App",
                size="lg",
                variant="primary",
                loading=SubmitPromptState.is_processing,
                on_click=show_default_prompt.set_value(False),
                class_name="rounded-[10px] font-semibold",
            ),
            class_name="flex flex-row items-center gap-2 justify-between",
        ),
        on_mount=rx.call_script(
            f"""
            if (window.innerWidth < 1024) {{
                {show_default_prompt.set}(false);
            }}
        """
        ),
        on_submit=SubmitPromptState.redirect_to_ai_builder,
        class_name="flex flex-col gap-4 mt-6 max-w-[29rem] w-full",
    )


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", class_name="lg:top-[65px] top-[45px]"),
        numbers_pattern(side="right", class_name="lg:top-[65px] top-[45px]"),
        rx.el.h1(
            """Build From Prompt to
 Production App, In Seconds""",
            class_name="text-slate-12 lg:text-4xl text-3xl font-semibold text-center lg:max-w-[576px] word-wrap break-words lg:whitespace-pre",
        ),
        prompt_box(),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-28 lg:pt-[8rem] relative lg:overflow-hidden overflow-hidden z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
