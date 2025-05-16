# Connecting to a Database

```python exec
import reflex as rx
```

Connecting to a database is critical to give your app access to real data. This section will cover how to connect to a database using the AI Builder. 

To connect to a database you will need a `DB_URI`. Reflex.build currently supports `postgresql` and `mysql` databases.

This is what it looks like for a Postgres database:

```bash
postgresql://username:password@hostname:port/database_name
```

```bash
postgresql://admin:secret123@db.mycompany.com:5432/mydatabase
```

```python eval
rx.box(height="1rem")
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header="DB URI (More Details)",
        content=rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Component"),
                    rx.table.column_header_cell("Example"),
                    rx.table.column_header_cell("Description"),
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(rx.code("postgresql://")),
                    rx.table.cell(rx.code("postgresql://")),
                    rx.table.cell("The database ", rx.el.span("dialect", font_weight="bold"), " or driver (can also be ", 
                                rx.code("mysql://"), ", ", rx.code("sqlite:///"), ", etc.)"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(rx.code("username")),
                    rx.table.cell(rx.code("admin")),
                    rx.table.cell("The ", rx.el.span("username", font_weight="bold"), " used to authenticate with the database"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(rx.code("password")),
                    rx.table.cell(rx.code("secret123")),
                    rx.table.cell("The ", rx.el.span("password", font_weight="bold"), " for the database user (insecure to expose this in plain text)"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(rx.code("hostname")),
                    rx.table.cell(rx.code("db.mycompany.com")),
                    rx.table.cell("The ", rx.el.span("host", font_weight="bold"), " where the database server is running"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(rx.code("port")),
                    rx.table.cell(rx.code("5432")),
                    rx.table.cell("The ", rx.el.span("port", font_weight="bold"), " the database server is listening on (default for PostgreSQL)"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(rx.code("database_name")),
                    rx.table.cell(rx.code("mydatabase")),
                    rx.table.cell("The ", rx.el.span("name", font_weight="bold"), " of the database to connect to"),
                ),
            ),
            width="100%",
        ),
    ),
    variant="surface",
)
```

```python eval
rx.box(height="1rem")
```

You can also use a MySQL database. The connection string looks like this:

```bash
mysql://username:password@hostname:port/database_name
```



## Connecting your Database before the app is generated

You can add your `Database URI` at the start of your generation as shown below. 

```python eval
rx.image(
    src="/ai_builder/add_db_before_app.gif",
    height="auto",
    padding_bottom="2rem",
)
```

Here if you wanted to build a dashboard for example we recommend a prompt as follows: 

`Build a dashboard around my database data`



## Connecting your Database after the app is generated

You can add your `Database URI` after you've already generated an app or directly from a template that you have forked as shown below.

```python eval
rx.image(
    src="/ai_builder/add_db_in_app.gif",
    height="auto",
    padding_bottom="2rem",
)
```

Here if you wanted to hook up your data correctly we recommend a prompt as follows: 

`Use the database I added to rewrite the dashboard to display my expense reporting data, keep the existing layout charts and structure the same`