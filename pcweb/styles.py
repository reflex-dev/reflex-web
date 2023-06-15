"""App styling."""

import pynecone as pc

# General styles.
BOLD_WEIGHT = "800"
NAVBAR_LOGO = "/Reflex.svg"
LOGO_URL = "/Reflex_white.svg"
PADDING_X = ["1em", "2em", "5em"]
PADDING_X2 = ["1em", "2em", "10em"]
HERO_FONT_SIZE = ["2em", "3em", "3em", "4em"]
H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = ["1.8em", "1.9em", "2em"]
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1.1em"
TEXT_FONT_SIZE = "1em"
TEXT_FONT_FAMILY = "Instrument Sans"
CODE_FONT_FAMILY = "Fira Code, Fira Mono, Menlo, Consolas, DejaVu Sans Mono, monospace"
ACCENT_COLOR = "rgb(107,99,246)"
ACCENT_COLOR_LIGHT = "rgba(107,99,246, 0.4)"
ACCENT_COLOR_DARK = "rgb(86, 77, 209)"
SUBHEADING_COLOR = "rgb(37,50,56)"
LIGHT_TEXT_COLOR = "#94a3b8"
LINK_STYLE = {
    "color": ACCENT_COLOR,
    "text_decoration": "underline",
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
    pc.Text: {
        "font_family": "Instrument Sans",
        "font_size": 16,
    },
    pc.Divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    pc.Code: {
        "color": ACCENT_COLOR,
    },
    pc.Alert: {
        "border_radius": "8px",
    }
}

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Silkscreen&display=swap",
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Roboto:wght@400;500;700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap",
]


# Styles to use for the navbar.
NAV_TEXT_COLOR = "#494369"
NAV_SEARCH_COLOR = "#342E5C"

NAV_TEXT_STYLE = {
    "color": NAV_TEXT_COLOR,
    "font_family": "Instrument Sans",
    "font_weight": "600",
}

NAV_SEARCH_STYLE = {
    "color": NAV_SEARCH_COLOR,
    "font_family": "Instrument Sans",
    "font_weight": "500",
}

Primary_Initial_Large_STYLE = {
    "justify_content": "center",
    "align_items": "center",
    "isolation": "isolate",
    "border_radius": 10,
    "font_family": "Instrument Sans",
    "font_style": "normal",
    "font_weight": 600,
    "font_feature_settings": "'tnum' on, 'lnum' on, 'case' on, 'cpsp' on, 'kern' off",
    "color": "#F5EFFE",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(52, 46, 92, 0.8) 0%, rgba(234, 228, 253, 0) 100%), #7E69E0",
    "box_shadow": "0px 0px 0px 1px rgba(32, 17, 126, 0.56), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 4px 8px rgba(3, 3, 11, 0.24), 0px 4px 10px -2px rgba(3, 3, 11, 0.32), inset 0px 1px 0px rgba(255, 255, 255, 0.16), inset 0px 12px 12px -2px rgba(149, 128, 247, 0.16), inset 0px -20px 12px -4px rgba(86, 70, 237, 0.32)"
}