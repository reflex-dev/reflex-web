from pcweb import flexdown

from pcweb.templates.docpage import docpage

import asyncio

import httpx
import reflex as rx

from pcweb import flexdown
from pcweb.base_state import State
from pcweb.templates.docpage import docpage


my_task_state_code = """
class MyTaskState(State):
    counter: int = 0
    max_counter: int = 10
    running: bool = False
    _n_tasks: int = 0

    @rx.background
    async def my_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return
            
            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
            async with self:
                # Check for stopping conditions inside context
                if self.counter >= self.max_counter:
                    self.running = False
                if not self.running:
                    self._n_tasks -= 1
                    return

                self.counter += 1

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5)

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            return MyTaskState.my_task

    def clear_counter(self):
        self.counter = 0
"""

exec(my_task_state_code)

my_task_render_code = """rx.hstack(
        rx.heading(MyTaskState.counter, " /"),
        rx.number_input(
            value=MyTaskState.max_counter,
            on_change=MyTaskState.set_max_counter,
            width="8em",
        ),
        rx.button(
            rx.cond(~MyTaskState.running, "Start", "Stop"),
            on_click=MyTaskState.toggle_running,
        ),
        rx.button(
            "Reset",
            on_click=MyTaskState.clear_counter,
        ),
    )
"""

my_task_code = f"""
import asyncio
import reflex as rx

{my_task_state_code.replace("(State)", "(rx.State)")}

def index():
    return {my_task_render_code}

app = rx.App()
app.add_page(index)"""


low_level_state_code = """
my_tasks = set()


async def _fetch_data(app, token):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/zen")
    async with app.modify_state(token) as state:
        substate = state.get_substate(
            LowLevelState.get_full_name().split("."),
        )
        substate.result = response.text


class LowLevelState(State):
    result: str = ""

    def fetch_data(self):
        task = asyncio.create_task(
            _fetch_data(
                app=rx.utils.prerequisites.get_app().app,
                token=self.get_token(),
            ),
        )

        # Always save a reference to your tasks until they are done
        my_tasks.add(task)
        task.add_done_callback(my_tasks.discard)
"""

exec(low_level_state_code)

low_level_render_code = """rx.vstack(
        rx.text(LowLevelState.result),
        rx.button(
            "Fetch Data",
            on_click=LowLevelState.fetch_data,
        ),
    )
"""

low_level_code = f"""
import asyncio
import httpx
import reflex as rx

{low_level_state_code.replace("(State)", "(rx.State)")}

def index():
    return {low_level_render_code}

app = rx.App()
app.add_page(index)"""

@docpage()
def background_events():
    return flexdown.render_file("docs/events/background_events.md")