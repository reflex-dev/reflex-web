```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from
```

# State Utility Methods

The state object has several methods and attributes that return information
about the current page, session, or state.

## Router

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

```python exec
class RouterState(State):
    pass


def router_values():
    return rx.table(
        headers=["Name", "Value"],
        rows=[
            [rx.text("router.page.host"), rx.code(RouterState.router.page.host)],
            [rx.text("router.page.path"), rx.code(RouterState.router.page.path)],
            [rx.text("router.page.raw_path"), rx.code(RouterState.router.page.raw_path)],
            [rx.text("router.page.full_path"), rx.code(RouterState.router.page.full_path)],
            [rx.text("router.page.full_raw_path"), rx.code(RouterState.router.page.full_raw_path)],
            [rx.text("router.page.params"), rx.code(RouterState.router.page.params.to_string())],
            [rx.text("router.session.client_token"), rx.code(RouterState.router.session.client_token)],
            [rx.text("router.session.session_id"), rx.code(RouterState.router.session.session_id)],
            [rx.text("router.session.client_ip"), rx.code(RouterState.router.session.client_ip)],
            [rx.text("router.headers.host"), rx.code(RouterState.router.headers.host)],
            [rx.text("router.headers.user_agent"), rx.code(RouterState.router.headers.user_agent)],
            [rx.text("router.headers.to_string()"), rx.code(RouterState.router.headers.to_string())],
        ],
        overflow_x="auto",
    )
```

```python eval
docdemo_from(RouterState, component=router_values, collapsible_code=True, demobox_props={"justify_content": "flex-start"})
```

## Other Methods

* `reset`: set all Vars to their default value for the given state (including substates).
* `get_value`: returns the value of a Var **without tracking changes to it**. This is useful
   for serialization where the tracking wrapper is considered unserializable.
* `dict`: returns all state Vars (and substates) as a dictionary. This is
  used internally when a page is first loaded and needs to be "hydrated" and
  sent to the client.

## Special Attributes

* `dirty_vars`: a set of all Var names that have been modified since the last
  time the state was sent to the client. This is used internally to determine
  which Vars need to be sent to the client after processing an event.