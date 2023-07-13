import reflex as rx
from pcweb import constants, styles
from pcweb.base_state import State
import openai
import os
from reflex.vars import ImportVar, Var

try:
    openai.api_key = os.environ["OPENAI_API_KEY"]
except Exception as e:
    print("OPENAI_API_KEY environment variable not set.")


def tag(text):
    return rx.text(
        text,
        color="#5646ED",
        bg="#F5EFFE",
        padding_x="0.5em",
        padding_y="0.25em",
        border_radius="8px",
        font_weight=600,
    )


class GptState(State):
    question: str = "What is Reflex?"
    answer: str = "Performant, customizable web apps in pure Python. Deploy in seconds."
    limit = 0

    def get_answer(self):
        if self.limit > 2:
            print("Limit Reached")
            return rx.window_alert("Limit Reached")
        self.limit += 1
        try:
            session = openai.Completion.create(
                engine="text-davinci-003",
                prompt=self.question,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.7,
                stream=True,  # Enable streaming
            )
            self.answer = ""
            yield
            # Stream the results, yielding after every word.
            for item in session:
                answer_text = item["choices"][0]["text"]
                self.answer += answer_text
                yield
        except Exception as e:
            print(e)
            self.answer = "Error OpenAI API Key not set"
            yield


def qa():
    return rx.vstack(
        rx.text(
            GptState.question,
            font_family=styles.MONO,
            margin_top=".5em",
            padding="1em",
            font_weight="500",
            font_size="11px",
            border_top="1px solid #EAE4FD",
            color="#1F1944",
        ),
        rx.cond(
            GptState.limit > 2,
            rx.text(
                "Limit Reached",
                bg="white",
                padding="1em",
                border_radius="6px",
                border="1px solid #EAE4FD",
                font_family=styles.MONO,
                font_weight="500",
                font_size="11px",
            ),
            rx.text(
                GptState.answer,
                bg="white",
                padding="1em",
                border_radius="6px",
                border="1px solid #EAE4FD",
                font_family=styles.MONO,
                font_weight="500",
                font_size="11px",
                color="#1F1944",
            ),
        ),
        spacing="0em",
        width="100%",
        align_items="left",
        padding_x="1em",
    )


class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/Br2ec3WwuRGxEuij/scene.splinecode"
    is_default = True


spline = Spline.create


def spline_component():
    return rx.center(
        rx.center(
            spline(),
            overflow="hidden",
            width="42em",
            height="42em",
        ),
        width="100%",
        display=["none", "none", "none", "none", "flex", "flex"],
    )
