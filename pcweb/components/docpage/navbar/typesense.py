"""Typesense search component for the navbar."""

import reflex as rx
from reflex.utils.imports import ImportVar
from reflex.vars import Var


class TypesenseSearchState(rx.State):
    """State for the Typesense search component."""
    
    search_query: str = ""
    search_results: list[dict] = []
    is_searching: bool = False
    show_results: bool = False
    show_modal: bool = False
    
    suggestions = [
        {"title": "Getting Started with Reflex", "url": "/docs/getting-started/introduction"},
        {"title": "Components Overview", "url": "/docs/library"},
        {"title": "State Management", "url": "/docs/state/overview"},
        {"title": "Event Handlers", "url": "/docs/events/event-handlers"},
        {"title": "Styling and Theming", "url": "/docs/styling/overview"},
        {"title": "Deployment Guide", "url": "/docs/hosting/deploy"},
    ]
    
    def open_modal(self):
        """Open the search modal."""
        self.show_modal = True
        
    def close_modal(self):
        """Close the search modal and reset state."""
        self.show_modal = False
        self.show_results = False
        self.search_query = ""
        self.search_results = []
        
    def handle_key_down(self, key: str):
        """Handle keyboard events."""
        if key == "Escape":
            self.close_modal()
    
    async def search_docs(self, query: str):
        """Search the documentation using Typesense."""
        self.search_query = query
        if not query.strip():
            self.search_results = []
            self.show_results = False
            return
        
        self.is_searching = True
        
        try:
            import typesense
            
            import os
            
            client = typesense.Client({
                'nodes': [{
                    'host': 'z2mi3hyewokc16a4p-1.a1.typesense.net',
                    'port': '443',
                    'protocol': 'https'
                }],
                'api_key': os.getenv('TYPESENSE_SEARCH_API_KEY'),
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
                'state_structure': 'State Structure'
            }.get(section, section.replace('-', ' ').replace('_', ' ').title())
            parts.append(section_display)
        
        subsection = document.get('subsection', '')
        if subsection:
            subsection_display = subsection.replace('-', ' ').replace('_', ' ').title()
            parts.append(subsection_display)
        
        title = document.get('title', '')
        if title and (not parts or title.lower() != parts[-1].lower()):
            parts.append(title)
        
        return ' > '.join(parts)

    def navigate_to_result(self, url: str):
        """Navigate to a search result."""
        self.show_results = False
        self.show_modal = False
        return rx.redirect(url)


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
        cursor="pointer",
        border_radius="6px",
        _hover={"background_color": "var(--c-slate-3)"},
        on_click=lambda: TypesenseSearchState.navigate_to_result(url),
        width="100%"
    )


def search_result_item(result: rx.Var) -> rx.Component:
    """Render a single search result item with breadcrumb navigation."""
    return rx.box(
        rx.vstack(
            rx.text(
                result['breadcrumb'],
                color="var(--c-slate-9)",
                font_size="12px",
                font_weight="500",
                margin_bottom="4px"
            ),
            rx.hstack(
                rx.icon("file-text", size=16, color="var(--c-slate-9)"),
                rx.text(
                    result['title'],
                    font_weight="600",
                    color="var(--c-slate-12)",
                    font_size="15px"
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
        padding="12px",
        border="1px solid var(--c-slate-4)",
        border_radius="8px",
        cursor="pointer",
        _hover={"background_color": "var(--c-slate-2)", "border_color": "var(--c-slate-5)"},
        on_click=lambda: TypesenseSearchState.navigate_to_result(result['url']),
        width="100%"
    )


def search_modal() -> rx.Component:
    """Create the full-screen search modal."""
    return rx.cond(
        TypesenseSearchState.show_modal,
        rx.box(
            rx.box(
                position="fixed",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background="rgba(0, 0, 0, 0.6)",
                backdrop_filter="blur(4px)",
                z_index="9999",
                on_click=TypesenseSearchState.close_modal
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.button(
                            "Esc",
                            variant="ghost",
                            size="2",
                            color="var(--c-slate-9)",
                            on_click=TypesenseSearchState.close_modal
                        ),
                        width="100%",
                        justify="end",
                        margin_bottom="12px"
                    ),
                    rx.input(
                        placeholder="What are you searching for?",
                        value=TypesenseSearchState.search_query,
                        on_change=TypesenseSearchState.search_docs,
                        auto_focus=True,
                        style={
                            "width": "100%",
                            "padding": "12px 16px",
                            "font_size": "16px",
                            "border": "1px solid var(--c-slate-6)",
                            "border_radius": "8px",
                            "background": "var(--c-slate-1)",
                            "color": "var(--c-slate-12)",
                            "outline": "none"
                        },
                        _focus={"border_color": "var(--c-violet-7)"}
                    ),
                    rx.cond(
                        TypesenseSearchState.search_query.length() > 0,
                        rx.cond(
                            TypesenseSearchState.search_results.length() > 0,
                            rx.vstack(
                                rx.foreach(
                                    TypesenseSearchState.search_results,
                                    search_result_item
                                ),
                                spacing="2",
                                width="100%",
                                margin_top="16px"
                            ),
                            rx.cond(
                                TypesenseSearchState.is_searching,
                                rx.text("Searching...", color="var(--c-slate-9)", margin_top="16px"),
                                rx.text("No results found", color="var(--c-slate-9)", margin_top="16px")
                            )
                        ),
                        rx.vstack(
                            rx.text(
                                "Suggestions",
                                font_weight="600",
                                color="var(--c-slate-11)",
                                font_size="14px",
                                margin_top="16px",
                                margin_bottom="8px"
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
                            width="100%",
                            align_items="start"
                        )
                    ),
                    spacing="3",
                    width="100%",
                    max_width="520px"
                ),
                position="fixed",
                top="20%",
                left="50%",
                transform="translateX(-50%)",
                background="var(--c-slate-1)",
                border="1px solid var(--c-slate-6)",
                border_radius="16px",
                padding="16px",
                box_shadow="0px 24px 48px rgba(0, 0, 0, 0.2)",
                z_index="10000",
                max_height="70vh",
                overflow_y="auto",
                tab_index=0
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="9998"
        )
    )


def typesense_search() -> rx.Component:
    """Create the Typesense search trigger component."""
    return rx.box(
        rx.input(
            placeholder="Search docs...",
            on_focus=TypesenseSearchState.open_modal,
            style={
                "display": "flex",
                "max_height": "32px",
                "min_height": "32px",
                "padding": "6px 12px",
                "min_width": ["32px", "32px", "256px"],
                "max_width": ["6em", "6em", "none"],
                "border_radius": "10px",
                "border": "1px solid var(--c-slate-5, #E0E1E6)",
                "background": "var(--c-slate-1)",
                "font_family": "Instrument Sans",
                "font_size": "14px",
                "font_weight": "500",
                "line_height": "20px",
                "letter_spacing": "-0.0125em",
                "color": "var(--c-slate-9, #8B8D98)",
                "box_shadow": "0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
                "transition": "background-color 0.1s linear",
                "outline": "none"
            },
            _hover={"background_color": "var(--c-slate-3, #F0F0F3)"},
        ),
        search_modal(),
        position="relative"
    )
