import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.icons.icons import get_icon
from pcweb.components.marketing_button import button
from pcweb.constants import REFLEX_URL
from pcweb.flexdown import xd2 as xd
from pcweb.templates.docpage import get_toc, right_sidebar_item_highlight

from .paths import blog_data


def share_post_button(icon: str, href: str, aria_label: str) -> rx.Component:
    return rx.el.a(
        button(
            get_icon(icon),
            native_button=False,
            variant="outline",
            size="icon-sm",
            aria_label=aria_label,
        ),
        target="_blank",
        to=href,
    )


@rx.memo
def copy_link_button(url: str):
    copied = ClientStateVar.create("is_copied", default=False, global_ref=False)
    return button(
        rx.cond(
            copied.value,
            ui.icon(
                "Tick02Icon",
            ),
            get_icon("link_blog"),
        ),
        variant="outline",
        aria_label="Copy link to post",
        size="icon-sm",
        on_click=[
            rx.call_function(copied.set_value(True)),
            rx.set_clipboard(url),
        ],
        on_mouse_down=rx.call_function(copied.set_value(False)).debounce(1500),
    )


def table_of_contents(toc: list, path: str, page_url: str) -> rx.Component:
    """Render the table of contents sidebar."""
    if len(toc) < 2:
        return rx.fragment()

    return rx.el.nav(
        rx.box(
            rx.el.p(
                "On This Page",
                class_name="text-sm h-8 flex items-center justify-start font-[525] dark:text-m-slate-3 text-m-slate-12",
            ),
            rx.el.ul(
                *[
                    (
                        rx.el.li(
                            rx.el.a(
                                text,
                                class_name="text-sm font-[525] text-m-slate-7 dark:text-m-slate-6 pl-4 py-1 block hover:text-m-slate-9 dark:hover:text-m-slate-5 transition-colors truncate",
                                href=path + "#" + text.lower().replace(" ", "-"),
                            ),
                        )
                        if level == 1
                        else (
                            rx.el.li(
                                rx.el.a(
                                    text,
                                    class_name="text-sm font-[525] text-m-slate-7 dark:text-m-slate-6 pl-4 py-1 block hover:text-m-slate-9 dark:hover:text-m-slate-5 transition-colors truncate",
                                    href=path + "#" + text.lower().replace(" ", "-"),
                                ),
                            )
                            if level == 2
                            else rx.el.li(
                                rx.el.a(
                                    text,
                                    class_name="text-sm font-[525] text-m-slate-7 dark:text-m-slate-6 pl-8 py-1 block hover:text-m-slate-9 dark:hover:text-m-slate-5 transition-colors truncate",
                                    href=path + "#" + text.lower().replace(" ", "-"),
                                ),
                            )
                        )
                    )
                    for level, text in toc
                ],
                id="toc-navigation",
                class_name="flex flex-col gap-y-1 list-none shadow-[1.5px_0_0_0_var(--m-slate-4)_inset] dark:shadow-[1.5px_0_0_0_var(--m-slate-9)_inset]",
            ),
            rx.el.div(
                rx.el.span(
                    "Share Post",
                    class_name="text-m-slate-12 dark:text-m-slate-3 font-[525] text-sm",
                ),
                rx.el.div(
                    share_post_button(
                        "twitter_blog",
                        f"https://twitter.com/intent/tweet?text={page_url}",
                        "Share on Twitter",
                    ),
                    share_post_button(
                        "linkedin_blog",
                        f"https://www.linkedin.com/feed/?shareActive=true&text={page_url}",
                        "Share on LinkedIn",
                    ),
                    share_post_button(
                        "reddit_blog",
                        f"https://www.reddit.com/submit?url={page_url}",
                        "Share on Reddit",
                    ),
                    copy_link_button(url=page_url),
                    class_name="flex flex-row gap-2",
                ),
                class_name="flex flex-col gap-5 mt-6",
            ),
            class_name="flex flex-col justify-start gap-y-4 overflow-y-auto",
        ),
        on_mount=rx.call_script(right_sidebar_item_highlight()),
        class_name=ui.cn(
            "sticky w-[14rem] shrink-0 hidden xl:block self-start max-lg:hidden",
            rx.cond(
                HostingBannerState.is_banner_visible, "top-[8.5rem]", "top-[6.5rem]"
            ),
        ),
    )


