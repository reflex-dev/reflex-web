from pcweb.pages.migration.common.hero import HeroLogo
from pcweb.pages.migration.common.hero import hero as common_hero

HERO_LOGOS: list[HeroLogo] = [
    {
        "image_name": "cursor.svg",
        "alt": "Cursor Logo",
        "class_name": "top-[9.5rem] -ml-[10.5rem]",
    },
    {
        "image_name": "claude.svg",
        "alt": "Claude Logo",
        "class_name": "top-[15rem] ml-[16.5rem]",
    },
    {
        "image_name": "replit.svg",
        "alt": "Replit Logo",
        "class_name": "top-[9.5rem] ml-[10.5rem]",
    },
    {
        "image_name": "lovable.svg",
        "alt": "Lovable Logo",
        "class_name": "top-[15rem] -ml-[16.5rem]",
    },
]


def hero():
    return common_hero(
        kicker="Move From Other AI Tools to Reflex",
        title="The Next-Gen Platform Built for Modern Enterprises",
        subtitle="Escape AI tool constraints without sacrificing speed. Build production-grade apps in pure Python with complete control over your stack.",
        cta_text="Book a Demo",
        logos=HERO_LOGOS,
        logo_base_path="/migration",
    )


__all__ = ["hero"]
