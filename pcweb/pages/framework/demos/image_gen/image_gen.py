import os

import aiohttp
import reflex as rx

from pcweb.components.button import button
from pcweb.components.icons import get_icon
from pcweb.constants import REPLICATE_FLUX_SCHNELL_PREDICTIONS_URL
from pcweb.utils.http import default_client

_REPLICATE_WAIT_SEC = 5

_FLUX_SCHNELL_INPUT_DEFAULTS: dict[str, str | int | bool] = {
    "go_fast": True,
    "num_inference_steps": 3,
    "num_outputs": 1,
    "aspect_ratio": "1:1",
    "output_format": "webp",
    "output_quality": 80,
}


async def _run_flux_schnell(prompt: str) -> str:
    token = os.environ.get("REPLICATE_API_TOKEN")

    session = default_client()
    timeout = aiohttp.ClientTimeout(total=_REPLICATE_WAIT_SEC)
    async with session.post(
        REPLICATE_FLUX_SCHNELL_PREDICTIONS_URL,
        json={"input": {"prompt": prompt, **_FLUX_SCHNELL_INPUT_DEFAULTS}},
        headers={
            "Authorization": f"Token {token}",
            "Prefer": f"wait={_REPLICATE_WAIT_SEC}",
        },
        timeout=timeout,
    ) as resp:
        resp.raise_for_status()
        prediction = await resp.json()

    output = prediction.get("output")
    if not output:
        raise RuntimeError("Replicate returned no output")
    return str(output[0] if isinstance(output, list) else output)


class ImageGenState(rx.State):
    """The app state."""

    image_url: str = ""
    processing: bool = False

    @rx.event(background=True)
    async def get_image(self, form_data):
        """Get the image from the prompt."""
        prompt = form_data["prompt"]
        if prompt == "":
            return
        async with self:
            self.processing = True
            yield

        try:
            image_url = await _run_flux_schnell(prompt)
            async with self:
                self.image_url = image_url
        except Exception:
            async with self:
                self.image_url = ""
        finally:
            async with self:
                self.processing = False


def image_gen() -> rx.Component:
    return rx.box(
        rx.skeleton(
            rx.box(
                rx.cond(
                    ImageGenState.image_url,
                    rx.image(
                        src=ImageGenState.image_url,
                        class_name="w-auto h-auto object-contain object-center rounded-2xl",
                    ),
                    rx.box(
                        get_icon("image_ai"),
                        # rx.icon("image", size=26, class_name="!text-slate-7"),
                        class_name="flex justify-center items-center border-slate-4 border bg-slate-3 w-full h-full rounded-2xl",
                    ),
                ),
                class_name="h-full w-full flex justify-center items-center overflow-hidden rounded-2xl aspect-square",
            ),
            loading=ImageGenState.processing,
            class_name="rounded-xl w-full h-full",
        ),
        rx.form(
            rx.el.input(
                placeholder="What do you want to see?",
                name="prompt",
                type="text",
                required=True,
                class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-slate-4 p-[0.5rem_0.75rem] border rounded-[0.625rem] font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
            ),
            button(
                text=rx.cond(ImageGenState.processing, "Generating...", "Generate"),
                style={
                    "input:placeholder-shown + &": {
                        "opacity": "0.65",
                        "cursor": "default",
                        "_hover": {"background": "var(--c-slate-5)"},
                    },
                    "cursor": rx.cond(ImageGenState.processing, "default", "pointer"),
                    "opacity": rx.cond(ImageGenState.processing, "0.65", "1"),
                },
                variant="muted",
                class_name="!bg-slate-5 !border-t-[rgba(255,255,255,0.05)] !rounded-[0.625rem] hover:!bg-slate-6 !text-slate-9",
                type="submit",
            ),
            class_name="flex flex-row gap-2 align-center",
            reset_on_submit=True,
            on_submit=ImageGenState.get_image,
        ),
        class_name="flex flex-col items-center gap-4 p-4 lg:px-10 lg:py-12 h-full overflow-hidden",
    )


image_gen_code = """import reflex as rx
import replicate

class ImageGenState(rx.State):

    image_url = ""
    processing = False

    @rx.event
    def get_image(self, form_data):
        prompt = form_data["prompt"]
        if prompt == "":
            return

        self.processing = True
        yield

        input = {
            "prompt": prompt,
            "go_fast": True,
            "num_inference_steps": 3,
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "output_quality": 80,
        }
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input=input,
        )
        self.image_url = output[0]
        self.processing = False

def image_gen():
    return rx.vstack(
        rx.skeleton(
            rx.flex(
                rx.cond(
                    ImageGenState.image_url,
                    rx.image(
                        src=ImageGenState.image_url,
                    ),
                    rx.flex(
                        rx.icon("image", size=26, color=rx.color("slate", 7)),
                    ),
                ),
            ),
            loading=ImageGenState.processing,
        ),
        rx.form(
            rx.input(
                placeholder="What do you want to see?",
                name="prompt"
            ),
            rx.button(
                "Generate",
                loading=ImageGenState.processing,
                type="submit",
            ),
            reset_on_submit=True,
            on_submit=ImageGenState.get_image,
        )
    )
"""
