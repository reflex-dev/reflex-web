# import reflex as rx

# from pcweb.components.icons import get_icon
# from pcweb.templates.mainpage import mainpage
# from pcweb.components.hosting_banner import HostingBannerState
# from pcweb.pages.pricing.table import create_feature_table_header, create_feature_row, create_table_body, TABLE_STYLE

# DATA_PROTECTION_FEATURES = [
#     ("Data Encryption", "AES-256 encryption at rest, TLS 1.2+ in transit."),
#     ("Database Backups", "Daily encrypted backups with 30-day retention."),
#     ("Data Segregation", "Customer data is logically isolated per tenant."),
# ]

# PRODUCT_SECURITY_FEATURES = [
#     ("Penetration Testing", "External tests conducted annually."),
#     ("Secure Development Lifecycle", "Code reviews, linting, and security scans."),
#     ("Dependency Management", "Automated scanning for vulnerabilities."),
# ]

# ENTERPRISE_SECURITY_FEATURES = [
#     ("SSO/SAML", "Supports major identity providers for centralized auth."),
#     ("Granular Permissions", "Role-based access control across teams."),
#     ("Audit Logs", "Track every access and change in the system."),
# ]

# DATA_PRIVACY_FEATURES = [
#     ("GDPR & CCPA Ready", "Compliant data handling and user rights."),
#     ("Data Deletion Requests", "Users can request full data erasure."),
#     ("Privacy by Design", "Privacy baked into product architecture."),
# ]


# trust_services_criteria = [
#     {
#         "title": "Security",
#         "description": "Protection of systems and data from unauthorized access through firewalls, multi-factor authentication, and continuous monitoring.",
#         "icon": "shield",
#     },
#     {
#         "title": "Availability",
#         "description": "Ensures that systems are operational and accessible as promised, with redundancy, failover systems, and uptime monitoring in place.",
#         "icon": "globe",
#     },
#     {
#         "title": "Confidentiality",
#         "description": "Restricts access to sensitive information using encryption, role-based access controls, and secure data handling policies.",
#         "icon": "backend_auth",
#     },
#     {
#         "title": "Processing Integrity",
#         "description": "Guarantees that system operations are accurate, timely, and authorized, using code reviews, automated tests, and deployment controls.",
#         "icon": "code_custom",
#     },
#     {
#         "title": "Privacy",
#         "description": "Covers the collection, use, retention, and disposal of personal information according to regulatory and contractual obligations.",
#         "icon": "clipboard",
#     }
# ]


# def outcomes_showcase() -> rx.Component:
#     """Central outcomes showcase component with prominent display."""
#     return rx.box(
#         rx.box(
#             rx.box(
#                 rx.el.h2(
#                     "Secure by default",
#                     class_name="text-slate-12 text-lg lg:text-2xl font-semibold text-center",
#                 ),
#                 rx.el.h3(
#                     "SOC 2 compliant with enterprise-grade security and flexible deployment options.",
#                     class_name="text-slate-9 text-md lg:text-xl font-semibold text-center",
#                 ),
#                 class_name="flex flex-col gap-2 p-10 items-center justify-center",
#             ),
#             rx.box(
#                 rx.box(
#                     rx.image(src="/soc2.webp", class_name="h-24 w-auto"),
#                     rx.image(src="/databricks-partner.svg", class_name="h-24 w-auto"),
#                     class_name="flex flex-row gap-10 items-center justify-center",
#                 ),
#                 class_name="p-10 flex items-center justify-center",
#             ),
#             class_name="flex flex-col justify-center items-center h-full",
#         ),
#         class_name="h-full w-full flex flex-col justify-center items-center relative overflow-hidden lg:row-span-3 lg:col-span-1 lg:border-l lg:border-r border-slate-3 p-8 lg:p-1",
#     )

# def security_title():
#     return rx.el.section(
#         # Headings
#         rx.el.h1(
#             "Security, Compliance, and Trust at Reflex",
#             class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-4xl lg:text-5xl text-center text-transparent text-balance mx-auto break-words font-semibold",
#         ),
#         # TODO: Change this wording
#         rx.el.h2(
#             """We're committed to protecting your data through enterprise-grade security practices and full SOC 2 compliance.""",
#             class_name="max-w-full w-full font-large text-center text-slate-11 -mt-2 font-normal text-[1.25rem] mx-auto text-balance word-wrap break-words md:whitespace-pre",
#         ),
#         class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-4 lg:pb-[7.875rem]"
#         + rx.cond(
#             HostingBannerState.show_banner,
#             " lg:pt-[15.2rem] pt-[8rem]",
#             " lg:pt-[13.2rem] pt-[6rem]",
#         ),
#     )


# def security_card(
#     title: str,
#     description: str,
#     icon: str,
#     cols: str = "1",
#     class_name: str = "",
# ) -> rx.Component:
#     """Individual outcomes feature card component."""
#     return rx.box(
#         rx.box(
#             _card_header(title, icon),
#             _card_description(description),
#             class_name="flex flex-col gap-[0.875rem]",
#         ),
#         class_name=f"overflow-hidden p-8 w-full {class_name} lg:col-span-{cols} h-[13rem] lg:h-[11rem] border-slate-3",
#     )


