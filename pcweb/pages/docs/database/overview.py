import reflex as rx

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
    return rx.box(
        docheader("Database", first=True),
        doctext(
            "Reflex comes with a built-in ORM wrapping SQLAlchemy. ",
            "We will cover some basic use cases, but you can refer to their ",
            doclink(
                text="docs",
                href="https://docs.sqlalchemy.org/en/14/orm/quickstart.html",
            ),
            " to learn more.",
        ),
        subheader("Connecting"),
        doctext(
            "Reflex provides a built-in SQLite database for storing and retrieving data. "
        ),
        doctext(
            "You can connect to your own SQL compatible database by modifying the ",
            rx.code("pcconfig.py"),
            " file with your database url.",
        ),
        doccode(
            """config = rx.Config(
    app_name="my_app",
    db_url="sqlite:///reflex.db",
)
"""
        ),
        doctext(
            "You can also use a DBConfig object to connect to your database.",
        ),
        doccode(
            """config = rx.Config(
    app_name="my_app",
    db_config=rx.DBConfig(engine="postgresql+psycopg2", username="your-db-username", password="your-db-password", host="localhost", port=5432, database="reflex"),
)
"""
        ),
        doctext(
            "DBConfig class has following constructors.",
        ),
        doccode(
            """
    DBConfig.sqlite(database="reflex.db")
    DBConfig.postgresql(username="your-db-username", password="your-db-password", host="localhost", port=5432, database="reflex")
    DBConfig.postgresql_psycopg2(username="your-db-username", password="your-db-password", host="localhost", port=5432, database="reflex")
"""
        ),
        subheader("Tables"),
        doctext(
            "To create a table make a class that inherits from ",
            rx.code("rx.Model"),
            " with and specify that it is a table.",
        ),
        doccode(
            """class User(rx.Model, table=True):
    username: str
    email: str
    password: str   
"""
        ),
        doctext(
            "Each time you run your app with ",
            rx.code("pc run"),
            " it will check if the table exists in the database, ",
            "and will create it if it does not exist.",
        ),
        subheader("Queries"),
        doctext(
            "To query the database you can create a ",
            rx.code("rx.session()"),
            ", which handles opening and closing the database connection.",
        ),
        doctext(
            "You can use normal SQLAlchemy queries to query the database. ",
        ),
        doccode(
            """
        with rx.session() as session:
            session.add(User(username="test", email="admin@pynecone.io", password="admin"))
            session.commit()
        """
        ),
    )