def more_posts(current_post: dict) -> rx.Component:
    from .blog import card_content

    posts = []
    blog_items = list(blog_data.items())
    current_index = next(
        (
            i
            for i, (path, document) in enumerate(blog_items)
            if document.metadata.get("title") == current_post.get("title")
        ),
        None,
    )

    if current_index is None:
        # If current post is not found, default to first 3 posts
        selected_posts = blog_items[:3]
    elif current_index == 0:
        # If it's the first post, get the next 3
        selected_posts = blog_items[1:4]
    elif current_index == len(blog_items) - 1:
        # If it's the last post, get the previous 3
        selected_posts = blog_items[-4:-1]
    else:
        # Get previous 1 and next 2, excluding current post
        selected_posts = (
            blog_items[max(0, current_index - 1) : current_index]
            + blog_items[current_index + 1 : current_index + 3]
        )

    for path, document in selected_posts:
        meta = document.metadata
        posts.append(card_content(meta=meta, path=f"/blog/{path}"))
    return rx.el.section(
        rx.el.h2(
            "More Posts",
            class_name="font-x-large gradient-heading",
        ),
        rx.box(
            *posts,
            class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-[320px] w-full mb-4 blog-grid",
        ),
        class_name="flex flex-col gap-10 mt-20",
    )


def page(document, route) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    toc = get_toc(document, route)
    page_url = f"{REFLEX_URL.strip('/')}{route}"
    return rx.el.section(
        rx.el.article(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        "Blog",
                        href="/blog",
                        class_name="text-m-slate-12 dark:text-m-slate-3 font-[575] hover:text-primary-10 dark:hover:text-primary-9 text-xs",
                    ),
                    rx.el.div(class_name="w-4 h-px bg-m-slate-5 dark:bg-m-slate-10"),
                    rx.moment(
                        str(meta["date"]),
                        format="MMM DD, YYYY",
                        class_name="font-[475] text-m-slate-7 dark:text-m-slate-6 text-xs",
                    ),
                    class_name="flex flex-row items-center gap-3 mb-6",
                ),
                rx.image(
                    src=f"/common/{rx.color_mode_cond('light', 'dark')}/squares_vertical_blog.svg",
                    alt="Squares Vertical Docs",
                    loading="lazy",
                    class_name="pointer-events-none w-auto h-[calc(100%-2rem)] absolute inset-y-4 left-2 max-lg:hidden",
                ),
                rx.image(
                    src=f"/common/{rx.color_mode_cond('light', 'dark')}/squares_vertical_blog.svg",
                    alt="Squares Vertical Docs",
                    loading="lazy",
                    class_name="pointer-events-none w-auto h-[calc(100%-2rem)] absolute inset-y-4 right-2 scale-x-[-1] max-lg:hidden",
                ),
                rx.el.header(
                    rx.el.h1(
                        meta["title"],
                        class_name="lg:text-5xl text-3xl text-m-slate-12 dark:text-m-slate-3 font-[575] mb-6 text-center text-balance",
                    ),
                    rx.el.h2(
                        str(meta["description"]),
                        class_name="lg:text-base text-sm text-m-slate-7 dark:text-m-slate-6 font-[475] mb-8 text-center",
                    ),
                    rx.el.span(
                        meta["author"],
                        class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
                    ),
                    class_name="flex flex-col justify-center items-center max-w-[45rem] mx-auto w-full",
                ),
                class_name="flex flex-col justify-center items-center max-w-[69rem] lg:border-x border-m-slate-4 dark:border-m-slate-9 lg:py-16 pb-8 w-full mx-auto relative",
            ),
            rx.el.hr(
                class_name="h-[1px] w-full bg-m-slate-4 dark:bg-m-slate-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src=f"{meta['image']}",
                            alt=f"Image for blog post: {meta['title']}",
                            loading="eager",
                            custom_attrs={"fetchPriority": "high"},
                            class_name="rounded-xl object-contain w-full h-auto mb-4",
                        ),
                        rx.el.div(
                            xd.render(document, document.filename),
                            class_name="flex flex-col gap-4 w-full max-w-2xl",
                        ),
                        class_name="flex flex-col gap-12 flex-1",
                    ),
                    table_of_contents(toc, route, page_url),
                    class_name="flex flex-row gap-24 max-w-[69rem] mx-auto w-full lg:py-24 py-12",
                ),
                rx.el.div(
                    more_posts(meta),
                    class_name="max-w-[69rem] mx-auto w-full",
                ),
                class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full flex flex-col gap-12",
            ),
        ),
        class_name=ui.cn(
            "flex flex-col mx-auto max-lg:px-6 w-full relative",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "lg:pt-[7rem] pt-[11rem]",
                "lg:pt-[4rem] pt-[8rem]",
            ),
        ),
    )
