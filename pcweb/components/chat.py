import pynecone as pc
from pcweb import constants, styles
from pcweb.base_state import State
import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

def tag(text):
    return pc.text(
        text,
        color="#5646ED",
        bg="#F5EFFE",
        padding_x="0.5em",
        padding_y="0.25em",
        border_radius="8px",
        font_weight=600,
    )

class GptState(State):
    question: str = "What is the best way to learn Python?" 
    answer: str = "The best way to learn Python is to learn Python."
    limit = 0

    def get_answer(self):
        if self.limit > 2:
            print("Limit Reached")
            return pc.window_alert("Limit Reached")
        self.limit += 1
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
        
def qa():
    return pc.vstack(
        pc.text(GptState.question, font_family="IBM Plex Mono",margin_top=".5em", padding = "1em", font_weight =  "500", font_size  ="11px",border_top="1px solid #EAE4FD"),
        pc.cond(
            GptState.limit > 2,
            pc.text("Limit Reached", bg = "white", padding = "1em", border_radius = "6px", border="1px solid #EAE4FD", font_family="IBM Plex Mono",font_weight =  "500",  font_size  ="11px"),
            pc.text(GptState.answer, bg = "white", padding = "1em", border_radius = "6px", border="1px solid #EAE4FD", font_family="IBM Plex Mono",font_weight =  "500",  font_size  ="11px"),
        ),
        width="100%",
        align_items="left",
        padding_x = "1em",
    )


def chat_component():
    return pc.vstack(
                    pc.vstack(
                        pc.hstack(
                            pc.input(
                                placeholder="Search docs...",
                                box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 2px rgba(84, 82, 95, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.04), inset 0px 1px 0px rgba(255, 255, 255, 0.1);",
                                border_radius="4px;",
                                border_color="transparent",
                                width="100%",
                                bg = "#FFFFFF",
                                on_blur = GptState.set_question,
                                _focus={
                                        "border": f"2px solid {styles.ACCENT_COLOR}",
                                        "box_shadow":"0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 2px rgba(84, 82, 95, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.04), inset 0px 1px 0px rgba(255, 255, 255, 0.1);",
                                },
                                font_family  = "Instrument Sans"
                            ),
                            pc.spacer(),
                            pc.button(
                                "Get answer",
                                on_click=GptState.get_answer,
                                background="radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
                                box_shadow="0px 0px 0px 1px rgba(52, 46, 92, 0.14), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.2), inset 0px 0px 0px 1px rgba(255, 255, 255, 0.32), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.2);",
                                border_radius="8px;",
                                padding_x="1em",
                                href="/docs",
                            ),
                            width="100%",
                            padding_x = "1em",
                            padding_top = "1em",    
                        ),
                        qa(),
                        min_height="15em",
                        width="100%",
                        bg="radial-gradient(82.06% 100% at 50% 100%, rgba(86, 70, 237, 0.06) 0%, rgba(245, 239, 254, 0) 100%), #FFFFFF;",
                        border_bottom= "2px solid #F4F3F6",
                        border_radius= "8px 8px 0 0"
                    ),
                    pc.hstack(
                        tag("GPT Demo"),
                        pc.text("View code", color="#777583"),
                        pc.spacer(),
                        pc.hstack(
                            pc.text("All examples"),
                            pc.icon(tag="arrow_forward", color="#494369"),
                            border_radius="6px",
                            box_shadow= "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
                            padding_x = ".5em"
                        ),
                        width="100%",
                        padding_x = "1em",
                        padding_bottom = ".5em"
                    ),
                    min_width="10em",
                    border="1px solid #F4F3F6;",
                    box_shadow="0px 0px 0px 1px rgba(52, 46, 92, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 12px 8px rgba(3, 3, 11, 0.04), 0px 8px 12px -4px rgba(3, 3, 11, 0.02);",
                    border_radius="8px;",
                    width="100%",
                    display=["none", "none", "none", "none", "flex", "flex"],
                )