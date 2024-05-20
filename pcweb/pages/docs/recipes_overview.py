
import reflex as rx
from pcweb.templates.docpage import docpage, h1_comp, text_comp



items = [
    "navbar",
    "footer",
    "header",
    "hero section",
    "CTA buttons",
    "forms",
    "image gallery",
    "testimonials",
    "blog posts",
    "social media icons",
    "search bar",
    "breadcrumbs",
    "pagination",
    "modal windows",
    "accordion",
    "tabs",
    "progress bars",
    "timeline",
    "pricing tables",
    "FAQ section"
]

def component_grid():
    sidebar = []
    for item in items:
        sidebar.append(
            rx.box(
                rx.icon("layout-template"),
                rx.heading(
                    rx.link(
                        item, 
                        href="https://www.miffy.com/",
                        color=rx.color("mauve", 11),
                    ),
                    margin_top="0.75em",
                    style={"fontSize": "1.25em"},
                ),
                rx.text("5 variants", color=rx.color("mauve", 11)),
                row_span=3,
                col_span=1,
                border_radius="8px",
                background_color=rx.color("mauve", 2),
                border=f"1px solid {rx.color('mauve', 4)}",
                padding="2em",
            )
        )

    return rx.box(
        rx.chakra.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@docpage(right_sidebar=False)
def overview():
    return rx.flex(
        h1_comp(text="Recipes"),
        text_comp(
            text="Reflex comes with a wide range of pre-built components that are designed to help you quickly create modern, responsive web pages."
        ),
        component_grid(),
        text_align="left",
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
