import reflex as rx
import textdistance
import unicodedata

from pcweb.components.docpage.navbar.docs_index import indexed_docs
from pcweb.components.docpage.navbar.blog_index import indexed_blogs
from scripts.indexer import CLUSTERS

# the score cutoff -> returns only strong to medium hits without sneaking in the weaker ones + acts as a natural max cap to the results
CUTOFF = 0.6

class FuzzySearch(rx.State): # type: ignore[misc]
    query: str
    selected_filter: str = "All Content"

    idxed_docs: list[dict] = indexed_docs
    idxed_docs_results: list[dict]

    idxed_blogs: list[dict] = indexed_blogs
    idxed_blogs_results: list[dict]

    @rx.event
    def reset_search(self):
        """Reset state variables"""
        self.idxed_blogs_results = []
        self.idxed_docs_results =  []
        self.query = ""

    def _normalize_and_split_query(self) -> list[str]:
        """Helper method to normalize and split query into words."""
        return [
            unicodedata.normalize("NFKD", w.lower()).strip()
            for w in self.query.strip().split()
            if w
        ]

    def _similarity_score(self, query_word: str, target_word: str) -> float:
        """Return similarity score between 0 and 1 (higher = better)."""

        if query_word == target_word:
            return 1.0

        if target_word.startswith(query_word):
            return 0.9

        return textdistance.levenshtein.normalized_similarity(query_word, target_word)

    def _score_match(self, query_words: list[str], target_fields: list[str]) -> float:
        """Compute total match score for query vs. target fields."""
        total_score = 0.0
        for query_word in query_words:
            best_word_score = 0.0
            for field in target_fields:
                for word in field.split():
                    best_word_score = max(
                        best_word_score,
                        self._similarity_score(query_word, word)
                    )
            total_score += best_word_score
        return total_score / len(query_words) if query_words else 0.0

    @rx.event
    async def apply_filter_search(self):
        """Re-run the fuzzy search efficiently depending on selected filter."""
        if self.selected_filter == "All Content":
            yield FuzzySearch.serve_fuzzy_query()
            yield FuzzySearch.serve_fuzzy_blogs()
        elif self.selected_filter == "Blog Posts":
            self.idxed_docs_results = []
            yield FuzzySearch.serve_fuzzy_blogs()
        else:
            self.idxed_blogs_results = []
            yield FuzzySearch.serve_fuzzy_query()

    @rx.event(background=True)
    async def serve_fuzzy_blogs(self):
        async with self:
            self.idxed_blogs_results = []
            query_words = self._normalize_and_split_query()
            if not query_words:
                return

            scored_results = []
            for blog in self.idxed_blogs:
                blog_fields = [
                    unicodedata.normalize("NFKD", blog.get(key, "").lower()).strip()
                    for key in ["title", "description", "author"]
                ]

                score = self._score_match(query_words, blog_fields)

                if score > CUTOFF:
                    if self.selected_filter in ("All Content", "Blog Posts"):
                        scored_results.append((score, blog))

            scored_results.sort(key=lambda x: x[0], reverse=True)
            self.idxed_blogs_results = [b for _, b in scored_results]

    @rx.event(background=True)
    async def serve_fuzzy_query(self):
        async with self:
            self.idxed_docs_results = []
            query_words = self._normalize_and_split_query()
            if not query_words:
                return

            scored_results = []
            for doc in self.idxed_docs:
                term_words_list = [
                    unicodedata.normalize("NFKD", term.lower()).strip().split()
                    for term in doc["parts"]
                ]
                flat_terms = [w for words in term_words_list for w in words]

                score = self._score_match(query_words, flat_terms)

                if score > CUTOFF:
                    if self.selected_filter == "All Content" or doc["cluster"] == self.selected_filter:
                        scored_results.append((score, doc))

            scored_results.sort(key=lambda x: x[0], reverse=True)
            self.idxed_docs_results = [d for _, d in scored_results]


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


def search_trigger() -> rx.Component: # type: ignore[misc]
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
                FuzzySearch.selected_filter == filter_name,
                rx.icon(tag="check", size=12)
            ),
            on_click=[FuzzySearch.set_selected_filter(filter_name), FuzzySearch.apply_filter_search],
            class_name="flex flex-row gap-x-2 items-center px-3 py-1 w-full justify-between cursor-pointer outline-none hover:bg-slate-3 focus:border-none",
        )
    )

def filter_component():
    return rx.popover.root(
        rx.popover.trigger(
            rx.el.button(
                "Filters",
                class_name="text-sm px-2 flex flex-row justify-between items-center gap-x-4 rounded-md outline-none",
                type="button",
                color=rx.color("slate", 11),
            ),
        ),
        rx.popover.content(
            rx.box(
                *[filter_items(filter_name) for filter_name in CLUSTERS.keys()],
                class_name="w-[180px] flex flex-col text-sm rounded-md shadow-md gap-y-1 py-2",
            ),
            side="left",
            side_offset=12,
            class_name="items-center !shadow-none !p-0 w-auto overflow-visible pointer-events-auto",
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
            # rx.box(
            #     "Esc",
            #     class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm border border-slate-5 rounded-md text-xs !text-slate-9 px-[5px] py-[2px] hidden md:inline",
            #     on_click=rx.run_script(
            #         "document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"
            #     ),
            # ),
            rx.el.input(
                on_change=[
                    lambda value: FuzzySearch.set_query(value.replace("rx.", "")).debounce(500),
                    FuzzySearch.serve_fuzzy_query(),
                    FuzzySearch.serve_fuzzy_blogs(),
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
                rx.el.strong(f"'{FuzzySearch.query}'"),
            ),
        ),
        class_name="w-full flex items-center justify-center text-sm py-4",
    )

def search_content():
    return rx.scroll_area(
        rx.cond(
            FuzzySearch.query.length() >= 3,
            rx.cond(
                (FuzzySearch.idxed_docs_results.length() >= 1) | (FuzzySearch.idxed_blogs_results.length() >= 1),
                rx.box(
                    # Docs results
                    rx.box(
                        rx.foreach(
                            FuzzySearch.idxed_docs_results,
                            lambda value: search_result(value["parts"].to(list), value)
                        ),
                        class_name="flex flex-col gap-y-2",
                    ),
                    # Blog results
                    rx.box(
                        rx.foreach(
                            FuzzySearch.idxed_blogs_results,
                            lambda value: search_result_blog(value)
                        ),
                        class_name="flex flex-col gap-y-2",
                    ),
                    class_name="flex flex-col",
                ),
                # No results
                no_results_found(),
            ),
            rx.box(
                rx.foreach(suggestion_items, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


def reflex_fuzzy_search():
    """Create the main search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_input(),
                search_content(),
                on_interact_outside=FuzzySearch.reset_search,
                on_escape_key_down=FuzzySearch.reset_search,
                class_name="w-full max-w-[640px] mx-auto h-[60vh] bg-slate-1 border-none outline-none p-3 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
            ),
        ),
        keyboard_shortcut_script(),
        class_name="w-full",
    )
