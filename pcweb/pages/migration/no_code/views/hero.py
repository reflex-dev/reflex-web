from pcweb.pages.migration.common.hero import HeroLogo
from pcweb.pages.migration.common.hero import hero as common_hero

HERO_LOGOS: list[HeroLogo] = [
    {
        "image_name": "powerbi.svg",
        "alt": "Power BI Logo",
        "class_name": "top-[9.5rem] -ml-[10.5rem]",
    },
    {
        "image_name": "retool.svg",
        "alt": "Retool Logo",
        "class_name": "top-[9.5rem] ml-[10.5rem]",
    },
    {
        "image_name": "tableau.svg",
        "alt": "Tableau Logo",
        "class_name": "top-[15rem] -ml-[16.5rem]",
    },
]


def hero():
    return common_hero(
        kicker="Move From No Code to Reflex",
        title="Full Control Without the Ceiling",
        subtitle="No-code tools get you to v1 fast, but you hit walls — custom logic, complex data flows, performance. With Reflex, you're writing Python, so there's no ceiling. You own your code, deploy anywhere, and ship what you demo.",
        cta_text="Book a Demo",
        logos=HERO_LOGOS,
        logo_base_path="/migration",
    )


__all__ = ["hero"]
