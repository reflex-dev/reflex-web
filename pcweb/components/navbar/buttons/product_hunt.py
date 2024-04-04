import reflex as rx

from .style import button_style


def product_hunt():
    return rx.link(
        rx.image(src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=445480&theme=light", 
            alt="Reflex - Build&#0032;web&#0032;apps&#0032;in&#0032;Pure&#0032;Python&#0032;10x&#0032;faster | Product Hunt",
            height="38px",
            width="190px",
            style={"box_shadow": button_style["box_shadow"]},
        ),
        href="https://www.producthunt.com/posts/reflex-6?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-reflex&#0045;6",
        is_external=True,
        flex_shrink="0",
        style={"@media screen and (max-width: 610px)": {"display": "none"}},
    )