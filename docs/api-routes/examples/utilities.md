# API Utilities

This guide demonstrates how to use Reflex's utility functions for working with API routes.

## get_backend_url

The `get_backend_url` utility function helps construct proper URLs for your API endpoints:

```python box
from reflex.utils import get_backend_url
import httpx

class State(rx.State):
    data: dict = {}

    async def fetch_data(self):
        """Fetch data from an API endpoint."""
        url = get_backend_url("/api/data")
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            self.data = response.json()

    async def call_api_with_token(self):
        """Example using call_script with token."""
        # Get the backend URL
        url = get_backend_url("/api/protected")

        # Use call_script to make the request with the current token
        response = await self.call_script(
            "fetch",
            url,
            {
                "headers": {
                    "Authorization": f"Bearer {self.router.session.client_token}"
                }
            }
        )
        return {"status": "success", "data": {"message": "API response data"}}
```

## Using call_script

The `call_script` method is useful when you need to make API calls from the frontend while preserving authentication:

```python
class State(rx.State):
    result: dict = {}

    async def submit_form(self, form_data: dict):
        """Submit form data to an API endpoint."""
        url = get_backend_url("/api/submit")

        # Use call_script to send a POST request
        response = await self.call_script(
            "fetch",
            url,
            {
                "method": "POST",
                "body": form_data,
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        )
        self.result = response.json()
```

## Important Notes

1. `get_backend_url` automatically handles:
   - Development vs. production URLs
   - Port configuration
   - Base path prefixing

2. `call_script` benefits:
   - Automatically includes authentication tokens
   - Handles CORS issues
   - Provides consistent behavior across environments

## Best Practices

1. Always use `get_backend_url` instead of hardcoding URLs
2. Use `call_script` when making API calls from event handlers
3. Handle API errors appropriately
4. Include proper type hints for better code maintainability

For more information about state management and API integration, see the [State Overview](../state/overview.md) documentation.
