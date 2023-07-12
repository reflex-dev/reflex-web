"""App styling."""

import reflex as rx

# General styles.
SANS = "Instrument Sans"
MONO = "IBM Plex Mono, Menlo, Consolas, DejaVu Sans Mono, monospace"
BOLD_WEIGHT = "800"
NAVBAR_LOGO = "/Reflex.svg"
LOGO_URL = "/Reflex_white.svg"
PADDING_X = ["1em", "2em", "5em"]
PADDING_X2 = ["1em", "2em", "10em"]
HERO_FONT_SIZE = ["2em", "3em", "3em", "4em"]
H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = ["1.8em", "1.9em", "2em"]
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1em"
TEXT_FONT_SIZE = "1em"
ACCENT_COLOR = "rgb(107,99,246)"
ACCENT_COLOR_LIGHT = "rgba(107,99,246, 0.4)"
ACCENT_COLOR_DARK = "rgb(86, 77, 209)"
SUBHEADING_COLOR = "rgb(37,50,56)"
LIGHT_TEXT_COLOR = "#94a3b8"
LINK_STYLE = {
    "color": ACCENT_COLOR,
}

# Doc page styles.
DOC_HEADER_COLOR = "#1F1944"
DOC_TEXT_COLOR = "#342E5C"
DOC_REG_TEXT_COLOR = "#342E5C"
DOC_LIGHT_TEXT_COLOR = "#342E5C"
DOCPAGE_BACKGROUND_COLOR = "#FAFAFA"

DOC_HEADING_FONT_WEIGHT = "700"
DOC_SUBHEADING_FONT_WEIGHT = "600"
DOC_SECTION_FONT_WEIGHT = "600"

DOC_SHADOW = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
DOC_SHADOW_DARK = "rgba(0, 0, 0, 0.3) 0px 2px 8px"
DOC_SHADOW_LIGHT = "0px 0px 0px 1px rgba(52, 46, 92, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 12px 8px rgba(3, 3, 11, 0.04), 0px 8px 12px -4px rgba(3, 3, 11, 0.02)"

DOC_BORDER_RADIUS = "6px"

# The base application style.
BASE_STYLE = {
    "::selection": {
        "background_color": ACCENT_COLOR_LIGHT,
    },
    rx.Text: {
        "font_family": SANS,
        "font_size": 16,
    },
    rx.Heading: {
        "font_family": SANS,
    },
    rx.Divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rx.Code: {
        "color": ACCENT_COLOR,
    },
    rx.Alert: {
        "border_radius": "8px",
    },
    rx.Link: {"text_decoration": "none", "_hover": {}},
}

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&display=swap",
    "style.css"
]


# Styles to use for the navbar.
NAV_TEXT_COLOR = "#494369"
NAV_SEARCH_COLOR = "#342E5C"

NAV_TEXT_STYLE = {
    "color": NAV_TEXT_COLOR,
    "font_family": SANS,
    "font_weight": "600",
}

NAV_SEARCH_STYLE = {
    "color": NAV_SEARCH_COLOR,
    "font_family": SANS,
    "font_weight": "500",
}

NAV_BOX_STYLE = {
    "color": NAV_SEARCH_COLOR,
    "margin": ".25em",
    "padding": ".25em",
    "border_radius": "6px",
}

NAV_DROPDOWN_STYLE = {
    "color": NAV_TEXT_COLOR,
    "font_family": SANS,
    "font_weight": "500",
    "_hover": {
        "color":"#5646ED",
        "bg":"#F5EFFE",
    },
}

# General styles for landing page.

ACCENT_BUTTON = {
    "justify_content": "center",
    "align_items": "center",
    "isolation": "isolate",
    "border_radius": 10,
    "font_family": SANS,
    "font_style": "normal",
    "font_weight": 600,
    "color": "#F5EFFE",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(52, 46, 92, 0.8) 0%, rgba(234, 228, 253, 0) 100%), #7E69E0",
    "box_shadow": "0px 4px 10px -2px rgba(3, 3, 11, 0.32), 0px 4px 8px 0px rgba(3, 3, 11, 0.24), 0px 2px 3px 0px rgba(3, 3, 11, 0.10), 0px 0px 0px 1px rgba(32, 17, 126, 0.56), 0px -20px 12px -4px rgba(86, 70, 237, 0.32) inset, 0px 12px 12px -2px rgba(149, 128, 247, 0.16) inset, 0px 1px 0px 0px rgba(255, 255, 255, 0.16) inset;",
    "_hover": {
        "background": "radial-gradient(82.06% 100% at 50.00% 100.00%, rgba(52, 46, 92, 0.80) 0%, rgba(234, 228, 253, 0.00) 100%), #7E69E0);",
        "box_shadow": "0px 4px 10px -2px rgba(3, 3, 11, 0.12), 0px 4px 8px 0px rgba(3, 3, 11, 0.12), 0px 2px 3px 0px rgba(3, 3, 11, 0.10), 0px 0px 0px 2px rgba(149, 128, 247, 0.60), 0px -20px 12px -4px rgba(126, 105, 224, 0.60) inset, 0px 12px 12px -2px rgba(86, 70, 237, 0.12) inset, 0px 0px 0px 1px rgba(32, 17, 126, 0.40) inset;"
    }
}

