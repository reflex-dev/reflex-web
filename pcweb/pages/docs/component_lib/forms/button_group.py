from pcweb.flexdown import component_map
import flexdown


def render_buttongroup():
    return flexdown.render_file("docs/library/forms/button_group.md", component_map=component_map)