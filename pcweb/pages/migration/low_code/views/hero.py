from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.pages.migration.common.hero import HeroLogo
from pcweb.pages.migration.common.hero import hero as common_hero

HERO_LOGOS: list[HeroLogo] = [
    {
        "image_name": "streamlit.svg",
        "alt": "Streamlit Logo",
        "class_name": "top-[9.5rem] -ml-[10.5rem]",
    },
    {
        "image_name": "plotly.svg",
        "alt": "Plotly Dash Logo",
        "class_name": "top-[9.5rem] ml-[10.5rem]",
    },
    {
        "image_name": "gradio.svg",
        "alt": "Gradio Logo",
        "class_name": "top-[15rem] -ml-[16.5rem]",
    },
]


def hero():
    return common_hero(
        kicker="Move From Low Code to Reflex",
        title="Architecture That Scales, Code That Stays Clean",
        subtitle="Streamlit, Dash, and Gradio get you prototyping fast, but you hit walls — rerun model, callback spaghetti, no real-time, no production path. Reflex gives you declarative state, event-driven updates, and production-ready output from day one.",
        cta_text="Book a Demo",
        logos=HERO_LOGOS,
        logo_base_path=f"{REFLEX_ASSETS_CDN}migration",
    )


__all__ = ["hero"]
