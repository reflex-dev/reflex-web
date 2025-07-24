import reflex as rx


def gallery_app_card(app: dict) -> rx.Component:
    return rx.box(
        rx.box(
            rx.link(
                rx.image(
                    src=app["image"],
                    loading="lazy",
                    alt="Image preview for app: " + app["title"],
                    class_name="w-full h-full duration-150 object-top object-cover hover:scale-105 transition-transform ease-out",
                ),
                href=f"/docs/getting-started/open-source-templates/{app['url'].replace(' ', '-').lower()}",
            ),
            class_name="relative border-slate-5 border-b border-solid w-full overflow-hidden h-[11.5rem]",
        ),
        rx.box(
            rx.text(
                app["title"],
                class_name="font-smbold text-slate-12 truncate",
                width="100%",
            ),
            rx.text(
                app["description"],
                class_name="text-slate-10 font-small truncate text-pretty",
                width="100%",
            ),
            class_name="flex flex-col items-start gap-2 p-6 w-full h-auto",
        ),
        class_name="box-border flex flex-col border-slate-4 bg-slate-2 shadow-large border rounded-xl w-full h-auto overflow-hidden",
    )


templates_name_map = {
    "dalle": "DALL-E",
    "sales": "Sales App",
    "nba": "NBA App",
    "reflex-llamaindex-template": "LLamaIndex App",
    "ai_image_gen": "AI Image Gen",
    "dashboard": "Dashboard",
    "customer_data_app": "Customer Data App",
    "ci_template": "CI/CD Template",
    "reflex-chat": "Chat App",
    "api_admin_panel": "API Admin Panel",
}


def component_grid() -> rx.Component:
    from pcweb.pages.gallery.apps import gallery_apps_data

    posts = []
    for path, document in list(gallery_apps_data.items()):
        document.metadata["url"] = document.metadata["title"]
        document.metadata["title"] = templates_name_map.get(
            document.metadata["title"], document.metadata["title"]
        )
        # Skip the DALL-E template
        if document.metadata["title"] == "DALL-E":
            continue
        posts.append(gallery_app_card(app=document.metadata))
    return rx.box(
        *posts,
        class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[22.5rem] w-full",
    )


def templates() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Quickly start with a template.",
                class_name="lg:text-3xl text-xl font-semibold text-slate-12 text-balance",
            ),
            rx.el.span(
                "Select one to continue",
                class_name="lg:text-3xl text-xl font-semibold text-slate-9 z-[1] text-balance",
            ),
            class_name="flex flex-col text-center pb-[3rem] max-w-[64.19rem] lg:border-x border-slate-3 border-t pt-[5rem] w-full mx-auto",
        ),
        component_grid(),
        rx.box(
            class_name="flex flex-col text-center pb-[3rem] max-w-[64.19rem] lg:border-x border-slate-3 pt-[5rem] w-full mx-auto",
        ),
        class_name="flex flex-col justify-center w-full h-auto relative max-w-[70.19rem] mx-auto",
    )
