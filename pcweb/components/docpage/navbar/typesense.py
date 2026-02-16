import os

import reflex as rx
import reflex_ui as ui
import typesense
from reflex.experimental import ClientStateVar

last_copied = ClientStateVar.create("is_copied", "")

suggestion_items = [
    {
        "name": "Components Overview",
        "path": "/docs/library",
        "icon": "blocks",
        "description": "Discover and explore the full library of available components",
    },
    {
        "name": "State Management",
        "path": "/docs/state/overview",
        "icon": "database",
        "description": "Master state handling, data flow, and reactive programming",
    },
    {
        "name": "Event Overview",
        "path": "/docs/events/events-overview",
        "icon": "zap",
        "description": "Learn how to handle user interactions and system events",
    },
    {
        "name": "Styling and Theming",
        "path": "/docs/styling/overview",
        "icon": "palette",
        "description": "Customize colors, layouts, and create beautiful app designs",
    },
    {
        "name": "Deployment Guide",
        "path": "/docs/hosting/deploy-quick-start/",
        "icon": "cloud",
        "description": "Deploy and host your application in production environments",
    },
]

CLUSTERS = {
    "All Content": [],
    "AI Builder": ["ai_builder"],
    "Hosting": ["hosting"],
    "Components": ["custom-components", "recipes"],
    "Enterprise": ["enterprise"],
    "API Reference": ["api-reference", "api-routes"],
    "Docs": [
        "advanced_onboarding",
        "assets",
        "authentication",
        "client_storage",
        "components",
        "database",
        "events",
        "getting_started",
        "library",
        "pages",
        "state",
        "state_structure",
        "styling",
        "ui",
        "utility_methods",
        "vars",
        "wrapping-react",
    ],
    "Blog Posts": [],
}


TYPESENSE_CONFIG = {
    "nodes": [
        {"host": os.getenv("TYPESENSE_HOST"), "port": "443", "protocol": "https"}
    ],
    "api_key": os.getenv("TYPESENSE_SEARCH_API_KEY"),
    "connection_timeout_seconds": 2,
}


