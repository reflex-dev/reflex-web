import pynecone as pc

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


@docpage()
def tables():
    return pc.box(
        docheader("Tables", first=True),
        doctext("Tables are database objects that contain all the data in a database."),
        doctext(
            "In tables, data is logically organized in a row-and-column format similar to a spreadsheet. Each row represents a unique record, and each column represents a field in the record."
        ),
        subheader("Creating a Table"),
        doctext(
            "To create a table make a class that inherits from ",
            pc.code("pc.Model"),
        ),
        doctext(
            "The following example shows how to create a table called ",
            pc.code("User"),
            ".",
        ),
        doccode(
            """class User(pc.Model, table=True):
    username: str
    email: str
"""
        ),
        doctext(
            "The ",
            pc.code("table=True"),
            " argument tells Pynecone to create a table in the database for this class.",
        ),
    )
