import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.meta.meta import blog_index_jsonld, create_meta_tags
from pcweb.signup import IndexState
from pcweb.templates.marketing_page import marketing_page

from .page import page
from .paths import blog_data, blog_data_visible

blog_filter_cs = ClientStateVar.create("blog_filter", default="All")

FILTERS = ["All", "Announcements", "Open Source", "Builder", "Cloud"]


def filter_button(filter: str) -> rx.Component:
    active_cn = "shadow-[inset_0_-1px_0_0_var(--primary-10)] text-primary-10 dark:text-primary-9"
    return marketing_button(
        filter,
        variant="ghost",
        size="sm",
        on_click=blog_filter_cs.set_value(filter),
        class_name=ui.cn(
            "h-full rounded-none",
            rx.cond(blog_filter_cs.value == filter, active_cn, ""),
        ),
    )


def blog_filters_row() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            *[filter_button(filter) for filter in FILTERS],
            class_name="flex flex-row gap-2 items-center px-4 h-full",
        ),
        newsletter_input(),
        class_name=ui.cn(
            "flex flex-row gap-4 items-center justify-between h-[3.25rem] border-x border-m-slate-4 dark:border-m-slate-10 bg-m-slate-1 dark:bg-m-slate-11 [box-shadow:0_-1px_0_0_rgba(0,_0,_0,_0.05),_0_-2px_2px_1px_rgba(0,_0,_0,_0.02),_0_1px_1px_0_rgba(0,_0,_0,_0.08),_0_4px_8px_0_rgba(0,_0,_0,_0.03),_0_1px_0_0_#FFF_inset] w-full z-10 lg:sticky dark:shadow-none max-lg:overflow-x-auto max-lg:-mx-4 max-lg:w-[calc(100%+2rem)]",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "lg:top-[7rem]",
                "lg:top-[4.5rem]",
            ),
        ),
    )


def newsletter_input() -> rx.Component:
    return rx.el.div(
        rx.cond(
            IndexState.signed_up,
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        tag="circle-check",
                        size=16,
                        class_name="!text-violet-9",
                    ),
                    rx.text(
                        "Thanks for subscribing!",
                        class_name="text-sm text-m-slate-7 dark:text-m-slate-6 font-medium",
                    ),
                    class_name="flex flex-row items-center gap-2",
                ),
                marketing_button(
                    "Sign up for another email",
                    variant="outline",
                    size="md",
                    on_click=IndexState.signup_for_another_user,
                ),
                class_name="flex flex-row items-center gap-2",
            ),
            rx.form(
                rx.el.input(
                    placeholder="Email",
                    name="input_email",
                    type="email",
                    required=True,
                    class_name="relative [box-shadow:0_-1px_0_0_rgba(0,_0,_0,_0.08)_inset,_0_0_0_1px_rgba(0,_0,_0,_0.08)_inset,_0_1px_2px_0_rgba(0,_0,_0,_0.02),_0_1px_4px_0_rgba(0,_0,_0,_0.02)] rounded-lg h-9 px-2.5 py-1.5 w-[12rem] text-sm placeholder:text-m-slate-7 dark:placeholder:text-m-slate-6 font-[525] focus:outline-none outline-none dark:border dark:border-m-slate-10 bg-white dark:bg-m-slate-12",
                ),
                marketing_button(
                    "Get Updates",
                    type="submit",
                    variant="outline",
                    size="md",
                    class_name="w-fit max-w-full",
                ),
                class_name="w-full flex flex-col lg:flex-row gap-2 lg:items-center items-start max-lg:hidden",
                on_submit=IndexState.signup,
            ),
        ),
        class_name="ml-auto mr-2",
    )


def card_inner(meta: dict, path: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=(
                    meta.get("image", "")
                    if meta.get("image", "").startswith(("http://", "https://"))
                    else f"{REFLEX_ASSETS_CDN}{meta.get('image', '').lstrip('/')}"
                ),
                loading="eager",
                custom_attrs={"fetchPriority": "high"},
                alt="Image preview for blog post: " + str(meta["title"]),
                class_name="group-hover:scale-105 w-full h-full transition-transform duration-150 ease-out object-top object-cover",
            ),
            class_name="relative flex-shrink-0 border-slate-5 border-b border-solid w-full h-[17.5rem] overflow-hidden",
        )
        if meta.get("image")
        else rx.fragment(),
        rx.el.div(
            rx.el.span(
                meta["title"],
                class_name="text-2xl font-[575] text-m-slate-12 dark:text-m-slate-3 mb-4 line-clamp-3",
            ),
            rx.el.p(
                meta["description"],
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475] mb-6 line-clamp-3",
            ),
            rx.el.span(
                meta["author"],
                class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525] mt-auto",
            ),
            class_name="flex flex-col w-full h-full pb-8 px-8",
        ),
        to=path,
        class_name="flex flex-col gap-8 rounded-xl backdrop-blur-[16px] [box-shadow:0_-2px_2px_1px_rgba(0,_0,_0,_0.02),_0_1px_1px_0_rgba(0,_0,_0,_0.08),_0_4px_8px_0_rgba(0,_0,_0,_0.03)] bg-white-1 dark:bg-m-slate-11 overflow-hidden group h-full",
    )


