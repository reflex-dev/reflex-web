import os
import reflex as rx
import typesense

CLUSTERS = {
    "All Content": [],
    "AI Builder": ["ai_builder"],
    "Hosting": ["hosting"],
    "Components": ["custom-components", "recipes"],
    "Enterprise": ["enterprise"],
    "API Reference": ["api-reference", "api-routes"],
    "Docs": ["advanced_onboarding", "assets", "authentication", "client_storage", "components", "database", "events", "getting_started", "library", "pages", "state", "state_structure", "styling", "ui", "utility_methods", "vars", "wrapping-react"],
    "Blog Posts": []
}

# Typesense configuration
TYPESENSE_CONFIG = {
    "nodes": [{"host": os.getenv("TYPESENSE_HOST"), "port": "443", "protocol": "https"}],
    "api_key": os.getenv("TYPESENSE_SEARCH_API_KEY"),
    "connection_timeout_seconds": 2,
}

# Score cutoff to filter weak results
CUTOFF = 0.6

class SimpleSearch(rx.State):
    query: str
    selected_filter: str = "All Content"
    is_fetching: bool = False

    # Results - keeping same structure as your fuzzy search
    idxed_docs_results: list[dict] = []
    idxed_blogs_results: list[dict] = []

    @rx.event
    def reset_search(self):
        """Reset state variables"""
        self.idxed_blogs_results = []
        self.idxed_docs_results = []
        self.query = ""

    @rx.event
    async def apply_filter_search(self, selected_filter: str):
        """Re-run search with new filter"""
        if self.selected_filter == selected_filter:
            return

        self.selected_filter = selected_filter

        if self.query.strip():
            yield SimpleSearch.perform_search()

    @rx.event(background=True)
    async def perform_search(self):
        """Perform Typesense search and split results"""
        async with self:
            if not self.query.strip():
                self.idxed_docs_results = []
                self.idxed_blogs_results = []
                return

        try:
            async with self:
                self.is_fetching = False
                yield

            client = typesense.Client(TYPESENSE_CONFIG)

            # Build search parameters
            search_params = {
                "q": self.query,
                "query_by": "title,content,headings",
                "query_by_weights": "10,3,5",
                "per_page": 15,
                "num_typos": 1,
                "sort_by": "_text_match:desc",
            }

            # Apply filter
            if self.selected_filter != "All Content":
                if self.selected_filter == "Blog Posts":
                    search_params["filter_by"] = "section:=Blog"
                else:
                    # Map cluster to sections
                    sections = self._get_sections_for_cluster(self.selected_filter)
                    if sections:
                        section_filter = " || ".join(f"section:={s}" for s in sections)
                        search_params["filter_by"] = section_filter

            # Perform search
            result = client.collections["docs"].documents.search(search_params)

            # Split results into docs and blogs
            docs_results = []
            blog_results = []

            for hit in result["hits"]:
                doc = hit["document"]
                formatted_doc = self._format_result(doc)

                if doc.get("section") == "Blog":
                    blog_results.append(formatted_doc)
                else:
                    docs_results.append(formatted_doc)

            async with self:
                self.idxed_docs_results = docs_results
                self.idxed_blogs_results = blog_results
                self.is_fetching = False

        except Exception as e:
            print(f"Search error: {e}")
            async with self:
                self.idxed_docs_results = []
                self.idxed_blogs_results = []
                self.is_fetching = False

    def _get_sections_for_cluster(self, cluster_name: str) -> list[str]:
        """Map cluster names to section names"""
        cluster_mapping = {
            "AI Builder": ["ai_builder"],
            "Hosting": ["hosting"],
            "Components": ["library", "components", "custom-components", "wrapping-react"],
            "Enterprise": ["enterprise"],
            "API Reference": ["api-reference", "api-routes"],
            "Docs": [
                "advanced_onboarding", "assets", "authentication", "client_storage",
                "components", "database", "events", "getting_started", "library",
                "pages", "state", "state_structure", "styling", "ui",
                "utility_methods", "vars", "wrapping-react"
            ],
        }
        return cluster_mapping.get(cluster_name, [])

    def _format_result(self, doc: dict) -> dict:
        """Format Typesense result to match your fuzzy search structure"""
        # For docs
        if doc.get("section") != "Blog":
            # Reconstruct parts from path for breadcrumb
            path_parts = doc.get("path", "").replace(".md", "").split("/")
            parts = [part.replace("-", " ").replace("_", " ").title() for part in path_parts if part]

            return {
                "name": doc.get("title", ""),
                "parts": parts,
                "url": doc.get("url", ""),
                "image": doc.get('path', ""),
                "cluster": self._get_cluster_from_section(doc.get("section", "")),
                "description": self._truncate_content(doc.get("content", "")),
            }

        # For blogs
        else:

            return {
                "title": doc.get("title", ""),
                "url": doc.get("url", ""),
                "author": doc.get("subsection", ""),  # Author stored in subsection for blogs
                "date": "2024",  # You might want to add proper date handling
                "description": self._truncate_content(doc.get("content", "")),
                "image": "/placeholder-image.jpg",  # You'll need to handle images properly
            }

    def _get_cluster_from_section(self, section: str) -> str:
        """Map section back to cluster name"""
        for cluster, sections in {
            "AI Builder": ["ai_builder"],
            "Hosting": ["hosting"],
            "Components": ["library", "components", "custom-components", "wrapping-react"],
            "Enterprise": ["enterprise"],
            "API Reference": ["api-reference", "api-routes"],
            "Docs": [
                "advanced_onboarding", "assets", "authentication", "client_storage",
                "database", "events", "getting_started", "pages", "state",
                "state_structure", "styling", "ui", "utility_methods", "vars"
            ],
        }.items():
            if section in sections:
                return cluster
        return "Docs"

    def _truncate_content(self, content: str, max_length: int = 200) -> str:
        """Truncate content for description"""
        if len(content) <= max_length:
            return content
        return content[:max_length].rstrip() + "..."


