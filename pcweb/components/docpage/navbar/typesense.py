"""Typesense search component for the navbar."""

import reflex as rx
import typesense
import os

# Constants
TYPESENSE_CONFIG = {
    'nodes': [{
        'host': os.getenv('TYPESENSE_HOST'),
        'port': '443',
        'protocol': 'https'
    }],
    'api_key': os.getenv('TYPESENSE_SEARCH_API_KEY'),
    'connection_timeout_seconds': 10
}

SEARCH_PARAMS = {
    'query_by': 'title,content,headings',
    'per_page': 8,
    'highlight_full_fields': 'title,content',
    'snippet_threshold': 30,
    'num_typos': 2
}

FILTER_CATEGORIES = [
    "All",
    "Docs",
    "Components",
    "API Reference",
    "Blogs"
]

FILTER_SECTION_MAPPING = {
    "All": None,
    "Docs": ["getting_started", "hosting", "events", "styling", "state", "vars",
             "database", "authentication", "recipes", "advanced_onboarding",
             "enterprise", "utility_methods", "client_storage", "pages",
             "assets", "api-routes", "ui", "state_structure"],
    "Components": ["library", "components", "custom-components", "wrapping-react"],
    "API Reference": ["api-reference"],
    "Blogs": ["Blog"]
}

SECTION_DISPLAY_NAMES = {
    'getting_started': 'Getting Started',
    'library': 'Components',
    'api-reference': 'API Reference',
    'hosting': 'Hosting',
    'events': 'Events',
    'styling': 'Styling',
    'state': 'State',
    'vars': 'Variables',
    'database': 'Database',
    'authentication': 'Authentication',
    'custom-components': 'Custom Components',
    'wrapping-react': 'Wrapping React',
    'ai_builder': 'AI Builder',
    'recipes': 'Recipes',
    'advanced_onboarding': 'Advanced',
    'enterprise': 'Enterprise',
    'utility_methods': 'Utilities',
    'client_storage': 'Client Storage',
    'components': 'Components',
    'pages': 'Pages',
    'assets': 'Assets',
    'api-routes': 'API Routes',
    'ui': 'UI',
    'state_structure': 'State Structure',
    'Blog': 'Blog'
}

DEFAULT_SUGGESTIONS = [
    {"title": "Getting Started with Reflex", "url": "/docs/getting-started/introduction"},
    {"title": "Components Overview", "url": "/docs/library"},
    {"title": "State Management", "url": "/docs/state/overview"},
    {"title": "Event Handlers", "url": "/docs/events/event-handlers"},
    {"title": "Styling and Theming", "url": "/docs/styling/overview"},
    {"title": "Deployment Guide", "url": "/docs/hosting/deploy"},
]


