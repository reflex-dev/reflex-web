import reflex as rx
from pcweb.components.new_button import button
from pcweb.components.hosting_banner import HostingBannerState
from pcweb.constants import (
    REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO,
    REFLEX_DOCS_URL,
)


def radial_circle(violet: bool = False) -> rx.Component:
    """Create a radial circle background image component.

    Args:
        violet: Whether to use the violet variant. Defaults to False.

    Returns:
        A Reflex image component configured as a radial circle background.

    """
    theme = "violet" if violet else ""
    return rx.fragment(
        rx.image(
            src=f"/logos/light/radial_circle{theme}.svg",
            alt="Radial circle",
            loading="lazy",
            class_name="top-0 right-0 absolute pointer-events-none z-[-1] dark:hidden",
        ),
        rx.image(
            src=f"/logos/dark/radial_circle{theme}.svg",
            alt="Radial circle",
            loading="lazy",
            class_name="dark:block hidden top-0 right-0 absolute pointer-events-none z-[-1]",
        ),
    )


def glow() -> rx.Component:
    """Radial gradient glow effect for popular card."""
    return rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="502" height="580" viewBox="0 0 502 580" fill="none">
  <path d="M0 290C0 450.163 112.377 580 251 580C389.623 580 502 450.163 502 290C502 129.837 389.623 0 251 0C112.377 0 0 129.837 0 290Z" fill="url(#paint0_radial_13685_26666)"/>
  <defs>
    <radialGradient id="paint0_radial_13685_26666" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(251 290) rotate(90) scale(290 251)">
      <stop stop-color="var(--c-violet-2)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>""",
        class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none",
    )


def grid() -> rx.Component:
    """Animated grid background for popular card."""
    return rx.html(
        """<svg width="326" height="472" viewBox="0 0 326 472" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_13685_24040)">
<mask id="mask0_13685_24040" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="-206" y="-52" width="768" height="576">
<g clip-path="url(#clip1_13685_24040)">
<line x1="178.5" y1="-52" x2="178.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="210.5" y1="-52" x2="210.5" y2="524" stroke="var(--c-slate-3)"/>
<g clip-path="url(#clip1_13685_24040)">
<line x1="178.5" y1="-52" x2="178.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="210.5" y1="-52" x2="210.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="242.5" y1="-52" x2="242.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="274.5" y1="-52" x2="274.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="306.5" y1="-52" x2="306.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="146.5" y1="-52" x2="146.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="114.5" y1="-52" x2="114.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="82.5" y1="-52" x2="82.5001" y2="524" stroke="var(--c-slate-3)"/>
<line x1="50.5" y1="-52" x2="50.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="18.5" y1="-52" x2="18.5" y2="524" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="11.5" x2="562" y2="11.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="43.5" x2="562" y2="43.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="75.5" x2="562" y2="75.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="107.5" x2="562" y2="107.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="139.5" x2="562" y2="139.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="171.5" x2="562" y2="171.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="203.5" x2="562" y2="203.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="235.5" x2="562" y2="235.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="267.5" x2="562" y2="267.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="299.5" x2="562" y2="299.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="331.5" x2="562" y2="331.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="363.5" x2="562" y2="363.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="395.5" x2="562" y2="395.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="427.5" x2="562" y2="427.5" stroke="var(--c-slate-3)"/>
<line x1="-206" y1="459.5" x2="562" y2="459.5" stroke="var(--c-slate-3)"/>
</g>
</mask>
<g mask="url(#mask0_13685_24040)">
<g filter="url(#filter0_f_13685_24040)">
<circle cx="266" cy="89" r="55" fill="light-dark(var(--c-violet-6), var(--c-violet-4))"/>
</g>
<g filter="url(#filter1_f_13685_24040)">
<circle cx="107" cy="258" r="64" fill="light-dark(var(--c-violet-6), var(--c-violet-4))"/>
</g>
<g filter="url(#filter2_f_13685_24040)">
<circle cx="265" cy="328" r="28" fill="light-dark(var(--c-violet-6), var(--c-violet-4))"/>
</g>
<g filter="url(#filter3_f_13685_24040)">
<circle cx="475" cy="174" r="64" fill="light-dark(var(--c-violet-6), var(--c-violet-4))"/>
</g>
<g filter="url(#filter4_f_13685_24040)">
<circle cx="292" cy="492" r="48" fill="light-dark(var(--c-violet-6), var(--c-violet-4))"/>
</g>
</g>
</g>
<defs>
<filter id="filter0_f_13685_24040" x="51" y="-126" width="430" height="430" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_24040"/>
</filter>
<filter id="filter1_f_13685_24040" x="-117" y="34" width="448" height="448" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_24040"/>
</filter>
<filter id="filter2_f_13685_24040" x="77" y="140" width="376" height="376" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_24040"/>
</filter>
<filter id="filter3_f_13685_24040" x="251" y="-50" width="448" height="448" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_24040"/>
</filter>
<filter id="filter4_f_13685_24040" x="84" y="284" width="416" height="416" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_24040"/>
</filter>
<clipPath id="clip0_13685_24040">
<rect width="768" height="576" fill="white" transform="translate(-206 -52)"/>
</clipPath>
<clipPath id="clip1_13685_24040">
<rect width="768" height="576" fill="white" transform="translate(-206 -52)"/>
</clipPath>
</defs>
</svg>
""",
        class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none",
    )

