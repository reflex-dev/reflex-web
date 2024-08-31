from pcweb.styles.colors import c_color
from pcweb.styles.fonts import small
from pcweb.styles.shadows import shadows

thumb_pill_style = {
    "display": "flex",
    "padding": "2px 8px",
    "color": c_color("slate", 9),
    "justify-content": "center",
    "align-items": "center",
    "gap": "8px",
    "white-space": "nowrap",
    "border-radius": "100px",
    "border": f"1px solid {c_color('slate', 5)}",
    "background-color": c_color("slate", 1),
    "box-shadow": shadows["large"],
    "cursor": "pointer",
    "transition": "background-color 0.075s ease-out",
    ":hover": {
        "background-color": c_color("slate", 3),
        "color": c_color("slate", 9),
    },
    **small,
}

pill_style = {
    "display": "flex",
    "padding": "2px 8px",
    "color": c_color("slate", 9),
    "justify-content": "center",
    "align-items": "center",
    "gap": "8px",
    "white-space": "nowrap",
    "border-radius": ["8px", "8px", "100px", "100px", "100px"],
    "border": [
        "none",
        "none",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
        f"1px solid {c_color('slate', 5)}",
    ],
    "background-color": [
        c_color("slate", 3),
        c_color("slate", 3),
        c_color("slate", 1),
        c_color("slate", 1),
        c_color("slate", 1),
    ],
    "box-shadow": [
        "none",
        "none",
        shadows["large"],
        shadows["large"],
        shadows["large"],
    ],
    "cursor": "pointer",
    "transition": "background-color 0.075s ease-out",
    ":hover": {
        "background-color": c_color("slate", 3),
        "color": c_color("slate", 9),
    },
    **small,
}


button_common_style = {
    **small,
    "display": "flex",
    "align-items": "center",
    "justify-content": "center",
    "padding": "8px 14px",
    "width": "auto",
    "height": "36px",
    "border-radius": "10px",
}

bg_color = f"linear-gradient(180deg, #6E56CF 0%, #654DC4 100%)"
hover_bg = c_color("violet", 9)

send_button_style = {
    **button_common_style,
    "position": "relative",
    "background": bg_color,
    "color": "#FFFFFF",
    "cursor": "pointer",
    "_hover": {
        "background": hover_bg,
    },
}

rectangle_style = {
    "box-sizing": "border-box",
    "position": "absolute",
    "left": "1px",
    "right": "1px",
    "top": "1px",
    "bottom": "1px",
    "border-top": "1px solid rgba(255, 255, 255, 0.22)",
    "border-radius": "11px",
    "z-index": 1,
}

cancel_button_style = {
    **button_common_style,
    "background": c_color("slate", 4),
    "color": c_color("slate", 9),
    "_hover": {
        "background": c_color("slate", 5),
    },
}


feedback_box_style = {
    "box-sizing": "border-box",
    "padding": "16px",
    "width": "341px",
    "height": "auto",
    "max-height": "564px",
    "background-color": c_color("white", 1),
    "box-shadow": shadows["large"],
    "border-radius": "26px",
}

text_area_style = {
    "color": c_color("slate", 11),
    **small,
    "background-color": c_color("white", 1),
    "border": f"1px solid {c_color('slate', 4)}",
    "width": "100%",
    "height": "100%",
    "padding": "8px 12px",
    "border-radius": "12px",
    "max-height": "300px",
    "min-height": "72px",
    "field-sizing": "content",
    "box-sizing": "border-box",
    "outline": "none",
    "overflow-y": "auto",
    "&::placeholder": {"color": c_color("slate", 9)},
}

input_style = {
    "color": c_color("slate", 11),
    **small,
    "background-color": c_color("white", 1),
    "border": f"1px solid {c_color('slate', 4)}",
    "width": "100%",
    "height": "100%",
    "padding": "8px 12px",
    "border-radius": "12px",
    "box-sizing": "border-box",
    "outline": "none",
    "&::placeholder": {"color": c_color("slate", 9)},
}
