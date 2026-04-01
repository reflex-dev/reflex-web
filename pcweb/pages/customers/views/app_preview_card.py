import reflex as rx
from reflex_image_zoom import image_zoom


def app_preview_card(image_url: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.06)_inset] dark:shadow-[0_0_0_0.5px_rgba(255,255,255,0.06)_inset] bg-secondary-4 rounded-full"
                        ),
                        rx.el.div(
                            class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.06)_inset] dark:shadow-[0_0_0_0.5px_rgba(255,255,255,0.06)_inset] bg-secondary-4 rounded-full"
                        ),
                        rx.el.div(
                            class_name="size-2 shadow-[0_0_0_0.5px_rgba(0,0,0,0.06)_inset] dark:shadow-[0_0_0_0.5px_rgba(255,255,255,0.06)_inset] bg-secondary-4 rounded-full"
                        ),
                        class_name="flex shrink-0 flex-row items-center gap-1",
                    ),
                    rx.el.p(
                        text,
                        class_name="absolute left-1/2 top-1/2 max-w-[calc(100%-5rem)] -translate-x-1/2 -translate-y-1/2 truncate text-center text-sm font-medium text-secondary-11",
                    ),
                    class_name="relative flex min-h-8 w-full shrink-0 flex-row items-center dark:border-b border-secondary-4 p-3 shadow-[0_0_0_1px_rgba(0,0,0,0.03),0_4px_4px_0_rgba(0,0,0,0.03),0_1px_2px_0_rgba(0,0,0,0.04)] dark:shadow-none",
                ),
                image_zoom(
                    rx.image(
                        src=image_url,
                        alt="App preview",
                        class_name="w-full h-full object-cover object-top h-full",
                    ),
                ),
                class_name="flex flex-col rounded-tl-xl w-full bg-white-1",
            ),
            class_name="list-inside flex flex-row relative rounded-xl bg-white-1 w-full overflow-hidden border border-black/10 dark:border-secondary-4 shadow-medium dark:shadow-none w-full mb-8",
        ),
    )
