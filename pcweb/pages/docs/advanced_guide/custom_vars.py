import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code1 = """import googletrans

class Translation(rx.Base):
    original_text: str
    translated_text: str

class TranslationState(State):
    input_text: str = "Hola Mundo"
    current_translation: Translation = Translation(original_text="", translated_text="")

    def translate(self):
        text = googletrans.Translator().translate(self.input_text, dest="en").text
        self.current_translation = Translation(original_text=self.input_text, translated_text=text)

"""
exec(code1)

code2 = """rx.vstack(
    rx.input(on_blur=TranslationState.set_input_text, default_value=TranslationState.input_text, placeholder="Text to translate..."),
    rx.button("Translate", on_click=TranslationState.translate),
    rx.text(TranslationState.current_translation.translated_text),
)"""


@docpage()
def custom_vars():
    from pcweb.pages.docs.state.vars import vars

    return rx.box(
        docheader("Custom Vars", first=True),
        doctext(
            "As mentioned in the ",
            doclink("vars", vars.path),
            " page, Reflex vars must be JSON serializable. ",
        ),
        doctext(
            "This means we can support any Python primitive types, as well as lists, dicts, and tuples. "
            "However, you can also create more complex var types by inheriting from ",
            rx.code("rx.Base"),
            ". ",
        ),
        subheader("Defining a Type"),
        doctext(
            "In this example, we will create a custom var type for storing translations. "
        ),
        doctext(
            "Once defined, we can use it as a state var, and reference it from within a component. ",
        ),
        docdemo(code2, code1, eval(code2)),
    )
