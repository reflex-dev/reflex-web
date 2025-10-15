import reflex as rx

from pcweb.components.icons import get_icon
from pcweb.components.new_button import button
from pcweb.pages.docs import hosting


def grid() -> rx.Component:
    return rx.html(
        """<svg width="1028" height="670" viewBox="0 0 1028 670" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_13685_23957)">
<mask id="mask0_13685_23957" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="1028" height="670">
<g clip-path="url(#clip1_13685_23957)">
<line x1="514.5" y1="-2.18557e-08" x2="514.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="546.5" y1="-2.18557e-08" x2="546.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="578.5" y1="-2.18557e-08" x2="578.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="610.5" y1="-2.18557e-08" x2="610.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="642.5" y1="-2.18557e-08" x2="642.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="674.5" y1="-2.18557e-08" x2="674.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="706.5" y1="-2.18557e-08" x2="706.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="738.5" y1="-2.18557e-08" x2="738.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="770.5" y1="-2.18557e-08" x2="770.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="802.5" y1="-2.18557e-08" x2="802.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="834.5" y1="-2.18557e-08" x2="834.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="866.5" y1="-2.18557e-08" x2="866.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="898.5" y1="-2.18557e-08" x2="898.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="930.5" y1="-2.18557e-08" x2="930.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="962.5" y1="-2.18557e-08" x2="962.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="994.5" y1="-2.18557e-08" x2="994.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="482.5" y1="-2.18557e-08" x2="482.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="450.5" y1="-2.18557e-08" x2="450.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="418.5" y1="-2.18557e-08" x2="418.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="386.5" y1="-2.18557e-08" x2="386.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="354.5" y1="-2.18557e-08" x2="354.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="322.5" y1="-2.18557e-08" x2="322.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="290.5" y1="-2.18557e-08" x2="290.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="258.5" y1="-2.18557e-08" x2="258.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="226.5" y1="-2.18557e-08" x2="226.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="194.5" y1="-2.18557e-08" x2="194.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="162.5" y1="-2.18557e-08" x2="162.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="130.5" y1="-2.18557e-08" x2="130.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="98.5" y1="-2.18557e-08" x2="98.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="66.5" y1="-2.18557e-08" x2="66.5" y2="670" stroke="var(--c-slate-3)"/>
<line x1="34.5" y1="-2.18557e-08" x2="34.5" y2="670" stroke="var(--c-slate-3)"/>
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
<line y1="351.5" x2="1028" y2="351.5" stroke="var(--c-slate-3)"/>
<line y1="383.5" x2="1028" y2="383.5" stroke="var(--c-slate-3)"/>
<line y1="415.5" x2="1028" y2="415.5" stroke="var(--c-slate-3)"/>
<line y1="447.5" x2="1028" y2="447.5" stroke="var(--c-slate-3)"/>
<line y1="479.5" x2="1028" y2="479.5" stroke="var(--c-slate-3)"/>
<line y1="511.5" x2="1028" y2="511.5" stroke="var(--c-slate-3)"/>
<line y1="543.5" x2="1028" y2="543.5" stroke="var(--c-slate-3)"/>
<line y1="575.5" x2="1028" y2="575.5" stroke="var(--c-slate-3)"/>
<line y1="607.5" x2="1028" y2="607.5" stroke="var(--c-slate-3)"/>
<line y1="639.5" x2="1028" y2="639.5" stroke="var(--c-slate-3)"/>
</g>
</mask>
<g mask="url(#mask0_13685_23957)">
<g filter="url(#filter0_f_13685_23957)">
<circle cx="490" cy="141" r="55" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter1_f_13685_23957)">
<circle cx="331" cy="310" r="64" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter2_f_13685_23957)">
<circle cx="699" cy="226" r="64" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
<g filter="url(#filter3_f_13685_23957)">
<circle cx="533" cy="475" r="48" fill="light-dark(var(--c-violet-7), var(--c-violet-5))"/>
</g>
</g>
</g>
<defs>
<filter id="filter0_f_13685_23957" x="275" y="-74" width="430" height="430" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_23957"/>
</filter>
<filter id="filter1_f_13685_23957" x="107" y="86" width="448" height="448" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_23957"/>
</filter>
<filter id="filter2_f_13685_23957" x="475" y="2" width="448" height="448" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_23957"/>
</filter>
<filter id="filter3_f_13685_23957" x="325" y="267" width="416" height="416" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="80" result="effect1_foregroundBlur_13685_23957"/>
</filter>
<clipPath id="clip0_13685_23957">
<rect width="1028" height="670" fill="white"/>
</clipPath>
<clipPath id="clip1_13685_23957">
<rect width="1028" height="670" fill="white"/>
</clipPath>
</defs>
</svg>
""",
        class_name="shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[-2] pointer-events-none w-full h-full ml-[-2px] mt-[1px]",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                get_icon(icon, class_name="!text-slate-12 !size-5"),
                rx.text(title, class_name="text-slate-12 text-base font-medium"),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.text(
                description, class_name="text-slate-9 font-medium text-sm text-start"
            ),
            class_name="flex flex-col gap-2 w-[22rem] h-[8rem] px-8 py-5",
        ),
        class_name="border-slate-3 border-b box-border",
    )


def features() -> rx.Component:
    return rx.el.section(
        # TODO: Fill with updated comments
        grid(),
        rx.box(
            rx.box(
                feature_card(
                    "backend_db",
                    "Build and deploy",
                    "Deploy and scale your Reflex app with a single command.",
                ),
                feature_card(
                    "infinity",
                    "Integrate with CI/CD",
                    "Deploy via GitHub Actions, GitLab CI, or your own custom pipeline.",
                ),
                feature_card(
                    "globe",
                    "Scale to multiple regions",
                    "Deploy your app to multiple regions for high availability and low latency.",
                ),
                rx.box(class_name="h-[4rem]"),
                class_name="flex flex-col pt-8 lg:border-r border-slate-3",
            ),
            rx.box(
                feature_card(
                    "backend_auth",
                    "Add team members",
                    "Invite team members to your Reflex app and manage their permissions.",
                ),
                feature_card(
                    "analytics",
                    "Get alerts and metrics",
                    "Get alerts and metrics for your Reflex app to help you monitor and optimize your app.",
                ),
                class_name="flex flex-col -mt-[32px]",
            ),
            class_name="flex lg:flex-row flex-col justify-center items-center",
        ),
        rx.link(
            button("Start deploying", variant="primary", size="xl"),
            href=hosting.deploy_quick_start.path,
            is_external=True,
            class_name="p-2 border border-slate-3 rounded-[1.375rem] border-solid lg:mt-0 mt-4",
        ),
        class_name="flex flex-col justify-center items-center max-w-[64.19rem] lg:border-x border-slate-3 w-full mx-auto lg:pb-[5.5rem] pb-4 relative overflow-hidden",
    )
