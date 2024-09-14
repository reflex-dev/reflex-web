import reflex as rx

from pcweb.templates.webpage import webpage
from .state import SideBarState
from pcweb.components.webpage.comps import h1_title
from pcweb.components.icons.icons import get_icon
from pcweb.components.code_card import code_card, community_code_card


@rx.memo
def skeleton_card() -> rx.Component:
    return rx.skeleton(
        class_name="box-border shadow-large border rounded-xl w-full h-[280px] overflow-hidden",
        loading=True,
    )


def component_grid() -> rx.Component:
    return rx.box(
        rx.cond(
            SideBarState.loading,
            rx.foreach(
                rx.Var.range(12),
                lambda i: skeleton_card(),
            ),
            rx.foreach(
                SideBarState.example_apps_to_return, lambda app: code_card(app=app)
            ),
        ),
        class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full mb-[7.5rem]",
    )


def community_component_grid() -> rx.Component:
    return rx.box(
        rx.cond(
            SideBarState.loading,
            rx.foreach(
                rx.Var.range(12),
                lambda i: skeleton_card(),
            ),
            rx.foreach(
                SideBarState.community_apps_to_return,
                lambda app: community_code_card(app=app),
            ),
        ),
        class_name="gap-6 grid grid-cols-1 lg:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full",
    )


def pagination() -> rx.Component:
    return rx.box(
        rx.el.button(
            get_icon(icon="arrow_right", class_name="p-[5px] rotate-180"),
            rx.text("Previous"),
            on_click=SideBarState.set_page(SideBarState.page - 1),
            class_name="flex flex-row items-center gap-2 font-small text-slate-9 hover:text-slate-11 transition-color",
        ),
        rx.text(SideBarState.page, class_name="font-small text-slate-9"),
        rx.el.button(
            rx.text("Next"),
            get_icon(icon="arrow_right", class_name="p-[5px]"),
            on_click=SideBarState.set_page(SideBarState.page + 1),
            class_name="flex flex-row items-center gap-2 font-small text-slate-9 hover:text-slate-11 transition-color",
        ),
        class_name="flex flex-row justify-center items-center gap-3",
    )


def gallery_heading() -> rx.Component:
    return rx.box(
        # pill(text="Apps made in Reflex"),
        h1_title(title="Reflex Showcase"),
        rx.el.h2(
            """Check out what the community is building with Reflex. See 2000+ more public projects on """,
            rx.link(
                "Github",
                href="https://github.com/reflex-dev/reflex/network/dependents",
                is_external=True,
            ),
            ".",  
            class_name="font-md text-balance text-slate-9",
        ),
        class_name="section-header",
    )


def filter_item(icon: str, text: str) -> rx.Component:
    is_selected = SideBarState.sort_by == text
    active_class_name = rx.cond(is_selected, " bg-slate-3", " text-slate-9 bg-slate-1")
    return rx.box(
        rx.icon(icon, size=20),
        rx.text(text, class_name="font-small"),
        rx.spacer(),
        rx.cond(
            is_selected,
            rx.box(
                class_name="justify-end bg-violet-9 rounded-full w-2 h-2",
            ),
        ),
        on_click=SideBarState.set_sort_by(text),
        class_name="flex flex-row items-center gap-[0.875rem] hover:bg-slate-3 px- px-3.5 py-2 w-full transition-bg cursor-pointer overflow-hidden"
        + active_class_name,
    )


def sorting_filters() -> rx.Component:
    return rx.box(
        filter_item(
            "eye",
            "Views",
        ),
        filter_item(
            "history",
            "Updated at",
        ),
        filter_item(
            "history",
            "Created at",
        ),
        class_name="flex flex-col divide-y divide-slate-5 w-full",
    )


def sorting_filters_dropdown_menu() -> rx.Component:
    condition = SideBarState.sort_by != ""
    common_class_name = "flex flex-row items-center gap-3 p-[6px_12px] rounded-full transition-bg cursor-pointer shadow-large outline-none box-border "
    active_class_name = "bg-violet-9 hover:bg-violet-9 border-none text-[#fff]"
    unactive_class_name = (
        "border-slate-5 bg-slate-1 border text-slate-9 hover:bg-slate-3"
    )
    return rx.popover.root(
        rx.popover.trigger(
            rx.el.button(
                rx.text(
                    "Sort",
                    rx.cond(
                        condition,
                        rx.text(
                            f": {SideBarState.sort_by}",
                            as_="span",
                            text_wrap="nowrap",
                        ),
                    ),
                    as_="span",
                    class_name="font-small",
                ),
                get_icon(icon="select"),
            ),
            class_name=common_class_name
            + rx.cond(
                condition,
                active_class_name,
                unactive_class_name,
            ),
        ),
        rx.popover.content(
            rx.box(
                sorting_filters(),
                class_name="box-border bg-slate-2 box-shadow-large p-0 rounded-xl w-[191px] h-auto text-slate-9 cursor-default overflow-hidden",
            ),
            align="center",
            padding="0px",
            class_name="items-center bg-transparent shadow-[none] border-none overflow-visible",
        ),
        width="100%",
    )


def sorting_menu() -> rx.Component:
    return rx.box(
        rx.el.button(
            rx.icon(
                "arrow-up-narrow-wide",
                size=16,
                class_name="flex-shrink-0"
                + rx.cond(SideBarState.is_reverse, " rotate-180", ""),
            ),
            on_click=SideBarState.toggle_sort_order(~SideBarState.is_reverse),
            class_name="flex justify-center items-center border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-large p-[0.125rem_0.75rem] border rounded-full w-8 h-8 text-slate-9 transition-bg cursor-pointer",
        ),
        sorting_filters_dropdown_menu(),
        class_name="flex flex-row justify-end gap-2 w-full",
    )


@webpage(path="/gallery", title="Gallery · Reflex")
def gallery() -> rx.Component:
    return rx.el.section(
        gallery_heading(),
        component_grid(),
        id="gallery",
        class_name="section-content",
        on_mount=SideBarState.fetch_apps_list,
    )
