"""Template for documentation pages."""

import asyncio
import textwrap
import uuid
from typing import Callable

import black
import reflex as rx

from pcweb import styles
from pcweb.base_state import State
from pcweb.route import Route, get_path
from pcweb.components.logo import navbar_logo

class CopyToClipboard(rx.Component):
    """Component to copy text to clipboard."""

    library = "react-copy-to-clipboard"

    tag = "CopyToClipboard"

    # The text to copy when clicked.
    text: rx.Var[str]

    @classmethod
    def get_triggers(cls) -> set[str]:
        return super().get_triggers() | {"on_copy"}


# Convenience method to create the compoennt.
copy_to_clipboard = CopyToClipboard.create


@rx.memo
def code_block(
    code: str,
    language: str,
    # copied: rx.Var[bool],
    # copy_text: rx.Var[str],
    # on_copy: rx.EventChain,
):
    return rx.box(
        rx.box(
            rx.code_block(
                code,
                rx.button("Copy", bg="white", border="1px solid #EAEAEA"),
                border_radius=styles.DOC_BORDER_RADIUS,
                theme="light",
                background="transparent",
                language=language,
                show_line_numbers=True,
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",

                    }
                },
            ),
            border_radius=styles.DOC_BORDER_RADIUS,
            border = "1px solid #F4F3F6"
        ),
        position="relative",
        margin_bottom="1em",
        width="100%",
    )


