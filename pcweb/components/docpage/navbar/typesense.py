"""Improved Typesense search component with better component search handling."""

import reflex as rx
import typesense
import os
import re

# Constants
TYPESENSE_CONFIG = {
    "nodes": [
        {"host": os.getenv("TYPESENSE_HOST"), "port": "443", "protocol": "https"}
    ],
    "api_key": os.getenv("TYPESENSE_SEARCH_API_KEY"),
    "connection_timeout_seconds": 10,
}

# Enhanced search parameters with component-aware boosting
BASE_SEARCH_PARAMS = {
    "per_page": 20,
    "highlight_full_fields": "title,content,components",
    "snippet_threshold": 30,
    "num_typos": 2,
    "typo_tokens_threshold": 1,
    "drop_tokens_threshold": 1,
    "prioritize_exact_match": True,
    "prioritize_token_position": True,
}

FILTER_CATEGORIES = ["All", "Docs", "Components", "API Reference", "Blogs"]

FILTER_SECTION_MAPPING = {
    "All": None,
    "Docs": [
        "getting_started",
        "hosting",
        "events",
        "styling",
        "state",
        "vars",
        "database",
        "authentication",
        "recipes",
        "advanced_onboarding",
        "enterprise",
        "utility_methods",
        "client_storage",
        "pages",
        "assets",
        "api-routes",
        "ui",
        "state_structure",
    ],
    "Components": ["library", "components", "custom-components", "wrapping-react"],
    "API Reference": ["api-reference"],
    "Blogs": ["Blog"],
}

DEFAULT_SUGGESTIONS = [
    {
        "title": "Getting Started with Reflex",
        "url": "/docs/getting-started/introduction",
    },
    {"title": "Components Overview", "url": "/docs/library"},
    {"title": "State Management", "url": "/docs/state/overview"},
    {"title": "Events Overview", "url": "/docs/events/events-overview"},
    {"title": "Styling and Theming", "url": "/docs/styling/overview"},
    {"title": "Deployment Guide", "url": "/docs/hosting/deploy-quick-start"},
]

# Precompiled regex patterns for component highlighting fixes
PATTERN_PARTIAL_WORD = re.compile(r"<mark>([^<]*?)</mark>([a-zA-Z0-9_]*)")
PATTERN_COMPONENT_NAME = re.compile(r"((?:rx|reflex)\.)<mark>([^<]*?)</mark>")
PATTERN_NAMESPACE = re.compile(r"<mark>(rx|reflex)</mark>\.([a-zA-Z0-9_]+)")
PATTERN_CHAINED = re.compile(
    r"<mark>((?:rx|reflex)\.[a-zA-Z0-9_]+)</mark>\.([a-zA-Z0-9_]+)"
)

# Styling for highlights
HIGHLIGHT_STYLE = '<span style="background-color: var(--violet-3); color: var(--violet-11); padding: 2px 4px; border-radius: 3px;">'


