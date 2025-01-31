import reflex as rx
from pcweb.components.new_button import button
from pcweb.constants import REFLEX_CLOUD_URL


def radial_circle(violet: bool = False) -> rx.Component:
    """Create a radial circle background image component.

    Args:
        violet: Whether to use the violet variant. Defaults to False.

    Returns:
        A Reflex image component configured as a radial circle background.

    """
    theme = "violet" if violet else ""
    return rx.image(
        src=rx.color_mode_cond(
            light=f"/logos/light/radial_circle{theme}.svg",
            dark=f"/logos/dark/radial_circle{theme}.svg",
        ),
        alt="Radial circle",
        loading="lazy",
        class_name="top-0 right-0 absolute pointer-events-none z-[-1]",
    )


def glow() -> rx.Component:
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


def card(
    title: str, description: str, features: list[tuple[str, str]], button_text: str, price: str = None
) -> rx.Component:
    return rx.box(
        rx.el.div(
            rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl"),
            rx.badge(price, color_scheme="gray", size="3") if price else rx.fragment(),
            class_name="flex items-center mb-2 gap-2",
        ),
        rx.el.p(
            description, class_name="text-sm font-medium text-slate-9 mb-8 text-pretty"
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.icon(feature[0], class_name="!text-slate-9", size=16),
                    feature[1],
                    rx.tooltip(
                            rx.icon("info", class_name="!text-slate-9", size=12),
                        content=feature[2],
                    ) if len(feature) == 3 else "",
                    class_name="text-sm font-medium text-slate-11 flex items-center gap-3",
                )
                for feature in features
            ],
            class_name="flex flex-col gap-2",
        ),
        rx.box(class_name="flex-1"),
        rx.link(
            button(
                button_text,
                variant="secondary",
                size="lg",
                class_name="w-full",
            ),
            href=(REFLEX_CLOUD_URL if button_text != "Contact sales" else "/sales"),
            is_external=True,
            underline="none",
        ),
        class_name="flex flex-col p-8 border border-slate-4 rounded-[1.125rem] shadow-small bg-slate-2 w-full min-w-[20.375rem] h-[33.5rem]",
    )


def popular_card(
    title: str, description: str, features: list[tuple[str, str]], button_text: str, price: str = None
) -> rx.Component:
    return rx.box(
        rx.box(
            "Most popular",
            class_name="absolute top-[-0.75rem] left-8 rounded-md bg-[--violet-9] h-[1.5rem] text-sm font-medium text-center px-2 flex items-center justify-center text-[#FCFCFD] z-[10]",
        ),
        rx.box(
            glow(),
            grid(),
            rx.hstack(
                rx.el.h3(title, class_name="font-semibold text-slate-12 text-2xl"),
                rx.badge(price, color_scheme="violet", size="3") if price else rx.fragment(),
                class_name="flex items-center mb-2 gap-2",
            ),
            rx.el.p(description, class_name="text-sm font-medium text-slate-9 mb-8"),
            rx.el.ul(
                *[
                    rx.el.li(
                        rx.icon(feature[0], class_name="!text-violet-9", size=16),
                        feature[1],
                        rx.tooltip(
                            rx.icon("info", class_name="!text-slate-9", size=12),
                            content=feature[2],
                        ) if len(feature) == 3 else "",
                        class_name="text-sm font-medium text-slate-11 flex items-center gap-3",
                    )
                    for feature in features
                ],
                class_name="flex flex-col gap-2",
            ),
            rx.box(class_name="flex-1"),
            rx.link(
                button(
                    button_text,
                    variant="primary",
                    size="lg",
                    class_name="w-full !text-sm !font-semibold",
                ),
                href=f"{REFLEX_CLOUD_URL}/?redirect_url={REFLEX_CLOUD_URL}/billing/",
                is_external=True,
                underline="none",
            ),
            class_name="flex flex-col p-8 border border-[--violet-9] rounded-[1.125rem] w-full min-w-[20.375rem] h-[33.5rem] relative z-[1] backdrop-blur-[6px] bg-[rgba(249,_249,_251,_0.48)] dark:bg-[rgba(26,_27,_29,_0.48)] shadow-[0px_2px_5px_0px_rgba(28_32_36_0.03)] overflow-hidden",
        ),
        class_name="relative",
    )


def plan_cards() -> rx.Component:
    return rx.box(
        card(
            "Hobby",
            "Everything you need to get started.",
            [
                ("heart-handshake", "Community support"),
                ("app-window", "Unlimited apps", "Free users are limited to 20 hours of 1 vCPU, 1 GB RAM  machines per month."),
                ("clock", "1 day log retention"),
                ("code", "Open Source Framework"),
                ("file-code", "Starter Templates"),
            ],
            "Start building for free",
            price="Free",
        ),
        popular_card(
            "Pro",
            "For professional projects and startups.",
            [   
                ("heart-handshake", "Priority Community support"),
                ("users", "1 seat incl. (additional seats at $20/mo)"),
                ("credit-card", "$10 / month free compute credits"),
                ("server", "Customize machine sizes"),
                ("clock", "30 days log retention"),
                ("globe", "Multi-region"),
                ("brush", "Custom domains"),
                ("file-badge", "Remove Branding", "Check out the Reflex Branding doc page to learn how to remove the 'Built with Reflex' badge from your app."),
                ("circle-plus", "Everything in Hobby"),
            ],
            "Start with Pro plan",
            price="$20/mo + compute",
        ),
        card(
            "Team",
            "For teams looking to scale their applications.",
            [
                ("mail", "Email/Slack support"),
                ("users", "5 seat incl. (additional seats available)"),
                ("credit-card", "Monthly free compute credits"),
                ("git-branch", "Create multiple projects"),
                ("signal", "Full Website Analytics"),
                ("lock-keyhole", "One Click Auth"),
                ("file-badge", "Remove Branding Everywhere", "Check out the Remove Reflex Branding section in the Self Hosting doc page to learn how to remove the 'Built with Reflex' badge from your app."),
                ("circle-plus", "Everything in Pro"),
            ],
            "Contact sales",
        ),
        card(
            "Enterprise",
            "Get a plan tailored to your business needs.",
            [
                ("headset", "Dedicated Support"),
                ("users", "Customized seat amount"),
                ("user-round-plus", "Personalized integration help"),
                ("hard-drive", "On Premise Deployment"),
                ("clock", "Unlimited log retention"),
                ("activity", "Error Monitoring and Observability"),
                ("git-pull-request", "Influence Reflex Roadmap"),
                ("shield-check", "Audit logs, SSO, SOC2 Reports"),
                ("circle-plus", "Everything in Team"),
            ],
            "Contact sales",
        ),
        class_name="grid 2xl:grid-cols-4 xl:grid-cols-2 sm:grid-cols-1 gap-4",
    )
