import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)


@docpage()
def database_overview():
    return pc.box(
        docheader("Database", first=True),
        doctext(
            "Pynecone comes with a built-in ORM wrapping SQLAlchemy. ",
            "We will cover some basic use cases, but you can refer to their ",
            doclink(
                text="docs",
                href="https://docs.sqlalchemy.org/en/14/orm/quickstart.html",
            ),
            " to learn more.",
        ),
        subheader("Connecting"),
        doctext(
            "Pynecone provides a built-in SQLite database for storing and retrieving data. "
        ),
        doctext(
            "You can connect to your own SQL compatible database by modifying the ",
            pc.code("pcconfig.py"),
            " file with your database url.",
        ),
        doccode(
            """config = pc.Config(
    app_name="my_app",
    db_url="sqlite:///pynecone.db",
)
"""
        ),
        doctext(
            "You can also use a DBConfig object to connect to your database.",
        ),
        doccode(
            """config = pc.Config(
    app_name="my_app",
    db_config=pc.DBConfig(engine="postgresql+psycopg2", username="your-db-username", password="your-db-password", host="localhost", port=5432, database="pynecone"),
)
"""
        ),
        doctext(
            "DBConfig class has following constructors.",
        ),
        doccode(
            """
    DBConfig.sqlite(database="pynecone.db")
    DBConfig.postgresql(username="your-db-username", password="your-db-password", host="localhost", port=5432, database="pynecone")
    DBConfig.postgresql_psycopg2(username="your-db-username", password="your-db-password", host="localhost", port=5432, database="pynecone")
"""
        ),
        subheader("Tables"),
        doctext(
            "To create a table make a class that inherits from ",
            pc.code("pc.Model"),
            " with and specify that it is a table.",
        ),
        doccode(
            """class User(pc.Model, table=True):
    username: str
    email: str
    password: str   
"""
        ),
        doctext(
            "Each time you run your app with ",
            pc.code("pc run"),
            " it will check if the table exists in the database, ",
            "and will create it if it does not exist.",
        ),
        subheader("Queries"),
        doctext(
            "To query the database you can create a ",
            pc.code("pc.session()"),
            ", which handles opening and closing the database connection.",
        ),
        doctext(
            "You can use normal SQLAlchemy queries to query the database. ",
        ),
        doccode(
            """
        with pc.session() as session:
            session.add(User(username="test", email="admin@pynecone.io", password="admin"))
            session.commit()
        """
        ),
    )
