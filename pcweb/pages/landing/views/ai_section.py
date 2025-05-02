import reflex as rx
import httpx
from pcweb.components.icons.hugeicons import hi
from pcweb.constants import SCREENSHOT_BUCKET, REFLEX_BUILD_URL, RX_CLOUD_BACKEND


class AIBuilderGallery(rx.State):
    items: list[str] = [
        "a0534e5a-53a6-4d34-bf44-fe7f2ab8e1bc",
        "d01840cc-13eb-4583-8782-1edd3dff1470",
        "87ac20d4-a1c5-4145-965c-085da602c89d",
        "a51dd890-5350-4b4c-97ca-16a2e0c609bb",
        "af522f77-87f1-43f7-ba92-62e9672308e0",
        "f4732ca5-3abe-433c-9197-8359f36306d7",
        "91099fa1-aa5a-4adc-955d-db4c9d4482a1",
        "62cea375-fe2e-41a3-b5b3-7f0bdc1a1503",
        "5e13d767-8f71-439f-963f-fe7fd805a4c3",
        "1264fe69-b26a-49df-b5a8-53c108dcdad2",
    ]

    # @rx.event
    # async def fetch_items(self):
    #     async with httpx.AsyncClient() as client:
    #         response = await client.get(f"{RX_CLOUD_BACKEND}v1/flexgen/templates")
    #         # self.items = response.json()


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
        href=f"{REFLEX_BUILD_URL}gen/{item}",
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