class TypesenseSearchState(rx.State):
    """Enhanced state management for the Typesense search component."""

    # State variables
    search_query: str = ""
    search_results: list[dict] = []
    is_searching: bool = False
    show_results: bool = False
    show_modal: bool = False
    selected_filter: str = "All"
    filter_categories: list[str] = FILTER_CATEGORIES
    suggestions: list[dict] = DEFAULT_SUGGESTIONS

    def open_modal(self):
        """Open the search modal and reset filter state."""
        self.show_modal = True
        self.selected_filter = "All"

    def close_modal(self):
        """Close the search modal and reset state."""
        self.show_modal = False
        self._reset_search_state()

    def _reset_search_state(self):
        """Reset all search-related state variables."""
        self.show_results = False
        self.is_searching = False
        self.search_query = ""
        self.search_results = []
        self.selected_filter = "All"

    async def set_filter(self, filter_name: str):
        """Set the selected filter and re-run search if there's an active query."""
        self.selected_filter = filter_name
        if self.search_query.strip():
            await self.search_docs(self.search_query)

    def _get_filter_sections(self) -> list[str]:
        """Get sections for current filter."""
        return FILTER_SECTION_MAPPING.get(self.selected_filter, [])

    def _clean_component_query(self, query: str) -> str:
        """Normalize component query by removing rx./reflex. prefix."""
        return re.sub(r"^(rx\.|reflex\.)", "", query.lower()).strip()

    def _expand_query_variants(self, query: str) -> str:
        """Return query string with rx./reflex. variants for flexible matching."""
        cleaned = self._clean_component_query(query)
        variants = {cleaned, f"rx.{cleaned}", f"reflex.{cleaned}"}
        return " ".join(sorted(variants))  # Order doesn't matter

    async def search_docs(self, query: str):
        """Enhanced search with component-aware logic."""
        self.search_query = query

        if not query.strip():
            self._clear_search_results()
            return

        self.is_searching = True

        try:
            results = await self._perform_unified_search(query)
            self.search_results = self._format_search_results(results)
            self.show_results = True
        except Exception as e:
            print(f"Search error: {e}")
            self._clear_search_results()

        self.is_searching = False

    async def _perform_unified_search(self, query: str) -> dict:
        """Perform a single search using is_component metadata for boosting/filtering."""
        client = typesense.Client(TYPESENSE_CONFIG)

        expanded_query = self._expand_query_variants(query)

        search_parameters = {
            "q": expanded_query,
            **BASE_SEARCH_PARAMS,
            "query_by": "title,content,headings,components",
            "query_by_weights": "10,3,3,6",
            "highlight_start_tag": "<mark>",
            "highlight_end_tag": "</mark>",
            "sort_by": "weight:desc, is_component:desc, _text_match:desc",
        }

        # Apply filter if not "All"
        if self.selected_filter != "All":
            if self.selected_filter == "Components":
                search_parameters["filter_by"] = "is_component:=true"
            else:
                sections = self._get_filter_sections()
                if sections:
                    search_parameters["filter_by"] = " || ".join(
                        f"section:={s}" for s in sections
                    )

        return client.collections["docs"].documents.search(search_parameters)

    def _clear_search_results(self):
        """Clear search results and hide results display."""
        self.search_results = []
        self.show_results = False

    def _format_search_results(self, result: dict) -> list[dict]:
        """Format search results for display with enhanced component info."""
        formatted_results = []

        for hit in result["hits"]:
            doc = hit["document"]
            components = doc.get("components", [])
            component_info = None
            if components:
                component_info = f"Components: {', '.join(components)}"
            formatted_result = {
                "title": doc["title"],
                "content": self._get_highlighted_content(hit),
                "url": doc["url"],
                "path": doc["path"],
                "section": doc.get("section", ""),
                "subsection": doc.get("subsection", ""),
                "breadcrumb": doc.get("breadcrumb", ""),
                "components": components,
                "component_info": component_info,
                "score": hit.get("text_match", 0),
            }
            formatted_results.append(formatted_result)

        return formatted_results

    def _get_highlighted_content(self, hit: dict) -> str:
        """Get highlighted content snippet with component-aware highlighting."""
        highlights = hit.get("highlights", [])

        def fix_component_highlighting(text):
            """Fix incomplete word and component highlighting patterns."""
            text = PATTERN_PARTIAL_WORD.sub(r"<mark>\1\2</mark>", text)
            text = PATTERN_COMPONENT_NAME.sub(r"<mark>\1\2</mark>", text)
            text = PATTERN_NAMESPACE.sub(r"<mark>\1.\2</mark>", text)
            text = PATTERN_CHAINED.sub(r"<mark>\1.\2</mark>", text)
            return text

        for highlight in highlights:
            field = highlight.get("field")
            if field == "components":
                values = highlight.get("values", [])
                if values:
                    fixed_values = [
                        fix_component_highlighting(value) for value in values
                    ]
                    highlighted_components = ", ".join(fixed_values)
                    styled = f"<span style='font-weight: 600;'>Components:</span> {highlighted_components}"
                    return styled.replace("<mark>", HIGHLIGHT_STYLE).replace(
                        "</mark>", "</span>"
                    )
            elif field in ["content", "title"]:
                content = highlight.get("snippet") or highlight.get("value", "")
                if content and "<mark>" in content:
                    content = fix_component_highlighting(content)
                    return content.replace("<mark>", HIGHLIGHT_STYLE).replace(
                        "</mark>", "</span>"
                    )

        # Fallback to truncated plain content
        return self._truncate_content(hit["document"]["content"])

    def _truncate_content(self, content: str, max_length: int = 150) -> str:
        """Truncate content to specified length."""
        if len(content) <= max_length:
            return content
        return content[:max_length] + "..."

    def hide_results(self):
        """Hide search results."""
        self.show_results = False

    def navigate_to_result(self, url: str):
        """Navigate to a search result."""
        self.show_results = False
        self.show_modal = False
        return rx.redirect(url)


