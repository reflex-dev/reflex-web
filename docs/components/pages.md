---
from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.templates.docpage import docalert, doccode, docheader, subheader, docdemobox

route = (
"""
@rx.page()
def index():
    return rx.text('Root Page')

@rx.page()
def about():
    return rx.text('About Page')

@rx.page(route='/custom-route')
def custom():
    return rx.text('Custom Route')

app = rx.App()
"""
)

nested_routes = (
"""
@rx.page(route='/nested/page')
def nested_page():
    return rx.text('Nested Page')

app = rx.App()
"""

)
  
dynamic_routes = (
"""
class State(rx.State):
    @rx.var
    def post_id(self) -> str:
        return self.get_query_params().get('pid', 'no pid')
        
@rx.page(route='/post/[pid]')
def post():
    \'''A page that updates based on the route.\'''
    return rx.heading(State.post_id)

app = rx.App()
"""
)
  
routes_get_query_params = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.get_query_params()
        username = args.get('username')
        post_id = args.get('id')
        return f'Posts by {username}: Post {post_id}'

@rx.page(route='/user/[username]/posts/[id]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)

meta_data = (
"""
@rx.page(
    title='My Beautiful App',
    description='A beautiful app built with Reflex',
    image='/splash.png',
    meta=meta,
)
def index():
    return rx.text('A Beautiful App')

@rx.page(title='About Page')
def about():
    return rx.text('About Page')


meta = [
    {'name': 'theme_color', 'content': '#FFFFFF'},
    {'char_set': 'UTF-8'},
    {'property': 'og:url', 'content': 'url'},
]

app = rx.App()
"""  

)

page_load_events = (
"""
class State(rx.State):
    data: Dict[str, Any]

    def get_data(self):
        # Fetch data
        self.data = fetch_data()

@rx.page(on_load=State.get_data)
def index():
    return rx.text('A Beautiful App')
"""  
)

page_decorator = (
"""
@rx.page(route='/', title='My Beautiful App')
def index():
    return rx.text('A Beautiful App')
"""  
)

current_page_link = (
"""
class State(rx.State):
    
    @rx.var
    def current_url(self) -> str:
        return f'{self.get_headers().get(\"origin\")}{self.get_current_page(origin=True)}'
"""  
)

catch_all_route = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.get_query_params()
        usernames = args.get('username', [])
        return f'Posts by {', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[...username]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)

optional_catch_all_route = (
"""
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.get_query_params()
        usernames = args.get('username', [])
        return f'Posts by {', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[[...username]]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()
"""  
)
current_page_info = (
"""
class State(rx.State):
    def some_method(self):
        current_page_route = self.get_current_page()
        current_page_url = self.get_current_page(origin=True)
        # ... Your logic here ...

"""  
)

client_ip = (
"""
class State(rx.State):
    def some_method(self):
        client_ip = self.get_client_ip()
        # ... Your logic here ...

"""  
)
---
# Pages
Pages in Reflex allow you to define components for different URLs. This section covers creating pages, handling URL 
arguments, accessing query parameters, managing page metadata, and handling page load events.

## Adding a Page
You can create a page by defining a function that returns a component.
By default, the function name will be used as the route, but you can also specify a route.

```python
  {route.strip()}
```

In this example we create three pages: 
- `index` - The root route, available at `/`
- `about` - available at `/about`
- `/custom` - available at `/custom-route`

## Page Decorator
You can also use the `@rx.page` decorator to add a page.

```python
{page_decorator}
```

This is equivalent to calling `app.add_page` with the same arguments.


```reflex
rx.alert(
    icon=True,
    title=rx.text(
        "Index is a special exception where it is available at both / and /index . All other pages are only available at their specified route.",
    ),
)
```

## Nested Routes
Pages can also have nested routes.

```python
{nested_routes}
```
This component will be available at `/nested/page`.

## Dynamic Routes
Dynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible
and adaptable web applications. This section covers regular dynamic routes, catch-all routes, 
and optional catch-all routes, each with detailed examples.

## Regular Dynamic Routes
Regular dynamic routes in Reflex allow you to match specific segments in a URL dynamically.

Example:
```python
{dynamic_routes}
```
In this case, a route like `/user/john/posts/5` would display "Posts by john: Post 5".

## Catch-All Routes
Catch-all routes in Reflex allow you to match any number of segments in a URL dynamically.

Example:
```python
{catch_all_route}
```
In this case, the `...username` catch-all pattern captures any number of segments after
`/users/`, allowing URLs like `/users/2/john/` and `/users/1/john/doe/` to match the route.

## Optional Catch-All Routes
Optional catch-all routes, enclosed in double square brackets (`[[...]]`). This indicates that the specified segments 
are optional, and the route can match URLs with or without those segments.

Example:
```python
{optional_catch_all_route}
```
Optional catch-all routes allow matching URLs with or without specific segments. 
Each optional catch-all pattern should be independent and not nested within another catch-all pattern.

```reflex
rx.alert(
    icon=True,
    title=rx.text(
        "Catch-all routes must be placed at the end of the URL pattern to ensure proper route matching.",
    ),
)
```

### Routes Validation Table
| Route Pattern                                         | Example URl                                            |    valid |
|:------------------------------------------------------|:-------------------------------------------------------|---------:|
| `/users/posts`                                        | `/users/posts`                                         |    valid |
| `/products/[category]`                                | `/products/electronics`                                |    valid |                                                  |         |
| `/users/[username]/posts/[id] `                       | `/users/john/posts/5`                                  |    valid |
| `/users/[...username]/posts`                          | `/users/john/posts`                                    |  invalid |
|                                                       | `/users/john/doe/posts`                                |  invalid |
| `/users/[...username]`                                | `/users/john/`                                         |    valid |
|                                                       | `/users/john/doe`                                      |    valid |
| `/products/[category]/[...subcategories]`             | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
| `/products/[category]/[[...subcategories]]`           | `/products/electronics`                                |    valid |
|                                                       | `/products/electronics/laptops`                        |    valid |
|                                                       | `/products/electronics/laptops/lenovo`                 |    valid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |    valid |
| `/products/[category]/[...subcategories]/[...items]`  | `/products/electronics/laptops`                        |  invalid |
|                                                       | `/products/electronics/laptops/lenovo`                 |  invalid |
|                                                       | `/products/electronics/laptops/lenovo/thinkpad`        |  invalid |




## Getting the Current Page Link
The `get_current_page()` method allows you to obtain the path of the current page from the router data. 
By setting the `origin` parameter to `True`, you can get the actual URL displayed in the browser. 
If `origin` is set to False (which is the default), it returns the route pattern.

```python
{current_page_info}
```
In the above example, `current_page_route` will contain the route pattern (e.g., `/posts/[id]`), while `current_page_url`
will contain the actual URL (e.g., `http://example.com/posts/123`).

To get the full URL, combine the origin data from the headers with the current page's path.

Example:

```python
{current_page_link}
```
In this example, running on `localhost` should display `http://localhost:3000/user/hey/posts/3/`


## Getting Client IP
You can use the `get_client_ip()` method to obtain the IP address of the client associated 
with the current state.

```python
{client_ip}
```


## Page Metadata
You can add page metadata such as:

- The title to be shown in the browser tab
- The description as shown in search results
- The preview image to be shown when the page is shared on social media
- Any additional metadata

```python
{meta_data}
```

## Page Load Events
You can also specify a function to run when the page loads. This can be useful for fetching data once vs on every render or state change.
In this example, we fetch data when the page loads:

```python
{page_load_events}
```
