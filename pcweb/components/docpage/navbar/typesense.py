import reflex as rx
from pcweb.components.docpage.navbar.docs_index import indexed_docs
from pcweb.components.docpage.navbar.blog_index import indexed_blogs
from reflex.experimental import ClientStateVar

BlogData = ClientStateVar.create("blog_Data", indexed_blogs)
SearchData = ClientStateVar.create("indexed_docs", indexed_docs)
SearchInput = ClientStateVar.create("search", "")

suggestion_items = [
    {"name": "Components Overview", "path": "/docs/library", "icon": "blocks", "description": "Discover and explore the full library of available components"},
    {"name": "State Management", "path": "/docs/state/overview", "icon": "database", "description": "Master state handling, data flow, and reactive programming"},
    {"name": "Event Overview", "path": "/docs/events/events-overview", "icon": "zap", "description": "Learn how to handle user interactions and system events"},
    {"name": "Styling and Theming", "path": "/docs/styling/overview", "icon": "palette", "description": "Customize colors, layouts, and create beautiful app designs"},
    {"name": "Deployment Guide", "path": "/docs/hosting/deploy-quick-start/", "icon": "cloud", "description": "Deploy and host your application in production environments"},
]

def keyboard_shortcut_script() -> rx.Component:
    """Add keyboard shortcut support for opening search."""
    return rx.script(
        """
        document.addEventListener('keydown', function(e) {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                document.getElementById('search-trigger').click();
            }
        });
    """
    )



def search_trigger() -> rx.Component:
    """Render the search trigger button."""
    return rx.box(
        rx.icon(
            "search",
            class_name="absolute left-2 top-1/2 transform -translate-y-1/2 text-md w-4 h-4 flex-shrink-0 !text-slate-9",
        ),
        rx.text(
            "⌘K",
            class_name="absolute right-2 top-1/2 transform -translate-y-1/2 text-sm bg-slate-3 rounded-md text-sm !text-slate-9 px-[5px] py-[2px] hidden md:inline",
        ),
        rx.el.input(
            placeholder="Search",
            read_only=True,
            class_name="bg-transparent border-none outline-none focus:outline-none pl-4 cursor-pointer hidden md:block",
        ),
        style={
            "padding": "6px 12px",
            "min_width": ["32px", "32px", "256px"],
            "max_width": ["6em", "6em", "none"],
            "box_shadow": "0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
        },
        class_name="w-full hover:bg-slate-3 cursor-pointer flex max-h-[32px] min-h-[32px] border border-slate-5 rounded-[10px] bg-slate-1 transition-bg relative",
    )


def search_breadcrumb(items):
    """Create a breadcrumb navigation component."""
    return rx.hstack(
        rx.foreach(
            items,
            lambda item, index: rx.fragment(
                rx.cond(
                    index > 0,
                    rx.el.label(
                        "›",
                        class_name="text-sm font-medium",
                        color=rx.color("slate", 11)
                    ),
                ),
                rx.el.label(
                    item,
                    class_name=rx.cond(
                        index == (items.length() - 1),
                        "text-sm font-medium",
                        "text-sm font-regular"
                    ),
                    color=rx.cond(
                        index == (items.length() - 1),
                        rx.color("slate", 12),
                        rx.color("slate", 11)
                    ),
                )
            )
        ),
        spacing="1",
        cursor="pointer"
    )

def search_input():
    return rx.box(
        rx.box(
            rx.icon(
                tag="search",
                size=14,
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 !text-gray-500/40",
            ),
            rx.box(
                "Esc",
                class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm border border-slate-5 rounded-md text-xs !text-slate-9 px-[5px] py-[2px] hidden md:inline",
                on_click=rx.run_script(
                    "document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"
                ),
            ),
            rx.el.input(
                on_change=lambda value: SearchInput.set_value(value),
                placeholder="Search documentation ...",
                class_name="py-2 px-7 w-full placeholder:text-sm "
                + "text-sm "
                + "rounded-md bg-transparent border-dashed border-[0.5px] border-gray-500/40 "
                + "focus:outline-none focus:border-gray-500/40",
            ),
            class_name="w-full relative focus:outline-none",
        ),
        class_name="w-full absolute top-0 left-0 p-3 bg-background z-[999]",
    )

