import reflex as rx

from pcweb.pages.use_cases.common.social_proof import first_card, social_proof_card


def social_proof() -> rx.Component:
    return rx.el.div(
        first_card("Trusted by innovative finance teams"),
        social_proof_card("man_group"),
        social_proof_card("world_bank"),
        social_proof_card("credit_agricole"),
        social_proof_card("bayesline"),
        class_name="grid lg:grid-cols-6 grid-cols-1 justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-t max-lg:divide-y",
    )