# Keep all your existing UI components exactly the same
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

def cluster_icon(filter_name: str):
    icons = {
        "All Content": "layout-grid",
        "AI Builder": "bot",
        "Hosting": "cloud",
        "Components": "component",
        "Docs": "file",
        "Enterprise": "building-2",
        "API Reference": "settings-2",
        "Blog Posts": "library-big"
    }
    return rx.icon(tag=icons.get(filter_name, "circle"), size=18)

def filter_items(filter_name: str):
    return rx.popover.close(
        rx.el.div(
            rx.el.div(
                cluster_icon(filter_name),
                rx.el.button(
                    filter_name,
                    class_name="w-full text-left",
                    type="button",
                ),
                class_name="flex flex-row items-center gap-x-3"
            ),
            rx.cond(
                SimpleSearch.selected_filter == filter_name,
                rx.icon(tag="check", size=12)
            ),
            on_click=SimpleSearch.apply_filter_search(filter_name),
            class_name="flex flex-row gap-x-2 items-center px-3 py-1 w-full justify-between cursor-pointer outline-none hover:bg-slate-3 focus:border-none",
        )
    )

def filter_icon(tag: str):
    """Helper to render icons for filters consistently."""
    return rx.icon(tag=tag, size=12)

def filter_component():
    return rx.popover.root(
        rx.popover.trigger(
            rx.el.button(
                rx.badge(
                    rx.el.div(
                        rx.el.div(
                            rx.match(
                                SimpleSearch.selected_filter,
                                ("All Content", filter_icon("layout-grid")),
                                ("AI Builder", filter_icon("bot")),
                                ("Hosting", filter_icon("cloud")),
                                ("Components", filter_icon("component")),
                                ("Docs", filter_icon("file")),
                                ("Enterprise", filter_icon("building-2")),
                                ("API Reference", filter_icon("settings-2")),
                                ("Blog Posts", filter_icon("library-big")),
                                ("", filter_icon("circle")),
                            ),
                            SimpleSearch.selected_filter,
                            class_name="text-sm flex flex-row items-center gap-x-1",
                        ),
                        rx.icon(tag="chevrons-up-down", size=12),
                        class_name="flex flex-row items-center justify-between w-full",
                    ),
                    variant="surface",
                    class_name="w-[140px] text-sm px-[5px] py-[2px]"
                ),
                class_name="flex flex-row justify-between items-center gap-x-4 rounded-md outline-none",
                type="button",
            ),
        ),
        rx.popover.content(
            rx.box(
                *[filter_items(filter_name) for filter_name in CLUSTERS.keys()],
                class_name="w-[190px] flex flex-col text-sm rounded-md shadow-md gap-y-1 py-2",
            ),
            side="left",
            side_offset=12,
            class_name="items-center !p-0 w-auto overflow-visible pointer-events-auto",
        ),
        style={
            "display": "inline-flex",
            "height": "1.925rem",
            "align_items": "baseline",
            "justify_content": "flex-start",
            "padding": "0.25rem",
        },
        class_name="rounded-md border border-slate-5",
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
                filter_component(),
                rx.box(
                    "Esc",
                    class_name="border border-slate-5 rounded-md !text-slate-9 px-[5px] py-[2px] hidden md:inline",
                    on_click=rx.run_script(
                        "document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"
                    ),
                ),
                class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm flex flex-row items-center gap-x-2",
            ),
            rx.el.input(
                on_change=[
                    lambda value: SimpleSearch.set_query(value.replace("rx.", "")).debounce(500),
                    SimpleSearch.perform_search(),
                ],
                placeholder="Search documentation ...",
                class_name="py-2 px-7 w-full placeholder:text-sm "
                + "text-sm "
                + "rounded-md bg-transparent border border-[0.5px] border-gray-500/40 "
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
        href=f"/{value['url'].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit hover:bg-slate-3",
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
            # rx.box(
            #     rx.image(
            #         src=value["image"].to(str),
            #         class_name="rounded-md",
            #         border_radius="10px 10px",
            #     ),
            #     class_name="w-full rounded-md pt-3",
            # ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=f"{value['url'].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit hover:bg-slate-3",
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
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md hover:bg-slate-3",
    )

