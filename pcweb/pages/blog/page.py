import reflex as rx
from pcweb.flexdown import xd2 as xd

def back(title, url):
    def create_linkedin_share_url(path):
        """Create a LinkedIn share URL."""
        encoded_url = "https://reflex.dev" + (path if path.startswith('/') else '/' + path)
        encoded_url = encoded_url.replace(':', '%3A').replace('/', '%2F') + ('' if encoded_url.endswith('%2F') else '%2F')
        return f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"
        

    return rx.flex(
        rx.link(
            "<- Back to Blog", 
            color="#6C6C81", 
            margin_bottom="2em",
            underline="hover",
            href="/blog",
        ),
        rx.link(
            rx.image(src="/companies/dark/twitter.svg", height="2em"),
            href=f"https://twitter.com/intent/tweet?text={title}&url=https://reflex.dev{url}&via=getreflex",        
        ),
        rx.link(
            rx.image(src="/companies/dark/linkedin.svg", height="2em"),
            href=create_linkedin_share_url(url),
            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/yc.svg", height="2em"),
            href=f"https://news.ycombinator.com/submitlink?u=https://reflex.dev{url}&t={title}",            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/reddit.svg", height="2em"),
            href=f"https://www.reddit.com/submit?url=https://reflex.dev{url}&title={title}",
            is_external=True,
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
        spacing = "2",
        direction="column",
        z_index=1,
        position="fixed",
        top="300px",
        left="15px",
        margin=0,
        width="auto",
    )

def page(document, route) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.vstack(
        back(meta["title"], route),
        rx.container(
            rx.vstack(
                    rx.hstack(
                        rx.flex(
                            rx.chakra.text(
                                "Blog posts", 
                                background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                                text_align="center",
                                background_clip="text",
                                padding_x="1em"
                            ),
                            border_radius= "15px;",
                            border= "1px solid #4435D4;",
                            background= "linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                            box_shadow= "0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);"
                        ),
                        rx.text(str(meta["date"]), color="#6C6C81")
                    ),
                    rx.chakra.text(
                        meta["title"], 
                        font_size="2em",
                        background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                        text_align="center",
                        background_clip="text",
                        font_weight="bold",
                        letter_spacing= "-1.28px;",
                        line_height="1.2",
                    ),
                    align_items="center",
                    text_align="left",
                    width="100%",
                    spacing="1",
            ),
            rx.center(
                rx.image(
                    src=f"{meta['image']}",
                    margin_top="1em",
                    border_radius="8px",
                    padding_bottom="1em",
                ),
                width="100%",
            ),
            align="center",
            border_radius= "40px 40px 0px 0px;",
            background= "linear-gradient(180deg, #0F0E12 0%, rgba(0, 0, 0, 0.00) 100%);",
            mix_blend_mode="plus-lighter;",
            padding_x=["1em", "1em", "4em", "4em", "4em", "4em"],
            padding_top="4em",
            margin_x="auto",
            size="2",
            max_width=["100vw", "100vw","100%","100%","100%","100%"]
        ),
        rx.theme(
            rx.container(
                xd.render(document, "blog.md"),
                margin_x="auto",
                padding_bottom="4em",
                size="2",
                overflow="hidden",
                background="#131217",
                max_width=["90vw", "90vw","100%","100%","100%","100%"]
            ),
            appearance="dark",
        )
    )
