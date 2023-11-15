"""Template for documentation pages."""

import inspect
import textwrap
from typing import Any, Callable

import black
import reflex as rx

from pcweb import styles
from pcweb.styles import colors as c
from pcweb.styles import text_colors as tc
from pcweb.styles import font_weights as fw

from pcweb.base_state import State
from pcweb.route import Route, get_path
from pcweb.components.logo import navbar_logo

 

@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx.box(
            rx.code_block(
                code,
                border_radius=styles.DOC_BORDER_RADIUS,
                theme="light",
                background="transparent",
                language=language,
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ),
            border_radius=styles.DOC_BORDER_RADIUS,
            border="2px solid #F4F3F6",
        ),
        position="relative",
        margin_bottom="1em",
        width="100%",
    )


@rx.memo
def code_block_memo(children: str, language: str):
    return rx.box(
        rx.box(
            rx.code_block(
                language=language,
                border_radius=styles.DOC_BORDER_RADIUS,
                theme="light",
                background="transparent",
                code_tag_props={
                    "style": {
                        "fontFamily": "inherit",
                    }
                },
            ).set(
                special_props={
                    rx.Var.create_safe("children={children}"),
                }
            ),
            border_radius=styles.DOC_BORDER_RADIUS,
            border="2px solid #F4F3F6",
        ),
        position="relative",
        margin_bottom="1em", 
        width="100%",
    )       


def code_block2(*_, **props):
    language = props.get("language", "none")
    return code_block_memo(children="", language=language)


# Docpage styles.
demo_box_style = {
    "bg": "rgba(255,255,255, 0.5)",
    "border_radius": "8px;",
    "box_shadow": "rgba(99, 99, 99, 0.1) 0px 2px 8px 0px;",
    "padding": 5,
    "width": "100%",
    "overflow_x": "auto",
    "border": "2px solid #F4F3F6",
    "align_items": "center",
    "justify_content": "center",
}
link_style = {
    "color": "#494369",
    "font_weight": "600",
    "box_shadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
    "background": "radial-gradient(82.06% 100% at 50% 100%, rgba(91, 77, 182, 0.04) 0%, rgba(234, 228, 253, 0.2) 100%), #FEFEFF;",
    "_hover": {
        "boxShadow": "0px 0px 0px 3px rgba(149, 128, 247, 0.6), 0px 2px 3px rgba(3, 3, 11, 0.2), 0px 4px 8px rgba(3, 3, 11, 0.04), 0px 4px 10px -2px rgba(3, 3, 11, 0.02), inset 0px 2px 0px rgba(255, 255, 255, 0.01), inset 0px 0px 0px 1px rgba(32, 17, 126, 0.4), inset 0px -20px 12px -4px rgba(234, 228, 253, 0.36);"
    },
    "padding_x": "0.5em",
    "border_radius": "8px",
}

logo_style = {
    "height": "1em",
    "opacity": 0.2,
}
logo = navbar_logo(**logo_style)


def doc_section(*contents):
    return rx.box(
        *contents,
        margin_top="1em",
        margin_left=".5em",
        border_left="1px #F4F3F6 solid",
        padding_left="1em",
        width="100%",
    )

def my_form():
    from pcweb.components.navbar import NavbarState
    return rx.form(
        rx.text_area(
            placeholder="Your Feedback",
            id="feedback",
            margin="0.25em 0.5em",
            width="24em",
            border_color="#eaeaef",
        ),
        rx.center(
            rx.button(
                "Send",
                type_="submit",
                style=styles.ACCENT_BUTTON,
                margin="0.5em",
            ),
            width="100%"
        ),
        on_submit=NavbarState.handle_submit,
        width="25em",
    )

class Rating(rx.Component):
    """Spline component."""

    library = "@smastrom/react-rating"
    tag = "Rating"

    value: rx.Var[int]

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0: [e0],
        }
    


rating = Rating.create