class SimpleSearch(rx.State):
    query: str
    selected_filter: str = "All Content"
    is_fetching: bool = False

    idxed_docs_results: list[dict] = []
    idxed_blogs_results: list[dict] = []

    @rx.event(temporal=True)
    def user_query(self, value: str):
        self.query = value.replace("rx.", "")

    @rx.event(temporal=True)
    def reset_search(self):
        """Reset state variables."""
        self.idxed_blogs_results = []
        self.idxed_docs_results = []
        self.query = ""

    @rx.event(temporal=True)
    async def apply_filter_search(self, selected_filter: str):
        """Re-run search with new filter."""
        if self.selected_filter == selected_filter:
            return

        self.selected_filter = selected_filter

        if self.query.strip():
            yield SimpleSearch.perform_search()

    @rx.event(background=True, temporal=True)
    async def perform_search(self):
        """Perform Typesense search and split results."""
        async with self:
            if not self.query.strip():
                self.idxed_docs_results = []
                self.idxed_blogs_results = []
                return

        try:
            async with self:
                self.is_fetching = True
                yield

            client = typesense.Client(TYPESENSE_CONFIG)

            search_params = {
                "q": self.query,
                "query_by": "title,content,headings,components",
                "query_by_weights": "6,8,3,12",
                "per_page": 15,
                "num_typos": 2,
                "sort_by": "_text_match:desc",
                "text_match_threshold": "0.6",
                "exhaustive_search": True,
                "highlight_fields": "content",
                "highlight_full_fields": "content,components",
                "highlight_start_tag": "<mark>",
                "highlight_end_tag": "</mark>",
                "snippet_threshold": 30,
            }

            if self.selected_filter != "All Content":
                if self.selected_filter == "Blog Posts":
                    search_params["filter_by"] = "section:=Blog"
                else:
                    sections = self._get_sections_for_cluster(self.selected_filter)
                    if sections:
                        section_filter = " || ".join(f"section:={s}" for s in sections)
                        search_params["filter_by"] = section_filter

            result = client.collections["docs"].documents.search(search_params)

            docs_results = []
            blog_results = []

            for hit in result["hits"]:
                doc = hit["document"]
                formatted_doc = self._format_result(doc, hit.get("highlights", []))

                if doc.get("section") == "Blog":
                    blog_results.append(formatted_doc)
                else:
                    docs_results.append(formatted_doc)

            async with self:
                self.idxed_docs_results = docs_results
                self.idxed_blogs_results = blog_results
                self.is_fetching = False

        except Exception:
            async with self:
                self.idxed_docs_results = []
                self.idxed_blogs_results = []
                self.is_fetching = False

    def _get_highlighted_content(
        self, doc, highlights: list | None, snippet_length=350
    ):
        import re

        bold_stype = '<span style="font-weight: 900; color: #AA99EC;">'
        close_tag = "</span>"
        content = doc.get("content", "") or ""

        def bold_tokens(snippet: str, tokens: list[str]) -> str:
            for tok in sorted({t for t in tokens if t}, key=len, reverse=True):
                try:
                    snippet = re.sub(
                        re.escape(tok),
                        f"{bold_stype}\\g<0>{close_tag}",
                        snippet,
                        flags=re.IGNORECASE,
                    )
                except re.error:
                    snippet = snippet.replace(tok, f"{bold_stype}{tok}{close_tag}")
            return snippet

        # 1) Typesense content/title highlights
        for h in highlights or []:
            if h.get("field") in ("content", "title"):
                snippet = h.get("snippet") or h.get("value") or ""
                if snippet:
                    marked = re.findall(
                        r"<mark>(.*?)</mark>", snippet, flags=re.IGNORECASE
                    )
                    if marked:
                        token = marked[0]
                        idx = content.lower().find(token.lower())
                        if idx != -1:
                            start = max(0, idx - snippet_length // 2)
                            end = min(
                                len(content), idx + len(token) + snippet_length // 2
                            )
                            snippet = content[start:end]
                            snippet = bold_tokens(snippet, marked)
                            if start > 0:
                                snippet = "..." + snippet
                            if end < len(content):
                                snippet = snippet + "..."
                            return snippet

                    snippet = snippet.replace("<mark>", bold_stype).replace(
                        "</mark>", close_tag
                    )
                    return snippet[:snippet_length] + (
                        "..." if len(snippet) > snippet_length else snippet
                    )

        # 2) Typesense component highlights (simplified)
        for h in highlights or []:
            if h.get("field", "").startswith("components"):
                values = h.get("values") or ([h.get("value")] if h.get("value") else [])
                if values:
                    cleaned = [
                        v.replace("<mark>", bold_stype).replace("</mark>", close_tag)
                        for v in values
                        if v
                    ]
                    return f"Matches found: {', '.join(cleaned[:6])}"

        # 3) Client-side components match
        q = (getattr(self, "query", "") or "").strip().lower()
        if q:
            comps = doc.get("components") or []
            matched = [c for c in comps if isinstance(c, str) and q in c.lower()]
            if matched:
                bolded = [
                    re.sub(
                        re.escape(q),
                        f"{bold_stype}\\g<0>{close_tag}",
                        c,
                        flags=re.IGNORECASE,
                    )
                    for c in matched[:6]
                ]
                return f"Matches found: {', '.join(bolded)}"

        # 4) fallback: truncated content
        return self._truncate_content(content, max_length=snippet_length)

    def _get_sections_for_cluster(self, cluster_name: str) -> list[str]:
        """Map cluster names to section names."""
        return CLUSTERS.get(cluster_name, [])

    def _format_result(self, doc: dict, highlights: list | None = None) -> dict:
        """Format Typesense result to match your fuzzy search structure."""
        if doc.get("section") != "Blog":
            return {
                "name": doc.get("title", ""),
                "parts": doc.get("parts", []),
                "url": doc.get("url", ""),
                "image": doc.get("path", ""),
                "cluster": self._get_cluster_from_section(doc.get("section", "")),
                "description": self._get_highlighted_content(doc, highlights),
            }

        else:
            return {
                "title": doc.get("title", ""),
                "url": doc.get("url", ""),
                "author": doc.get("author", ""),
                "date": doc.get("date", ""),
                "description": self._truncate_content(doc.get("content", "")),
                "image": doc.get("image", ""),
            }

    def _get_cluster_from_section(self, section: str) -> str:
        """Map section back to cluster name."""
        for cluster, sections in CLUSTERS.items():
            if section in sections:
                return cluster
        return "Docs"

    def _truncate_content(self, content: str, max_length: int = 200) -> str:
        """Truncate content for description."""
        if len(content) <= max_length:
            return content
        return content[:max_length].rstrip() + "..."


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
    return rx.el.button(
        ui.icon(icon="Search01Icon", class_name="shrink-0"),
        rx.el.span(
            "Search",
            class_name="hidden md:block text-sm font-medium",
        ),
        rx.html(
            rx.color_mode_cond(
                """<svg width="38" height="20" viewBox="0 0 38 20" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="38" height="20" rx="4" fill="#f0f0f3"/><path d="M6.448 14q-.84 0-1.344-.492-.492-.492-.492-1.32 0-.876.516-1.356.528-.492 1.548-.492h.708V9.02h-.708q-1.02 0-1.548-.48-.516-.492-.516-1.368 0-.828.492-1.32.504-.492 1.344-.492.672 0 1.056.252.396.252.552.672.168.42.168.924v.996h1.32v-.996q0-.504.156-.924.168-.42.552-.672.396-.252 1.068-.252.84 0 1.332.492.504.492.504 1.32 0 .876-.516 1.368-.516.48-1.548.48h-.708v1.32h.708q1.032 0 1.548.492.516.48.516 1.356 0 .828-.504 1.32Q12.16 14 11.32 14q-.672 0-1.068-.252a1.4 1.4 0 0 1-.552-.672 2.6 2.6 0 0 1-.156-.924v-.996h-1.32v.996q0 .504-.168.924a1.33 1.33 0 0 1-.552.672Q7.12 14 6.448 14m3.936-6.816v1.02h.708q.636 0 .924-.252.288-.264.288-.78 0-.528-.288-.756-.276-.228-.696-.228-.468 0-.708.276-.228.264-.228.72m-3.708 1.02h.708v-1.02q0-.456-.24-.72-.228-.276-.696-.276-.42 0-.708.228-.276.228-.276.756 0 .516.288.78.288.252.924.252m1.548 2.136h1.32V9.02h-1.32zm-1.776 2.832q.468 0 .696-.264.24-.276.24-.732v-1.02h-.708q-.636 0-.924.264-.288.252-.288.768 0 .528.276.756.288.228.708.228m3.936-.996q0 .456.228.732.24.264.708.264.42 0 .696-.228.288-.228.288-.756 0-.516-.288-.768-.288-.264-.924-.264h-.708zm8.504.048V6.86h.972v5.364zm-2.04-2.208V9.08H21.9v.936zM25.888 14V5.36h1.2V14zm.973-4.488 4.344-4.152h1.644l-4.464 4.152zM31.397 14l-4.56-4.488h1.548L33.089 14z" fill="#60646c"/></svg>""",
                """<svg width="38" height="20" viewBox="0 0 38 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="38" height="20" rx="4" fill="#21252B"/>
<path d="M6.448 14C5.888 14 5.44 13.836 5.104 13.508C4.776 13.18 4.612 12.74 4.612 12.188C4.612 11.604 4.784 11.152 5.128 10.832C5.48 10.504 5.996 10.34 6.676 10.34H7.384V9.02H6.676C5.996 9.02 5.48 8.86 5.128 8.54C4.784 8.212 4.612 7.756 4.612 7.172C4.612 6.62 4.776 6.18 5.104 5.852C5.44 5.524 5.888 5.36 6.448 5.36C6.896 5.36 7.248 5.444 7.504 5.612C7.768 5.78 7.952 6.004 8.056 6.284C8.168 6.564 8.224 6.872 8.224 7.208V8.204H9.544V7.208C9.544 6.872 9.596 6.564 9.7 6.284C9.812 6.004 9.996 5.78 10.252 5.612C10.516 5.444 10.872 5.36 11.32 5.36C11.88 5.36 12.324 5.524 12.652 5.852C12.988 6.18 13.156 6.62 13.156 7.172C13.156 7.756 12.984 8.212 12.64 8.54C12.296 8.86 11.78 9.02 11.092 9.02H10.384V10.34H11.092C11.78 10.34 12.296 10.504 12.64 10.832C12.984 11.152 13.156 11.604 13.156 12.188C13.156 12.74 12.988 13.18 12.652 13.508C12.324 13.836 11.88 14 11.32 14C10.872 14 10.516 13.916 10.252 13.748C9.996 13.58 9.812 13.356 9.7 13.076C9.596 12.796 9.544 12.488 9.544 12.152V11.156H8.224V12.152C8.224 12.488 8.168 12.796 8.056 13.076C7.952 13.356 7.768 13.58 7.504 13.748C7.248 13.916 6.896 14 6.448 14ZM10.384 7.184V8.204H11.092C11.516 8.204 11.824 8.12 12.016 7.952C12.208 7.776 12.304 7.516 12.304 7.172C12.304 6.82 12.208 6.568 12.016 6.416C11.832 6.264 11.6 6.188 11.32 6.188C11.008 6.188 10.772 6.28 10.612 6.464C10.46 6.64 10.384 6.88 10.384 7.184ZM6.676 8.204H7.384V7.184C7.384 6.88 7.304 6.64 7.144 6.464C6.992 6.28 6.76 6.188 6.448 6.188C6.168 6.188 5.932 6.264 5.74 6.416C5.556 6.568 5.464 6.82 5.464 7.172C5.464 7.516 5.56 7.776 5.752 7.952C5.944 8.12 6.252 8.204 6.676 8.204ZM8.224 10.34H9.544V9.02H8.224V10.34ZM6.448 13.172C6.76 13.172 6.992 13.084 7.144 12.908C7.304 12.724 7.384 12.48 7.384 12.176V11.156H6.676C6.252 11.156 5.944 11.244 5.752 11.42C5.56 11.588 5.464 11.844 5.464 12.188C5.464 12.54 5.556 12.792 5.74 12.944C5.932 13.096 6.168 13.172 6.448 13.172ZM10.384 12.176C10.384 12.48 10.46 12.724 10.612 12.908C10.772 13.084 11.008 13.172 11.32 13.172C11.6 13.172 11.832 13.096 12.016 12.944C12.208 12.792 12.304 12.54 12.304 12.188C12.304 11.844 12.208 11.588 12.016 11.42C11.824 11.244 11.516 11.156 11.092 11.156H10.384V12.176ZM18.8883 12.224V6.86H19.8603V12.224H18.8883ZM16.8483 10.016V9.08H21.9003V10.016H16.8483ZM25.8888 14V5.36H27.0888V14H25.8888ZM26.8608 9.512L31.2048 5.36H32.8488L28.3848 9.512H26.8608ZM31.3968 14L26.8368 9.512H28.3848L33.0888 14H31.3968Z" fill="#979FAA"/>
</svg>
""",
            ),
            class_name="ml-auto hidden md:block",
        ),
        class_name="text-m-slate-7 dark:text-m-slate-6 h-8 px-2 py-1.5 rounded-lg bg-m-slate-1 dark:bg-m-slate-11 flex flex-row items-center justify-start gap-2 lg:w-[10rem] w-full hover:bg-m-slate-2 dark:hover:bg-m-slate-10 dark:shadow-[0_-1px_0_0_rgba(255,_255,_255,_0.06)_inset,_0_0_0_1px_rgba(255,_255,_255,_0.04)_inset] shadow-[0_-1px_0_0_rgba(0,_0,_0,_0.08)_inset,_0_0_0_1px_rgba(0,_0,_0,_0.08)_inset,_0_1px_2px_0_rgba(0,_0,_0,_0.02),_0_1px_4px_0_rgba(0,_0,_0,_0.02)]",
        id="search-trigger",
        custom_attrs={"aria-label": "Search documentation"},
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
                        "›",  # noqa: RUF001
                        class_name="text-sm font-medium",
                        color=rx.color("slate", 11),
                    ),
                ),
                rx.el.label(
                    item,
                    class_name=rx.cond(
                        index == (items.length() - 1),
                        "text-sm font-medium",
                        "text-sm font-regular",
                    ),
                    color=rx.cond(
                        index == (items.length() - 1),
                        rx.color("slate", 12),
                        rx.color("slate", 11),
                    ),
                ),
            ),
        ),
        spacing="1",
        cursor="pointer",
    )


