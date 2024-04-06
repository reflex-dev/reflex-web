import reflex as rx

def chat_box():
    return rx.vstack(
        rx.text("hello", color="red"),
        rx.text("world", color="red"),
        rx.text("hello", color="red"),
        rx.text("world", color="red"),
        rx.text("hello", color="red"),
        rx.text("world", color="red"),
        rx.text("hello", color="red"),
        rx.text("world", color="red"),
    )