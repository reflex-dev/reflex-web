# Models and Data Types

This guide explains how to work with data models in your Reflex API routes, with special attention to Pydantic integration and rx.Base usage.

## rx.Base and Pydantic Compatibility

When working with complex data types in Reflex, you have several options:

### Using rx.Base

```python
import reflex as rx

class User(rx.Base):
    """Basic user model."""
    name: str
    age: int
    email: str
```

### Pydantic V2 Considerations

There are some important considerations when working with Pydantic V2 and rx.Base:

1. rx.Base is designed to work with Pydantic V1 patterns
2. For compatibility with Pydantic V2, use one of these approaches:

```python
# Approach 1: Use Pydantic V1 explicitly
from pydantic.v1 import BaseModel

class UserModel(BaseModel):
    name: str
    age: int
    email: str

class AppState(rx.State):
    user: UserModel
```

```python
# Approach 2: Use dataclasses
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int
    email: str

class AppState(rx.State):
    user: UserData
```

### Best Practices

1. Use rx.Base for simple data structures that don't require complex validation
2. Use Pydantic V1 models when you need:
   - Complex validation
   - JSON schema generation
   - Data serialization/deserialization
3. Use dataclasses for:
   - Simple data containers
   - Performance-critical code
   - When you don't need Pydantic's features

## API Route Examples

Here's how to use these models in your API routes:

```python
@app.api.post("/users")
async def create_user(user_data: UserModel):
    """Create a new user."""
    async with app.state_manager.modify_state(token) as state:
        state.user = user_data
        return {"status": "success", "user": user_data}

@app.api.get("/users/{user_id}")
async def get_user(user_id: str):
    """Get user data."""
    state = await app.state_manager.get_state(token)
    if state.user and state.user.id == user_id:
        return state.user
    raise HTTPException(status_code=404, detail="User not found")
```

## Important Notes

1. rx.Base is primarily designed for Reflex's state management system
2. When working with external APIs or complex validation, prefer Pydantic models
3. Consider performance implications when choosing between rx.Base, Pydantic models, and dataclasses
4. Always validate input data in your API routes
5. Handle serialization/deserialization appropriately

For more information about state management and data modeling, see the [State Overview](../state/overview.md) documentation.