def cluster_icon(filter_name: str):
    icons = {
        "All Content": "DragDropIcon",
        "AI Builder": "RoboticIcon",
        "Hosting": "CloudIcon",
        "Components": "BlockGameIcon",
        "Docs": "File01Icon",
        "Enterprise": "City02Icon",
        "API Reference": "ApiIcon",
        "Blog Posts": "BloggerIcon",
    }
    return ui.icon(icon=icons.get(filter_name, ""), class_name="shrink-0 size-4")


def filter_items(filter_name: str):
    return ui.popover.close(
        rx.el.div(
            rx.el.div(
                cluster_icon(filter_name),
                rx.el.button(
                    filter_name,
                    class_name="w-full text-left",
                    type="button",
                ),
                class_name="flex flex-row items-center gap-x-3",
            ),
            rx.cond(
                SimpleSearch.selected_filter == filter_name,
                rx.icon(tag="check", size=12),
            ),
            on_click=SimpleSearch.apply_filter_search(filter_name),
            class_name="flex flex-row gap-x-2 items-center px-3 py-1 w-full justify-between cursor-pointer outline-none hover:bg-slate-3 focus:border-none",
        )
    )


def filter_icon(tag: str):
    """Helper to render icons for filters consistently."""
    return ui.icon(icon=tag, class_name="shrink-0 size-3")


