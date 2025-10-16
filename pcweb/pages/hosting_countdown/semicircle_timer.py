import reflex as rx

TimeSecondsClientState = rx._x.client_state("timer", default=0)


def semicircle_timer():
    segments = [
        rx.box(
            class_name=rx.cond(
                TimeSecondsClientState.value < i,
                "timer-segment",
                "timer-segment active",
            ),
            style={"--segment-index": i},
        )
        for i in range(61)
    ]

    return rx.box(
        TimeSecondsClientState,
        rx.el.style(
            """
            .timer-segment {
                width: 0.25rem;
                height: 1.5rem;
                position: absolute;
                left: 50%;
                bottom: 0;
                transform-origin: bottom center;
                border-radius: 0.4375rem;
                transform: rotate(calc((var(--segment-index) * 3deg) - 90deg)) translateY(-15.25rem);
                background-color: var(--slate-3, #222326);
                transition: all 0.2s ease-out;
            }

            .timer-segment.active {
                background-color: var(--violet-9, #6E56CF);
                box-shadow: 0px 0px 8px 0px var(--violet-9, #6E56CF);
            }
        """
        ),
        rx.box(
            *segments,
        ),
        # Use moment with interval to update every second
        rx.moment(
            interval=1000,
            format="ss",
            on_change=TimeSecondsClientState.set_value,
            class_name="hidden pointer-events-none",
        ),
        class_name="w-[33.5rem] h-[16.625rem] relative mb-[0.75rem] z-[1] pointer-events-none",
    )


def ellipsis():
    return rx.html(
        rx.color_mode_cond(
            dark="""<svg width="616" height="373" viewBox="0 0 616 373" fill="none" xmlns="http://www.w3.org/2000/svg">
<g filter="url(#filter0_di_12917_7257)">
<mask id="path-1-inside-1_12917_7257" fill="white">
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z"/>
</mask>
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z" fill="#1A1B1D"/>
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z" stroke="#222326" stroke-width="2" mask="url(#path-1-inside-1_12917_7257)"/>
</g>
<defs>
<filter id="filter0_di_12917_7257" x="0" y="0" width="616" height="372.926" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset/>
<feGaussianBlur stdDeviation="16"/>
<feComposite in2="hardAlpha" operator="out"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.431373 0 0 0 0 0.337255 0 0 0 0 0.811765 0 0 0 0.08 0"/>
<feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_12917_7257"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_12917_7257" result="shape"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feMorphology radius="4" operator="dilate" in="SourceAlpha" result="effect2_innerShadow_12917_7257"/>
<feOffset/>
<feGaussianBlur stdDeviation="4"/>
<feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.0823958 0 0 0 0 0.0875 0 0 0 0 0.0926042 0 0 0 1 0"/>
<feBlend mode="normal" in2="shape" result="effect2_innerShadow_12917_7257"/>
</filter>
</defs>
</svg>

        """,
            light="""<svg width="616" height="373" viewBox="0 0 616 373" fill="none" xmlns="http://www.w3.org/2000/svg">
<g filter="url(#filter0_di_12790_7018)">
<mask id="path-1-inside-1_12790_7018" fill="white">
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z"/>
</mask>
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z" fill="#F9F9FB"/>
<path d="M582.029 340.926C586.668 302.32 583.097 263.17 571.55 226.041C560.004 188.911 540.742 154.641 515.027 125.474C489.313 96.3078 457.726 72.904 422.336 56.7962C386.946 40.6884 348.551 32.2401 309.669 32.005C270.786 31.7699 232.293 39.7533 196.71 55.432C161.128 71.1107 129.26 94.1308 103.195 122.984C77.1295 151.837 57.4549 185.873 45.4602 222.86C33.4655 259.847 29.4214 298.951 33.5929 337.61L73.4144 333.313C69.8482 300.264 73.3055 266.835 83.5595 235.215C93.8136 203.596 110.633 174.499 132.916 149.833C155.199 125.167 182.442 105.488 212.86 92.0842C243.279 78.6808 276.187 71.856 309.427 72.0569C342.667 72.2579 375.489 79.4802 405.743 93.2504C435.998 107.021 463.001 127.028 484.984 151.962C506.967 176.896 523.433 206.193 533.304 237.934C543.175 269.676 546.228 303.144 542.262 336.148L582.029 340.926Z" stroke="#E8E8EC" stroke-width="2" mask="url(#path-1-inside-1_12790_7018)"/>
</g>
<defs>
<filter id="filter0_di_12790_7018" x="0" y="0" width="616" height="372.926" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset/>
<feGaussianBlur stdDeviation="16"/>
<feComposite in2="hardAlpha" operator="out"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.431373 0 0 0 0 0.337255 0 0 0 0 0.811765 0 0 0 0.08 0"/>
<feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_12790_7018"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_12790_7018" result="shape"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feMorphology radius="4" operator="dilate" in="SourceAlpha" result="effect2_innerShadow_12790_7018"/>
<feOffset/>
<feGaussianBlur stdDeviation="4"/>
<feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.988235 0 0 0 0 0.988235 0 0 0 0 0.992157 0 0 0 1 0"/>
<feBlend mode="normal" in2="shape" result="effect2_innerShadow_12790_7018"/>
</filter>
</defs>
</svg>
""",
        ),
        class_name="absolute flex justify-center items-center mb-[0.75rem] top-[10.35rem] pointer-events-none",
    )
