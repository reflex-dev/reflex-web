import reflex as rx


def pattern_1() -> rx.Component:
    return rx.html(
        """
<svg width="1319" height="821" viewBox="0 0 1319 821" fill="none" xmlns="http://www.w3.org/2000/svg">
<g opacity="0.48" filter="url(#filter0_f_13685_26547)">
<path d="M178.56 318.045C69.0006 76.0001 -27.8837 6.62419 647.928 137.846C910.499 188.829 1430.13 -59.7894 1175 238C999.596 442.731 1180 344 1234 522C1255.21 591.912 1279 857 1022 699C962.219 662.247 591.448 673.823 392.795 727.42C194.141 781.018 103.578 707.09 75.3383 573.096C47.0983 439.102 254.184 485.118 178.56 318.045Z" stroke="var(--c-violet-7)" stroke-width="16"/>
</g>
<defs>
<filter id="filter0_f_13685_26547" x="0.675781" y="0.454468" width="1317.53" height="819.985" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="32" result="effect1_foregroundBlur_13685_26547"/>
</filter>
</defs>
</svg>

        """,
        class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none",
    )


def preview() -> rx.Component:
    return rx.box(
        pattern_1(),
        rx.image(
            src=rx.color_mode_cond(
                light="/hosting/light/hosting-preview.jpg",
                dark="/hosting/dark/hosting-preview.jpg",
            ),
            alt="Reflex Hosting Preview",
            class_name="w-full h-full rounded-lg lg:rounded-2xl object-cover bg-center border border-slate-3",
            loading="lazy",
        ),
        class_name="w-full h-full max-w-[71rem] max-h-[41rem] rounded-[2rem] backdrop-blur-[6px] bg-[rgba(26, 27, 29, 0.48)] lg:p-4 lg:border border-slate-3 relative lg:mt-0 mt-[3.5rem]",
    )
