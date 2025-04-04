from .item import create_item


def get_sidebar_items_cloud():
    from pcweb.pages.docs.cloud import pages as cloud_pages
    from pcweb.pages.docs.cloud_cliref import pages as cloud_cli_pages

    items = [
        create_item("Cloud", children=cloud_pages),
        create_item("CLI Reference", children=cloud_cli_pages),
    ]

    return items


cloud_items = get_sidebar_items_cloud()
