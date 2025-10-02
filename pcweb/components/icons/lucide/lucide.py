import reflex as rx
from reflex.components.lucide.icon import LUCIDE_ICON_LIST
from typing import List, Dict
from pcweb.components.hint import hint
from pcweb.components.button import button
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")


def load_json(filename):
    with open(os.path.join(data_dir, filename), "r") as f:
        return json.load(f)


icon_nodes = load_json("icon-nodes.json")
icon_tags = load_json("icon-tags.json")
icon_categories = load_json("icon-categories.json")

# Convert LUCIDE_ICON_LIST to use hyphens instead of underscores
LUCIDE_ICON_LIST = [icon_name.replace("_", "-") for icon_name in LUCIDE_ICON_LIST]


def create_lucide_icon(tag: str, attrs: dict, children: list = None) -> str:
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
    merged_attrs = {**default_attributes, **attrs}
    attr_string = " ".join(f'{key}="{value}"' for key, value in merged_attrs.items())
    children_string = "".join(
        child if isinstance(child, str) else create_lucide_icon(*child)
        for child in (children or [])
    )
    return f"<{tag} {attr_string}>{children_string}</{tag}>"


def lucide_icon(tag: str, **attrs):
    return rx.html(create_lucide_icon("svg", {"tag": tag, **attrs}))


class IconState(rx.State):
    search_query: str = ""
    icons: List[Dict[str, str]] = []
    filtered_icons: List[Dict[str, str]] = []
    expanded: bool = False

    @rx.event
    def set_expanded(self):
        self.expanded = not self.expanded

    @rx.event
    def fetch_icons(self):
        default_svg_attrs = {
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

        self.icons = [
            {
                "name": icon_name,
                "content": create_lucide_icon(
                    "svg",
                    {**default_svg_attrs, "class": f"lucide lucide-{icon_name}"},
                    [
                        create_lucide_icon(node[0], node[1])
                        for node in icon_nodes[icon_name]
                    ],
                ),
                "path": f"https://lucide.dev/api/icons/{icon_name}",
                "component": f"<{icon_name.replace('-', '').title()} />",
                "keywords": icon_tags.get(icon_name, [])
                + icon_categories.get(icon_name, []),
            }
            for icon_name in LUCIDE_ICON_LIST
            if icon_name in icon_categories
        ]

        self.filtered_icons = self.icons

    def filter_icons(self):
        if not self.search_query:
            self.filtered_icons = self.icons
        else:
            query = self.search_query.lower().strip()
            self.filtered_icons = [
                icon
                for icon in self.icons
                if self._is_similar(query, icon["name"].lower())
                or any(self._is_similar(query, kw.lower()) for kw in icon["keywords"])
            ]

    @staticmethod
    def _is_similar(query: str, target: str) -> bool:
        # Exact match
        if query == target:
            return True

        # Start of word match
        if target.startswith(query):
            return True

        # Word boundary match
        if f" {query}" in f" {target} ":
            return True

        # Acronym match
        if query == "".join(word[0] for word in target.split() if word):
            return True

        # Substring match with minimum length
        if len(query) >= 3 and query in target:
            return True

        return False

    @rx.event
    def update_search(self, value: str):
        self.search_query = value
        self.filter_icons()

    @rx.event
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
                IconState.set_expanded,
                rx.scroll_to("icons-list"),
            ],
            display=rx.cond(IconState.filtered_icons.length() > 40, "block", "none"),
            # class_name="max-w-[350px]",
        ),
        on_mount=IconState.fetch_icons,
        class_name="flex flex-col gap-4",
    )