def filter_component():
    return ui.popover.root(
        ui.popover.trigger(
            ui.button(
                rx.el.div(
                    rx.el.div(
                        rx.match(
                            SimpleSearch.selected_filter,
                            ("All Content", filter_icon("DragDropIcon")),
                            ("AI Builder", filter_icon("RoboticIcon")),
                            ("Hosting", filter_icon("CloudIcon")),
                            ("Components", filter_icon("BlockGameIcon")),
                            ("Docs", filter_icon("File01Icon")),
                            ("Enterprise", filter_icon("City02Icon")),
                            ("API Reference", filter_icon("ApiIcon")),
                            ("Blog Posts", filter_icon("BloggerIcon")),
                        ),
                        SimpleSearch.selected_filter,
                        class_name="text-sm flex flex-row items-center gap-x-2",
                    ),
                    ui.icon(icon="UnfoldMoreIcon", class_name="shrink-0 size-3"),
                    class_name="flex flex-row items-center justify-between w-[150px] text-sm",
                ),
                class_name="flex flex-row justify-between items-center gap-x-4 rounded-md outline-none",
                type="button",
                variant="outline",
                size="xs",
            ),
        ),
        ui.popover.portal(
            ui.popover.positioner(
                ui.popover.popup(
                    rx.box(
                        *[filter_items(filter_name) for filter_name in CLUSTERS],
                        class_name="w-[190px] flex flex-col text-sm rounded-md shadow-md gap-y-1 py-2",
                    ),
                    class_name="items-center !p-0 w-auto overflow-visible pointer-events-auto",
                ),
                side="bottom",
                side_offset=15,
            ),
        ),
        class_name="rounded-md border border-slate-5",
        id="my-popover",
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
                ui.link(
                    render_=ui.button(
                        ui.icon(icon="SparklesIcon", class_name="shrink-0 size-3.5"),
                        "Ask AI",
                        type="button",
                        variant="secondary",
                        size="xs",
                    ),
                    to="https://reflex.dev/docs/ai-builder/integrations/mcp-overview/",
                ),
                ui.button(
                    "Esc",
                    size="xs",
                    type="button",
                    variant="outline",
                    on_click=rx.run_script(
                        "document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }))"
                    ),
                ),
                class_name="hidden md:flex absolute right-2 top-1/2 transform -translate-y-1/2 text-sm flex-row items-center gap-x-2",
            ),
            rx.el.input(
                on_change=[
                    lambda value: SimpleSearch.user_query(value).debounce(500),
                    SimpleSearch.perform_search(),
                ],
                auto_focus=True,
                placeholder="Search documentation ...",
                class_name="py-2 pl-7 md:pr-[310px] w-full placeholder:text-sm text-sm rounded-lg outline-none focus:outline-none border border-secondary-a4 bg-secondary-1 text-secondary-12",
            ),
            class_name="w-full relative focus:outline-none",
        ),
        class_name="w-full flex flex-col absolute top-0 left-0 p-3 z-[999]",
    )


