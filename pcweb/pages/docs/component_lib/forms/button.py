from pcweb.flexdown import component_map
import flexdown


def render_button():
    return flexdown.render_file(
        "docs/library/forms/button.md", component_map=component_map
    )
