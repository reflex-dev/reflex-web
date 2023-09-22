import reflex as rx
from pcweb import flexdown

def render_form():
    # Get the file.
    front_matter, output = flexdown.read("docs/library/forms/form.md")
    return rx.box(
        *output,
    )