# Component functions (keeping your existing UI components)
def filter_pill(filter_name: str) -> rx.Component:
    """Render a single filter pill."""
    is_selected = TypesenseSearchState.selected_filter == filter_name

    selected_classes = "bg-violet-3 border-violet-9 !text-violet-9"
    unselected_classes = "bg-slate-1 border-slate-5 !text-slate-9"

    return rx.box(
        rx.text(
            filter_name,
            class_name=f"text-sm font-medium {rx.cond(is_selected, '!text-violet-9', '!text-slate-9')}",
        ),
        on_click=TypesenseSearchState.set_filter(filter_name),
        class_name=f"shrink-0 typesense-filter-pill hover:bg-slate-3 cursor-pointer px-2 py-1 rounded-[10px] transition-bg border {rx.cond(is_selected, selected_classes, unselected_classes)}",
    )


def filter_pills() -> rx.Component:
    """Render the filter pills container."""
    return rx.box(
        rx.foreach(TypesenseSearchState.filter_categories, filter_pill),
        class_name="hidden md:flex md:flex-row gap-x-3 pt-2 overflow-x-auto justify-start w-full",
    )


def suggestion_item(title: str, url: str, icon: str = "book-open") -> rx.Component:
    """Render a single suggestion item."""
    return rx.box(
        rx.hstack(
            rx.icon(icon, size=16, color="var(--c-slate-9)"),
            rx.text(
                title, font_weight="500", color="var(--c-slate-12)", font_size="14px"
            ),
            spacing="2",
            align_items="center",
        ),
        on_click=lambda: TypesenseSearchState.navigate_to_result(url),
        class_name="w-full border-b border-slate-4 hover:bg-slate-3 cursor-pointer rounded-[6px] py-2 px-2",
    )


def suggestions_section() -> rx.Component:
    """Render the suggestions section."""
    return rx.box(
        rx.text(
            rx.cond(
                TypesenseSearchState.search_query.length() > 0,
                rx.cond(
                    TypesenseSearchState.search_results.length() > 0,
                    "Results",
                    rx.cond(
                        TypesenseSearchState.is_searching,
                        "Searching...",
                        "No results found",
                    ),
                ),
                "Suggestions",
            ),
            class_name="text-sm text-slate-11 font-medium",
        ),
        rx.cond(
            TypesenseSearchState.search_query.length() == 0,
            rx.box(
                suggestion_item(
                    "Getting Started with Reflex",
                    "/docs/getting-started/introduction",
                    "rocket",
                ),
                suggestion_item("Components Overview", "/docs/library", "blocks"),
                suggestion_item("State Management", "/docs/state/overview", "database"),
                suggestion_item(
                    "Event Overview", "/docs/events/events-overview", "zap"
                ),
                suggestion_item(
                    "Styling and Theming", "/docs/styling/overview", "palette"
                ),
                suggestion_item(
                    "Deployment Guide", "/docs/hosting/deploy-quick-start/", "cloud"
                ),
                class_name="w-full flex flex-col gap-y-1 items-start",
            ),
            rx.box(),
        ),
        class_name="w-full flex flex-col gap-y-2 items-start",
    )


