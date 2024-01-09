import reflex as rx
from pcweb.templates.docpage import docheader, docpage, doctext


def component_grid():
    from pcweb.pages.docs import component_list

    sidebar = []
    for category in component_list:
        sidebar.append(
            rx.box(
                rx.heading(category, style={"fontSize": "1.5em"}),
                rx.divider(),
                rx.vstack(
                    *[
                        rx.link(
                            c[0].__name__,
                            href=f"/docs/library/{category.lower()}/{c[0].__name__.lower()}",
                            style={"fontSize": "1em"},
                        )
                        for c in component_list[category]
                        if not isinstance(c[0], str)
                    ],
                    align_items="start",
                ),
                row_span=3,
                col_span=1,
                box_shadow="rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px",
                border_radius="1em",
                bg_color="white",
                padding=5,
                _hover={
                    "box_shadow": "rgba(38, 57, 77, .3) 0px 20px 30px -10px",
                },
            )
        )

    return rx.box(
        rx.responsive_grid(*sidebar, columns=[1, 2, 2, 2, 3], gap=4),
    )


@docpage()
def library():
    return rx.flex(
        rx.hstack(
            rx.box(
                docheader("Component Library", first=True),
                doctext(
                    "Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. This page contains a list of all builtin components. "
                ),
                rx.divider(),
                component_grid(),
                text_align="left",
            ),
            align_items="start",
        ),
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
