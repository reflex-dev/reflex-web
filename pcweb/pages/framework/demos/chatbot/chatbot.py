# state.py
import os

from openai import AsyncOpenAI
from pcweb.components.icon_button import icon_button
import reflex as rx


class TutorialState(rx.State):
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]] = [
        (
            "What is Reflex?",
            "Reflex is the open-source framework empowering Python developers to build web apps faster.",
        )
    ]

    @rx.event(background=True)
    async def submit(self, form_data: dict):
        question = form_data["question"]
        # Our chatbot has some brains now!
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        # self.chat_history = []
        async with self:
            self.chat_history.append((question, answer))
            yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                async with self:
                    self.chat_history[-1] = (self.chat_history[-1][0], answer)
                    yield

    @rx.event
    def clear_chat(self):
        self.chat_history = []


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question),
            class_name="font-base text-slate-10 rounded-lg p-2 bg-slate-3 ml-[20%] text-end self-end",
        ),
        rx.box(
            rx.text(answer),
            class_name="font-base text-violet-10 rounded-lg p-2 bg-violet-3 max-w-[60%] mr-[20%] text-start self-start",
        ),
        class_name="flex flex-col gap-4 w-full",
    )


def chatbot() -> rx.Component:
    return rx.box(
        rx.el.button(
            rx.icon(
                tag="trash",
                size=22,
                class_name="shrink-0",
            ),
            class_name="!text-slate-11 rounded-[10px] hover:bg-slate-3 p-2 self-end shrink-0",
            on_click=TutorialState.clear_chat,
        ),
        rx.box(
            rx.auto_scroll(
                rx.foreach(
                    TutorialState.chat_history,
                    lambda messages: qa(messages[0], messages[1]),
                ),
                rx.box(overflow_anchor="auto", height="0.5rem"),
                overflow_anchor="none",
                class_name="flex flex-col gap-4 w-full overflow-y-auto",
            ),
            rx.form(
                rx.el.input(
                    placeholder="Ask me anything",
                    name="question",
                    type="text",
                    required=True,
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-slate-4 p-[0.5rem_0.75rem] border rounded-[0.625rem] font-base text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                ),
                icon_button(
                    "arrow-up",
                    variant="muted",
                    type="submit",
                    class_name="!bg-slate-5 !border-t-[rgba(255,255,255,0.05)] hover:!bg-slate-6 !text-slate-9",
                ),
                on_submit=TutorialState.submit,
                reset_on_submit=True,
                class_name="flex flex-row gap-4 w-full items-center",
            ),
            class_name="flex flex-col h-full max-h-full overflow-hidden gap-4 justify-between w-full",
        ),
        class_name="flex flex-col items-center gap-4 p-4 lg:px-10 lg:py-12 h-full overflow-hidden",
    )


chatbot_code = """
rx.box(
    rx.icon_button("trash", on_click=ChatState.clear_chat),
    rx.box(
        rx.auto_scroll(
            rx.foreach(
                ChatState.chat_history,
                lambda messages: qa(messages[0], messages[1]),
            ),
        ),
        rx.form(
            rx.input(
                placeholder="Ask me anything",
                name="question",
            ),
            rx.icon_button("arrow-up"),
            on_submit=TutorialState.submit,
            reset_on_submit=True
        ),
    )
)
"""