def search_result_item(result: rx.Var) -> rx.Component:
    """Enhanced search result item with component information."""
    return rx.box(
        rx.vstack(
            rx.text(
                result["breadcrumb"],
                class_name="text-sm text-slate-9 mb-2",
            ),
            rx.hstack(
                rx.icon("file-text", class_name="size-4 shrink-0 !text-slate-9"),
                rx.html(
                    result["title"],
                    class_name="text-md font-medium !text-slate-12",
                    word_break="keep-all",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="4px",
            ),
            rx.html(
                result["content"],
                font_size="14px",
                line_height="1.5",
                class_name="prose prose-sm text-slate-12",
            ),
            align_items="start",
            spacing="1",
            width="100%",
        ),
        class_name="p-2 border border-slate-4 rounded-[8px] cursor-pointer w-full hover:border-slate-5 hover:bg-slate-2 shadow-small",
        on_click=lambda: TypesenseSearchState.navigate_to_result(result["url"]),
    )


def search_results_section() -> rx.Component:
    """Render the search results section."""
    return rx.box(
        rx.foreach(TypesenseSearchState.search_results, search_result_item),
        class_name="w-full flex flex-col gap-y-4 my-4",
    )


def search_input() -> rx.Component:
    """Render the search input field."""
    return rx.box(
        rx.el.button(
            "Esc",
            class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm border border-slate-5 rounded-md text-xs !text-slate-9 px-[5px] py-[2px] hidden md:inline",
            on_click=rx.run_script(
                "document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"
            ),
        ),
        rx.el.input(
            placeholder="Search components, docs, or features...",
            on_change=TypesenseSearchState.search_docs.debounce(500),
            id="search-input",
            auto_focus=True,
            class_name="w-full bg-transparent border-none outline-none focus:outline-none pr-10 placeholder:text-lg text-base",
        ),
        style={"padding": "6px 0px"},
        class_name="w-full cursor-pointer flex max-h-[32px] min-h-[32px] relative",
    )


def search_modal() -> rx.Component:
    """Create the full-screen search modal."""
    return rx.box(
        # Header with search input and filters
        rx.box(
            rx.box(
                search_input(),
                class_name="w-full py-2 top-0 left-0 absolute border-b border-slate-5 px-6",
            ),
            filter_pills(),
            class_name="w-full flex flex-col items-center gap-y-4 px-6",
        ),
        # Content area
        rx.scroll_area(
            rx.cond(
                TypesenseSearchState.search_query.length() > 0,
                rx.cond(
                    TypesenseSearchState.search_results.length() > 0,
                    rx.box(suggestions_section(), search_results_section()),
                    suggestions_section(),
                ),
                suggestions_section(),
            ),
            class_name=f"w-full overflow-y-scroll [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mb-[1rem] px-6 py-2 pb-4 {rx.cond(TypesenseSearchState.search_results.length() > 0, 'h-[50vh]', 'h-full')}",
        ),
        class_name="w-full flex flex-col gap-y-2 relative pt-16",
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
        on_click=TypesenseSearchState.open_modal,
    )


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

from pcweb.components.docpage.navbar.docs_index import indexed_docs
from reflex.experimental import ClientStateVar

SearchData = ClientStateVar.create("indexed_docs", indexed_docs)
SearchInput = ClientStateVar.create("search", "")

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
        href=value["url"].to(str),
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md",
        _hover={"bg": rx.color("gray", 2)},
    )

suggestion_items = [
    {"name": "Components Overview", "path": "/docs/library", "icon": "blocks", "description": "Discover and explore the full library of available components"},
    {"name": "State Management", "path": "/docs/state/overview", "icon": "database", "description": "Master state handling, data flow, and reactive programming"},
    {"name": "Event Overview", "path": "/docs/events/events-overview", "icon": "zap", "description": "Learn how to handle user interactions and system events"},
    {"name": "Styling and Theming", "path": "/docs/styling/overview", "icon": "palette", "description": "Customize colors, layouts, and create beautiful app designs"},
    {"name": "Deployment Guide", "path": "/docs/hosting/deploy-quick-start/", "icon": "cloud", "description": "Deploy and host your application in production environments"},
]

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
                rx.box(
                    rx.foreach(
                        SearchData.value,
                        lambda value, index: rx.cond(
                            value["name"].to(str).lower().contains(SearchInput.value.lower()),
                            search_result(
                                value['parts'].to(list), value
                            ),
                        ),
                    ),
                    class_name="flex flex-col gap-y-2",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                # rx.text("Suggustions", class_name="text-sm font-medium pl-1"),
                rx.foreach(suggestion_items, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )

def typesense_search() -> rx.Component:
    """Create the main Typesense search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_input(),
                search_content(),
                on_interact_outside=SearchInput.set_value(""),
                on_escape_key_down=SearchInput.set_value(""),
                # class_name="focus:outline-none bg-background h-[60vh] p-3 border-none",
                class_name="w-full max-w-[640px] mx-auto h-[60vh] bg-slate-1 border-none outline-none p-3 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
            ),
        ),
        keyboard_shortcut_script(),
        class_name="w-full",
    )
