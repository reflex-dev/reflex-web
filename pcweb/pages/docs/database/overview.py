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
            "Reflex uses ",
            doclink(
                text="sqlmodel",
                href="https://sqlmodel.tiangolo.com",
            ),
            " to provide a built-in ORM wrapping SQLAlchemy. ",
        ),
        doctext(
            "The examples on this page refer specifically to how Reflex uses various tools ",
            "to expose an integrated database interface. ",
            "Only basic use cases will be covered below, but you can refer to the ",
            doclink(
                text="sqlmodel tutorial",
                href="https://sqlmodel.tiangolo.com/tutorial/select/",
            ),
            " for more examples and information ",
            *["(just replace ", rx.code("SQLModel"), " with ", rx.code("rx.Model")],
            " and ",
            *[rx.code("Session(engine)"), " with ", rx.code("rx.session()"), "). "],
        ),
        doctext(
            "For advanced use cases, please see the ",
            doclink(
                text="SQLAlchemy docs",
                href="https://docs.sqlalchemy.org/en/14/orm/quickstart.html",
            ),
            " (v1.4).",
        ),
        subheader("Connecting"),
        doctext(
            "Reflex provides a built-in SQLite database for storing and retrieving data. "
        ),
        doctext(
            "You can connect to your own SQL compatible database by modifying the ",
            rx.code("rxconfig.py"),
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
        subheader("Migrations"),
        doctext(
            "Reflex leverages ",
            doclink(
                text="alembic",
                href="https://alembic.sqlalchemy.org/en/latest/",
            ),
            " to manage database schema changes. ",
        ),
        doctext(
            "Before the database feature can be used in a new app ",
            "you must call ",
            rx.code("reflex db init"),
            " to initialize alembic and create a migration script with ",
            "the current schema.",
        ),
        doctext(
            "After making changes to the schema, use ",
            rx.code("reflex db makemigrations --message 'something changed'"),
            " to generate a script in the ",
            rx.code("alembic/versions"),
            " directory that will update the database schema. It is recommended ",
            "that scripts be inspected before applying them.",
        ),
        doctext(
            "The ",
            rx.code("reflex db migrate"),
            " command is used to apply migration scripts to bring the database ",
            "up to date. During app startup, if Reflex detects that the current ",
            "database schema is not up to date, a warning will be displayed on ",
            "the console.",
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
