import reflex as rx
from pcweb.pages.customers.views.bento_cards import bento_cards

def hero() -> rx.Component:
    return rx.el.section(
        rx.el.h1(
            "Hear from the teams that use Reflex",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-xx-large text-center text-transparent text-balance whitespace-pre mx-auto break-words",
        ),
        rx.el.h2(
            """Companies of all sizes trust Reflex to build internal tools and customer-facing apps""",
            class_name="max-w-full w-full font-md-smbold text-center text-slate-9 whitespace-pre mx-auto text-balance word-wrap break-words",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[2.5rem] border-t border-slate-3 pt-[2.5rem]",
    )

def landing_social_proof():
    return rx.el.div(
        hero(),
        bento_cards(),
        class_name="flex flex-col w-full justify-center items-center",
    )
