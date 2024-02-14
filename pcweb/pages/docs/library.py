import reflex as rx
from pcweb.templates.docpage import docpage, h1_comp, text_comp


def component_grid():
    from pcweb.components.sidebar import get_component_link
    from pcweb.pages.docs import component_list

    sidebar = []
    for category in component_list:
        sidebar.append(
            rx.box(
                rx.heading(category, style={"fontSize": "1.5em"}),
                rx.chakra.divider(),
                rx.vstack(
                    *[
                        rx.link(
                            rx.utils.format.to_title_case(c[0]),
                            href=get_component_link(category, c),
                            font_size="1em",
                            color=rx.color("mauve", 12)
                        )
                        for c in component_list[category]
                    ],
                    align_items="start",
                ),
                row_span=3,
                col_span=1,
                box_shadow="rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
                border_radius="1em",
                bg_color="white",
                padding="2em",
                _hover={
                    "box_shadow": "rgba(38, 57, 77, .3) 0px 20px 30px -10px",
                },
            )
        )

    return rx.box(
        rx.chakra.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@docpage()
def library():
    return rx.flex(
        rx.hstack(
            rx.box(
                h1_comp(text="Component Library"),
                text_comp(
                    text="Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. This page contains a list of all builtin components. "
                ),
                rx.chakra.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
