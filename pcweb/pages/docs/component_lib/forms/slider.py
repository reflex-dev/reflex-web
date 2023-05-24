import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    doctext,
)

slider_state = """class SliderState(State):
    value: int = 50
"""

slider_base_example = """pc.vstack(
    pc.heading(SliderState.value),
    pc.slider(
        on_change=SliderState.set_value
    ),
    width="100%",
)
"""

slider_state_start = """class SliderVariation(State):
    value: int = 50

    def set_end(self, value):
        self.value = value
"""

slider_on_change_start = """pc.vstack(
    pc.heading(SliderVariation.value),
    pc.slider(
        on_change_end=SliderVariation.set_end
    ),
    width="100%",
)
"""

slider_state_combo = """class SliderCombo(State):
    value: int = 50
    color: str = "black"

    def set_start(self, value):
        self.color = "#68D391" 

    def set_end(self, value):
        self.color = "#F56565" 
"""

slider_combo = """pc.vstack(
    pc.heading(SliderCombo.value, color=SliderCombo.color),
    pc.slider(
        on_change_start=SliderCombo.set_start,
        on_change_end=SliderCombo.set_end
    ),
    width="100%",
)
"""


slider_state_manual = """class SliderManual(State):
    value: int = 50

    def set_end(self, value):
        self.value = value
"""

slider_manual = """pc.vstack( 
    pc.heading("Weather is " + SliderManual.value + " degrees"),
    pc.slider(
        pc.slider_track(
            pc.slider_filled_track(bg="tomato"),
            bg='red.100'
        ),
        pc.slider_thumb(
            pc.icon(tag="sun", color="white"),
            box_size="1.5em",
            bg="tomato",
        ),
        on_change_end=SliderManual.set_end,
    ),
    width="100%",
)
"""

exec(slider_state_manual)
exec(slider_state_combo)
exec(slider_state_start)
exec(slider_state)


def render_slider():
    return pc.vstack(
        doctext(
            "The Slider is used to allow users to make selections from a range of values."
        ),
        docdemo(
            slider_on_change_start,
            state=slider_state_start,
            comp=eval(slider_on_change_start),
            context=True,
        ),
        doctext(
            "You can also combine all three event handlers ",
            pc.code("on_change"),
            ", ",
            pc.code("on_change_start"),
            ", and ",
            pc.code("on_change_end"),
            " together.",
        ),
        docdemo(
            slider_combo,
            state=slider_state_combo,
            comp=eval(slider_combo),
            context=True,
        ),
        doctext(
            "You can also customize the appearance of the slider by passing in custom components for the track and thumb."
        ),
        docdemo(
            slider_manual,
            state=slider_state_manual,
            comp=eval(slider_manual),
            context=True,
        ),
        doctext(
            "If you want to trigger state change on every slider movement, you can use the ",
            pc.code("on_change"),
            " event handler.",
        ),
        doctext(
            "For performance reasons, you may want to trigger state change only when the user releases the slider. By using the ",
            pc.code("on_change_end"),
            " but if you need preform an event on every slider movement, you can use the ",
            pc.code("on_change"),
            " event handler.",
        ),
        docdemo(
            slider_base_example,
            state=slider_state,
            comp=eval(slider_base_example),
            context=True,
        ),
        align_items="start",
    )


range_slider_state = """class RangeSliderState(State):
    value = [0,100]
"""

range_slider_base_example = """pc.vstack(
    pc.heading(RangeSliderState.value[0]+" : "+RangeSliderState.value[1]),
    pc.range_slider(
        on_change=RangeSliderState.set_value
    ),
    width="100%",
)
"""

range_slider_state_start = """class RangeSliderVariation(State):
    value = [0,100]

    def set_end(self, value):
        self.value = value
"""

range_slider_on_change_start = """pc.vstack(
    pc.heading(RangeSliderVariation.value[0]+" : "+RangeSliderVariation.value[1]),
    pc.range_slider(
        on_change_end=RangeSliderVariation.set_end
    ),
    width="100%",
)
"""

range_slider_state_combo = """class RangeSliderCombo(State):
    value = [0,100]
    color: str = "black"

    def set_start(self, value):
        self.color = "green" 

    def set_val(self, value):
        self.value = value
        self.color = "orange" 

    def set_end(self, value):
        self.color = "red" 
"""

range_slider_combo = """pc.vstack(
    pc.heading(RangeSliderCombo.value[0]+" : "+RangeSliderCombo.value[1], color=RangeSliderCombo.color),
    pc.range_slider(
        on_change_start=RangeSliderCombo.set_start,
        on_change=RangeSliderCombo.set_val,
        on_change_end=RangeSliderCombo.set_end
    ),
    width="100%",
)
"""

range_slider_state_manual = """class RangeSliderManual(State):
    value = [0,100]
"""

range_slider_manual = """pc.vstack( 
    pc.heading("Between " + RangeSliderManual.value[0] + " and " + RangeSliderManual.value[1]),
    pc.range_slider(
        pc.range_slider_track(
            pc.range_slider_filled_track(bg="#48BB78"),
            bg='#C6F6D5'
        ),
        pc.range_slider_thumb( 
            pc.icon(tag="arrow_left", color="white"),
            bg="#48BB78",
            box_size="2em",
            index = 0
        ),
        pc.range_slider_thumb(
            pc.icon(tag="arrow_right", color="white"),
            bg="#48BB78",
            box_size="2em",
            index = 1
        ),
        on_change_end=RangeSliderManual.set_value,
    ),
    width="100%",
)
"""
exec(range_slider_state_combo)
exec(range_slider_state_start)
exec(range_slider_state)
exec(range_slider_state_manual)


def render_rangeslider():
    return pc.vstack(
        doctext(
            "The range slider is used to allow users to make selections from a range of values."
        ),
        docdemo(
            range_slider_on_change_start,
            state=range_slider_state_start,
            comp=eval(range_slider_on_change_start),
            context=True,
        ),
        docdemo(
            range_slider_manual,
            state=range_slider_state_manual,
            comp=eval(range_slider_manual),
            context=True,
        ),
        doctext(
            "If you want to trigger state change on every slider movement, you can use the ",
            pc.code("on_change"),
            " event handler. This is not recommended for performance reasons and should only be used if you need to perform an event on every slider movement.",
        ),
        docdemo(
            range_slider_base_example,
            state=range_slider_state,
            comp=eval(range_slider_base_example),
            context=True,
        ),
        align_items="start",
    )
