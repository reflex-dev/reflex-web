import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog

from pcweb.components.docpage.navbar.buttons.sidebar import navbar_sidebar_button
from pcweb.components.marketing_button import button
from pcweb.constants import REFLEX_BUILD_URL
from pcweb.views.marketing_navbar import (
    about_content,
    github,
    logo,
    menu_trigger,
    platform_content,
    resources_content,
    solutions_content,
)


def menu_item(text: str, href: str, active_str: str = "") -> rx.Component:
    router_path = rx.State.router.page.path
    active_cn = "shadow-[inset_0_-1px_0_0_var(--primary-10)] [&_button]:text-primary-10 [&_div]:text-primary-10"

    # For paths starting with "/" (like Start), use exact match
    # For "framework", it's the default - active when in /docs but not matching other sections
    # For other segments (like "ai-builder"), use contains
    if active_str.startswith("/"):
        active = router_path == active_str
    elif active_str == "framework":
        # Framework is active when in /docs but not in other specific sections
        is_docs = router_path.contains("/docs")
        is_ai_builder = router_path.contains("ai-builder")
        is_enterprise = router_path.contains("enterprise")
        is_hosting = router_path.contains("hosting")
        is_start = router_path == "/docs"
        active = is_docs & ~is_ai_builder & ~is_enterprise & ~is_hosting & ~is_start
    else:
        active = router_path.contains(active_str)

    return ui.navigation_menu.item(
        rx.el.a(
            button(
                text,
                size="sm",
                variant="ghost",
                native_button=False,
            ),
            to=href,
        ),
        class_name=ui.cn(
            "xl:flex hidden h-full items-center justify-center",
            rx.cond(active, active_cn, ""),
        ),
        custom_attrs={"role": "menuitem"},
    )


def navigation_menu() -> rx.Component:
    return ui.navigation_menu.root(
        ui.navigation_menu.list(
            menu_trigger("Platform", platform_content()),
            menu_trigger("Solutions", solutions_content()),
            menu_trigger("Resources", resources_content()),
            ui.navigation_menu.item(
                rx.el.a(
                    button(
                        "Pricing",
                        size="sm",
                        variant="ghost",
                        native_button=False,
                    ),
                    to="/pricing",
                ),
                class_name="xl:flex hidden px-1",
                custom_attrs={"role": "menuitem"},
            ),
            ui.navigation_menu.item(
                rx.el.a(
                    button(
                        "Docs",
                        size="sm",
                        variant="ghost",
                    ),
                    to="/docs",
                ),
                class_name="xl:flex hidden px-1",
                custom_attrs={"role": "menuitem"},
            ),
            menu_trigger("About", about_content()),
            class_name="flex flex-row items-center m-0 h-full list-none",
            custom_attrs={"role": "menubar"},
        ),
        ui.navigation_menu.list(
            ui.navigation_menu.item(
                github(),
                custom_attrs={"role": "menuitem"},
            ),
            ui.navigation_menu.item(
                rx.el.a(
                    button(
                        "Sign In",
                        ui.icon("Login01Icon", class_name="scale-x-[-1]"),
                        size="sm",
                        variant="outline",
                        native_button=False,
                    ),
                    to=f"{REFLEX_BUILD_URL.strip('/')}/cloud-login?redirect_to={REFLEX_BUILD_URL.strip('/')}/callback/",
                    target="_blank",
                ),
                custom_attrs={"role": "menuitem"},
            ),
            ui.navigation_menu.item(
                demo_form_dialog(
                    trigger=button(
                        "Book a Demo",
                        size="sm",
                        variant="primary",
                        class_name=" whitespace-nowrap max-xl:hidden",
                        native_button=False,
                    ),
                ),
                unstyled=True,
                class_name="xl:flex hidden",
                custom_attrs={"role": "menuitem"},
            ),
            ui.navigation_menu.item(
                navbar_sidebar_button(),
                class_name="xl:hidden flex",
                unstyled=True,
                custom_attrs={"role": "menuitem"},
            ),
            class_name="flex flex-row lg:gap-4 gap-2 m-0 h-full list-none items-center",
            custom_attrs={"role": "menubar"},
        ),
        ui.navigation_menu.portal(
            ui.navigation_menu.positioner(
                ui.navigation_menu.popup(
                    ui.navigation_menu.viewport(
                        unstyled=True,
                        class_name="relative h-full w-full overflow-hidden rounded-[inherit]",
                    ),
                    unstyled=True,
                    class_name="relative h-[var(--popup-height)] w-[var(--popup-width)] origin-[var(--transform-origin)] rounded-xl bg-m-slate-1 dark:bg-m-slate-12 navbar-shadow transition-[opacity,transform,width,height,scale,translate] duration-150 ease-[cubic-bezier(0.22,1,0.36,1)] data-[ending-style]:ease-[ease] data-[ending-style]:scale-90 data-[ending-style]:opacity-0 data-[ending-style]:duration-150 data-[starting-style]:scale-90 data-[starting-style]:opacity-0",
                ),
                unstyled=True,
                class_name="safari-nav-positioner box-border h-[var(--positioner-height)] w-[var(--positioner-width)] max-w-[var(--available-width)] transition-[top,left,right,bottom] duration-[0.35s] ease-[cubic-bezier(0.22,1,0.36,1)] data-[instant]:transition-none",
                side_offset=30,
                align="start",
                align_offset=-20,
                position_method="fixed",
            ),
        ),
        unstyled=True,
        class_name="relative flex w-full items-center h-full justify-between gap-6 mx-auto flex-row",
    )


@rx.memo
def secondary_navbar() -> rx.Component:
    from pcweb.components.hosting_banner import hosting_banner

    return rx.el.div(
        hosting_banner(),
        rx.el.header(
            rx.el.div(
                logo(),
                navigation_menu(),
                class_name="relative flex w-full items-center h-full justify-between gap-6 mx-auto flex-row max-w-[108rem]",
            ),
            class_name="w-full max-full h-[4.5rem] mx-auto flex flex-row items-center 3xl:px-16 px-6 backdrop-blur-[16px] shadow-[0_-2px_2px_1px_rgba(0,0,0,0.02),0_1px_1px_0_rgba(0,0,0,0.08),0_4px_8px_0_rgba(0,0,0,0.03),0_0_0_1px_#FFF_inset] dark:shadow-none dark:border-b dark:border-m-slate-10 bg-gradient-to-b from-white to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12",
        ),
        class_name="flex flex-col w-full top-0 z-[9999] fixed self-center",
    )
