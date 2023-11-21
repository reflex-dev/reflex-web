import reflex as rx
import flexdown

from pcweb.templates.docpage import (
    code_block2,
    text_comp,
    h1_comp,
    h2_comp,
    h3_comp,
    code_comp,
    doclink2,
)

component_map = {
    "h1": lambda text: h1_comp(text=text),
    "h2": lambda text: h2_comp(text=text),
    "h3": lambda text: h3_comp(text=text),
    "p": lambda text: text_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block2,
}
xd = flexdown.Flexdown(component_map=component_map)

# Monkeypatch markdown custom components.
md = rx.markdown("", component_map=component_map)
custom = md.get_custom_components()

def get_custom_components(self, seen):
    return custom

rx.Markdown.get_custom_components = get_custom_components


@rx.memo
def markdown_memo(content: str) -> rx.Component:
    return rx.markdown(content, component_map=component_map)


def render_file(path):
    return xd.render_file(path)