def no_results_found():
    return rx.box(
        rx.el.p(
            rx.fragment(
                "No results found for ",
                rx.el.strong(f"'{SimpleSearch.query}'"),
            ),
        ),
        class_name="w-full flex items-center justify-center text-sm py-4",
    )

def search_content():
    return rx.scroll_area(
        rx.cond(
            SimpleSearch.query.length() < 3,
            # Show suggestions when query is too short
            rx.box(
                rx.foreach(suggestion_items, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
            # Query is 3+ characters
            rx.cond(
                SimpleSearch.is_fetching,
                rx.cond(
                    (SimpleSearch.idxed_docs_results.length() >= 1) | (SimpleSearch.idxed_blogs_results.length() >= 1),
                    rx.box(
                        # Docs results
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_docs_results,
                                lambda value: search_result(value["parts"].to(list), value)
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        # Blog results
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_blogs_results,
                                lambda value: search_result_blog(value)
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.box()
                ),
                rx.cond(
                    (SimpleSearch.idxed_docs_results.length() >= 1) | (SimpleSearch.idxed_blogs_results.length() >= 1),
                    rx.box(
                        # Docs results
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_docs_results,
                                lambda value: search_result(value["parts"].to(list), value)
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        # Blog results
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_blogs_results,
                                lambda value: search_result_blog(value)
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    no_results_found()
                )
            )
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


def typesense_search():
    """Create the main search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_input(),
                search_content(),
                on_interact_outside=SimpleSearch.reset_search,
                on_escape_key_down=SimpleSearch.reset_search,
                class_name="w-full max-w-[640px] mx-auto h-[57vh] bg-slate-1 border-none outline-none p-3 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
            ),
        ),
        keyboard_shortcut_script(),
        class_name="w-full",
    )