class TypesenseSearchState(rx.State):
    """State management for the Typesense search component."""

    # State variables
    search_query: str = ""
    search_results: list[dict] = []
    is_searching: bool = False
    show_results: bool = False
    show_modal: bool = False
    selected_filter: str = "All"
    filter_categories: list[str] = FILTER_CATEGORIES
    suggestions: list[dict] = DEFAULT_SUGGESTIONS

    # Modal management
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

    # Filter management
    async def set_filter(self, filter_name: str):
        """Set the selected filter and re-run search if there's an active query."""
        self.selected_filter = filter_name
        if self.search_query.strip():
            await self.search_docs(self.search_query)

    def _get_filter_sections(self) -> list[str]:
        """Get sections for current filter."""
        return FILTER_SECTION_MAPPING.get(self.selected_filter, [])

    # Search functionality
    async def search_docs(self, query: str):
        """Search the documentation using Typesense."""
        self.search_query = query

        if not query.strip():
            self._clear_search_results()
            return

        self.is_searching = True

        try:
            results = await self._perform_search(query)
            self.search_results = self._format_search_results(results)
            self.show_results = True
        except Exception as e:
            print(f"Search error: {e}")
            self._clear_search_results()

        self.is_searching = False

    def _clear_search_results(self):
        """Clear search results and hide results display."""
        self.search_results = []
        self.show_results = False

    async def _perform_search(self, query: str) -> dict:
        """Perform the actual Typesense search."""
        client = typesense.Client(TYPESENSE_CONFIG)

        search_parameters = {
            'q': query,
            **SEARCH_PARAMS,
            'highlight_start_tag': '<mark>',
            'highlight_end_tag': '</mark>'
        }

        # Apply filter if not "All"
        if self.selected_filter != "All":
            sections = self._get_filter_sections()
            if sections:
                filter_conditions = [f'section:={section}' for section in sections]
                search_parameters['filter_by'] = ' || '.join(filter_conditions)

        return client.collections['docs'].documents.search(search_parameters)

    def _format_search_results(self, result: dict) -> list[dict]:
        """Format search results for display."""
        return [
            {
                'title': hit['document']['title'],
                'content': self._get_highlighted_content(hit),  # <-- use highlight-aware content
                'url': hit['document']['url'],
                'path': hit['document']['path'],
                'section': hit['document'].get('section', ''),
                'subsection': hit['document'].get('subsection', ''),
                'breadcrumb': self._create_breadcrumb(hit['document'])
            }
            for hit in result['hits']
        ]


    def _get_highlighted_content(self, hit: dict) -> str:
        """Get highlighted content snippet."""
        highlights = hit.get('highlights', [])
        if highlights:
            for highlight in highlights:
                if highlight.get('field') == 'content':
                    # Prefer the short 'snippet' if available, else fallback to 'value'
                    content = highlight.get('snippet') or highlight.get('value')
                    if content and '<mark>' in content:
                        content = content.replace(
                            '<mark>', '<span style="background-color: var(--violet-3); color: var(--violet-11); padding: 2px 4px; border-radius: 3px;">'
                        ).replace('</mark>', '</span>')

                        return content

        # Fallback to truncated plain content
        return self._truncate_content(hit['document']['content'])


    def _truncate_content(self, content: str, max_length: int = 150) -> str:
        """Truncate content to specified length."""
        if len(content) <= max_length:
            return content
        return content[:max_length] + '...'

    def _create_breadcrumb(self, document: dict) -> str:
        """Create a breadcrumb string from document metadata."""
        parts = []

        # Add section
        section = document.get('section', '')
        if section:
            section_display = SECTION_DISPLAY_NAMES.get(
                section,
                section.replace('-', ' ').replace('_', ' ').title()
            )
            parts.append(section_display)

        # Add subsection
        subsection = document.get('subsection', '')
        if subsection:
            subsection_display = subsection.replace('-', ' ').replace('_', ' ').title()
            parts.append(subsection_display)

        # Add title if different from last part
        title = document.get('title', '')
        if title and (not parts or title.lower() != parts[-1].lower()):
            parts.append(title)

        return ' › '.join(parts)

    # Navigation
    def hide_results(self):
        """Hide search results."""
        self.show_results = False

    def navigate_to_result(self, url: str):
        """Navigate to a search result."""
        self.show_results = False
        self.show_modal = False
        return rx.redirect(url)


# Component functions
def filter_pill(filter_name: str) -> rx.Component:
    """Render a single filter pill."""
    is_selected = TypesenseSearchState.selected_filter == filter_name

    selected_classes = "bg-violet-3 border-violet-9 !text-violet-9"
    unselected_classes = "bg-slate-1 border-slate-5 !text-slate-9"

    return rx.box(
        rx.text(
            filter_name,
            class_name=f"text-sm font-medium {rx.cond(is_selected, '!text-violet-9', '!text-slate-9')}"
        ),
        on_click=TypesenseSearchState.set_filter(filter_name),
        class_name=f"shrink-0 typesense-filter-pill hover:bg-slate-3 cursor-pointer px-2 py-1 rounded-[10px] transition-bg border {rx.cond(is_selected, selected_classes, unselected_classes)}"
    )


def filter_pills() -> rx.Component:
    """Render the filter pills container."""
    return rx.box(
        rx.foreach(
            TypesenseSearchState.filter_categories,
            filter_pill
        ),
        class_name="hidden md:flex md:flex-row gap-x-3 pt-2 overflow-x-auto justify-start w-full"
    )


def suggestion_item(title: str, url: str, icon: str = "book-open") -> rx.Component:
    """Render a single suggestion item."""
    return rx.box(
        rx.hstack(
            rx.icon(icon, size=16, color="var(--c-slate-9)"),
            rx.text(
                title,
                font_weight="500",
                color="var(--c-slate-12)",
                font_size="14px"
            ),
            spacing="2",
            align_items="center"
        ),
        on_click=lambda: TypesenseSearchState.navigate_to_result(url),
        class_name="w-full shadow-sm hover:bg-slate-3 cursor-pointer rounded-[6px] py-2 px-2"
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
                        "No results found"
                    )
                ),
                "Suggestions"
            ),
            class_name="text-sm text-slate-11 font-medium mb-2",
        ),
        rx.cond(
            TypesenseSearchState.search_query.length() == 0,
            rx.box(
                suggestion_item("Getting Started with Reflex", "/docs/getting-started/introduction", "rocket"),
                suggestion_item("Components Overview", "/docs/library", "blocks"),
                suggestion_item("State Management", "/docs/state/overview", "database"),
                suggestion_item("Event Handlers", "/docs/events/event-handlers", "zap"),
                suggestion_item("Styling and Theming", "/docs/styling/overview", "palette"),
                suggestion_item("Deployment Guide", "/docs/hosting/deploy", "cloud"),
                class_name="w-full flex flex-col gap-y-1 items-start"
            ),
            rx.box(),
        ),
        class_name="w-full flex flex-col gap-y-2 items-start",
    )


