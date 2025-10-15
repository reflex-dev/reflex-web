import reflex as rx

from pcweb.pages.hosting_countdown.animated_box import (
    deploy_box,
    terminal_box,
    typing_text_script,
)


def grid() -> rx.Component:
    return rx.html(
        """<svg width="1028" height="320" viewBox="0 0 1028 320" fill="none" xmlns="http://www.w3.org/2000/svg">
<mask id="mask0_13685_23941" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="1028" height="320">
<g clip-path="url(#clip0_13685_23941)">
<line x1="514.5" y1="-2.18557e-08" x2="514.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="546.5" y1="-2.18557e-08" x2="546.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="578.5" y1="-2.18557e-08" x2="578.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="610.5" y1="-2.18557e-08" x2="610.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="642.5" y1="-2.18557e-08" x2="642.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="674.5" y1="-2.18557e-08" x2="674.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="706.5" y1="-2.18557e-08" x2="706.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="738.5" y1="-2.18557e-08" x2="738.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="770.5" y1="-2.18557e-08" x2="770.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="802.5" y1="-2.18557e-08" x2="802.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="834.5" y1="-2.18557e-08" x2="834.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="866.5" y1="-2.18557e-08" x2="866.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="898.5" y1="-2.18557e-08" x2="898.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="930.5" y1="-2.18557e-08" x2="930.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="962.5" y1="-2.18557e-08" x2="962.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="994.5" y1="-2.18557e-08" x2="994.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="482.5" y1="-2.18557e-08" x2="482.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="450.5" y1="-2.18557e-08" x2="450.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="418.5" y1="-2.18557e-08" x2="418.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="386.5" y1="-2.18557e-08" x2="386.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="354.5" y1="-2.18557e-08" x2="354.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="322.5" y1="-2.18557e-08" x2="322.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="290.5" y1="-2.18557e-08" x2="290.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="258.5" y1="-2.18557e-08" x2="258.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="226.5" y1="-2.18557e-08" x2="226.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="194.5" y1="-2.18557e-08" x2="194.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="162.5" y1="-2.18557e-08" x2="162.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="130.5" y1="-2.18557e-08" x2="130.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="98.5" y1="-2.18557e-08" x2="98.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="66.5" y1="-2.18557e-08" x2="66.5" y2="320" stroke="var(--c-slate-3)"/>
<line x1="34.5" y1="-2.18557e-08" x2="34.5" y2="320" stroke="var(--c-slate-3)"/>
<line y1="31.5" x2="1028" y2="31.5" stroke="var(--c-slate-3)"/>
<line y1="63.5" x2="1028" y2="63.5" stroke="var(--c-slate-3)"/>
<line y1="95.5" x2="1028" y2="95.5" stroke="var(--c-slate-3)"/>
<line y1="127.5" x2="1028" y2="127.5" stroke="var(--c-slate-3)"/>
<line y1="159.5" x2="1028" y2="159.5" stroke="var(--c-slate-3)"/>
<line y1="191.5" x2="1028" y2="191.5" stroke="var(--c-slate-3)"/>
<line y1="223.5" x2="1028" y2="223.5" stroke="var(--c-slate-3)"/>
<line y1="255.5" x2="1028" y2="255.5" stroke="var(--c-slate-3)"/>
<line y1="287.5" x2="1028" y2="287.5" stroke="var(--c-slate-3)"/>
<line y1="319.5" x2="1028" y2="319.5" stroke="var(--c-slate-3)"/>
</g>
</mask>
<g mask="url(#mask0_13685_23941)">
<g filter="url(#filter0_f_13685_23941)">
<circle cx="149" cy="181" r="77" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter1_f_13685_23941)">
<circle cx="476" cy="334" r="58" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter2_f_13685_23941)">
<circle cx="750" cy="68" r="60" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter3_f_13685_23941)">
<circle cx="454" cy="88" r="28" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter4_f_13685_23941)">
<circle cx="914" cy="208" r="48" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
</g>
<defs>
<filter id="filter0_f_13685_23941" x="-108" y="-76" width="514" height="514" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="90" result="effect1_foregroundBlur_13685_23941"/>
</filter>
<filter id="filter1_f_13685_23941" x="238" y="96" width="476" height="476" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="90" result="effect1_foregroundBlur_13685_23941"/>
</filter>
<filter id="filter2_f_13685_23941" x="510" y="-172" width="480" height="480" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="90" result="effect1_foregroundBlur_13685_23941"/>
</filter>
<filter id="filter3_f_13685_23941" x="246" y="-120" width="416" height="416" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="90" result="effect1_foregroundBlur_13685_23941"/>
</filter>
<filter id="filter4_f_13685_23941" x="686" y="-20" width="456" height="456" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="90" result="effect1_foregroundBlur_13685_23941"/>
</filter>
<clipPath id="clip0_13685_23941">
<rect width="1028" height="320" fill="white"/>
</clipPath>
</defs>
</svg>
""",
        class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none w-full h-full",
    )


def animated_box() -> rx.Component:
    return rx.box(
        rx.box(
            terminal_box(),
            deploy_box(),
            # Glow
            rx.html(
                """
                <svg width="426" height="272" viewBox="0 0 426 272" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="213" cy="136" rx="213" ry="136" fill="url(#paint0_radial_12785_6973)"/>
                    <defs>
                        <radialGradient id="paint0_radial_12785_6973" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(213 136) rotate(90) scale(136 213)">
                            <stop stop-color="var(--violet-3)"/>
                            <stop offset="1" stop-color="var(--slate-1)" stop-opacity="0"/>
                        </radialGradient>
                    </defs>
                </svg>
                """,
                class_name="absolute bottom-[-6.5rem] left-1/2 transform -translate-x-1/2 w-[26.625rem] h-[6rem] flex-shrink-0 pointer-events-none",
            ),
            class_name="justify-center flex flex-col items-center max-w-[34.5rem] max-h-[17.875rem] shrink-0 relative w-full h-full overflow-hidden",
        ),
        on_mount=rx.call_script(typing_text_script()),  # On dev it will run twice
        class_name="flex items-center justify-center w-full h-[6rem] mx-auto",
    )


def deploy_animation() -> rx.Component:
    return rx.el.section(
        grid(),
        rx.box(
            rx.el.h2(
                "Deploy, manage, and scale.",
                class_name="lg:text-3xl text-xl font-semibold text-slate-12 text-balance",
            ),
            rx.el.span(
                "A complete infrastructure for your apps",
                class_name="lg:text-3xl text-xl font-semibold text-slate-9 z-[1] text-balance",
            ),
            class_name="flex flex-col text-center",
        ),
        animated_box(),
        class_name="overflow-hidden flex flex-col justify-center gap-[3.5rem] w-full h-auto max-w-[64.19rem] lg:border-x border-slate-3 lg:px-[8.5rem] lg:pt-[5.5rem] pt-12 border-b border-t relative",
    )