def feedback_button():
    from pcweb.components.navbar import NavbarState, hover_button_style
    return rx.hstack(
        rx.menu(
            rx.hstack(
                rx.text("Feedback", style=styles.NAV_TEXT_STYLE, padding="0.2em", font_size="1em"),
                rating(
                    value=NavbarState.page_score,
                    on_change=NavbarState.update_score,
                ),
                width="5em",
                height="1em",
            ),
            rx.menu_list(my_form()),
        ),
        box_shadow="0px 0px 0px 1px rgba(84, 82, 95, 0.14), 0px 1px 2px rgba(31, 25, 68, 0.14);",
        padding_x=".5em",
        height="2em",
        border_radius="8px",
        bg="#FFFFFF",
        style=hover_button_style,
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
                next_prev_name = (
                    prev.alt_name_for_next_prev
                    if prev.alt_name_for_next_prev
                    else prev.names
                )
                links.append(
                    rx.link(
                        "← " + next_prev_name,
                        href=prev.link,
                        style=link_style,
                    )
                )   
            else:   
                links.append(rx.box())

            # Create the next component link.
            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.link(
                        next_prev_name + " →",
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
                            rx.spacer(),
                            rx.center(
                                feedback_button(),
                                width="100%",
                            ),
                            rx.box(height="2em"),
                            rx.hstack(
                                logo,
                                rx.spacer(),
                                rx.text(
                                    "Copyright © 2023 Pynecone, Inc.", color="#CDCCD1"
                                ),
                                width="100%",
                            ),
                            padding_left=["1em", "2em", "5em", "8em"],
                            padding_right=styles.PADDING_X,
                            width=["100%", "100%", "100%", "75%"],
                            padding_y="2em",
                            height="100%",
                        ),
                    ),
                    max_width="80em",
                    margin_x="auto",
                    margin_top="1em",
                    height="100%",
                ),
                color=tc["docs"]["body"],
                background="radial-gradient(35.39% 37.5% at 100% 0%, rgba(188, 136, 255, 0.08) 0%, rgba(255, 255, 255, 0) 100%)",
                background_attachment="fixed",
                font_family=styles.SANS,
            )

        # Return the route.
        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return docpage


@rx.memo
def text_comp(text: rx.Var[str]) -> rx.Component:
    return rx.text(text, margin_bottom="1em", font_size=styles.TEXT_FONT_SIZE)


@rx.memo
def code_comp(text: rx.Var[str]) -> rx.Component:
    return rx.code(text, color="#1F1944", bg="#EAE4FD")


