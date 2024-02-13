import openai

import reflex as rx


class ChatappState(rx.State):
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self, data):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((data["message"], answer))

    async def answer3(self, data):
        import asyncio

        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((data["message"], ""))

        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (self.chat_history[-1][0], answer[: i + 1])
            yield

    def answer4(self, data):
        # Our chatbot has some brains now!
        session = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data["message"]}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((data["message"], answer))

        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield
