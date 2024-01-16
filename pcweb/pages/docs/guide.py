import reflex as rx
from pcweb.flexdown import xd
from pcweb.templates.webpage import webpage


@webpage(path="/flexdown-guide", title="Flexdown Guide")
def guide():
    print(rx.radix.themes.Badge)
    return rx.container(
        xd.render_file("docs/flexdown-guide.md"),
        padding_y="2em",
        max_width="960px",
    )
