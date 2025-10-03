import reflex as rx
import reflex_ui as ui

from reflex.experimental import ClientStateVar

from .integration_list import get_integration_path
from .integration_request import request_integration_dialog

selected_filter = ClientStateVar.create("selected_filter", "All")

FilterOptions = [
    {"name": "AI", "icon": "BotIcon"},
    {"name": "DevTools", "icon": "WorkflowSquare10Icon"},
    {"name": "Data Infrastructure", "icon": "DatabaseAddIcon"},
    {"name": "Authentication", "icon": "LockPasswordIcon"},
    {"name": "All", "icon":"CellsIcon"},
]


def integration_filter_button(data: dict):

    active_pill = "border border-violet-8 bg-violet-3 hover:bg-violet-3 !text-violet-10"

    return ui.button(
        ui.icon(icon=data["icon"]),
        rx.el.p(data["name"], class_name="text-sm"),
        variant="outline",
        class_name="flex flex-row items-center " + rx.cond(selected_filter.value == data["name"], active_pill, "").to(str),
        on_click=selected_filter.set_value(data["name"])
    )

def integration_filters():
    return rx.el.div(
        rx.el.div(
            *[integration_filter_button(data) for data in FilterOptions],
            class_name="flex flex-row gap-3 items-center justify-center flex-wrap"
        ),
        class_name="w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-12"
    )



def integration_gallery_cards(data):
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=rx.color_mode_cond(
                        f"/integrations/{data['name']}.svg",
                        f"/integrations/{data['name']}_light.svg",
                    ),
                    class_name="size-8",
                ),
                rx.link(
                    ui.button("Learn More", variant="outline", class_name="group-hover:bg-secondary-2 hover:bg-transparent"),
                    href=data['path'],
                    text_decoration="none",
                ),
                class_name="w-full flex flex-row items-center justify-between"
            ),
            rx.el.div(
                rx.el.p(data['title'], class_name="text-lg font-semibold text-secondary-12"),
                rx.el.p(data['description'], class_name="font-medium text-secondary-11 leading-[1.35]"),
                class_name="flex flex-col gap-y-1"
            ),
            class_name="flex flex-col gap-y-6 rounded-ui-xl border border-secondary-a4 bg-secondary-1 shadow-small p-6 h-[13rem] justify-between hover:bg-secondary-2"
        ),
        href=data['path'],
        class_name="group text-inherit hover:!text-inherit decoration-none no-underline "
        + rx.cond(
            (selected_filter.value == data['tags']) | (selected_filter.value == "All"), "flex", "hidden"
        ),
    )

def integration_gallery():
    return rx.el.div(
        rx.el.div(
            *[
                integration_gallery_cards(list(item.values())[0])
                for item in get_integration_path()
            ],
            class_name="w-full lg:max-w-[80rem] grid lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-6 px-4 md:px-10"
        ),
        class_name=""
    )

def integration_request_form():
    return rx.el.div(
        rx.el.p("Missing an integration?"),
        rx.el.p(rx.fragment("Click ", request_integration_dialog(), " to tell us what you need.")),
        class_name="w-full max-w-[64.19rem] flex flex-col gap-y-1 text-md font-semibold py-10 items-center justify-center lg:border-x border-slate-3"
    )
