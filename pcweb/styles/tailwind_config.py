from pcweb.styles.tailwind_radix_map import radix_colors_dict, custom_colors_dict

tw_config = {
    "plugins": ["@tailwindcss/typography", "tailwindcss-radix"],
    "darkMode": "class",
    "theme": {
        "fontFamily": {
            "code": ["JetBrains Mono", "monospace"],
        },
        "colors": {
            **radix_colors_dict,
            **custom_colors_dict,
            "transparent": "transparent",
        },
        "boxShadow": {
            "small": "0px 2px 4px 0px rgba(28, 32, 36, 0.05)",
            "medium": "0px 4px 8px 0px rgba(28, 32, 36, 0.04)",
            "large": "0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02)",
        },
    },
}
