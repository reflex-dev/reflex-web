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