def _get_price_label(title: str) -> str:
    """Get the appropriate price label for each plan."""
    if title == "Free":
        return "Free"
    elif title == "Pro":
        return "From"
    else:
        return "Custom"


def _render_price_display(price: str, title: str) -> rx.Component:
    """Render the price display section with proper formatting."""
    if "user" in price:
        # Handle user-based pricing (e.g., "$49 user/month")
        parts = price.split(" ", 1)
        return rx.el.div(
            rx.el.span(parts[0], class_name="text-4xl font-bold text-slate-12"),
            rx.el.span(f"  {parts[1]}", class_name="text-sm text-slate-9 ml-2"),
            class_name="flex items-baseline",
        )
    else:
        # Handle regular pricing (e.g., "$25/month", "Custom")
        main_price = price.split("/")[0] if "/" in price else price
        period = f" / {price.split('/')[1]}" if "/" in price else ""

        return rx.el.div(
            rx.el.span(main_price, class_name="text-4xl font-bold text-slate-12"),
            rx.el.span(period, class_name="text-sm text-slate-9"),
            class_name="flex items-baseline",
        )


def _render_messaging_section(title: str) -> rx.Component:
    """Render the messaging/features section for each plan."""
    messaging_config = {
        "Free": {
            "main": "5 credits/day, 20 credits/month",
            "sub": rx.text("Filler Text", class_name="opacity-0 cursor-default"),
        },
        "Pro": {
            "main": "Reflex Build 100 msgs/month",
            "sub": rx.link(
                "Upgrade to Enterprise for more messages",
                href="#reflex-build",
                class_name="text-xs text-slate-9 hover:text-slate-11 underline",
            ),
        },
        "Enterprise": {
            "main": "Reflex Build 500+ msgs/month",
            "sub": rx.link(
                "More messages available on request",
                href="#reflex-build",
                class_name="text-xs text-slate-9 hover:text-slate-11 underline",
            ),
        },
    }

    if title in messaging_config:
        config = messaging_config[title]
        return rx.el.div(
            rx.el.p(
                config["main"], class_name="text-md font-semibold text-slate-12 mt-4"
            ),
            config["sub"] if config["sub"] else None,
        )
    return rx.el.div()


def _get_features_header(title: str) -> str:
    """Get the appropriate features section header for each plan."""
    headers = {
        "Free": "What's included:",
        "Pro": "Everything in Free, plus:",
        "Enterprise": "Everything in Pro, plus:",
    }
    return headers.get(title, "Features:")


def _render_feature_list(features: list[tuple[str, str, bool]]) -> rx.Component:
    """Render the feature list with green checks or red X's based on availability."""
    return rx.el.ul(
        *[
            rx.el.li(
                rx.icon(
                    "check" if feature[2] else "x",
                    class_name=f"!text-{'green-500' if feature[2] else 'red-500'}",
                    size=16
                ),
                rx.el.span(
                    feature[1],
                    class_name=f"text-sm font-medium {'text-slate-11' if feature[2] else 'text-slate-9 line-through'} flex-1",
                ),
                (
                    rx.tooltip(
                        rx.icon("info", class_name="!text-slate-9", size=12),
                        content=feature[3],
                    )
                    if len(feature) == 4
                    else ""
                ),
                class_name="flex items-center gap-3 mb-2",
            )
            for feature in features
        ],
        class_name="flex flex-col",
    )


