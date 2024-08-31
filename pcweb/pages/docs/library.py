import reflex as rx

from pcweb.templates.docpage import docpage
from pcweb.templates.docpage import h1_comp
from pcweb.templates.docpage import text_comp


def component_grid():
    from pcweb.components.docpage.sidebar import get_component_link
    from pcweb.pages.docs import component_list
    from pcweb.pages.docs import graphing_components

    def generate_gallery(
        components,
        prefix: str = "",
    ):
        sidebar = []
        for category in components:
            sidebar.append(
                rx.box(
                    rx.heading(
                        category,
                        style={
                            "fontSize": "1.5em",
                        },
                    ),
                    rx.divider(),
                    rx.vstack(
                        *[
                            rx.link(
                                rx.utils.format.to_title_case(c[0]),
                                href=get_component_link(
                                    category=category,
                                    clist=c,
                                    prefix=prefix,
                                ),
                                font_size="1em",
                                color=rx.color(
                                    color="mauve",
                                    shade=12,
                                ),
                                _hover={
                                    "color": rx.color(
                                        color="violet",
                                        shade=9,
                                    ),
                                },
                            )
                            for c in components[category]
                        ],
                        align_items="start",
                    ),
                    row_span=3,
                    col_span=1,
                    border_radius="8px",
                    background_color=rx.color(
                        color="mauve",
                        shade=2,
                    ),
                    border=f"1px solid {rx.color(color='mauve', shade=4,)}",
                    padding="2em",
                ),
            )

        return sidebar

    core = generate_gallery(
        components=component_list,
    )
    # add `graphing/` prefix when generating graphing components to assume the url `/docs/library/graphing/<category>/<component>`.
    graphs = generate_gallery(
        components=graphing_components,
        prefix="graphing/",
    )
    return rx.box(
        rx.chakra.responsive_grid(
            *core,
            columns=[1, 2, 2, 2, 3],
            gap=4,
        ),
        rx.heading(
            "Graphing Components",
            margin_top="1em",
            style={
                "fontSize": "2em",
            },
        ),
        rx.separator(),
        rx.chakra.responsive_grid(
            *graphs,
            columns=[1, 2, 2, 2, 3],
            gap=4,
        ),
        width="100%",
    )


@docpage(
    right_sidebar=False,
)
def library():
    return rx.flex(
        h1_comp(
            text="Component Library",
        ),
        text_comp(
            text="Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. This page contains a list of all builtin components.",
        ),
        component_grid(),
        text_align="left",
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
