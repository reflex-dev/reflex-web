```python exec
import reflex as rx
```

# Backend API Routes

In addition to your frontend app, Reflex uses a [FastAPI](https://fastapi.tiangolo.com/) backend to serve your app. FastAPI provides a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Adding API Routes

To add additional endpoints to the backend API, you can use either `app.add_api_route` or FastAPI-style decorators:

### Method 1: Using add_api_route

```python
async def api_test(item_id: int):
    return {"my_result": r"item_id"}

app = rx.App()
app.api.add_api_route("/items/[item_id]", api_test)
```

Now you can access the endpoint at `localhost:8000/items/23` and get the result.

### Method 2: Using Decorators

```python
@app.api.get("/items/[item_id]")
async def get_item(item_id: int):
    return {"item_id": r"item_id"}

@app.api.post("/items")
async def create_item(item: dict):
    return {"created": r"item"}
```

This is useful for creating a backend API that can be used for purposes other than your Reflex app.

## Reserved Routes

Some routes on the backend are reserved for the runtime of Reflex. Here's a comprehensive list of reserved routes:

| Route | Purpose | Response |
|-------|---------|----------|
| /ping | Health check | "pong" |
| /_event | Frontend event communication | Event processing |
| /_upload | File upload handling | Upload processing |
| /_health | Service health status | JSON status of DB/Redis |

### Route Conflicts

If you need to use a path that conflicts with a reserved route, you can use nginx to redirect traffic:

```nginx
location /my_health {
    proxy_pass http://localhost:8000/_health;
}
```

```md alert error
# Important: Do not override /_event
Overriding the /_event route will break the event communication between frontend and backend.
```

For more examples of working with:
- Token passing and state modification
- rx.Base and Pydantic models
- API utilities

See the detailed examples in:
- [Token and State Examples](examples/token_state.md)
- [Models and Data Types](examples/models.md)
- [API Utilities](examples/utilities.md)

For more information about FastAPI routing, parameters, and request handling, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/first-steps/).
