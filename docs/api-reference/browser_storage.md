---
from pcweb.templates.docpage import docalert, doccode, docheader, subheader, docdemobox

code_state_gc = (
"""
class CookieState(State):
    cookie_val: str = 'Hello'
    
    def set_cookie(self):
        yield rx.set_cookie('hello', 'world')
        self.cookie_val = self.get_cookies().get('hello','')
"""
  
)

code_gc = (
"""
rx.heading(CookieState.cookie_val)
""" 
)

code_sc = (
"""
rx.button(CookieState.cookie_val, on_click=CookieState.set_cookie)
"""
)

code_gls = (
"""
rx.button('Copy Local Storage to clipboard', on_click=rx.set_clipboard(rx.get_local_storage('key')))
"""  
)

code_sls = (
"""
rx.button(
    'Set Local Storage', on_click=rx.set_local_storage('key', 'value1')
)
"""  

)

set_cookies = (
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

remove_cookies = (
"""
def index():
    return rx.button(
        'Remove cookie', on_click=rx.remove_cookie('key')
    )
"""  

)
  

set_local_storage = (
"""
class LocalStorageState(rx.State):
    l1: str = rx.LocalStorage()
    l2: rx.LocalStorage = 'l2 default'

    # local storage with custom settings
    l3: str = rx.LocalStorage(name='l3')
    l4: str = rx.LocalStorage('l4 default')
"""  
)

remove_local_storage = (
"""
def index():
    return rx.button(
        'Remove Local Storage',
        on_click=rx.remove_local_storage('key'),
    )
"""  
)

clear_local_storage = (
"""
def index():
    return rx.button(
        'Clear all Local Storage',
        on_click=rx.clear_local_storage(),
    )
"""  
)
---

# Browser Storage

## Cookies

Cookies are small pieces of data stored in a user's browser. They are designed to hold a modest amount of 
specific information, which the server can later retrieve. Cookies are commonly used for authentication, session
management, and tracking user behavior on websites.

### Using Cookies in Reflex
In Reflex, cookies are managed using the `rx.Cookie` class, providing flexible options for customization and control.


## Setting cookies
To create a client-side cookie, use the `rx.Cookie` var. Here's an explanation of its parameters:

- `encoding`: The character encoding to use.
- `errors` : The error handling scheme to use.
- `name` : The name of the cookie on the client side.
- `path`: The cookie path. Use `/` to make the cookie accessible on all pages.
- `max_age` : Relative max age of the cookie in seconds from when the client receives it.
- `domain`: Domain for the cookie (e.g., `sub.domain.com` or `.allsubdomains.com`).
- `secure`: Is the cookie only accessible through HTTPS?
- `same_site`: Whether the cookie is sent with third-party requests. Can be one of (`True`, `False`, `None`, `lax`, `strict`).

```python
{set_cookies}
```

## Remove cookies
To remove a cookie on the frontend, use the `rx.remove_cookie(key)` method. This removes the cookie named `key`.

```python
{remove_cookies}
```


## Local Storage
Local Storage is another web storage option that allows websites to store data persistently in a web browser. 
Unlike cookies, local storage offers a larger storage capacity and does not expire. It's commonly used for caching 
data, offline web apps, and maintaining user preferences.
In Reflex, local storage can be handy for caching data, storing user-specific settings, or saving app state.

## Reading from Local Storage

```python
{code_gls}
```
In this example, clicking the "Read Local Storage" button retrieves the `user_id` from local storage and displays it on the UI.

To write a variable inside the local storage, you can use the [special event]("/docs/api-reference/special-events")
rx.set_local_storage(key,value)

```python
{code_sls}
```

```reflex
rx.alert(
    icon=True,
    title=rx.text(
        rx.code("get_local_storage()"),
        " cannot be used for direct rendering",
    ),
    status="warning"
)
```

## Remove local storage
Set a value in the local storage on the frontend.

```python
{remove_local_storage}
```

## Clear local storage
Set a value in the local storage on the frontend.

```python
{clear_local_storage}
```
