```python exec
from pcweb.templates.docpage import doccode
```

# Browser Storage

## rx.Cookie

Represents a state Var that is stored as a cookie in the browser.

 Parameters
- `encoding`: The character encoding to use.
- `errors` : The error handling scheme to use.
- `name` : The name of the cookie on the client side.
- `path`: The cookie path. Use `/` to make the cookie accessible on all pages.
- `max_age` : Relative max age of the cookie in seconds from when the client receives it.
- `domain`: Domain for the cookie (e.g., `sub.domain.com` or `.allsubdomains.com`).
- `secure`: If the cookie is only accessible through HTTPS.
- `same_site`: Whether the cookie is sent with third-party requests. Can be one of (`True`, `False`, `None`, `lax`, `strict`).

```python eval
doccode(
    """
class CookieState(rx.State):
    c1: str = rx.Cookie()
    c2: rx.Cookie = 'c2 default'

    # cookies with custom settings
    c3: str = rx.Cookie(max_age=2)  # expires after 2 second
    c4: rx.Cookie = rx.Cookie(same_site='strict')
    c5: str = rx.Cookie(path='/foo/')  # only accessible on `/foo/`
    c6: str = rx.Cookie(name='c6')
    c7: str = rx.Cookie('c7 default')
""" 
)
```

## rx.remove_cookies
Remove a cookie from the client's browser.


Parameters:
- `key`: The name of cookie to remove.

```python eval
doccode(
    """
def index():
    return rx.button(
        'Remove cookie', on_click=rx.remove_cookie('key')
    )
"""  
)
```


## rx.LocalStorage
Represents a state Var that is stored in localStorage in the browser.

Parameters
- `encoding`: The encoding to use
- `errors`: The error handling scheme to use.
- `name`: The name of the storage key on the client side.

```python eval
doccode(
    """
class LocalStorageState(rx.State):
    # local storage with default settings
    l1: str = rx.LocalStorage()
    l2: rx.LocalStorage = "l2 default"  # type: ignore

    # local storage with custom settings
    l3: str = rx.LocalStorage(name="l3")
    l4: str = rx.LocalStorage("l4 default")
""" 
)
```


## rx.remove_local_storage
Remove a local storage item from the client's browser.


Parameters
- `key`: The key to remove from local storage.

```python eval
doccode(
    """
def index():
    return rx.button(
        'Remove Local Storage',
        on_click=rx.remove_local_storage('key'),
    )
"""  
)
```

## rx.clear_local_storage()
Clear all local storage items from the client's browser.


```python eval
doccode(
    """
def index():
    return rx.button(
        'Clear all Local Storage',
        on_click=rx.clear_local_storage(),
    )
""" 
)
```
