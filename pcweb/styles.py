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
DOC_HEADER_COLOR = "#000000"
DOC_TEXT_COLOR = "#000000"
DOC_REG_TEXT_COLOR = "#666666"
DOC_LIGHT_TEXT_COLOR = "#999999"
DOCPAGE_BACKGROUND_COLOR = "#fafafa"

DOC_HEADING_FONT_WEIGHT = "700"
DOC_SUBHEADING_FONT_WEIGHT = "600"
DOC_SECTION_FONT_WEIGHT = "500"

DOC_SHADOW = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
DOC_SHADOW_DARK = "rgba(0, 0, 0, 0.3) 0px 2px 8px"
DOC_SHADOW_LIGHT = "rgba(0, 0, 0, 0.08) 0px 4px 12px"

DOC_BORDER_RADIUS = "1em"

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
