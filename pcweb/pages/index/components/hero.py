import reflex as rx
from .logo import landing

def feature_button(name: str):
    return rx.button(
        name,
        color="848496",
        border_radius="50px;",
        border="1px solid rgba(186, 199, 247, 0.12);",
        background= "rgba(161, 157, 213, 0.03);",
        backdrop_filter= "blur(2px);",
        size="2"
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
            "Web apps in Pure Python.",
            text_align="left" if not mobile else "center",
            background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size=["30px", "40px", "54px", "54px", "54px", "54px"],
            background_clip="text",
            font_weight="bold",
            line_height="1",
            
        ),
        rx.chakra.text(
            "Deploy with a single command.",
            text_align="left" if not mobile else "center",
            color="#6C6C81",
            font_size=["30px", "40px", "54px", "54px", "54px", "54px"],
            font_weight="bold",
            line_height="1",
            max_width=["300px", "350px","650px", "650px", "650px","650px"],
        ),
        align_items="center",
        
    )

def hero_section_buttons(mobile=False):
    return rx.hstack(
        rx.link(
            rx.button(
                "Get Started",
                color="#FFFFFF",
                background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
                box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
                size="4"
            ),
            href="/docs/getting-started",        
        ),
        rx.link(
            rx.button(
                "Get a demo",
                variant="ghost",
                border_radius="8px",
                border="2px solid rgba(186, 199, 247, 0.12)",
                background="rgba(161, 157, 213, 0.03)",
                backdrop_filter="blur(2px)",
                color="white",
                size="4"
            ),
            href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX", 
            margin_left="1em",        
        ),
        padding_top="1em",
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
                spacing="3",
                align_items="left",
            )),
            rx.mobile_and_tablet(
                rx.vstack(
                    feature_button_hstack(mobile=True),
                    hero_section_text(mobile=True),
                    hero_section_buttons(mobile=True),
                    spacing="3",
                    margin_top=["-4em", "-2em", "-2em", "-2em", "0", "0"],
                ),
            ),
            direction="column",
            align_items="left",
            margin_top=["-6em", "-4em", "0", "0", "0", "0"],
            padding_bottom=["4em", "4em", "14em", "14em", "14em", "14em"],
        ),
        width="100%",
    )
