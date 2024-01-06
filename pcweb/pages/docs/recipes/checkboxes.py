import reflex as rx

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


code_example = """
class CBoxeState(rx.State):
    
    choices: dict[str, bool] = {k: False for k in ["Choice A", "Choice B", "Choice C"]}
    _check_limit = 2

    def check_choice(self, value, index):
        self.choices[index] = value

    @rx.var
    def choice_limit(self):
        return sum(self.choices.values()) >= self._check_limit

    @rx.var
    def checked_choices(self):
        choices = [l for l, v in self.choices.items() if v]
        return " / ".join(choices) if choices else "None"

import reflex as rx


def render_checkboxes(values, limit, handler):
    return rx.vstack(
        rx.checkbox_group(
            rx.foreach(
                values,
                lambda choice: rx.checkbox(
                    choice[0],
                    is_checked=choice[1],
                    is_disabled=~choice[1] & limit,
                    on_change=lambda val: handler(val, choice[0]),
                ),
            )
        )
    )


def index() -> rx.Component:
    
    return rx.center(
        rx.vstack(
            rx.text("Make your choices (2 max):"),
            render_checkboxes(
                CBoxeState.choices,
                CBoxeState.choice_limit,
                CBoxeState.check_choice,
            ),
            rx.text("Your choices: ", CBoxeState.checked_choices),
        ),
        height="100vh",
    )
"""


@docpage()
def checkboxes():
    return rx.box(
        docheader("Smart Checkboxes Group", first=True),
        doctext(
            "A smart checkboxes group where you can track all checked boxes simply, "
            "as well as place limit on how many checks are possible."
        ),
        subheader("Recipe"),
        rx.center(rx.image(src="/gallery/smart_checkboxes.gif")),
        doctext(
            "This recipe use a ",
            rx.code("dict[str, bool]"),
            " for the checkboxes state tracking",
        ),
        doctext(
            "Additionnaly, the limit that prevent the user from checking more boxes than allowed is done with a computed var."
        ),
        doccode(code_example),
    )
