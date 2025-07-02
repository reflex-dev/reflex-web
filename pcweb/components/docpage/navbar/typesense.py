"""Typesense search component for the navbar."""

import reflex as rx
from reflex.utils.imports import ImportVar
from reflex.vars import Var
import typesense
import os
from reflex.experimental import ClientStateVar

SearchInputClientState = ClientStateVar.create("SearchInputClientState", "")


class TypesenseSearchState(rx.State):
    """State for the Typesense search component."""

    search_query: str = ""
    search_results: list[dict] = []
    is_searching: bool = False
    show_results: bool = False
    show_modal: bool = False
    selected_filter: str = "All"

    filter_categories = [
        "All",
        "Docs",
        "Components",
        "API Reference",
        "Blogs"
    ]

    filter_section_mapping = {
        "All": None,
        "Docs": ["getting_started", "hosting", "events", "styling", "state", "vars", "database", "authentication", "recipes", "advanced_onboarding", "enterprise", "utility_methods", "client_storage", "pages", "assets", "api-routes", "ui", "state_structure"],
        "Components": ["library", "components", "custom-components", "wrapping-react"],
        "API Reference": ["api-reference"],
        "Blogs": ["Blog"]
    }

    suggestions = [
        {"title": "Getting Started with Reflex", "url": "/docs/getting-started/introduction"},
        {"title": "Components Overview", "url": "/docs/library"},
        {"title": "State Management", "url": "/docs/state/overview"},
        {"title": "Event Handlers", "url": "/docs/events/event-handlers"},
        {"title": "Styling and Theming", "url": "/docs/styling/overview"},
        {"title": "Deployment Guide", "url": "/docs/hosting/deploy"},
    ]


    def open_modal(self):
        """Open the search modal and reset filter state."""
        self.show_modal = True
        self.selected_filter = "All"

    def close_modal(self):
        """Close the search modal and reset state."""
        self.show_modal = False
        self.show_results = False
        self.search_query = ""
        self.search_results = []
        self.selected_filter = "All"

    async def set_filter(self, filter_name: str):
        """Set the selected filter and re-run search if there's an active query."""
        self.selected_filter = filter_name
        if self.search_query.strip():
            await self.search_docs(self.search_query)


    async def search_docs(self, query: str):
        """Search the documentation using Typesense."""
        self.search_query = query
        if not query.strip():
            self.search_results = []
            self.show_results = False
            return

        self.is_searching = True

        try:
            client = typesense.Client({
                'nodes': [{
                    'host': 'z2mi3hyewokc16a4p-1.a1.typesense.net',
                    'port': '443',
                    'protocol': 'https'
                }],
                'api_key': 'KuwU0fBZYHMuvhtv32LXekhBo9bTWDU0',
                'connection_timeout_seconds': 10
            })

            search_parameters = {
                'q': query,
                'query_by': 'title,content,headings',
                'per_page': 8,
                'highlight_full_fields': 'title,content',
                'snippet_threshold': 30,
                'num_typos': 2
            }

            if self.selected_filter != "All":
                sections = self.filter_section_mapping.get(self.selected_filter, [])
                if sections:
                    filter_conditions = [f'section:={section}' for section in sections]
                    search_parameters['filter_by'] = ' || '.join(filter_conditions)

            result = client.collections['docs'].documents.search(search_parameters)

            self.search_results = [
                {
                    'title': hit['document']['title'],
                    'content': hit['document']['content'][:150] + '...' if len(hit['document']['content']) > 150 else hit['document']['content'],
                    'url': hit['document']['url'],
                    'path': hit['document']['path'],
                    'section': hit['document'].get('section', ''),
                    'subsection': hit['document'].get('subsection', ''),
                    'breadcrumb': self._create_breadcrumb(hit['document'])
                }
                for hit in result['hits']
            ]
            self.show_results = True

        except Exception as e:
            print(f"Search error: {e}")
            self.search_results = []
            self.show_results = False

        self.is_searching = False

    def hide_results(self):
        """Hide search results."""
        self.show_results = False

    def _create_breadcrumb(self, document: dict) -> str:
        """Create a breadcrumb string from document metadata."""
        parts = []

        section = document.get('section', '')
        if section:
            section_display = {
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
            }.get(section, section.replace('-', ' ').replace('_', ' ').title())
            parts.append(section_display)

        subsection = document.get('subsection', '')
        if subsection:
            subsection_display = subsection.replace('-', ' ').replace('_', ' ').title()
            parts.append(subsection_display)

        title = document.get('title', '')
        if title and (not parts or title.lower() != parts[-1].lower()):
            parts.append(title)

        return ' › '.join(parts)

    def navigate_to_result(self, url: str):
        """Navigate to a search result."""
        self.show_results = False
        self.show_modal = False
        return rx.redirect(url)


def filter_pill(filter_name: str) -> rx.Component:
    """Render a single filter pill."""
    is_selected = TypesenseSearchState.selected_filter == filter_name

    return rx.box(
        rx.text(
            filter_name,
            class_name="text-sm font-medium " + rx.cond(is_selected, "!text-violet-9", "!text-slate-9").to(str)
        ),

        on_click=TypesenseSearchState.set_filter(filter_name),
        class_name="shrink-0 typesense-filter-pill hover:bg-slate-3 cursor-pointer px-2 py-1 rounded-[10px] transition-bg " + rx.cond(is_selected, "bg-violet-3 border border-violet-9", "bg-slate-1 border border-slate-5").to(str)
    )



