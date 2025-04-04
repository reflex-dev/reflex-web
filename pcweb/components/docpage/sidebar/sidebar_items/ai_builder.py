from .item import create_item


def get_sidebar_items_ai_builder():
    from pcweb.pages.docs.ai_builder import pages as ai_builder_pages

    items = [create_item("AI Builder", children=ai_builder_pages)]

    return items


ai_builder_items = get_sidebar_items_ai_builder()