BUTTON_LIGHT = {
    "justify_content": "center",
    "align_items": "center",
    "isolation": "isolate",
    "border_radius": 10,
    "font_family": SANS,
    "font_style": "normal",
    "font_weight": 600,
    "color": "#494369",
    "bg": "radial-gradient(82.06% 100% at 50.00% 100.00%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.20) 100%), #FEFEFF);",
    "box_shadow": " 0px 4px 10px -2px rgba(3, 3, 11, 0.02), 0px 4px 8px 0px rgba(3, 3, 11, 0.04), 0px 2px 3px 0px rgba(3, 3, 11, 0.20), 0px 0px 0px 1px rgba(52, 46, 92, 0.20), 0px -20px 12px -4px rgba(234, 228, 253, 0.36) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.32) inset, 0px 2px 0px 0px rgba(255, 255, 255, 0.40) inset;",
    "_hover": {
        "box_shadow": "0px 4px 10px -2px rgba(3, 3, 11, 0.28), 0px 4px 8px 0px rgba(3, 3, 11, 0.24), 0px 2px 3px 0px rgba(3, 3, 11, 0.12), 0px 0px 0px 1px rgba(32, 17, 126, 0.64), 0px -20px 20px -4px rgba(86, 70, 237, 0.66) inset, 0px 12px 12px -2px #9580F7 inset, 0px 1px 0px 0px rgba(255, 255, 255, 0.20) inset;",
    },
    "_active": {
        "bg": "radial-gradient(82.06% 100% at 50.00% 100.00%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.20) 100%), #FEFEFF);",
        "box_shadow": " 0px 4px 10px -2px rgba(3, 3, 11, 0.02), 0px 4px 8px 0px rgba(3, 3, 11, 0.04), 0px 2px 3px 0px rgba(3, 3, 11, 0.20), 0px 0px 0px 1px rgba(52, 46, 92, 0.20), 0px -20px 12px -4px rgba(234, 228, 253, 0.36) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.32) inset, 0px 2px 0px 0px rgba(255, 255, 255, 0.40) inset;",
        "color": "#342E5C",
    },
}

BUTTON_LIGHT_NO_BACKGROUND = {
    "border_radius":"6px",
    "box_shadow":"0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
    "bg":"#FFFFFF",
    "padding_x":".75em",
    "border_radius":"8px",
    "_hover": {
        "box_shadow": "0px 0px 0px 2px rgba(149, 128, 247, 0.60), 0px 2px 3px 0px rgba(3, 3, 11, 0.01), 0px 1px 2px 0px rgba(84, 82, 95, 0.12), 0px 0px 0px 1px rgba(32, 17, 126, 0.40) inset;",
    },
}


INPUT_STYLE = {
    "box_shadow": "0px 2px 3px 0px rgba(3, 3, 11, 0.04), 0px 1px 2px 0px rgba(84, 82, 95, 0.12), 0px 0px 0px 1px rgba(84, 82, 95, 0.18), 0px 1px 0px 0px rgba(255, 255, 255, 0.10) inset;",
    "color": "#1F1944",
    "background": "transparent",
    "border_radius": "8px",
    "border": "0px solid transparent",
    "_focus": {
        "box_shadow": "0px 0px 0px 2px rgba(149, 128, 247, 0.60), 0px 2px 3px 0px rgba(3, 3, 11, 0.01), 0px 1px 2px 0px rgba(84, 82, 95, 0.12), 0px 0px 0px 1px rgba(32, 17, 126, 0.40) inset;",
        "border": "0px solid transparent",
    },
    "_placeholder": {
        "color": "#1F1944",
        "font_weight": "500",
    },
}

INPUT_STYLE_BLANK = {
    "color": "#1F1944",
    "background": "transparent",
    "border": "0px solid transparent",
    "focus_border_color":"transparent",
    "_placeholder": {
        "color": "#1F1944",
        "font_weight": "500",
    },
}