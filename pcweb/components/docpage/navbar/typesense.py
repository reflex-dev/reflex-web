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
                    'path': hit['document']['path']
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
    
    def navigate_to_result(self, url: str):
        """Navigate to a search result."""
        self.show_results = False
        return rx.redirect(url)


def search_result_item(result: rx.Var) -> rx.Component:
    """Render a single search result item."""
    return rx.box(
        rx.vstack(
            rx.text(
                result['title'],
                font_weight="600",
                color="var(--c-slate-12)",
                font_size="14px",
                margin_bottom="4px"
            ),
            rx.text(
                result['content'],
                color="var(--c-slate-11)",
                font_size="13px",
                line_height="1.4",
                margin_bottom="4px"
            ),
            rx.text(
                result['path'],
                color="var(--c-slate-9)",
                font_size="12px"
            ),
            align_items="start",
            spacing="1"
        ),
        padding="12px",
        border_bottom="1px solid var(--c-slate-3)",
        cursor="pointer",
        _hover={"background_color": "var(--c-slate-2)"},
        on_click=lambda: TypesenseSearchState.navigate_to_result(result['url'])
    )


def typesense_search() -> rx.Component:
    """Create the Typesense search component."""
    return rx.box(
        rx.input(
            placeholder="Search docs...",
            value=TypesenseSearchState.search_query,
            on_change=TypesenseSearchState.search_docs,
            on_blur=TypesenseSearchState.hide_results,
            style={
                "display": "flex",
                "max_height": "32px",
                "min_height": "32px",
                "padding": "6px 12px",
                "min_width": "256px",
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
            _focus={"border_color": "var(--c-violet-7)"}
        ),
        rx.cond(
            TypesenseSearchState.show_results & (TypesenseSearchState.search_results.length() > 0),
            rx.box(
                rx.foreach(
                    TypesenseSearchState.search_results,
                    search_result_item
                ),
                position="absolute",
                top="100%",
                left="0",
                right="0",
                background="var(--c-slate-1)",
                border="1px solid var(--c-slate-5)",
                border_radius="10px",
                box_shadow="0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
                max_height="400px",
                overflow_y="auto",
                z_index="1000",
                margin_top="4px"
            )
        ),
        rx.cond(
            TypesenseSearchState.is_searching,
            rx.box(
                rx.text(
                    "Searching...",
                    color="var(--c-slate-9)",
                    font_size="12px"
                ),
                position="absolute",
                top="100%",
                left="0",
                right="0",
                background="var(--c-slate-1)",
                border="1px solid var(--c-slate-5)",
                border_radius="10px",
                padding="12px",
                margin_top="4px",
                z_index="1000"
            )
        ),
        position="relative",
        class_name="search-container"
    )

search_styles = """
<style>
.search-container {
    position: relative;
}

@media (max-width: 80em) {
    .search-container input {
        min-width: 32px !important;
        max-width: 6em !important;
        padding: 2px 12px !important;
    }
}
</style>
"""

def typesense_search_with_styles() -> rx.Component:
    """Create the Typesense search component with styles."""
    return rx.fragment(
        rx.html(search_styles),
        typesense_search()
    )
