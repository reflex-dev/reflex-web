```python exec
import reflex as rx
from pcweb.styles.styles import get_code_style, cell_style

class RouterState(rx.State):
    pass


router_data = [
      {"name": "rx.State.router.page.host", "value": RouterState.router.page.host},
      {"name": "rx.State.router.page.path", "value": RouterState.router.page.path},
      {"name": "rx.State.router.page.raw_path", "value": RouterState.router.page.raw_path},
      {"name": "rx.State.router.page.full_path", "value": RouterState.router.page.full_path},
      {"name": "rx.State.router.page.full_raw_path", "value": RouterState.router.page.full_raw_path},
      {"name": "rx.State.router.page.params", "value": RouterState.router.page.params.to_string()},
      {"name": "rx.State.router.session.client_token", "value": RouterState.router.session.client_token},
      {"name": "rx.State.router.session.session_id", "value": RouterState.router.session.session_id},
      {"name": "rx.State.router.session.client_ip", "value": RouterState.router.session.client_ip},
      {"name": "rx.State.router.headers.host", "value": RouterState.router.headers.host},
      {"name": "rx.State.router.headers.user_agent", "value": RouterState.router.headers.user_agent},
      {"name": "rx.State.router.headers.to_string()", "value": RouterState.router.headers.to_string()},
  ]

```

# State Utility Methods

The state object has several methods and attributes that return information
about the current page, session, or state.

## Router Attributes

The `self.router` attribute has several sub-attributes that provide various information:

* `router.page`: data about the current page and route
  * `host`: The hostname and port serving the current page (frontend).
  * `path`: The path of the current page (for dynamic pages, this will contain the slug)
  * `raw_path`: The path of the page displayed in the browser (including params and dynamic values)
  * `full_path`: `path` with `host` prefixed
  * `full_raw_path`: `raw_path` with `host` prefixed
  * `params`: Dictionary of query params associated with the request

* `router.session`: data about the current session
  * `client_token`: UUID associated with the current tab's token. Each tab has a unique token.
  * `session_id`: The ID associated with the client's websocket connection. Each tab has a unique session ID.
  * `client_ip`: The IP address of the client. Many users may share the same IP address.

* `router.headers`: a selection of common headers associated with the websocket
  connection. These values can only change when the websocket is re-established
  (for example, during page refresh). All other headers are available in the
  dictionary `self.router_data.headers`.
  * `host`: The hostname and port serving the websocket (backend).

### Example Values on this Page

```python eval
rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Value"),
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(item["name"], style=cell_style),
                    rx.table.cell(rx.code(item["value"], style=get_code_style("violet"))),
                )
                for item in router_data
            ]
        ),
        variant="surface",
        margin_y="1em",
    )
```
