import pynecone as pc

from pcweb import constants, styles
from pcweb.components.logo import logo
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.getting_started import installation, introduction
from pcweb.pages.docs.library import library
from pcweb.pages.docs.hosting.deploy import deploy
from pcweb.pages.index import index

footer_item_style = {
    "font_family": "Inter",
    "font_weight": "500",
    "_hover": {"color": "#82799E"},
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.1em solid #82799E",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "#110F1F",
}


def footer(style=footer_style):
    return pc.box(
        pc.vstack(
            pc.hstack(
                pc.desktop_only(
                    logo(
                        width=["4.28em", "4.28em", "5.35em"],
                        height=["4em", "4em", "5em"],
                    ),
                ),
                pc.vstack(
                    pc.text("Site", color="#DACEEE"),
                    pc.link("Home", href=index.path, style=footer_item_style),
                    pc.link("Gallery", href=gallery.path, style=footer_item_style),
                    pc.link("Hosting", href=deploy.path, style=footer_item_style),
                    align_items="start",
                ),
                pc.vstack(
                    pc.text("Documentation", color="#DACEEE"),
                    pc.link(
                        "Introduction",
                        href=introduction.path,
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Installation",
                        href=installation.path,
                        style=footer_item_style,
                    ),
                    pc.link("Components", href=library.path, style=footer_item_style),
                    align_items="start",
                ),
                pc.vstack(
                    pc.text("Resources", color="#DACEEE"),
                    pc.link(
                        "GitHub",
                        href=constants.GITHUB_URL,
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Discord",
                        href=constants.DISCORD_URL,
                        style=footer_item_style,
                    ),
                    pc.link(
                        "Twitter",
                        href=constants.TWITTER_URL,
                        style=footer_item_style,
                    ),
                    align_items="start",
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            pc.hstack(
                pc.text(
                    "Copyright © 2023 Pynecone",
                    font_weight="500",
                ),
                pc.link(
                    "Contact",
                    href=constants.CONTACT_URL,
                    font_weight="500",
                    style=footer_item_style,
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )
