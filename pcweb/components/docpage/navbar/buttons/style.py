import reflex as rx
from pcweb.styles.colors import c_color
from pcweb.styles.shadows import shadows

button_style = {
    "border_radius": "50px",
    "border": f"1px solid {rx.color('mauve', 4)}",
    "background": rx.color("mauve", 2),
    "box_shadow": "0px 3px 7px -4px rgba(21, 18, 44, 0.15)",
    "padding": "7px 12px 7px 12px",
    "align_items": "center",
}

new_button_style = {
    "display": "flex",
    "height": "32px",
    "padding": "2px 12px",
    "justify-content": "center",
    "align-items": "center",
    "border-radius": "1000px",
    "border": f"1px solid {c_color('slate', 5)}",
    "background-color": c_color("slate", 1),
    "box-shadow": shadows["large"],
    "cursor": "pointer",
    "transition": "background 0.075s ease-out",
    "_hover": {
        "background-color": c_color("slate", 3),
    },
}
