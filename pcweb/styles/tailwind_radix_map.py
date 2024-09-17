from reflex.constants.colors import ColorType


# Default Radix Colors
def create_colors_dict() -> dict:
    colors_dict = {}
    for color in ColorType.__args__:
        if color not in ["black", "white"]:
            colors_dict[color] = {
                shade: f"var(--{'c-' if color in ['slate', 'violet'] else ''}{color}-{shade})"
                for shade in range(1, 13)
            }
            # Append the alpha colors
            colors_dict[f"{color}A"] = {
                shade: f"var(--{color}-a{shade})" for shade in range(1, 13)
            }
    return colors_dict


# Custom Colors from the 'custom-colors.css' file
def create_custom_colors_dict() -> dict:
    custom_colors_dict = {}
    for color in ["slate", "violet"]:
        custom_colors_dict[color] = {
            shade: f"var(--c-{color}-{shade})" for shade in range(1, 13)
        }
    # Add the white color
    custom_colors_dict["white"] = {1: "var(--c-white-1)"}
    return custom_colors_dict


radix_colors_dict = create_colors_dict()
custom_colors_dict = create_custom_colors_dict()
