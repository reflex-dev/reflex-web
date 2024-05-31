import reflex as rx
from pcweb import constants, styles
from pcweb.components.logo import logo
from pcweb.pages.docs import getting_started
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.library import library
from pcweb.pages.index import index
from pcweb.signup import IndexState
import asyncio
import json
import os
from datetime import datetime
import httpx
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field


footer_item_style = {
    "font_family": styles.SANS,
    "font_weight": "500",
    "_hover": {"color": rx.color("accent", 5)},
    "color": "#6C6C81"
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": f"0.1em solid {rx.color('accent', 5)}",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "#110F1F",
}

def prompt_sign():
    return rx.chakra.text(
        "$",
        color=rx.color("accent"),
        font_family=styles.SANS,
        style={"userSelect": "none"},
    )

def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


number_color = "#4E5A6A"
text_color="#A9ABD8"
other_color ="#5646ED"
bottom_color = "#6C6C81"

def installation():
    return rx.center(
        rx.flex( 
            rx.flex(
                rx.flex(rx.text("1", color=number_color),rx.text("$", color=other_color), rx.text("pip install reflex", color=text_color), spacing ="2"),
                rx.flex(rx.text("2", color=number_color),rx.text("$",  color=other_color), rx.text("reflex init", color=text_color), spacing ="2"),
                rx.flex(rx.text("3", color=number_color),rx.text("$",  color=other_color), rx.text("reflex run", color=text_color), spacing ="2"),
                rx.flex(
                    rx.text("You should see your first app", color=bottom_color),
                    rx.box(flex_grow=1),
                    rx.link(
                        rx.button(
                            "View Docs",
                            border_radius= "8px;",
                            background= "linear-gradient(180deg, #6151F3 0%, #5646ED 100%);",
                            box_shadow= "0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset, 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 2px 24px -1px #080525, 0px 3px 9px -2px #4033C0;",
                        ),
                        href=getting_started.installation.path,
                    )
                ),
                direction="column",
                spacing="2"
            ),
            direction="column",
            border_radius= "10px 10px 0px 0px;",
            border_top= "1px solid #3C3646;",
            border_right= "1px solid #3C3646;",
            border_left= "1px solid #3C3646;",
            background= "linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%);",
            box_shadow= "0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
            padding="1em",
            width="30em",
            spacing="3"
        ), 
        width="100%",
        border_bottom="1px solid #3C3646;"
    )

button_style = {
    "border_radius": "50px",
    "": "",
    "padding": "7px 12px 7px 12px",
    "align_items": "center",
}

def news_letter_form():
    return rx.el.form(
        rx.chakra.input_group(
            rx.chakra.input_right_element(
                rx.chakra.button(
                    "->",
                    type_="submit",
                    color="#FFF",
                    background="rgba(161, 157, 213, 0.03)",
                    border_left="1px solid rgba(186, 199, 247, 0.12)",
                    border_top_left_radius="0px",
                    border_bottom_left_radius="0px",
                    _hover={"linear-gradient(180deg, #6151F3 0%, #5646ED 100%);"},
                )           
            ),
            rx.chakra.input(
                name="input_email",
                placeholder="Your email...",
                color="#fff",
                background="rgba(161, 157, 213, 0.03)",
                border="1px solid rgba(186, 199, 247, 0.12)",
                border_radius="8px",
            ),
            width="100%",
        ),
        on_submit=IndexState.signup,
    )

def message_group():
    return rx.vstack(
        rx.text("You have successfully signed up!", color="#6C6C81"),
        rx.link(
            "Sign up for another email",
            href="#",
            size='2',
            color="#FFFFFF",
            underline="always",
            on_click=IndexState.signup_for_another_user().prevent_default,
        )
    )

def news_letter(align="left"):
    return rx.vstack(
        rx.text("Join Newsletter", color="#E8E8F4", style=footer_item_style),
        rx.text(
            "Get the latest updates and news about Reflex.",
            color="#6C6C81",
            font_size="0.8em",
        ),
        rx.cond(  
            IndexState.signed_up,
            message_group(),
            news_letter_form(),
        ),
        align_items=align,
        width="100%",
    )




def links():
    from pcweb.pages.blog import blogs
    from pcweb.pages.changelog import changelog
    from pcweb.pages.faq import faq
    from pcweb.pages.errors import errors
    return rx.hstack(
        rx.desktop_only(
            logo(
                width=["5em", "6em", "7em"],
            ),
        ),
        rx.vstack(
            rx.text("Site", color="#E8E8F4"),
            rx.link("Home", href=index.path, style=footer_item_style),
            rx.link("Gallery", href=gallery.path, style=footer_item_style),
            rx.link("Blog", href=blogs.path, style=footer_item_style),
            rx.link(
                "Changelog",
                href=changelog.path,
                style=footer_item_style,
            ),
            align_items="start",
        ),
        rx.vstack(
            rx.text("Documentation", color="#E8E8F4"),
            rx.link(
                "Introduction",
                href=getting_started.introduction.path,
                style=footer_item_style,
            ),
            rx.link(
                "Installation",
                href=getting_started.installation.path,
                style=footer_item_style,
            ),
            rx.link(
                "Components",
                href=library.path,
                style=footer_item_style,
            ),
            align_items="start",
        ),
        rx.desktop_only(rx.vstack(
            rx.text("Resources", color="#E8E8F4"),
            rx.link(
                "FAQ",
                href=faq.path,
                style=footer_item_style,
            ),
            rx.link(
                "Common Errors",
                href=errors.path,
                style=footer_item_style,
            ),
            rx.link(
                "Roadmap",
                href=constants.ROADMAP_URL,
                style=footer_item_style,
            ),
            rx.link(
                "Forum",
                href=constants.GITHUB_DISCUSSIONS_URL,
                style=footer_item_style,
            ),
            align_items="start",
        )),
        rx.tablet_and_desktop(
            news_letter(),
        ),
        justify="between",
        align_items="top",
        padding_bottom="2em",
        min_width="100%",
        padding_top="2em"
    )



def footer(style=footer_style):
    return rx.box(
        rx.vstack(
            installation(),
            links(),
            rx.mobile_only(
                news_letter(),
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Copyright © 2024 Pynecone, Inc.",
                    style=footer_item_style,
                    font_size="0.8em",
                ),
                rx.hstack(
                    rx.link(
                        rx.image(src="/companies/light/github.svg", alt="A link to Reflex's Github", height="1.5em"),
                        href=constants.GITHUB_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/linkedin.svg", alt="A link to Reflex's Linkedin", height="1.5em"),
                        href=constants.LINKEDIN_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/yc.svg", alt="A link to Reflex's YC profile", height="1.5em"),
                        href=constants.YC_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/twitter.svg", alt="A link to Reflex's Twitter", height="1.5em"),
                        href=constants.TWITTER_URL,
                    ),
                    rx.link(
                        rx.image(src="/companies/light/discord.svg", alt="A link to Reflex's Discord", height="1.5em"),
                        href=constants.DISCORD_URL,
                    ),
                    gap="1em",
                ),
                padding_top="2em",
                justify="between",
                color=rx.color("mauve", 5),
                padding_bottom="2em",
                min_width="100%",
            ),
            padding_x=["1em", "1em", "1em", "2em", "4em", "4em"],
            padding_y=[".5em", ".5em", ".5em", "2em", "2em", "2em"],
            width="100%",
        ),
        background="#131217",
        width="100%",
        z_index=1,
    )

