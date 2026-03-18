from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.pages.migration.common.hero import HeroLogo
from pcweb.pages.migration.common.hero import hero as common_hero

HERO_LOGOS: list[HeroLogo] = [
    {
        "image_name": "react.svg",
        "alt": "React Logo",
        "class_name": "top-[9.5rem] -ml-[10.5rem]",
    },
    {
        "image_name": "js.svg",
        "alt": "JavaScript Logo",
        "class_name": "top-[15rem] ml-[16.5rem]",
    },
    {
        "image_name": "django.svg",
        "alt": "Django Logo",
        "class_name": "top-[9.5rem] ml-[10.5rem]",
    },
    {
        "image_name": "fastapi.svg",
        "alt": "FastAPI Logo",
        "class_name": "top-[15rem] -ml-[16.5rem]",
    },
]


def hero():
    return common_hero(
        kicker="Move From Other Frameworks to Reflex",
        title="The Next-Gen Platform Built for Modern Enterprises",
        subtitle="Escape other framework constraints without sacrificing speed. Build production-grade apps in pure Python with complete control over your stack.",
        cta_text="Book a Demo",
        logos=HERO_LOGOS,
        logo_base_path=f"{REFLEX_ASSETS_CDN}migration",
    )


__all__ = ["hero"]
