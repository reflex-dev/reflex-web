import reflex as rx
from .logo import landing
from pcweb.pages.docs import getting_started

def feature_button(name: str):
    return rx.flex(
        name,
        color="#848496",
        size="2",
        padding=".25em 1em",
        background= "linear-gradient(#131217, #131217) padding-box, linear-gradient(to bottom right, #8F93BC 5%, #656484 15%, #232329) border-box;",
        border= "1px solid transparent;",
        font_size=".8em",
        border_radius="50px", 
    )

def feature_button_hstack(mobile=False):
    return rx.hstack(
        feature_button("Frontend"),
        feature_button("Backend"),
        feature_button("Hosting"),
        justify="start" if not mobile else "center",
        width="100%",
    )


def hero_section_text(mobile=False):
    return rx.vstack(
        rx.chakra.text(
            "Web apps in pure Python.",
            text_align="left" if not mobile else "center",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
            background_clip="text",
            font_weight="bold",
            line_height="1",
            
        ),
        rx.chakra.text(
            "Deploy with a single command.",
            text_align="left" if not mobile else "center",
            color="#6C6C81",
            font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
            font_weight="bold",
            line_height="1",
            max_width=["200px", "300px", "400px", "650px", "650px", "650px"],
        ),
        align_items="center" if mobile else "start",
        
    )

def hero_section_buttons(mobile=False):
    button_size={
        "padding_y": "1.5em",
        "padding_x": "2em",
        "border_radius": "8px",
        "color":"#FFFFFF",
        "align_items":"center",
        "justify_content":"center",
        "font_weight":"400",
        "font_size":"1em",
    }
    return rx.hstack(
        rx.link(
            rx.flex(
                rx.button(
                    "Get Started",
                    rx.icon(
                    tag="chevron-right",
                        size=18,
                        stroke_width="1px",
                        padding_left=".1em",
                    ),
                    background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
                    box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
                    display= "inline-flex;",   
                    border= "1px solid transparent;", 
                    style=button_size,
                ),
                _hover={
                    "border": "1px solid rgba(94, 78, 242, .15)",
                },
                border= "1px solid transparent;",
                padding="3px",
                border_radius="8px",
            ),
            href=getting_started.introduction.path,        
        ),
        rx.link(
            rx.button(
                "Get a demo ",
                rx.icon(
                    tag="chevron-right",
                    size=18,
                    stroke_width="1px",
                    padding_left=".1em",
                ),
                bg="none",
                _hover={
                    "background": "linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%)",
                    "box-shadow": "0px 0px 27px -4px rgba(0, 0, 0, 0.30), 0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset;"
                },
                style=button_size,
            ),
            href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX", 
            is_external=True,
            margin_left=".25em",        
        ),
        align_items="center",
        justify="start" if not mobile else "center",
        width="100%",
    )

def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.center(
        rx.chakra.vstack(
            landing(),
            rx.desktop_only(rx.vstack(
                feature_button_hstack(),
                hero_section_text(),
                hero_section_buttons(),
                padding_left="3em",
                spacing="5",
                align_items="left",
            )),
            rx.mobile_and_tablet(
                rx.vstack(
                    #feature_button_hstack(mobile=True),
                    hero_section_text(mobile=True),
                    hero_section_buttons(mobile=True),
                    spacing="5",
                    margin_top=["-4em", "-3em", "-1em", "0", "0", "0"],
                ),
            ),
            direction="column",
            align_items="left",
            margin_top=["-6em", "-4em", "0", "0", "0", "0"],
            padding_bottom=["0em", "0em", "10em", "10em", "10em", "10em"],
        ),
        width="100%",
    )
