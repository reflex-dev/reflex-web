import reflex as rx
import httpx
from pcweb.components.icons.hugeicons import hi
from pcweb.constants import SCREENSHOT_BUCKET, REFLEX_BUILD_URL, RX_CLOUD_BACKEND
import asyncio
import contextlib

TEMPLATES_LIST = [
    "bbfcc0b8-8f09-4211-884e-7ad2f1a36906",
    "e6293a74-4a47-44a3-bc1e-8966863feb46",
    "a7f5bf05-a34a-4b40-a39f-4f6c71ded78f",
    "dd3a7d49-e174-41d3-8856-cad921a98749",
    "576aab1d-e733-42fa-a13e-515fd72ba012",
    "28194790-f5cc-4625-bd30-cf2693890e08",
    "7e5346b7-025c-4ff3-9b32-c1b9d7afcaec",
    "2f969644-3140-4dbb-b639-5d0a940603c2",
    "47f86c01-59ec-4088-b47a-64ceddf58a6e",
    "98afee02-538f-4334-ab10-f05c1c3d564b",
]


async def retreive_templates():
    """Fetch and update the TEMPLATES_LIST."""
    try:
        while True:
            with contextlib.suppress(Exception):
                async with httpx.AsyncClient() as client:
                    global TEMPLATES_LIST
                    response = await client.get(
                        f"{RX_CLOUD_BACKEND}v1/flexgen/templates",
                    )
                    response_data = response.json()
                    if isinstance(response_data, list):
                        TEMPLATES_LIST = response_data

            await asyncio.sleep(60 * 10)
    except asyncio.CancelledError:
        pass


class AIBuilderGallery(rx.State):
    @rx.var(interval=60 * 10)
    def items(self) -> list[str]:
        return TEMPLATES_LIST


def header() -> rx.Component:
    return rx.box(
        rx.image(
            src="/landing/patterns/light/pattern_ai.webp",
            class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none",
        ),
        rx.box(
            hi("magic-wand-01", class_name="shrink-0"),
            rx.el.span("AI Builder", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-violet-9",
        ),
        rx.el.h2(
            """Instantly turn your ideas into real apps. 
Try AI-powered generation""",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            """Describe what you want to build, and AI will generate a working Python app instantly 
—complete with a backend, frontend, and database integration.""",
            class_name="text-slate-11 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 p-10 justify-center items-center relative overflow-hidden h-[22.75rem]",
    )


def gallery_item(item: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=f"{SCREENSHOT_BUCKET}{item}",
            class_name="absolute top-0 left-0 w-full h-full object-cover hover:scale-105 transition-all duration-200 ease-out object-center",
        ),
        href=f"{REFLEX_BUILD_URL}gen/{item}/",
        is_external=True,
        class_name="relative overflow-hidden border-slate-3 border rounded-[1.125rem] h-[14rem] bg-slate-2 flex justify-center items-center w-full shadow-small",
    )


def gallery() -> rx.Component:
    return rx.box(
        rx.foreach(
            AIBuilderGallery.items,
            lambda item: gallery_item(item),
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4",
    )


def ai_section() -> rx.Component:
    return rx.el.section(
        header(),
        gallery(),
        # on_mount=AIBuilderGallery.fetch_items,
        class_name="flex flex-col mx-auto w-full max-w-[84.19rem]",
    )
