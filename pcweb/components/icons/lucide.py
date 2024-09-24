import reflex as rx
from reflex.components.lucide.icon import LUCIDE_ICON_LIST
from typing import List, Dict
import httpx
from pcweb.components.hint import hint
from pcweb.components.button import button


def create_lucide_icon(tag: str, attrs: dict, children: list = None) -> str:
    if children is None:
        children = []
    default_attributes = {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "24",
        "height": "24",
        "viewBox": "0 0 24 24",
        "fill": "none",
        "stroke": "currentColor",
        "stroke-width": "2",
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
    }
    # Merge default attributes with provided attributes
    merged_attrs = {**default_attributes, **attrs}

    # Convert attributes object to a string
    attr_string = " ".join([f'{key}="{value}"' for key, value in merged_attrs.items()])

    # Process children, recursively calling create_lucide_icon for nested elements
    children_string = "".join(
        [
            (
                child
                if isinstance(child, str)
                else create_lucide_icon(child[0], child[1], child[2])
            )
            for child in children
        ]
    )

    # Construct and return the element string
    return f"<{tag} {attr_string}>{children_string}</{tag}>"


def lucide_icon(tag: str, **attrs):
    return rx.html(create_lucide_icon("svg", {"tag": tag, **attrs}))


class IconState(rx.State):
    search_query: str = ""
    icons: List[Dict[str, str]] = []
    filtered_icons: List[Dict[str, str]] = []
    expanded: bool = False

    async def fetch_icons(self):
        icon_nodes_url = "https://lucide.dev/api/icon-nodes"
        icon_tags_url = "https://lucide.dev/api/tags"
        icon_categories_url = "https://lucide.dev/api/categories"

        try:
            async with httpx.AsyncClient() as client:
                icon_nodes_response = await client.get(icon_nodes_url)
                icon_tags_response = await client.get(icon_tags_url)
                icon_categories_response = await client.get(icon_categories_url)

            icon_nodes = icon_nodes_response.json()
            icon_tags = icon_tags_response.json()
            icon_categories = icon_categories_response.json()
        except httpx.HTTPError as e:
            print(f"Error fetching data: {e}")
            return

        icons = []
        for icon_name, icon_node in icon_nodes.items():
            content = create_lucide_icon(
                "svg",
                {
                    "class": f"lucide lucide-{icon_name.replace('_', '-')}",
                    "xmlns": "http://www.w3.org/2000/svg",
                    "width": "24",
                    "height": "24",
                    "viewBox": "0 0 24 24",
                    "fill": "none",
                    "stroke": "currentColor",
                    "stroke-width": "2",
                    "stroke-linecap": "round",
                    "stroke-linejoin": "round",
                },
                [create_lucide_icon(node[0], node[1]) for node in icon_node],
            )
            icons.append(
                {
                    "name": icon_name,
                    "content": content,
                    "path": f"https://lucide.dev/api/icons/{icon_name}",
                    "component": f"<{icon_name.replace('_', ' ').title().replace(' ', '')} />",
                    "keywords": icon_tags.get(icon_name, [])
                    + icon_categories.get(icon_name, []),
                }
            )
        # Filter only the ones that are in LUCIDE_ICON_LIST (icons from the current Reflex version)
        self.icons = [
            icon
            for icon in icons
            if icon["name"] in [name.replace("_", "-") for name in LUCIDE_ICON_LIST]
        ]
        self.filtered_icons = self.icons

    def filter_icons(self):
        if not self.search_query:
            self.filtered_icons = self.icons
        else:
            query = self.search_query.lower()
            self.filtered_icons = [
                icon
                for icon in self.icons
                if self._is_similar(query, icon["name"].lower())
                or any(self._is_similar(query, kw.lower()) for kw in icon["keywords"])
            ]

    def _is_similar(self, query: str, target: str) -> bool:
        if query in target:
            return True
        # Check for typos (allow one character difference)
        if len(query) > 3 and (
            query[:-1] in target
            or query[1:] in target
            or query[0] + query[2:] in target
        ):
            return True
        # Check for word order (split query into words and check if all words are in target)
        query_words = query.split()
        if len(query_words) > 1 and all(word in target for word in query_words):
            return True
        return False

    def update_search(self, value: str):
        self.search_query = value
        self.filter_icons()

    def copy_icon_name(self, name: str):
        yield rx.set_clipboard(name)
        return rx.toast(f'Copied "{name}" to clipboard')


def lucide_icons():
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(
                    tag="search",
                    size=20,
                    class_name="shrink-0 !text-slate-11",
                ),
                class_name="absolute left-2 top-1/2 transform -translate-y-1/2 z-[1] shrink-0 flex items-center justify-center pb-2",
            ),
            rx.el.input(
                placeholder="Search icons...",
                on_change=IconState.update_search.debounce(250),
                class_name="relative box-border border-slate-4 focus:border-violet-9 focus:border-1 bg-slate-2 p-[0.5rem_0.75rem] border rounded-xl font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full mb-2 pl-10",
            ),
            class_name="relative flex items-center",
        ),
        rx.box(
            rx.foreach(
                rx.cond(
                    IconState.expanded,
                    IconState.filtered_icons,
                    IconState.filtered_icons[:39],
                ),
                lambda icon: hint(
                    rx.text(icon["name"]),
                    content=rx.box(
                        rx.html(
                            icon["content"],
                            title=icon["name"],
                        ),
                        class_name="flex items-center justify-center rounded-md hover:bg-slate-3 transition-bg p-2 cursor-pointer",
                        on_click=IconState.copy_icon_name(icon["name"]),
                    ),
                ),
            ),
            class_name="flex flex-wrap justify-start gap-4 mb-4",
        ),
        button(
            rx.cond(
                IconState.expanded,
                "Show less",
                f"Show all ({IconState.filtered_icons.length()})",
            ),
            on_click=[
                IconState.setvar("expanded", ~IconState.expanded),
                rx.scroll_to("icons-list"),
            ],
            display=rx.cond(IconState.filtered_icons.length() > 40, "block", "none"),
            # class_name="max-w-[350px]",
        ),
        on_mount=IconState.fetch_icons,
        class_name="flex flex-col gap-4",
    )