def search_result(tags: list, value: dict):
    return rx.link(
        rx.box(
            rx.text(value["name"], class_name="text-sm font-bold"),
            rx.text(
                value["description"],
                class_name=(
                    "text-sm font-regular opacity-[0.81] "
                    "line-clamp-2 overflow-hidden text-ellipsis"
                ),
                style={"display": "-webkit-box", "-webkit-line-clamp": "2", "-webkit-box-orient": "vertical"},
            ),
            search_breadcrumb(tags),
            class_name="p-2 w-full flex flex-col gap-y-2 justify-start items-start align-start",
        ),
        href=f"/{value["url"].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit",
        _hover={"bg": rx.color("gray", 2)},
    )

def search_result_blog(value: dict):
    return rx.link(
        rx.box(
            rx.box(
                rx.text(value["author"]),
                "-",
                rx.text(value["date"]),
                class_name="flex flex-row gap-x-2 items-center text-sm !text-slate-10",
            ),
            rx.text(value["title"], class_name="text-md font-bold"),
            rx.text(
                value["description"],
                class_name=(
                    "text-sm font-regular opacity-[0.81] "
                    "line-clamp-2 overflow-hidden text-ellipsis"
                ),
                style={"display": "-webkit-box", "-webkit-line-clamp": "2", "-webkit-box-orient": "vertical"},
            ),
            rx.box(
                rx.image(
                    src=value["image"].to(str),
                    class_name="rounded-md",
                    border_radius="10px 10px",
                ),
                class_name="w-full rounded-md pt-3",
            ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=f"{value["url"].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit",
        _hover={"bg": rx.color("gray", 2)},
    )

def search_result_start(item: dict):
    return rx.link(
        rx.box(
            rx.box(
                rx.icon(tag=item["icon"], size=11, class_name="size-4 !text-slate-9"),
                rx.text(item["name"], class_name="text-sm font-bold"),
                class_name="flex flex-row items-center justify-start gap-x-2",
            ),
            rx.text(
                item["description"],
                class_name=(
                    "text-xs font-regular opacity-[0.81] "
                    "line-clamp-2 overflow-hidden text-ellipsis"
                ),
                style={"display": "-webkit-box", "-webkit-line-clamp": "2", "-webkit-box-orient": "vertical"},
            ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=item["path"],
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md",
        _hover={"bg": rx.color("gray", 2)},
    )

def search_content():
    return rx.scroll_area(
        rx.cond(
            SearchInput.value.length() > 0,
            rx.box(
                # ... Docs
                rx.box(
                    rx.foreach(
                        SearchData.value,
                        lambda value: rx.cond(
                            value["name"].to(str).lower().contains(SearchInput.value.lower()),
                            search_result(
                                value['parts'].to(list), value
                            ),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                # ... Blog
                # maybe add this later: divide-y divide-[0.61px] !divide-slate-5
                rx.box(
                    rx.foreach(
                        BlogData.value,
                        lambda value: rx.cond(
                            value["title"].to(str).lower().contains(SearchInput.value.lower()),
                            search_result_blog(value),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                rx.foreach(suggestion_items, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


FilterToggle = ClientStateVar.create("filter_toggle", "docs")

def toggle_doc_and_blog():
    active = "text-slate-9 bg-slate-1"
    passive = "text-slate-9"

    return rx.box(
        rx.icon("file",
            class_name=" " + rx.cond(FilterToggle.value=="docs", active, passive).to(str),
            on_click=FilterToggle.set_value('docs'),

        ),
        rx.icon("notebook-pen",
            class_name=" " + rx.cond(FilterToggle.value=="blogs", active, passive).to(str),
            on_click=FilterToggle.set_value('blogs'),
        ),
        class_name="flex flex-row bg-slate-3 items-center justify-between rounded-md divide-x divide-[0.61px] !divide-slate-5 absolute bottom-5 right-5 px-4 py-2"
    )

def typesense_search() -> rx.Component:
    """Create the main Typesense search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_input(),
                search_content(),
                # toggle_doc_and_blog(),
                on_interact_outside=SearchInput.set_value(""),
                on_escape_key_down=SearchInput.set_value(""),
                class_name="w-full max-w-[640px] mx-auto h-[60vh] bg-slate-1 border-none outline-none p-3 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
            ),
        ),
        keyboard_shortcut_script(),
        class_name="w-full",
    )