def card(
    title: str,
    description: str,
    features: list[tuple[str, str, bool]],  # Added bool for included/not included
    button_text: str,
    price: str = None,
    redirect_url: str = None,
    coming_soon: bool = False,
) -> rx.Component:
    """Standard pricing card component."""
    return rx.box(
        # Header
        rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl mb-4"),
        rx.el.p(
            description, class_name="text-sm font-medium text-slate-9 mb-6 text-pretty"
        ),
        # CTA Button
        rx.cond(
            coming_soon,
            button(
                "Coming Soon",
                variant="secondary",
                size="lg",
                disabled=True,
                class_name="w-full mb-6 opacity-50 cursor-not-allowed",
            ),
            rx.link(
                button(
                    button_text,
                    variant="secondary",
                    size="lg",
                    class_name="w-full mb-6",
                ),
                href=redirect_url,
                is_external=True,
                underline="none",
            ),
        ),
        # Pricing Section
        rx.el.div(
            rx.el.span(
                _get_price_label(title), class_name="text-sm text-slate-9 block mb-1"
            ),
            _render_price_display(price, title),
            _render_messaging_section(title),
            class_name="mb-6",
        ),
        # Divider
        rx.el.hr(class_name="border-slate-3 mb-6"),
        # Features Section
        rx.el.div(
            rx.el.p(
                _get_features_header(title),
                class_name="text-sm font-medium text-slate-9 mb-4",
            ),
            _render_feature_list(features),
        ),
        class_name="flex flex-col p-6 border border-slate-4 rounded-lg shadow-small bg-slate-2 w-full min-w-0 max-w-md w-[28rem] overflow-hidden h-[46rem]",
    )


def popular_card(
    title: str,
    description: str,
    features: list[tuple[str, str, bool]],  # Added bool for included/not included
    button_text: str,
    price: str = None,
    coming_soon: bool = False,
) -> rx.Component:
    """Popular pricing card component with special styling and effects."""
    return rx.box(
        # Card Content with Background Effects
        rx.box(
            glow(),
            grid(),
            # Header
            rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl mb-4"),
            rx.el.p(
                description,
                class_name="text-sm font-medium text-slate-9 mb-6 text-pretty",
            ),
            # CTA Button
            rx.cond(
                coming_soon,
                button(
                    "Coming Soon",
                    variant="primary",
                    size="lg",
                    disabled=True,
                    class_name="w-full mb-6 !text-sm !font-semibold opacity-50 cursor-not-allowed",
                ),
                rx.link(
                    button(
                        button_text,
                        variant="primary",
                        size="lg",
                        class_name="w-full mb-6 !text-sm !font-semibold",
                    ),
                    href=REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO,
                    is_external=True,
                    underline="none",
                ),
            ),
            # Pricing Section
            rx.el.div(
                rx.el.span(_get_price_label(title), class_name="text-sm text-slate-9 block mb-1"),
                _render_price_display(price, title),
                _render_messaging_section(title),
                class_name="mb-6",
            ),
            # Divider
            rx.el.hr(class_name="border-slate-3 mb-6"),
            # Features Section
            rx.el.div(
                rx.el.p(
                    _get_features_header(title),
                    class_name="text-sm font-medium text-slate-9 mb-4",
                ),
                _render_feature_list(features),
            ),
            class_name="flex flex-col p-6 border-2 border-[--violet-9] rounded-lg w-full min-w-0 max-w-md w-[28rem] relative z-[1] backdrop-blur-[6px] bg-[rgba(249,_249,_251,_0.48)] dark:bg-[rgba(26,_27,_29,_0.48)] shadow-[0px_2px_5px_0px_rgba(28_32_36_0.03)] overflow-hidden h-[46rem]",
        ),
        class_name="relative w-full min-w-0 max-w-md w-[28rem]",
    )