# def _card_header(title: str, icon: str) -> rx.Component:
#     """Card header with icon and title."""
#     return rx.box(
#         get_icon(icon, class_name="!text-slate-9"),
#         rx.el.h3(title, class_name="text-slate-12 text-base font-semibold"),
#         class_name="flex flex-row items-center gap-2",
#     )


# def _card_description(description: str) -> rx.Component:
#     """Card description text."""
#     return rx.el.p(
#         description, class_name="text-slate-9 font-medium text-sm text-start"
#     )


# def security_grid() -> rx.Component:
#     """Main outcomes features grid component with responsive layout."""
#     # For small/medium screens: simple single column stack
#     mobile_layout = rx.box(
#         # All cards in simple order for mobile
#         # outcomes_showcase(),                          # Showcase
#         security_card(**trust_services_criteria[0]),  # Security
#         security_card(**trust_services_criteria[1]),  # Availability
#         security_card(**trust_services_criteria[2]),  # Confidentiality
#         security_card(**trust_services_criteria[3]),  # Processing Integrity
#         security_card(**trust_services_criteria[4]),  # Privacy
#         class_name="lg:hidden flex flex-col divide-y divide-slate-3 border border-slate-3"
#     )

#     # For large screens: complex grid layout
#     desktop_layout = rx.box(
#         # First 2 cards (Security, Availability)
#         security_card(**trust_services_criteria[0]),
#         security_card(**trust_services_criteria[1]),

#         # Insert the tall center showcase (spans 3 rows, 1 column)
#         outcomes_showcase(),

#         # Next 2 cards (Confidentiality, Processing Integrity)
#         security_card(**trust_services_criteria[2]),
#         security_card(**trust_services_criteria[3]),

#         # Privacy card (spans 2 columns, bottom row)
#         security_card(
#             **trust_services_criteria[4],
#             cols="2",
#             class_name="lg:col-span-2"
#         ),
#         class_name=(
#             "hidden lg:grid lg:grid-cols-3 lg:grid-rows-3 "
#             "w-full border border-slate-3"
#         )
#     )

#     return rx.box(
#         mobile_layout,
#         desktop_layout,
#         class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
#     )

# def security_table_header() -> rx.Component:
#     return rx.box(
#         rx.el.h3(
#             "Enterprise-Grade Security at Every Layer",
#             class_name="text-slate-12 text-3xl font-semibold text-center",
#         ),
#         rx.el.p(
#             "From data protection to privacy compliance, Reflex is built with security-first principles to meet the needs of modern teams and enterprises.",
#             class_name="text-slate-9 text-xl font-medium text-center mt-4",
#         ),
#         class_name="flex items-center justify-between text-slate-11 flex-col py-[5rem] max-w-[64.19rem] mx-auto w-full px-6 lg:border-x border-slate-3",
#     )


# def table_security() -> rx.Component:
#     return rx.table.root(
#         rx.el.style(TABLE_STYLE),
#         rx.table.header(
#             create_feature_table_header("Data Protection"),
#             class_name="relative",
#         ),
#         create_table_body(
#             *[
#                 create_feature_row(feature, desc)
#                 for feature, desc in DATA_PROTECTION_FEATURES
#             ],
#         ),
#         rx.table.header(
#             create_feature_table_header("Product Security"),
#             class_name="relative",
#         ),
#         create_table_body(
#             *[
#                 create_feature_row(feature, desc)
#                 for feature, desc in PRODUCT_SECURITY_FEATURES
#             ],
#         ),
#         rx.table.header(
#             create_feature_table_header("Enterprise Security"),
#             class_name="relative",
#         ),
#         create_table_body(
#             *[create_feature_row(feature, desc) for feature, desc in ENTERPRISE_SECURITY_FEATURES],
#         ),
#         rx.table.header(
#             create_feature_table_header("Data Privacy"),
#             class_name="relative",
#         ),
#         create_table_body(
#             *[create_feature_row(feature, desc) for feature, desc in DATA_PRIVACY_FEATURES],
#         ),
#         class_name="w-full overflow-x-auto max-w-[69.125rem] -mt-[2rem]",
#     )

# @mainpage(path="/security", title="Security - Reflex")
# def security():
#     return rx.box(
#         rx.box(
#             security_title(),
#             security_grid(),
#             rx.box(
#                 security_table_header(),
#                 table_security(),
#                 class_name="flex-col w-full  max-w-[69.125rem] desktop-only",
#             ),
#             class_name="flex flex-col relative justify-center items-center w-full",
#         ),
#         class_name="flex flex-col w-full",
#     )


"""Main security page implementation."""

import reflex as rx
from pcweb.templates.mainpage import mainpage
from .views import security_title, security_grid, features_table_section


@mainpage(path="/security", title="Security - Reflex")
def security():
    """Main security page with modular sections."""
    return rx.box(
        rx.box(
            security_title(),
            security_grid(),
            features_table_section(),
            class_name="flex flex-col relative justify-center items-center w-full",
        ),
        class_name="flex flex-col w-full",
    )