def copy_button(url: str):
    return ui.button(
        rx.cond(
            last_copied.value == url,
            ui.icon("CheckmarkCircle02Icon", class_name="size-2"),
            ui.icon("Share08Icon", size=10, class_name="size-2"),
        ),
        variant="outline",
        size="xs",
        on_click=[
            rx.set_clipboard(url).prevent_default,
            rx.call_function(last_copied.set_value(url)),
        ],
        on_mouse_down=rx.call_function(last_copied.set_value("")).debounce(1500),
    )


def search_result(tags: list, value: dict):
    return rx.link(
        rx.box(
            rx.box(
                rx.text(value["name"], class_name="text-sm font-bold"),
                copy_button(url=f"https://reflex.dev/{value['url'].to(str)}"),
                class_name="flex flex-row items-center justify-between pr-1 w-full",
            ),
            rx.html(
                value["description"],
                class_name=(
                    "text-sm font-regular opacity-[0.81] "
                    "line-clamp-2 overflow-hidden text-ellipsis"
                ),
                style={
                    "display": "-webkit-box",
                    "-webkit-line-clamp": "2",
                    "-webkit-box-orient": "vertical",
                },
            ),
            search_breadcrumb(tags),
            class_name="p-2 w-full flex flex-col gap-y-2 justify-start items-start align-start",
        ),
        href=f"/{value['url'].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit hover:bg-secondary-2 group",
    )


