import reflex as rx
import uuid
import httpx
import base64
from pcweb.constants import (
    REFLEX_BUILD_URL,
    RX_BUILD_BACKEND,
    MAX_FILE_SIZE_MB,
    MAX_FILE_SIZE_BYTES,
    MAX_IMAGES_COUNT,
    PROMPT_MAP,
)
from pcweb.components.numbers_pattern import numbers_pattern
import reflex_ui as ui
from reflex.experimental import ClientStateVar
from typing import TypedDict
from reflex.experimental import ClientStateVar


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
    is_uploading: bool = False

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
                        "when critical metrics",
                        # Cursor
                        rx.el.span(
                            class_name="w-0.5 h-8 bg-slate-12 animate-blink inline-block align-middle animate-fill-both animate-delay-450",
                        ),
                        class_name="animate-[prompt-box-line] animate-duration-[200ms] animate-ease-out origin-left absolute top-23 left-5 h-10 animate-delay-400 animate-fill-both pointer-events-none",
                    ),
                    class_name="text-slate-11 text-xl leading-[2.5rem] font-medium cursor-text",
                ),
                rx.el.textarea(
                    placeholder="What do you want to build?",
                    auto_focus=True,
                    id="prompt-box",
                    custom_attrs={
                        "autoComplete": "off",
                        "autoCapitalize": "none",
                        "autoCorrect": "off",
                        "spellCheck": "false",
                    },
                    class_name="text-slate-12 text-xl font-medium size-full placeholder:text-slate-9 border-none focus:border-none focus:outline-none outline-none resize-none caret-slate-12 mt-2",
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
            on_click=rx.set_focus("prompt-box"),
            class_name="h-[9rem] w-[29rem] rounded-2xl bg-white-1 border border-slate-4 px-5 py-3 relative overflow-hidden",
            style={
                "box-shadow": "0 2px 0 0 #FFF inset, 0 2px 6px 0 rgba(28, 32, 36, 0.08) inset, 0 1px 5px 0 rgba(28, 32, 36, 0.03) inset;",
            },
        ),
        rx.el.div(
            ui.button(
                ui.icon(icon="AttachmentIcon"),
                "Attach",
                size="lg",
                type="button",
                variant="ghost",
                class_name="rounded-[10px] font-semibold text-slate-10",
            ),
            ui.button(
                "Build Your App",
                size="lg",
                variant="primary",
                on_click=show_default_prompt.set_value(False),
                class_name="rounded-[10px] font-semibold",
            ),
            class_name="flex flex-row items-center gap-2 justify-between",
        ),
        class_name="flex flex-col gap-4 mt-6",
    )


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", class_name="lg:top-[65px] top-[45px]"),
        numbers_pattern(side="right", class_name="lg:top-[65px] top-[45px]"),
        rx.el.h1(
            """Build From Prompt to 
Production App, In Seconds""",
            class_name="text-slate-12 text-4xl font-semibold text-center max-w-[576px] word-wrap break-words whitespace-pre",
        ),
        prompt_box(),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-28 lg:pt-[8rem] relative lg:overflow-hidden overflow-hidden z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
