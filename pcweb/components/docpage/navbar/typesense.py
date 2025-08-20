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
    "connection_timeout_seconds": 2,
}
from pcweb.components.icons.hugeicons import hi

# Enhanced search parameters with component-aware boosting
BASE_SEARCH_PARAMS = {
    "per_page": 15,
    "highlight_full_fields": "title,content,components",
    "snippet_threshold": 20,
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
HIGHLIGHT_STYLE = '<span class="bg-violet-3 text-violet-11 px-1 py-0.5 rounded-[3px]">'


class TypesenseSearchState(rx.State):
    """Enhanced state management for the Typesense search component."""

    # State variables
    search_query: rx.Field[str] = rx.field("")
    search_results: rx.Field[list[dict]] = rx.field(default_factory=list)
    is_searching: rx.Field[bool] = rx.field(False)
    _show_results: bool = False
    selected_filter: rx.Field[str] = rx.field("All")

    @rx.event(temporal=True)
    def close_modal(self):
        """Close the search modal and reset state."""
        self.reset()

    @rx.event(temporal=True)
    async def set_filter(self, filter_name: str):
        """Set the selected filter and re-run search if there's an active query."""
        self.selected_filter = filter_name
        if self.search_query.strip():
            yield TypesenseSearchState.search_docs(self.search_query)

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

    @rx.event(background=True, temporal=True)
    async def search_docs(self, query: str):
        """Enhanced search with component-aware logic."""
        async with self:
            self.search_query = query

            if not query.strip():
                self._clear_search_results()
                return

            self.is_searching = True
            yield

        try:
            results = await self._perform_unified_search(query)
            formatted_results = self._format_search_results(results)
            async with self:
                self.search_results = formatted_results
                self._show_results = True
        except Exception:
            async with self:
                self._clear_search_results()

        finally:
            async with self:
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
        self._show_results = False

    def _format_search_results(self, result: dict) -> list[dict]:
        """Format search results for display with enhanced component info."""
        formatted_results = []

        for hit in result["hits"]:
            doc = hit["document"]
            components = doc.get("components", [])
            formatted_result = {
                "title": doc["title"],
                "content": self._get_highlighted_content(hit),
                "url": doc["url"],
                "path": doc["path"],
                "section": doc.get("section", ""),
                "breadcrumb": doc.get("breadcrumb", ""),
                "components": components,
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
        return self._truncate_content(hit["document"].get("content", ""))

    def _truncate_content(self, content: str, max_length: int = 150) -> str:
        """Truncate content to specified length."""
        if len(content) <= max_length:
            return content
        return content[:max_length] + "..."


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
        *[filter_pill(filter_name) for filter_name in FILTER_CATEGORIES],
        class_name="hidden md:flex md:flex-row gap-x-3 pt-2 overflow-x-auto justify-start w-full",
    )


def suggestion_item(title: str, url: str, icon: str = "book-open") -> rx.Component:
    """Render a single suggestion item."""
    return rx.el.a(
        rx.hstack(
            rx.icon(icon, size=16, class_name="!text-slate-9"),
            rx.text(
                title,
                font_weight="500",
                class_name="!text-slate-12",
                font_size="14px",
            ),
            spacing="2",
            align_items="center",
        ),
        to=url,
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
    return rx.el.a(
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
        to=result["url"],
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
        rx.el.a(
            hi("sparkles", class_name="fill-current"),
            "Ask AI",
            class_name="absolute right-0 top-1/2 transform -translate-y-1/2 text-md border border-violet-9 rounded-md text-violet-9 bg-violet-3 px-2 py-1 flex flex-row items-center gap-x-1 font-medium hover:bg-violet-4 transition-colors",
            to="/docs/ai-builder/integrations/mcp-overview",
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
        class_name="w-full hover:bg-slate-3 cursor-pointer flex max-h-[32px] min-h-[32px] border border-slate-5 rounded-[3px] !rounded-[10px] bg-slate-1 transition-bg relative",
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


def typesense_search() -> rx.Component:
    """Create the main Typesense search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_modal(),
                class_name="w-full max-w-[640px] mx-auto bg-slate-1 border-none outline-none p-0 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
            ),
            on_open_change=TypesenseSearchState.close_modal,
        ),
        keyboard_shortcut_script(),
    )
