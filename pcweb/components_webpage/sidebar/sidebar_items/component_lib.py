import reflex as rx
from reflex.components.chakra.base import ChakraComponent

from ..state import SidebarItem
from pcweb.pages.docs.library import library


def get_component_link(category, clist, prefix="") -> str:
    if issubclass(clist[1], ChakraComponent):
        prefix = "chakra/"
    component_name = rx.utils.format.to_snake_case(clist[0])
    return f"{library.path.strip('/')}/{prefix}{category.lower()}/{component_name.lower()}"


def get_category_children(category, category_list, prefix=""):
    if isinstance(category_list, dict):
        return SidebarItem(
            names=category,
            children=[
                get_category_children(c, category_list[c]) for c in category_list
            ],
        )
    category_item_children = []
    for c in category_list:
        component_name = rx.utils.format.to_snake_case(c[0])
        name = rx.utils.format.to_title_case(component_name)
        item = SidebarItem(
            names=name,
            link=get_component_link(category, c, prefix=prefix),
        )
        category_item_children.append(item)
    return SidebarItem(names=category, children=category_item_children)


def get_sidebar_items_component_lib():
    from pcweb.pages.docs import component_list

    library_item_children = []

    for category in component_list:
        category_item = get_category_children(category, component_list[category])
        library_item_children.append(category_item)

    return [
        SidebarItem(
            names="Overview",
            alt_name_for_next_prev="Components Reference: Overview",
            link=library.path,
        ),
        *library_item_children,
    ]


def get_sidebar_items_other_libraries():
    from pcweb.pages.docs import chakra_components

    chakra_children = []
    for category in chakra_components:
        category_item = get_category_children(
            category, chakra_components[category], prefix="chakra/"
        )
        chakra_children.append(category_item)

    chakra_item = SidebarItem(names="Chakra", children=chakra_children)

    return [chakra_item]


component_lib = get_sidebar_items_component_lib()
other_libs = get_sidebar_items_other_libraries()
