import reflex as rx

from ..state import SidebarItem


def get_component_link(category, clist, prefix="") -> str:
    component_name = rx.utils.format.to_kebab_case(clist[0])
    # construct the component link. The component name points to the name of the md file.
    return f"/docs/library/{prefix}{category.lower().replace(' ', '-')}/{component_name.lower()}"


def get_category_children(category, category_list, prefix=""):
    category = category.replace("-", " ")
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
        *library_item_children,
    ]


def get_sidebar_items_graphings():
    from pcweb.pages.docs import graphing_components

    graphing_children = []
    for category in graphing_components:
        category_item = get_category_children(
            category,
            graphing_components[category],
            prefix="graphing/",
        )
        graphing_children.append(category_item)

    return [
        *graphing_children,
    ]


component_lib = get_sidebar_items_component_lib()
graphing_libs = get_sidebar_items_graphings()
