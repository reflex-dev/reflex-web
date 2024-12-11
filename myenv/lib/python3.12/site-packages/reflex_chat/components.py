import reflex as rx


def chat_bubble(message: str, idx: int = 0) -> rx.Component:
    """Display a single chat bubble.

    Args:
        message: The message to display.

    Returns:
        A component displaying the message/answer pair.
    """
    return rx.cond(
        message["role"] == "system",
        rx.fragment(),
        rx.box(
            rx.markdown(
                message["content"],
                background_color=rx.cond(
                    message["role"] == "user",
                    rx.color("mauve", 4),
                    rx.color("accent", 4),
                ),
                color=rx.cond(
                    message["role"] == "user",
                    rx.color("mauve", 12),
                    rx.color("accent", 12),
                ),
                display="inline-block",
                padding_x="1em",
                border_radius="8px",
                max_width=["30em", "30em", "50em", "50em", "50em", "50em"],
            ),
            id=f"message-{idx}",
            text_align=rx.cond(message["role"] == "user", "right", "left"),
            margin_top="1em",
            width="100%",
        ),
    )


def action_bar(ChatState) -> rx.Component:
    """The action bar to send a new message."""
    return rx.form(
        rx.hstack(
            rx.input(
                placeholder="Type something...",
                id=ChatState.__name__,
                width="100%",
            ),
            rx.spacer(),
            rx.button(
                "Send",
                type="submit",
            ),
            align_items="center",
            width="100%",
        ),
        width="100%",
        on_submit=ChatState.submit_message,
        reset_on_submit=True,
    )
