# Queries

Queries are used to retrieve data from a database.

A query is a request for information from a database table or combination of
tables. A query can be used to retrieve data from a single table or multiple
tables. A query can also be used to insert, update, or delete data from a table.
        
## Session

To execute a query you must first create a `rx.session`. You can use the session
to query the database using SQLAlchemy syntax.

The `rx.session` statement will automatically close the session when the code
block is finished.

The following example shows how to create a session and query the database.
First we create a table called `User`.
            
```python
class User(rx.Model, table=True):
    username: str
    email: str
```

Then we create a session and query the User table.

```python
class QueryUser(State):
    name: str
    users: list[User]

    def get_users(self):
        with rx.session() as session:
            self.users = session.query(User).filter(User.username.contains(self.name)).all()
```

The `get_users` method will query the database for all users that contain the
value of the state var `name`.

Similarly you can use the `session.add()` method to add a new record to the
database.

```python
class AddUser(State):
    username: str
    email: str
    
    def add_user(self):
        with rx.session() as session:
            session.add(User(username=self.username, email=self.email))
            session.commit()
```