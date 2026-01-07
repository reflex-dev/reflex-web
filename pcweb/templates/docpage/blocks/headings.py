"""Template for documentation pages."""

import reflex as rx

icon_margins = {
    "h1": "10px",
    "h2": "5px",
    "h3": "2px",
    "h4": "0px",
}


def h_comp_common(
    text: str,
    heading: str,
    style: dict | None = None,
    mt: str = "4",
    class_name: str = "",
) -> rx.Component:
    id_ = text.lower().split(" ").join("-")
    href = rx.State.router.page.full_path + "#" + id_

    return rx.link(
        rx.heading(
            text,
            id=id_,
            as_=heading,
            style=style if style is not None else {},
            class_name=class_name + " scroll-m-[5rem] mt-" + mt,
        ),
        rx.icon(
            tag="link",
            size=18,
            class_name="!text-violet-11 invisible transition-[visibility_0.075s_ease-out] group-hover:visible mt-"
            + mt,
        ),
        underline="none",
        href=href,
        on_click=lambda: rx.set_clipboard(href),
        # as_child=True,
        class_name="flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group",
    )


@rx.memo
def h1_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        class_name="font-x-large lg:font-xx-large",
    )


@rx.memo
def h1_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        class_name="font-x-large lg:font-xx-large",
    )


@rx.memo
def h2_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        mt="8",
        class_name="font-large lg:font-x-large",
    )


@rx.memo
def h2_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        mt="8",
        class_name="font-large lg:font-x-large",
    )


@rx.memo
def h3_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        mt="4",
        class_name="font-large",
    )


@rx.memo
def h3_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        mt="4",
        class_name="font-large",
    )


@rx.memo
def h4_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        mt="2",
        class_name="font-md-smbold",
    )


@rx.memo
def h4_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        mt="2",
        class_name="font-md-smbold",
    )


@rx.memo
def img_comp_xd(src: str) -> rx.Component:
    return rx.image(
        src=src,
        class_name="rounded-lg border border-secondary-a4 mb-2",
    )
