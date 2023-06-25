import reflex as rx

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


@docpage()
def queries():
    return rx.box(
        docheader("Queries", first=True),
        doctext("Queries are used to retrieve data from a database."),
        doctext(
            "A query is a request for information from a database table or combination of tables. A query can be used to retrieve data from a single table or multiple tables. A query can also be used to insert, update, or delete data from a table."
        ),
        subheader("Session"),
        doctext(
            "To execute a query you must first create a ",
            rx.code("rx.session"),
            ". You can use the session to query the database using SQLAlchemy syntax.",
        ),
        doctext(
            "The ",
            rx.code("with rx.session"),
            " statement will automatically close the session when the code block is finished.",
        ),
        doctext(
            "The following example shows how to create a session and query the database. First we create a table called ",
            rx.code("User"),
            ".",
        ),
        doccode(
            """class User(rx.Model, table=True):
    username: str
    email: str
"""
        ),
        doctext("Then we create a session and query the User table."),
        doccode(
            """
class QueryUser(State):
    name: str
    users: list[User]

    def get_users(self):
        with rx.session() as session:
            self.users = session.query(User).filter(User.username.contains(self.name)).all()
"""
        ),
        doctext(
            "The ",
            rx.code("get_users"),
            " method will query the database for all users that contain the value of the state var ",
            rx.code("name"),
            ".",
        ),
        doctext(
            "Similarly you can use the ",
            rx.code("session.add()"),
            " method to add a new record to the database.",
        ),
        doccode(
            """class AddUser(State):
    username: str
    email: str
    
    def add_user(self):
        with rx.session() as session:
            session.add(User(username=self.username, email=self.email))
            session.commit()
"""
        ),
    )