@rx.memo
def code_block_dark(
    code: str,
    language: str,
    copied: bool,
    copy_text: str,
    on_copy: rx.EventChain,
):
    return rx.box(
        rx.box(
            rx.code_block(
                code,
                rx.button("Copy", bg="white", border="1px solid #EAEAEA"),
                border_radius=styles.DOC_BORDER_RADIUS,
                theme="dark",
                language=language,
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
            border_radius=styles.DOC_BORDER_RADIUS,
            box_shadow=styles.DOC_SHADOW_LIGHT,
        ),
        rx.cond(
            copied,
            rx.tooltip(
                rx.icon(
                    tag="check_circle",
                    style=icon_style,
                    color=styles.ACCENT_COLOR,
                ),
                label="Copied!",
                close_on_click=False,
                padding="0.5em",
                border_radius="0.5em",
                background_color=styles.ACCENT_COLOR,
                is_open=copied,
            ),
            rx.tablet_and_desktop(
                copy_to_clipboard(
                    rx.icon(
                        tag="copy",
                        style=icon_style,
                    ),
                    text=rx.Var.create(copy_text, is_string=True),
                    on_copy=on_copy,
                ),
            ),
        ),
        position="relative",
        margin_bottom="1em",
        width="100%",
    )


class ClipboardState(State):
    """State for the clipboard."""

    # The copied text.
    text: str = ""

    def copy(self, text: str):
        """Set the text to copy.

        Args:
            text: The text to copy.
        """
        self.text = text

    async def reset_text(self):
        """Reset the copied text."""
        # Wait in order to show the toast.
        await asyncio.sleep(2)

        # Reset the text.
        self.reset()
        self.text = ""


# Docpage styles.
icon_style = {
    "right": "1em",
    "top": "1em",
    "position": "absolute",
    "color": "gray",
    "width": "1.5em",
    "height": "1.5em",
    "_hover": {
        "cursor": "pointer",
        "color": styles.ACCENT_COLOR,
    },
}
demo_box_style = {
    "borderRadius": styles.DOC_BORDER_RADIUS,
    #"border": "1px solid #F4F3F6",
    "bg": "rgba(255,255,255, 0.5)",
    "boxShadow": styles.DOC_SHADOW_LIGHT,
    "padding": 5,
    "width": "100%",
    "overflow_x": "auto",
}
link_style = {
    "color": "#494369",
    "font_weight": "600",
    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
    "border_radius": "8px",
    "padding_x": "0.5em",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
    "_hover": {
        "box-shadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"
    },
    "fontSize": "1.2em",
}

font_sizes = [styles.H3_FONT_SIZE, styles.H3_FONT_SIZE, styles.H3_FONT_SIZE, styles.H3_FONT_SIZE]
logo_style = {
    "height": "1em",
    "opacity": 0.2,
}
logo = navbar_logo(**logo_style)


def doc_section(*contents):
    return rx.box(
        *contents,
        margin_top = "1em",
        margin_left = ".5em",
        border_left = "1px #F4F3F6 solid",
        padding_left = "1em",
        width = "100%"
        
    )



def docpage(set_path: str | None = None, t: str | None = None) -> rx.Component:
    """A template that most pages on the pynecone.io site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        prop: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """

    def docpage(contents: Callable[[], Route]) -> Route:
        """Wrap a component in a docpage template.

        Args:
            contents: A function that returns a page route.

        Returns:
            The final route with the template applied.
        """
        # Get the path to set for the sidebar.
        if set_path is None:
            path = get_path(contents)
        else:
            path = set_path

        # Set the page title.
        if t is None:
            title = f"{contents.__name__.replace('_', ' ').title()} | Reflex"
        else:
            title = t

        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.footer import footer
            from pcweb.components.navbar import navbar
            from pcweb.components.sidebar import get_prev_next
            from pcweb.components.sidebar import sidebar as sb

            # Create the docpage sidebar.
            sidebar = sb(url=path)

            # Set the sidebar path for the navbar sidebar.
            nav_sidebar = sb(url=path)

            # Get the previous and next sidebar links.
            prev, next = get_prev_next(path)
            links = []

            # Create the previous component link.
            if prev:
                links.append(
                    rx.link(
                        "← " + prev.names,
                        href=prev.link,
                        style=link_style,
                    )
                )
            else:
                links.append(rx.box())

            # Create the next component link.
            if next:
                links.append(
                    rx.link(
                        next.names + " →",
                        href=next.link,
                        style=link_style,
                    )
                )
            else:
                links.append(rx.box())

            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            # Return the templated page.
            return rx.box(
                navbar(sidebar=nav_sidebar),
                rx.box(
                    rx.flex(
                        rx.desktop_only(
                            sidebar,
                            width=["0", "0%", "25%"],
                            padding_left=styles.PADDING_X,
                            padding_y="2em",
                        ),
                        rx.box(
                            rx.box(comp),
                            rx.hstack(
                                *links,
                                justify="space-between",
                                margin_y="3em",
                            ),
                            rx.hstack(
                                logo,
                                rx.spacer(),
                                rx.text("Copyright © 2023 Pynecone, Inc.", color="#CDCCD1"), 
                                width="100%",
                            ),
                            padding_left=["1em", "2em", "5em", "8em"],
                            padding_right=styles.PADDING_X,
                            width=["100%", "100%", "100%", "75%"],
                            padding_y="2em",
                        ),
                    ),
                    max_width="80em",
                    margin_x="auto",
                    margin_top="1em",
                ),
                color=styles.DOC_TEXT_COLOR,
                background= "radial-gradient(35.39% 37.5% at 100% 0%, rgba(188, 136, 255, 0.08) 0%, rgba(255, 255, 255, 0) 100%);",
                background_attachment="fixed;",
                font="Instrument Sans",
                font_family="Inter",
            )

        # Return the route.
        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return docpage


@rx.memo
def divider_comp() -> rx.Component:
    return rx.divider(
        margin_bottom="1em",
        margin_top="0.5em",
    )


@rx.memo
def header_comp(
    text: str,
    first: bool,
) -> rx.Component:
    return rx.box(
        rx.cond(
            first,
            rx.heading(text),
            rx.heading(
                text,
                margin_top="1em",
            ),
        ),
        divider_comp(),
        color=styles.DOC_HEADER_COLOR,
        font_weight=styles.DOC_HEADING_FONT_WEIGHT,
        width="100%",
    )


def docheader(
    text: str,
    first: bool = False,
    font_size: float = None,
    coming_soon: bool = False,
    divider: bool = True,
    **props,
) -> rx.Component:
    """Style the header on a docpage.

    Args:
        text: The text to display.
        first: Whether this is the first header on the page.
        font_size: The font size to use.
        coming_soon: Whether this is a coming soon header.
        divider: Whether to show a divider below the header.
        props: Props to apply to the header.

    Returns:
        The styled header.
    """
    # Get the basic styles.
    style = {"marginTop": "1em"} if not first else {}
    if font_size:
        style["fontSize"] = font_size

    # Set the text.
    children = [rx.heading(text, style=style, **props)]

    # Add a badge if the header is coming soon.
    if coming_soon:
        children.append(
            rx.badge(
                "Coming Soon!",
                bg=styles.ACCENT_COLOR,
                color="white",
            ),
        )

    # Add a divider if needed.
    if divider:
        children.append(rx.divider())

    # Return the header.
    return rx.box(
        *children,
        id="-".join(text.lower().split()),
        color=styles.DOC_HEADER_COLOR,
        font_weight=styles.DOC_HEADING_FONT_WEIGHT,
        width="100%",
    )


def subheader_comp(
    text: rx.Var[str],
) -> rx.Component:
    return rx.box(
        rx.heading(
            text,
            margin_top="1em",
            font_size=styles.H3_FONT_SIZE,
        ),
        divider_comp(),
        color=styles.DOC_HEADER_COLOR,
        font_weight=styles.DOC_SUBHEADING_FONT_WEIGHT,
        width="100%",
    )


def subheader(
    text: str, level: int = 0, coming_soon: bool = False, divider: bool = True, **props
) -> rx.Component:
    """Create a subheader for a docpage.

    Args:
        text: The text to display.
        level: The level of the subheader.
        coming_soon: Whether this is a coming soon header.
        divider: Whether to show a divider below the header.
        props: Props to apply to the subheader.

    Returns:
        The styled subheader.
    """
    return docheader(
        text,
        font_size=font_sizes[level],
        coming_soon=coming_soon,
        divider=divider,
        color=styles.DOC_HEADER_COLOR,
        font_weight=styles.DOC_SUBHEADING_FONT_WEIGHT,
        **props,
    )


def text_comp(
    text: rx.Var[str],
) -> rx.Component:
    return rx.text(text, margin_bottom="1em", font_size=styles.TEXT_FONT_SIZE)


def doctext(*text, **props) -> rx.Component:
    """Create a documentation paragraph.

    Args:
        text: The text components to display.
        props: Props to apply to the paragraph.

    Returns:
        The styled paragraph.
    """
    return rx.box(
        *text,
        margin_bottom="1em",
        font_size=styles.TEXT_FONT_SIZE,
        width="100%",
        **props,
    )


def doccode(
    code: str,
    language: str = "python",
    lines: tuple[int, int] | None = None,
    theme: str = "light",
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        code: The code to display.
        language: The language of the code.
        lines: The start/end lines to display.
        props: Props to apply to the code snippet.

    Returns:
        The styled code snippet.
    """
    # For Python snippets, lint the code with black.
    if language == "python":
        code = black.format_str(
            textwrap.dedent(code), mode=black.FileMode(line_length=60)
        ).strip()

        # Replace "State" with "rx.State".
        code = code.replace("(State)", "(rx.State)")

    # If needed, only display a subset of the lines.
    if lines is not None:
        code = textwrap.dedent(
            "\n".join(code.strip().split("\n")[lines[0] : lines[1]])
        ).strip()

    # Remove prompt characters from the copy text.
    copy_text = code.replace("$ ", "")

    # A unique id for the code snippet.
    uid = str(uuid.uuid4())

    # Create the code snippet.
    # cb = code_block if theme == "light" else code_block_dark
    cb = code_block
    return cb(
        code=code,
        language=language,
        # copied=ClipboardState.text == uid,
        # copy_text=copy_text,
        # on_copy=lambda: [
        #     ClipboardState.copy(rx.Var.create(utils.wrap(uid, '"'))),
        #     ClipboardState.reset_text(),
        # ],
    )


def docdemobox(*children) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.box(
        rx.center(*children),
        style=demo_box_style,
    )


def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    **props,
) -> rx.Component:
    """Create a documentation demo with code and output.

    Args:
        code: The code to render the component.
        state: Code for any state needed for the component.
        comp: The pre-rendered component.
        context: Whether to wrap the render code in a function.
        props: Additional props to apply to the component.

    Returns:
        The styled demo.
    """
    # Render the component if necesssary.
    if comp is None:
        comp = eval(code)

    # Wrap the render code in a function if needed.
    if context:
        code = f"""def index():
        return {code}
        """

    # Add the state code
    if state is not None:
        code = state + code

    # Create the demo.
    return rx.vstack(
        docdemobox(comp),
        doccode(code),
        width="100%",
        padding_bottom="2em",
        spacing = "1em",
        **props,
    )


def doclink(text: str, href: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, href=href, style=styles.LINK_STYLE, **props)


def definition(title: str, *children) -> rx.Component:
    """Create a definition for a doc page.

    Args:
        title: The title of the definition.
        children: The children to display.

    Returns:
        The styled definition.
    """
    return rx.box(
        rx.heading(title, font_size="1em", margin_bottom="0.5em", font_weight="bold"),
        *children,
        padding="1em",
        border=f"1px solid {styles.ACCENT_COLOR}",
        border_radius="15px",
    )


def docalert(
    title: str = "", description: str = "", status: str = "info"
) -> rx.Component:
    """Create an alert for a doc page.

    Args:
        title: The title of the alert.
        description: The description of the alert.
        status: The status of the alert.

    Returns:
        The styled alert.
    """
    return doctext(
        rx.alert(
            rx.alert_icon(),
            rx.box(
                rx.alert_title(title),
                rx.alert_description(description),
            ),
            status=status,
        ),
    )


def docgraphing(data_example, data_rendered, description):
    return rx.fragment(
        subheader("Data"),
        description,
        doccode(data_example),
        doctext(
            "Which will render as: ",
        ),
        doccode(data_rendered),
        subheader("Examples"),
    )
