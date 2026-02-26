from pcweb.pages.migration.common.quotes import CompanyInfo
from pcweb.pages.migration.common.quotes import quotes as common_quotes

COMPANIES: list[CompanyInfo] = [
    {
        "key": "open_sea",
        "logo_image_name": "open_sea.svg",
        "logo_alt": "OpenSea logo",
        "name": "Alex Atallah",
        "title": "Co-founder & CEO, OpenSea",
        "quote": "Have been playing with Reflex since January and realized I should just say, from a fellow YC member: love the architecture decisions you guys are making!",
        "profile_image": "/landing/social/alex_opensea.webp",
    },
    {
        "key": "fastly",
        "logo_image_name": "fastly.svg",
        "logo_alt": "Fastly logo",
        "name": "Emanuele Bonura",
        "title": "Senior SOC Engineer",
        "quote": "Migrating our cybersecurity app from Streamlit to Reflex has been excellent. We quickly built a unified interface connecting BigQuery, Salesforce, and PagerDuty for our 15+ team members. The ease of use and rapid development, supported by your responsive team, made it a great experience.",
        "profile_image": "",
    },
    {
        "key": "autodesk",
        "logo_image_name": "autodesk.svg",
        "logo_alt": "Autodesk logo",
        "name": "Paolo",
        "title": "Principal Consultant",
        "quote": "One person can do the job of two with Reflex, so it cut our cost in half. I am able to wear all the caps at once: Solution Architecture, UI/UX, front-end and back-end.",
        "profile_image": "",
    },
    {
        "key": "accenture",
        "logo_image_name": "accenture.svg",
        "logo_alt": "Accenture logo",
        "name": "Jordan Lee",
        "title": "Senior Automation Developer",
        "quote": "Reflex let us automate workflows that were impossible with previous low-code platforms. We went from prototype to rollout in days, and our team loves writing real Python instead of fighting drag-and-drop UI pain.",
        "profile_image": "",
    },
]


def quotes():
    return common_quotes(
        companies=COMPANIES,
        default_active_key="open_sea",
        logo_base_path="/migration",
    )


__all__ = ["quotes"]
