# Common styles for questions and answers.
import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    background_color=rx.color("crimson", 9), margin_left=chat_margin
)
answer_style = message_style | dict(
    background_color=rx.color("teal", 8), margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(border_width="1px", padding="1em", box_shadow=shadow, width="350px")
button_style = dict(bg=rx.color("accent", 10), box_shadow=shadow)
