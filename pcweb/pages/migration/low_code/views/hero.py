from pcweb.pages.migration.common.hero import HeroLogo
from pcweb.pages.migration.common.hero import hero as common_hero

HERO_LOGOS: list[HeroLogo] = [
    {
        "image_name": "plotly.svg",
        "alt": "Plotly Logo",
        "class_name": "top-[9.5rem] -ml-[10.5rem]",
    },
    {
        "image_name": "powerbi.svg",
        "alt": "Power BI Logo",
        "class_name": "top-[15rem] ml-[16.5rem]",
    },
    {
        "image_name": "retool.svg",
        "alt": "Retool Logo",
        "class_name": "top-[9.5rem] ml-[10.5rem]",
    },
    {
        "image_name": "streamlit.svg",
        "alt": "Streamlit Logo",
        "class_name": "top-[15rem] -ml-[16.5rem]",
    },
]


def hero():
    return common_hero(
        kicker="Move From Low Code to Reflex",
        title="The Next-Gen Platform Built for Modern Enterprises",
        subtitle="Escape low-code constraints without sacrificing speed. Build production-grade apps in pure Python with complete control over your stack.",
        cta_text="Book a Demo",
        logos=HERO_LOGOS,
        logo_base_path="/migration",
    )


__all__ = ["hero"]
