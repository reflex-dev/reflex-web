import reflex as rx
import flexdown

from pcweb.templates.docpage import (
    code_block2,
    docheader2,
    doctext,
    subheader2,
    subheader3,
    doclink2,
)


component_map = {
    "h1": docheader2,
    "h2": subheader2,
    "h3": subheader3,
    "a": doclink2,
    "p": doctext,
    "code": lambda source: rx.code(source, color="#1F1944", bg="#EAE4FD"),
    "codeblock": code_block2,
}


def render_file(path):
    return flexdown.render_file(path, component_map=component_map)