def card_content(meta: dict, path: str, class_name: str = "") -> rx.Component:
    return rx.el.div(
        card_inner(meta, path),
        display=rx.cond(
            (blog_filter_cs.value == "All")
            | (blog_filter_cs.value == meta.get("tag", "")),
            "block",
            "none",
        ),
        class_name=ui.cn(
            "relative border-y border-m-slate-4 dark:border-m-slate-10 lg:before:absolute lg:before:w-[calc(2rem+2px)] lg:before:-left-[calc(2rem+1px)] lg:before:-top-[0.5px] lg:before:-bottom-[0.5px] lg:before:border-y lg:before:border-m-slate-4 lg:dark:before:border-m-slate-10 lg:max-xl:odd:border-r lg:max-xl:even:border-l lg:max-xl:even:before:content-[''] xl:[&:nth-child(3n+1)]:border-r xl:[&:nth-child(3n+2)]:border-l xl:[&:nth-child(3n+2)]:border-r xl:[&:nth-child(3n+2)]:before:content-[''] xl:[&:nth-child(3n)]:border-l xl:[&:nth-child(3n)]:before:content-['']",
            class_name,
        ),
    )


def component_grid() -> rx.Component:
    posts = [
        card_content(meta=doc.metadata, path=f"/blog/{path}")
        for path, doc in blog_data_visible()
    ]
    return rx.el.div(
        *posts,
        rx.el.div(
            class_name="absolute -top-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -left-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -right-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        class_name="grid lg:grid-cols-2 xl:grid-cols-3 grid-cols-1 lg:border border-m-slate-4 dark:border-m-slate-10 w-full gap-x-8 gap-y-8 lg:gap-y-24 relative py-24",
    )


@marketing_page(
    path="/blog",
    title="Reflex Blog - Python Web App Development",
    description="Reflex blog: tutorials, framework comparisons, release notes, and tips for building Python web apps, dashboards, and internal tools.",
    image=f"{REFLEX_ASSETS_CDN}previews/index_preview.webp",
    meta=create_meta_tags(
        title="Reflex Blog - Python Web App Development",
        description="Reflex blog: tutorials, framework comparisons, release notes, and tips for building Python web apps, dashboards, and internal tools.",
        image=f"{REFLEX_ASSETS_CDN}previews/index_preview.webp",
        url="https://reflex.dev/blog",
    ),
)
def blogs():
    posts = [(path, doc.metadata) for path, doc in list(blog_data.items())[:20]]
    return rx.el.section(
        blog_index_jsonld(posts, url="https://reflex.dev/blog"),
        rx.el.header(
            rx.el.h1(
                "Reflex Blog - Python Web App Development",
                class_name="text-4xl font-[575] text-m-slate-12 dark:text-m-slate-3 text-center",
            ),
            rx.el.h2(
                "Reflex is the open-source framework empowering Python ",
                rx.el.br(class_name=""),
                " developers to build web apps faster.",
                class_name="font-medium text-center text-m-slate-7 dark:text-m-slate-6 text-base",
            ),
            class_name="pb-12 pt-24 lg:border-x border-m-slate-4 dark:border-m-slate-10 flex flex-col justify-center items-center gap-6 w-full",
        ),
        blog_filters_row(),
        component_grid(),
        id="blog",
        class_name="flex flex-col justify-center items-center max-w-(--docs-layout-max-width) mx-auto w-full max-lg:px-4",
    )


blog_routes = [blogs]
for path, document in blog_data.items():
    # Get the docpage component.
    route = f"/blog/{path}"
    title = rx.utils.format.to_snake_case(path.rsplit("/", 1)[1].replace(".md", ""))
    # Use title_tag for <title> and og/twitter if provided, otherwise fall back to title.
    seo_title = document.metadata.get("title_tag") or document.metadata["title"]
    comp = marketing_page(
        path=route,
        title=seo_title,
        description=document.metadata["description"],
        image=document.metadata.get("image") or None,
        meta=create_meta_tags(
            title=seo_title,
            description=document.metadata["description"],
            image=document.metadata.get("image") or None,
            url=f"https://reflex.dev{route}",
        ),
    )(lambda doc=document, route=route: page(doc, route))

    # Add the route to the list of routes.
    blog_routes.append(comp)
