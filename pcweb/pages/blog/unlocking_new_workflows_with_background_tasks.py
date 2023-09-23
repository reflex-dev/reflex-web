import asyncio
import reflex as rx
from pcweb.base_state import State


prev_collatz_state = '''class CollatzState(rx.State):
    count: int = 0

    def start_collatz(self, count: str):
        """Run the collatz conjecture on the given number."""
        self.count = abs(int(count))
        return CollatzState.run_step

    async def run_step(self):
        """Run a single step of the collatz conjecture."""

        if self.count > 1:
            await asyncio.sleep(0.5)
            
            if self.count % 2 == 0:
                # If the number is even, divide by 2.
                self.count /= 2
            else:
                # If the number is odd, multiply by 3 and add 1.
                self.count = self.count * 3 + 1
            yield CollatzState.run_step'''


class CollatzBackgroundState(State):
    # The current count
    count: int = 1

    # Whether the task is running (and should be running)
    task_running: bool = False

    @rx.background  # decorator marks the handler as a background task
    async def run_collatz(self):
        async with self:
            # Inside the context, the latest state values are available
            if self.task_running:
                # Do not start multiple tasks
                return
            self.task_running = True

        while self.task_running:
            # The task can await long-running processes without blocking the UI
            await asyncio.sleep(0.5)

            async with self:
                # After refreshing the state and taking exclusive access, check stopping condition
                if self.count <= 1:
                    self.task_running = False  # Allow task to be restarted
                    return

                # Apply collatz conjecture while holding lock
                if self.count % 2 == 0:
                    self.count /= 2
                else:
                    self.count = self.count * 3 + 1

    def set_count(self, count: str):
        self.count = abs(int(count))
        if not self.task_running:
            return CollatzBackgroundState.set_task_running(True)

    def set_task_running(self, is_checked: bool):
        if is_checked and not self.task_running:
            return CollatzBackgroundState.run_collatz
        elif not is_checked:
            self.task_running = False


def collatz_background_render_code():
    return rx.vstack(
        rx.link(
            rx.heading("Collatz Conjecture"),
            href="https://en.wikipedia.org/wiki/Collatz_conjecture",
        ),
        rx.text("Enter a number below"),
        rx.hstack(
            rx.input(
                value=CollatzBackgroundState.count.to_string(),
                on_change=CollatzBackgroundState.set_count,
                debounce_timeout=500,
            ),
            rx.switch(
                is_checked=CollatzBackgroundState.task_running,
                on_change=CollatzBackgroundState.set_task_running,
            ),
        ),
    )