def filter_pills() -> rx.Component:
    """Render the filter pills container."""
    return rx.box(
        rx.foreach(
            TypesenseSearchState.filter_categories,
            filter_pill
        ),
        class_name="typesense-filter-pills flex flex-row gap-x-3 px-6 pt-2 w-full overflow-x-auto"
    )


def suggestion_item(title: str, url: str) -> rx.Component:
    """Render a single suggestion item."""
    return rx.box(
        rx.hstack(
            rx.icon("book-open", size=16, color="var(--c-slate-9)"),
            rx.text(
                title,
                font_weight="500",
                color="var(--c-slate-12)",
                font_size="14px"
            ),
            spacing="2",
            align_items="center"
        ),
        padding="8px 12px",
        on_click=lambda: TypesenseSearchState.navigate_to_result(url),
        class_name="w-full shadow-sm hover:bg-slate-3 cursor-pointer rounded-[6px]"
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
                rx.text(
                    result['title'],
                    class_name="text-md font-medium text-slate-12",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="4px"
            ),
            rx.text(
                result['content'],
                color="var(--c-slate-11)",
                font_size="14px",
                line_height="1.5"
            ),
            align_items="start",
            spacing="1",
            width="100%"
        ),
        class_name="p-2 border border-slate-4 rounded-[8px] cursor-pointer w-full hover:border-slate-5 hover:bg-slate-2 shadow-small",
        on_click=lambda: TypesenseSearchState.navigate_to_result(result['url']),
    )


def search_modal() -> rx.Component:
    """Create the full-screen search modal."""

    return rx.box(
        rx.box(
            rx.box(rx.box(
                rx.icon(
                    "search",
                    class_name="absolute left-1 top-1/2 transform -translate-y-1/2 text-md w-4 h-4 flex-shrink-0 !text-slate-9",
                ),
                rx.el.button(
                    "ESC",
                    class_name="absolute right-1 top-1/2 transform -translate-y-1/2 text-sm border border-slate-5 rounded-md text-sm !text-slate-9 px-[5px] py-[2px] hidden md:inline",
                    on_click=rx.call_function("document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"),
                ),
                rx.el.input(
                    placeholder="What are you searching for?",
                    on_change=TypesenseSearchState.search_docs,
                    id="search-input",
                    auto_focus=True,
                    class_name="w-full bg-transparent border-none outline-none focus:outline-none pl-4 pr-10 placeholder:text-base text-base",
                ),
                align_items="center",
                spacing="2",
                style={
                    "padding": "6px 12px",
                },
                class_name="w-full cursor-pointer flex max-h-[32px] min-h-[32px] relative"
            ),
            class_name="w-full px-6 py-2 top-0 left-0 absolute border-b border-slate-5"
            ),
            filter_pills(),
            class_name="w-full flex flex-col items-center gap-y-4"
        ),
        rx.scroll_area(
            rx.cond(
                TypesenseSearchState.search_query.length() > 0,
                rx.cond(
                    TypesenseSearchState.search_results.length() > 0,
                    rx.box(
                        rx.foreach(
                            TypesenseSearchState.search_results,
                            search_result_item
                        ),
                        class_name="w-full flex flex-col gap-y-4 mt-4"
                    ),
                    rx.cond(
                        TypesenseSearchState.is_searching,
                        rx.text("Searching...", color="var(--c-slate-9)", margin_top="16px"),
                        rx.text("No results found", color="var(--c-slate-9)", margin_top="16px")
                    )
                ),
                rx.box(
                    rx.text(
                        "Suggestions",
                        class_name="text-sm text-slate-11 font-medium",
                    ),
                    rx.vstack(
                        suggestion_item("Getting Started with Reflex", "/docs/getting-started/introduction"),
                        suggestion_item("Components Overview", "/docs/library"),
                        suggestion_item("State Management", "/docs/state/overview"),
                        suggestion_item("Event Handlers", "/docs/events/event-handlers"),
                        suggestion_item("Styling and Theming", "/docs/styling/overview"),
                        suggestion_item("Deployment Guide", "/docs/hosting/deploy"),
                        spacing="1",
                        width="100%"
                    ),
                    class_name="w-full flex flex-col gap-y-2 align-start",
                )
            ),
            class_name="w-full h-[50vh] overflow-y-scroll [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mb-[1rem] px-6 py-2"
        ),
        class_name="w-full flex flex-col gap-y-2 relative pt-16"
    )

def typesense_search() -> rx.Component:
    """Create the Typesense search trigger component."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
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
                    align_items="center",
                    spacing="2",
                    style={
                        "padding": "6px 12px",
                        "min_width": ["32px", "32px", "256px"],
                        "max_width": ["6em", "6em", "none"],
                        "box_shadow": "0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
                    },
                    class_name="w-full hover:bg-slate-3 cursor-pointer flex max-h-[32px] min-h-[32px] border border-slate-5 rounded-[10px] bg-slate-1 transition-bg relative",
                    on_click=TypesenseSearchState.open_modal
                ),
                id="search-trigger"
            ),
            rx.dialog.content(search_modal(), class_name="w-full max-w-[640px] bg-slate-1 border-none outline-none p-0",
                on_interact_outside=TypesenseSearchState.close_modal,
                on_escape_key_down=TypesenseSearchState.close_modal,

            )
        ),
        rx.script("""
            document.addEventListener('keydown', function(e) {
                if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                    e.preventDefault();
                    document.getElementById('search-trigger').click();
                }
            });
        """)
    )
