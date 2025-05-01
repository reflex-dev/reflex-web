```python exec
import reflex as rx
from pcweb import constants, styles
```

# Utility Functions

Reflex provides utility functions to help with common tasks in your applications.

## run_in_thread

The `run_in_thread` function allows you to run a non-async function in a separate thread, which is useful for preventing long-running operations from blocking the UI event queue.

```python
async def run_in_thread(func: Callable, *, timeout: float | None = None) -> Any
```

### Parameters

- `func`: The non-async function to run in a separate thread.
- `timeout`: Maximum number of seconds to wait for the function to complete. If `None` (default), wait indefinitely.

### Returns

- The return value of the function.

### Raises

- `ValueError`: If the function is an async function.
- `asyncio.TimeoutError`: If the function execution exceeds the specified timeout.

### Usage


```python demo exec id=run_in_thread_demo
import asyncio
import time
import reflex as rx


class RunInThreadState(rx.State):
    result: str = "No result yet"
    status: str = "Idle"
    
    @rx.event(background=True)
    async def run_quick_task(self):
        """Run a quick task that completes within the timeout."""
        async with self:
            self.status = "Running quick task..."
        
        def quick_function():
            time.sleep(0.5)
            return "Quick task completed successfully!"
        
        try:
            # Run with a timeout of 2 seconds (more than enough time)
            result = await rx.run_in_thread(quick_function, timeout=2.0)
            async with self:
                self.result = result
                self.status = "Idle"
        except Exception as e:
            async with self:
                self.result = f"Error: {str(e)}"
                self.status = "Idle"
    
    @rx.event(background=True)
    async def run_slow_task(self):
        """Run a slow task that exceeds the timeout."""
        async with self:
            self.status = "Running slow task..."
        
        def slow_function():
            time.sleep(3.0)
            return "This should never be returned due to timeout!"
        
        try:
            # Run with a timeout of 1 second (not enough time)
            result = await rx.run_in_thread(slow_function, timeout=1.0)
            async with self:
                self.result = result
                self.status = "Idle"
        except asyncio.TimeoutError:
            async with self:
                self.result = "Task timed out after 1 second!"
                self.status = "Idle"
        except Exception as e:
            async with self:
                self.result = f"Error: {str(e)}"
                self.status = "Idle"


def run_in_thread_example():
    return rx.vstack(
        rx.heading("run_in_thread Example", size="3"),
        rx.text("Status: ", RunInThreadState.status),
        rx.text("Result: ", RunInThreadState.result),
        rx.hstack(
            rx.button(
                "Run Quick Task (completes within timeout)",
                on_click=RunInThreadState.run_quick_task,
                color_scheme="green",
            ),
            rx.button(
                "Run Slow Task (exceeds timeout)",
                on_click=RunInThreadState.run_slow_task,
                color_scheme="red",
            ),
        ),
        width="100%",
        align_items="start",
        spacing="4",
    )
```

### When to Use run_in_thread

Use `run_in_thread` when you need to:

1. Execute CPU-bound operations that would otherwise block the event loop
2. Call synchronous libraries that don't have async equivalents
3. Prevent long-running operations from blocking UI responsiveness
4. Set a maximum execution time for potentially slow operations

### Example: Processing a Large File

```python
import reflex as rx
import time

class FileProcessingState(rx.State):
    progress: str = "Ready"
    
    @rx.event(background=True)
    async def process_large_file(self):
        self.progress = "Processing file..."
        
        def process_file():
            # Simulate processing a large file
            time.sleep(5)
            return "File processed successfully!"
        
        try:
            # Set a timeout of 10 seconds
            result = await rx.run_in_thread(process_file, timeout=10.0)
            async with self:
                self.progress = result
        except asyncio.TimeoutError:
            async with self:
                self.progress = "File processing timed out!"
```

### Notes

- The function passed to `run_in_thread` must be a regular (non-async) function.
- Consider setting appropriate timeouts to prevent indefinite blocking.
- Handle `asyncio.TimeoutError` exceptions to gracefully manage timeouts.
