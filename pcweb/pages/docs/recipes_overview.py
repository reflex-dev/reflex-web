
import reflex as rx

from pcweb.templates.docpage import docpage, h1_comp, text_comp

def get_component_link(category, clist) -> str:
    file_name_without_extension = clist.split('/')[-1].split('.')[0]
    return f"/docs/recipes/{category}/{file_name_without_extension}"

def format_titles(path):
    title_without_ext = path.split('.')[0]
    parts = title_without_ext.split('/')
    last_part = parts[-1]
    capitalized_last_part = last_part.replace('_', '-').title()
    return capitalized_last_part


def component_grid():
    from pcweb.pages.docs import recipes_list

    sidebar = []
    for item in recipes_list:
        category = item.split('/')[-1]
        sidebar.append(
            rx.box(
                rx.card(
                    rx.icon("layout-template", stroke_width=2.5),
                    width="48px",
                ),
                rx.heading(
                    rx.link(
                        category,
                        href="https://www.miffy.com/",
                        color=rx.color("mauve", 11),
                    ),
                    margin_top="0.75em",
                    style={"fontSize": "1.25em"},
                ),
                rx.vstack(
                    *[
                        rx.link(
                            format_titles(c),
                            href=get_component_link(category, c),
                            font_size="1em",
                            color=rx.color("mauve", 12),
                            _hover={"color": rx.color("violet", 9)},
                        )
                        for c in recipes_list[category]
                    ],
                    align_items="start",
                ),
                row_span=3,
                col_span=1,
                border_radius="8px",
                background_color=rx.color("mauve", 2),
                border=f"1px solid {rx.color('mauve', 4)}",
                padding="2em",
            )
        )

    return rx.box(
        rx.chakra.responsive_grid(*sidebar, columns=[1, 2, 2, 3, 3], gap=4),
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
