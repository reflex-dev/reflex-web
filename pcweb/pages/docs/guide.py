import reflex as rx

from pcweb.templates.webpage import webpage


@webpage(path="/flexdown-guide", title="Flexdown Guide")
def guide():
    return rx.box("Coming Soon")
