# Token and State Examples

This guide demonstrates how to work with tokens and state modification in your Reflex API routes.

## Token Passing

When building protected endpoints, you can use tokens to authenticate requests and access state:

```python
from fastapi import HTTPException
import reflex as rx

class AuthState(rx.State):
    is_authenticated: bool = False
    user_id: str = ""

@app.api.get("/protected")
async def protected_route(token: str):
    """Example of a protected route that checks authentication status."""
    state = await app.state_manager.get_state(token)
    if not state.is_authenticated:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"message": "Protected data", "user_id": state.user_id}

@app.api.post("/login")
async def login(credentials: dict):
    """Example of setting authentication state."""
    # Validate credentials (simplified for example)
    if credentials.get("username") == "admin" and credentials.get("password") == "password":
        token = "user_session_token"  # In practice, generate a secure token
        async with app.state_manager.modify_state(token) as state:
            state.is_authenticated = True
            state.user_id = credentials["username"]
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
```

## State Modification

When modifying state in API routes, use the state manager's context manager to ensure thread-safe updates:

```python
class CounterState(rx.State):
    counter: int = 0
    last_modified: str = ""

@app.api.post("/increment")
async def increment_counter(token: str):
    """Example of modifying state in an API route."""
    async with app.state_manager.modify_state(token) as state:
        state.counter += 1
        state.last_modified = datetime.now().isoformat()
        return {"new_count": state.counter, "last_modified": state.last_modified}

@app.api.get("/counter")
async def get_counter(token: str):
    """Example of reading state in an API route."""
    state = await app.state_manager.get_state(token)
    return {"counter": state.counter, "last_modified": state.last_modified}
```

## Important Notes

1. Always use `async with app.state_manager.modify_state(token)` when modifying state to ensure thread safety.
2. Use `await app.state_manager.get_state(token)` for read-only state access.
3. Handle exceptions appropriately when working with tokens and state.
4. Consider implementing proper token generation and validation in production.

## Best Practices

1. Keep state modifications atomic and minimal
2. Always validate tokens before accessing state
3. Use appropriate HTTP status codes for different scenarios
4. Include proper error handling in your routes
5. Consider implementing token expiration and refresh mechanisms

For more information about authentication and state management, see the [Authentication Overview](../authentication/authentication_overview.md).