def search_result_item(result: rx.Var) -> rx.Component:
    """Render a single search result item with breadcrumb navigation."""
    return rx.box(
        rx.vstack(
            rx.text(
                result['breadcrumb'],
                class_name="text-sm text-slate-9 mb-2",
            ),
            rx.hstack(
                rx.icon("file-text", class_name="size-4 shrink-0 !text-slate-9"),
                rx.html(
                    result['title'],
                    class_name="text-md font-medium text-slate-12",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="4px"
            ),
            rx.html(
                result['content'],
                color="var(--c-slate-11)",
                font_size="14px",
                line_height="1.5",
                class_name="prose prose-sm"
            ),
            align_items="start",
            spacing="1",
            width="100%"
        ),
        class_name="p-2 border border-slate-4 rounded-[8px] cursor-pointer w-full hover:border-slate-5 hover:bg-slate-2 shadow-small",
        on_click=lambda: TypesenseSearchState.navigate_to_result(result['url']),
    )


def search_results_section() -> rx.Component:
    """Render the search results section."""
    return rx.box(
        rx.foreach(
            TypesenseSearchState.search_results,
            search_result_item
        ),
        class_name="w-full flex flex-col gap-y-4 mt-4"
    )


def search_input() -> rx.Component:
    """Render the search input field."""
    return rx.box(
        rx.el.button(
            "Esc",
            class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm border border-slate-5 rounded-md text-xs !text-slate-9 px-[5px] py-[2px] hidden md:inline",
            on_click=rx.run_script("document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"),
        ),
        rx.el.input(
            placeholder="What are you searching for?",
            on_change=TypesenseSearchState.search_docs.debounce(500),
            id="search-input",
            auto_focus=True,
            class_name="w-full bg-transparent border-none outline-none focus:outline-none pr-10 placeholder:text-lg text-base",
        ),
        style={"padding": "6px 0px"},
        class_name="w-full cursor-pointer flex max-h-[32px] min-h-[32px] relative"
    )


def search_modal() -> rx.Component:
    """Create the full-screen search modal."""
    return rx.box(
        # Header with search input and filters
        rx.box(
            rx.box(
                search_input(),
                class_name="w-full py-2 top-0 left-0 absolute border-b border-slate-5 px-6"
            ),
            filter_pills(),
            class_name="w-full flex flex-col items-center gap-y-4 px-6"
        ),

        # Content area
        rx.scroll_area(
            rx.cond(
                TypesenseSearchState.search_query.length() > 0,
                rx.cond(
                    TypesenseSearchState.search_results.length() > 0,
                    rx.box(
                        suggestions_section(),
                        search_results_section()
                    ),
                    suggestions_section()
                ),
                suggestions_section()
            ),
            class_name=f"w-full overflow-y-scroll [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mb-[1rem] px-6 py-2 {rx.cond(TypesenseSearchState.search_results.length() > 0, 'h-[50vh]', 'h-full')}"),
        class_name="w-full flex flex-col gap-y-2 relative pt-16"
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
        on_click=TypesenseSearchState.open_modal
    )


def keyboard_shortcut_script() -> rx.Component:
    """Add keyboard shortcut support for opening search."""
    return rx.script("""
        document.addEventListener('keydown', function(e) {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                document.getElementById('search-trigger').click();
            }
        });
    """)


def typesense_search() -> rx.Component:
    """Create the main Typesense search component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(
                search_trigger(),
                id="search-trigger"
            ),
            rx.dialog.content(
                search_modal(),
                class_name="w-full max-w-[640px] mx-auto bg-slate-1 border-none outline-none p-0 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0",
                on_interact_outside=TypesenseSearchState.close_modal,
                on_escape_key_down=TypesenseSearchState.close_modal,
            )
        ),
        keyboard_shortcut_script(),
        class_name="w-full"
    )
