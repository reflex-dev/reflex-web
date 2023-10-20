# Tables

Tables are database objects that contain all the data in a database.

In tables, data is logically organized in a row-and-column format similar to a
spreadsheet. Each row represents a unique record, and each column represents a
field in the record.

## Creating a Table

To create a table make a class that inherits from `rx.Model`.

The following example shows how to create a table called `User`.
            
```python
class User(rx.Model, table=True):
    username: str
    email: str
```

The `table=True` argument tells Reflex to create a table in the database for
this class.

## Foreign Key Relationships

Foreign key relationships are used to link two tables together. For example,
a `User` table may have a foreign key relationship with a `Post` table. This
would allow us to relate multiple `Post` objects to a `User` that created them.

Defining relationships like this requires the use of `sqlmodel` objects as
seen in the example.

```python
import sqlmodel


class Post(rx.Model, table=True):
    title: str
    body: str
    user_id: int = sqlmodel.Field(default=None, foreign_key="user.id")

    user: Optional["User"] = sqlmodel.Relationship(back_populates="posts")


class User(rx.Model, table=True):
    username: str
    email: str

    posts: List[Post] = sqlmodel.Relationship(back_populates="user")
```


See the [SQLModel Relationship Docs](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/define-relationships-attributes/) for more details.

## Advanced Column Types

SQLModel automatically maps basic python types to SQLAlchemy column types, but for more advanced use cases, it is
possible to define the column type using `sqlalchemy` directly. For example, we can add a last updated timestamp
to the post example.

```python
import datetime

import sqlmodel
import sqlalchemy

class Post(rx.Model, table=True):
    ...
    update_ts: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update_ts",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
```

To make the `Post` model more usable on the frontend, a `dict` method may be provided
that converts any fields to a JSON serializable value. In this case, the dict method is
overriding the default `datetime` serializer to strip off the microsecond part.

```python
class Post(rx.Model, table=True):
    ...

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["update_ts"] = self.update_ts.replace(microsecond=0).isoformat()
        return d
```