def docheader(
    text: str,
    first: bool = False,
    **props,
) -> rx.Component:
    """Style the header on a docpage.

    Args:
        text: The text to display.
        first: Whether this is the first header on the page.
        font_size: The font size to use.
        props: Props to apply to the header.

    Returns:
        The styled header.
    """
    # id_ = "-".join(text.lower().split())
    # href = State.current_page + "#" + id_

    # Return the header.
    return rx.box(
        rx.heading(text, **props),
        rx.divider(margin_y="1em"),
        margin_top="0em" if first else "1.5em",
        color=tc["docs"]["header"],
        font_weight=fw["heading"],
        width="100%",
    )
    return rx.box(
        rx.link(
            rx.hstack(
                rx.heading(text, id=id_, **props),
                rx.icon(
                    tag="link",
                    color="#696287",
                    _hover={
                        "color": styles.ACCENT_COLOR,
                    },
                ),
                margin_top="0em" if first else "1.5em",
                align_items="center",
            ),
            _hover={
                "cursor": "pointer",
                "textDecoration": "none",
            },
            href=href,
            on_click=lambda: rx.set_clipboard(href),
        ),
        rx.divider(margin_y="1em"),
        color=tc["docs"]["header"],
        font_weight=fw["heading"],
        width="100%",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return rx.box(
        rx.heading(
            text,
            as_="h1",
            font_size=styles.H1_FONT_SIZE,
            font_weight=fw["heading"],
        ),
        rx.divider(margin_y="1em"),
        color=tc["docs"]["header"],
        width="100%",
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return rx.box(
        rx.heading(
            text,
            as_="h2",
            font_size=styles.H3_FONT_SIZE,
            font_weight=fw["subheading"],
        ),
        rx.divider(margin_y="1em"),
        margin_top="1.5em",
        color=tc["docs"]["header"],
        width="100%",
    )


@rx.memo
def h3_comp(text: rx.Var[str]) -> rx.Component:
    return rx.box(
        rx.heading(
            text,
            as_="h3",
            font_size=styles.H4_FONT_SIZE,
            font_weight=fw["subheading"],
        ),
        rx.divider(margin_y="1em"),
        margin_top="1.5em",
        color=tc["docs"]["header"],
        width="100%",
    )


def subheader(text: str, level: int = 0, **props) -> rx.Component:
    """Create a subheader for a docpage.

    Args:
        text: The text to display.
        level: The level of the subheader.
        props: Props to apply to the subheader.

    Returns:
        The styled subheader.
    """
    return docheader(
        text,
        font_size=styles.H2_FONT_SIZE,
        color=tc["docs"]["header"],
        font_weight=fw["subheading"],
        **props,
    )


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

    # Create the code snippet.
    cb = code_block
    return cb(
        code=code,
        language=language,
    )
  

def docdemobox(*children, **props) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.flex(
        *children,
        style=demo_box_style,
        **props,
    )


def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    demobox_props: dict[str, Any] | None = None,
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
    # Render the component if necessary.
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
        docdemobox(comp, **(demobox_props or {})),
        doccode(code),
        width="100%",
        padding_bottom="2em",
        spacing="1em",
        **props,
    )


def docdemo_from(
    *state_models_helpers: Any,
    component: Callable[..., rx.Component] = None,
    imports: list[str] = None,
    assignments: dict[str, Any] | None = None,
    collapsible_code: bool = False,
    demobox_props: dict[str, Any] | None = None,
    **props,
):
    """Create a documentation demo from a component and state.
    
    Reading the source code from the given objects and rendering the component
    above it.
    
    Args:
        *state_and_models: The state and any models to read.
        component: The component to render.
    """
    if imports is None:
        imports = []
    if "import reflex as rx" not in imports:
        imports.append("import reflex as rx")
    if assignments is None:
        assignments = {}
    state = "\n\n".join(
        [
            "\n".join(imports),
            "\n".join(f"{k} = {v}" for k, v in assignments.items()),
            *(
                inspect.getsource(obj).replace("(State)", "(rx.State)")
                for obj in state_models_helpers
            ),
        ]
    )
    code = inspect.getsource(component) if component is not None else ""
    if not collapsible_code:
        if component is not None:
            return docdemo(
                code=code,
                state=state,
                comp=component(),
                demobox_props=demobox_props,
                **props,
            )
        return doccode(state)

    # collabsible code
    return rx.vstack(
        docdemobox(
            component(),
            **(demobox_props or {}),
        ) if component is not None else rx.fragment(),
        rx.accordion(
            rx.accordion_item(
                rx.accordion_button(
                    rx.text("View Code"),
                    rx.accordion_icon(),
                ),
                rx.accordion_panel(doccode(state + code), width="100%"),
            ),
            allow_toggle=True,
            width="100%",
        ),
        width="100%",
        padding_bottom="2em",
        spacing="1em",
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


def doclink2(text: str, **props) -> rx.Component:
    """Create a styled link for doc pages.

    Args:
        text: The text to display.
        href: The link to go to.
        props: Props to apply to the link.

    Returns:
        The styled link.
    """
    return rx.link(text, style=styles.LINK_STYLE, **props)


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
        border=styles.DOC_BORDER,
        border_radius=styles.DOC_BORDER_RADIUS,
        _hover={
            "box_shadow": styles.DOC_SHADOW_LIGHT,
            "border": f"2px solid {c['violet'][200]}",
        },
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


tab_style = {
    "color": "#494369",
    "font_weight": 600,
    "_selected": {
        "color": "#5646ED",
        "bg": "#F5EFFE",
        "padding_x": "0.5em",
        "padding_y": "0.25em",
        "border_radius": "8px",
    },
}
 
 
def docgraphing(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    data: str | None = None,
    context: bool = False,
    **props,
):
    return rx.vstack(
        rx.flex(
            comp,
            height="15em",
            style=demo_box_style,
        ),
        rx.tabs(
            rx.tab_list(
                rx.tab("Code", style=tab_style),
                rx.tab("Data", style=tab_style),
                padding_x=0,
            ),
            rx.tab_panels(
                rx.tab_panel(
                    doccode(code), width="100%", padding_x=0, padding_y=".25em"
                ),
                rx.tab_panel(
                    doccode(data), width="100%", padding_x=0, padding_y=".25em"
                ),
                width="100%",
            ),
            variant="unstyled",
            color_scheme="purple",
            align="end",
            width="100%",
            padding_top=".5em",
        ),
        width="100%",
    )
    