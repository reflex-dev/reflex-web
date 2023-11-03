from pcweb import flexdown

from pcweb.templates.docpage import docpage


@docpage("/docs/database/overview")
def database_overview():
    return flexdown.render_file("docs/database/overview.md")


@docpage("/docs/database/tables")
def tables():
    return flexdown.render_file("docs/database/tables.md")


@docpage("/docs/database/queries")
def queries():
    return flexdown.render_file("docs/database/queries.md")


@docpage("/docs/database/relationships")
def relationships():
    return flexdown.render_file("docs/database/relationships.md")
