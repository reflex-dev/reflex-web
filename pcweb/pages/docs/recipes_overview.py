
import reflex as rx

from pcweb.templates.docpage import docpage, h1_comp, h2_comp, h3_comp, h4_comp, text_comp

def get_component_link(category, clist) -> str:
    file_name_without_extension = clist.split('/')[-1].split('.')[0].replace('_', '-')
    return f"/docs/recipes/{category}/{file_name_without_extension}"

def format_titles(path):
    title_without_ext = path.split('.')[0]
    parts = title_without_ext.split('/')
    last_part = parts[-1]
    capitalized_last_part = last_part.replace('_', '-').title()
    return capitalized_last_part
  
def component_grid():
    from pcweb.pages.docs import recipes_list
    icons = {
        "layout": "panels-top-left",
        "content": "layout-grid",
        "auth": "lock-keyhole",
    }
    sidebar = []
    for item in recipes_list:
        category = item.split('/')[-1]
        sidebar.append(
            rx.box(
                rx.card(
                    rx.icon(
                        icons.get(category, "shapes"),
                        stroke_width=2,
                        color=rx.color("mauve", 11),
                    ),
                    width="48px",
                ),
                rx.heading(
                    rx.utils.format.to_title_case(category),
                    color=rx.color("mauve", 12),
                    margin_top="0.75em",
                    style={"fontSize": "1.25em"},
                ),
                rx.divider(),
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

def info_card(icon, color, title, content):
    return rx.flex(
        rx.button(
            rx.icon(
                tag=icon,
                color="white",
                fill="rgba(255, 255, 255, 0.25)",
                size=20,
            ),
            height="35px",
            width="35px",
            padding="0px",
            border_radius="6px",
            color_scheme=color,
            variant="classic",
            align_items="center",
            justify="center",
        ),
        rx.heading(
            title,
            color=rx.color("mauve", 12),
            style={"fontSize": "1.25em"},
        ),
        rx.text(
            content,
            font_size=".8em",
        ),
        row_span=3,
        col_span=1,
        border_radius="8px",
        background_color=rx.color("mauve", 1),
        border=f"1px solid {rx.color('mauve', 4)}",
        padding_x="2em",
        padding_y="1em",
        spacing="2",
        direction="column",
    )

def card_section():
    return rx.box(
        rx.chakra.responsive_grid(
            info_card("box", "violet", "Portable", "Easy to copy and integrate into your your next Reflex project."),
            info_card("palette", "violet", "Themed", "Automatically adapts to the theme of your Reflex project."),
            info_card("settings", "violet",  "Customizable", "Every aspect of the components can be customized to fit your needs."),
            columns=[1, 2, 3, 3, 3],
            gap=4,
        ),
    )

@docpage(right_sidebar=False)
def overview():
    return rx.flex(
        h1_comp(
            text="Recipes"
        ),
        text_comp(
            text="Recipes are a collection of common patterns and components that can be used to build Reflex applications. Each recipe is a self-contained component that can be easily copied and pasted into your project."
        ),
        card_section(),
        h2_comp(
            text="Categories",
            margin_button="2em",
        ),
        component_grid(),
        text_align="left",
        flex_direction="column",
        height="100%",
        margin_bottom="4em",
    )
