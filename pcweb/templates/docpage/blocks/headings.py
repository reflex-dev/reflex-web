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
    convert_to_str: bool = False,
    style: dict = {},
    mt: str = "4",
    class_name: str = "",
) -> rx.Component:
    if convert_to_str:
        id_ = text.to(list[str])[0].lower().split(" ").join("-")
    else:
        id_ = text.lower()

    href = rx.State.router.page.full_path + "#" + id_

    return rx.link(
        rx.heading(
            text,
            id=id_,
            as_=heading,
            style=style,
            class_name=class_name + " scroll-m-[5rem] mt-" + mt,
        ),
        rx.icon(
            tag="link",
            size=18,
            class_name="!text-violet-11 invisible transition-[visibility_0.075s_ease-out] group-hover:visible mt-" + mt,
        ),
        underline="none",
        href=href,
        on_click=lambda: rx.set_clipboard(href),
        # as_child=True,
        class_name=f"flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group",
    )


@rx.memo
def h1_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        convert_to_str=True,
        class_name="font-x-large lg:font-xx-large",
    )


@rx.memo
def h1_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        convert_to_str=True,
        class_name="font-x-large lg:font-xx-large",
    )


@rx.memo
def h2_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        convert_to_str=True,
        mt="8",
        class_name="font-large lg:font-x-large",
    )


@rx.memo
def h2_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        convert_to_str=True,
        mt="8",
        class_name="font-large lg:font-x-large",
    )


@rx.memo
def h3_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        mt="4",
        convert_to_str=True,
        class_name="font-large",
    )


@rx.memo
def h3_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        convert_to_str=True,
        mt="4",
        class_name="font-large",
    )


@rx.memo
def h4_comp(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        convert_to_str=True,
        scroll_margin="6em",
        mt="2",
        class_name="font-md-smbold",
    )


@rx.memo
def h4_comp_xd(text: str) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        convert_to_str=True,
        mt="2",
        class_name="font-md-smbold",
    )