def search_result_blog(value: dict):
    return rx.link(
        rx.box(
            rx.box(
                rx.box(
                    rx.text(value["author"]),
                    "-",
                    rx.text(value["date"]),
                    class_name="flex flex-row gap-x-2 items-center text-sm !text-slate-10",
                ),
                copy_button(url=f"https://reflex.dev{value['url'].to(str)}"),
                class_name="flex flex-row w-full items-center justify-between pr-1",
            ),
            rx.text(value["title"], class_name="text-md font-bold"),
            rx.text(
                value["description"],
                class_name=(
                    "text-sm font-regular opacity-[0.81] "
                    "line-clamp-2 overflow-hidden text-ellipsis"
                ),
                style={
                    "display": "-webkit-box",
                    "-webkit-line-clamp": "2",
                    "-webkit-box-orient": "vertical",
                },
            ),
            rx.box(
                rx.image(
                    src=value["image"].to(str),
                    class_name="rounded-md",
                ),
                class_name="w-full rounded-[10px] pt-3",
            ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=f"{value['url'].to(str)}",
        class_name="!text-inherit no-underline hover:!text-inherit hover:bg-secondary-2",
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
                style={
                    "display": "-webkit-box",
                    "-webkit-line-clamp": "2",
                    "-webkit-box-orient": "vertical",
                },
            ),
            class_name="p-2 w-full flex flex-col gap-y-1 justify-start items-start align-start",
        ),
        href=item["path"],
        class_name="!text-inherit no-underline hover:!text-inherit rounded-md hover:bg-secondary-2",
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


def searching_in_progress():
    return rx.box(
        rx.el.p(
            rx.fragment(
                "Searching for ",
                rx.el.strong(f"'{SimpleSearch.query}'"),
                "...",
            ),
        ),
        class_name="w-full flex items-center justify-center text-sm py-4",
    )


def search_content():
    return rx.scroll_area(
        rx.cond(
            SimpleSearch.query.length() < 3,
            rx.box(
                rx.foreach(suggestion_items, lambda value: search_result_start(value)),
                class_name="flex flex-col gap-y-2",
            ),
            rx.cond(
                SimpleSearch.is_fetching,
                rx.cond(
                    (SimpleSearch.idxed_docs_results.length() >= 1)
                    | (SimpleSearch.idxed_blogs_results.length() >= 1),
                    rx.box(
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_docs_results,
                                lambda value: search_result(
                                    value["parts"].to(list), value
                                ),
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_blogs_results,
                                lambda value: search_result_blog(value),
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    searching_in_progress(),
                ),
                rx.cond(
                    (SimpleSearch.idxed_docs_results.length() >= 1)
                    | (SimpleSearch.idxed_blogs_results.length() >= 1),
                    rx.box(
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_docs_results,
                                lambda value: search_result(
                                    value["parts"].to(list), value
                                ),
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        rx.box(
                            rx.foreach(
                                SimpleSearch.idxed_blogs_results,
                                lambda value: search_result_blog(value),
                            ),
                            class_name="flex flex-col gap-y-2",
                        ),
                        class_name="flex flex-col",
                    ),
                    no_results_found(),
                ),
            ),
        ),
        class_name="w-full h-full pt-11 [&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] [&_.rt-ScrollAreaScrollbar]:mt-[3rem]",
    )


def typesense_search() -> rx.Component:
    """Create the main search component for Reflex Web."""
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(search_trigger(), id="search-trigger"),
            rx.dialog.content(
                search_input(),
                search_content(),
                on_interact_outside=SimpleSearch.reset_search,
                on_escape_key_down=SimpleSearch.reset_search,
                class_name="!font-sans w-full max-w-[650px] mx-auto bg-secondary-1 border-none outline-none p-3 lg:!fixed lg:!top-24 lg:!left-1/2 lg:!transform lg:!-translate-x-1/2 lg:!translate-y-0 lg:!m-0 "
                + rx.cond(SimpleSearch.query.length() < 3, "min-h[57vh]", "h-[57vh]"),
            ),
        ),
        keyboard_shortcut_script(),
        class_name="w-full",
    )
