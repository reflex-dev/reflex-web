```python exec
import reflex as rx
from pcweb import constants, styles
```


# Dynamic Routes

Dynamic routes in Reflex allow you to handle varying URL structures, enabling you to create flexible
and adaptable web applications. This section covers regular dynamic routes, catch-all routes,
and optional catch-all routes, each with detailed examples.

## Regular Dynamic Routes

Regular dynamic routes in Reflex allow you to match specific segments in a URL dynamically.

Example:

```python

class State(rx.State):
    @rx.var
    def post_id(self) -> str:
        # Retrieves the value of the 'pid' parameter from the current route
        # If 'pid' is not found, it defaults to 'no pid'
        return self.router.page.params.get('pid', 'no pid')
        
@rx.page(route='/post/[pid]')
def post():
    '''A page that updates based on the route.'''
    # Displays the dynamic part of the URL, the post ID
    return rx.heading(State.post_id)

app = rx.App()
```

The [pid] part in the route is a dynamic segment, meaning it can match any value provided in the URL. For instance, `/post/5`, `/post/10`, or `/post/abc` would all match this route.

If a user navigates to `/post/5`, `State.post_id` will return `5`, and the page will display `5` as the heading. If the URL is `/post/xyz`, it will display `xyz`. If the URL is `/post/` without any additional parameter, it will display `'no pid'`.


### Using `app.add_page` Method

If you are using the `app.add_page` method to define pages, it is necessary to add the dynamic routes first, especially if they use the same function as a non dynamic route.

For example the code snippet below will:

```python
app.add_page(index, route="/page/[page_id]", on_load=DynamicState.on_load)
app.add_page(index, route="/static/x", on_load=DynamicState.on_load)
app.add_page(index)
```

But if we switch the order of adding the pages, like in the example below, it will not work:

```python
app.add_page(index, route="/static/x", on_load=DynamicState.on_load) 
app.add_page(index)
app.add_page(index, route="/page/[page_id]", on_load=DynamicState.on_load)
```


## Catch-All Routes

Catch-all routes in Reflex allow you to match any number of segments in a URL dynamically.

Example:

```python
class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f'Posts by \{', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[...username]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()

```

In this case, the `...username` catch-all pattern captures any number of segments after
`/users/`, allowing URLs like `/users/2/john/` and `/users/1/john/doe/` to match the route.

## Optional Catch-All Routes

Optional catch-all routes, enclosed in double square brackets (`[[...]]`). This indicates that the specified segments
are optional, and the route can match URLs with or without those segments.

Example:

```python

class State(rx.State):
    @rx.var
    def user_post(self) -> str:
        args = self.router.page.params
        usernames = args.get('username', [])
        return f'Posts by \{', '.join(usernames)}'

@rx.page(route='/users/[id]/posts/[[...username]]')
def post():
    return rx.center(
        rx.text(State.user_post)
    )


app = rx.App()

```

Optional catch-all routes allow matching URLs with or without specific segments.
Each optional catch-all pattern should be independent and not nested within another catch-all pattern.

```md alert
# Catch-all routes must be placed at the end of the URL pattern to ensure proper route matching.
```

### Routes Validation Table

| Route Pattern                                         | Example URl                                            |    valid |
|:------------------------------------------------------|:-------------------------------------------------------|---------:|
| `/users/posts`                                        | `/users/posts`                                         |    valid |
| `/products/[category]`                                | `/products/electronics`                                |    valid |
| `/users/[username]/posts/[id]`                       | `/users/john/posts/5`                                  |    valid |
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