def price_cards() -> rx.Component:
    """Render all three pricing plan cards following the tier structure."""

    # Define all features with their availability across tiers
    # Format: (icon, description, free_included, pro_included, enterprise_included, tooltip)
    all_features = [
        ("app-window", "Public Apps Only", True, True, False, "Free and Pro are limited to public apps"),
        ("eye-off", "Private Apps", False, False, True, "Enterprise allows private applications"),
        ("cloud", "Deploy to Reflex Cloud", True, True, True, "Available across all tiers"),
        ("github", "Github Integration (Public)", False, True, True, "Pro and Enterprise get public repo integration"),
        ("github", "Github Integration (Private)", False, False, True, "Only Enterprise supports private repositories"),
        ("download", "Download App Code", False, True, True, "Pro and Enterprise can download their app code"),
        ("badge", "'Built with Reflex' Attribution", True, False, False, "Free tier requires attribution badge"),
        ("key", "OpenAI Integration", False, True, True, "Pro and Enterprise include OpenAI integration"),
        ("mail", "Gmail Auth Integration", False, True, True, "Pro and Enterprise support Gmail authentication"),
        ("database", "Database Integration", False, True, True, "Pro and Enterprise include database support"),
        ("shield", "SSO (Okta, Azure)", False, False, True, "Enterprise-only single sign-on support"),
        ("building-2", "Databricks Integration", False, False, True, "Enterprise connects to Databricks"),
        ("server", "Private Cloud Deployment", False, False, True, "Enterprise can deploy to private cloud"),
        ("heart-handshake", "Discord/Github Support", True, True, True, "Community support available to all"),
        ("headset", "Dedicated Support Channel", False, False, True, "Enterprise gets dedicated support"),
        ("user-round-plus", "White Glove Onboarding", False, False, True, "Enterprise includes personalized onboarding"),
        ("git-pull-request", "Influence Reflex Roadmap", False, False, True, "Enterprise customers help shape the roadmap"),
    ]

    # Create feature lists for each tier
    free_features = [
        (f[0], f[1], f[2], f[5]) for f in all_features
        if f[2] or not f[2]  # Show all features for Free tier
    ][:8]  # Limit to most relevant features

    pro_features = [
        (f[0], f[1], f[3], f[5]) for f in all_features
        if f[3] or (f[2] and not f[3])  # Show included features and newly excluded ones
    ][:10]

    enterprise_features = [
        (f[0], f[1], f[4], f[5]) for f in all_features
        if f[4] or (f[3] and not f[4])  # Show included features and newly excluded ones
    ][:12]

    return rx.box(
        # Free Tier
        card(
            "Free",
            "Perfect for getting started and trying out Reflex.",
            [
                ("zap", "5 credits/day, 20 credits/month", True),
                ("eye", "Public Apps Only", True),
                ("cloud", "Deploy to Reflex Cloud", True),
                ("badge", "'Built with Reflex' Attribution", True),
                ("heart-handshake", "Discord/Github Support", True),
                ("github", "Github Integration", False),
                ("download", "Download App Code", False),
                ("key", "AI Integrations", False),
            ],
            "Start for Free",
            price="Free",
            redirect_url=REFLEX_DOCS_URL,
        ),

        # Pro Tier (Popular)
        popular_card(
            "Pro",
            "Everything you need for professional development.",
            [
                ("eye", "Public Apps", True),
                ("github", "Github Integration (Public)", True),
                ("download", "Download App Code", True),
                ("key", "OpenAI Integration", True),
                ("mail", "Gmail Auth Integration", True),
                ("database", "Database Integration", True),
                ("eye-off", "Private Apps", False),
                ("github", "Private Github Repos", False),
                ("shield", "SSO Integration", False),
                ("server", "Private Cloud Deploy", False),
            ],
            "Get Started",
            price="$29/month",
            coming_soon=True,  # Add this parameter to enable "Coming Soon"
        ),

        # Enterprise Tier
        card(
            "Enterprise",
            "Tailored solutions for enterprise needs.",
            [
                ("eye-off", "Private Apps Only", True),
                ("github", "Private Github Integration", True),
                ("server", "Private Cloud Deployment", True),
                ("shield", "SSO (Okta, Azure)", True),
                ("building-2", "Databricks Integration", True),
                ("headset", "Dedicated Support", True),
                ("user-round-plus", "White Glove Onboarding", True),
                ("git-pull-request", "Influence Roadmap", True),
                ("key", "Bring Your Own AI Keys", True),
                ("circle-plus", "Everything in Pro", True),
            ],
            "Contact Sales",
            price="Custom",
            redirect_url=REFLEX_DEV_WEB_LANDING_FORM_URL_GET_DEMO,
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 items-center place-items-center [&>*:nth-child(3)]:md:col-span-2 [&>*:nth-child(3)]:lg:col-span-1 mx-auto gap-6 w-full lg:border-x border-slate-3 max-w-[80rem]",
    )

def header():
    return rx.box(
            rx.el.h3(
                "Choose the perfect plan for your needs",
                class_name="text-slate-12 text-3xl font-semibold text-center",
            ),
            rx.el.p(
                "Start free, scale as you grow, or go enterprise for maximum power",
                class_name="text-slate-9 text-xl font-semibold text-center",
            ),
            class_name="flex items-center justify-between text-slate-11 flex-col py-[4.5rem] 2xl:border-t 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full",
        )

def plan_cards():
    return rx.box(
        header(),
        price_cards(),
        class_name="flex flex-col gap-y-4 w-full "
        + rx.cond(
            HostingBannerState.show_banner,
            "pt-[8rem] lg:pt-[11rem]",
            "pt-[8rem] lg:pt-[12rem]",
        ),
    )
