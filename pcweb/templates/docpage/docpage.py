"""Template for documentation pages."""

import functools
from datetime import datetime
from typing import Callable

import flexdown
import mistletoe
import reflex as rx
import reflex_ui as ui
from reflex.components.radix.themes.base import LiteralAccentColor
from reflex.utils.format import to_snake_case, to_title_case

from pcweb.components.button import button
from pcweb.components.icons.icons import get_icon
from pcweb.route import Route, get_path
from pcweb.styles.colors import c_color

from .blocks import *
from .state import FeedbackState


def right_sidebar_item_highlight():
    return r"""
   function setupTableOfContentsHighlight() {
    // Delay to ensure DOM is fully loaded
    setTimeout(() => {
        const tocLinks = document.querySelectorAll('#toc-navigation a');
        const activeClass = 'text-violet-9';
        const defaultClass = 'text-slate-9';

        function normalizeId(id) {
            return id.toLowerCase().replace(/\s+/g, '-');
        }

        function highlightTocLink() {
            // Get the current hash from the URL
            const currentHash = window.location.hash.substring(1);

            // Reset all links
            tocLinks.forEach(link => {
                link.classList.remove(activeClass);
                link.classList.add(defaultClass);
            });

            // If there's a hash, find and highlight the corresponding link
            if (currentHash) {
                const correspondingLink = Array.from(tocLinks).find(link => {
                    // Extract the ID from the link's href
                    const linkHash = new URL(link.href).hash.substring(1);
                    return normalizeId(linkHash) === normalizeId(currentHash);
                });

                if (correspondingLink) {
                    correspondingLink.classList.remove(defaultClass);
                    correspondingLink.classList.add(activeClass);
                }
            }
        }

        // Add click event listeners to TOC links to force highlight
        tocLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                // Remove active class from all links
                tocLinks.forEach(otherLink => {
                    otherLink.classList.remove(activeClass);
                    otherLink.classList.add(defaultClass);
                });

                // Add active class to clicked link
                e.target.classList.remove(defaultClass);
                e.target.classList.add(activeClass);
            });
        });

        // Intersection Observer for scroll-based highlighting
        const observerOptions = {
            root: null,
            rootMargin: '-20% 0px -70% 0px',
            threshold: 0
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const headerId = entry.target.id;

                    // Find corresponding TOC link
                    const correspondingLink = Array.from(tocLinks).find(link => {
                        const linkHash = new URL(link.href).hash.substring(1);
                        return normalizeId(linkHash) === normalizeId(headerId);
                    });

                    if (correspondingLink) {
                        // Reset all links
                        tocLinks.forEach(link => {
                            link.classList.remove(activeClass);
                            link.classList.add(defaultClass);
                        });

                        // Highlight current link
                        correspondingLink.classList.remove(defaultClass);
                        correspondingLink.classList.add(activeClass);
                    }
                }
            });
        }, observerOptions);

        // Observe headers
        const headerSelectors = Array.from(tocLinks).map(link =>
            new URL(link.href).hash.substring(1)
        );

        headerSelectors.forEach(selector => {
            const header = document.getElementById(selector);
            if (header) {
                observer.observe(header);
            }
        });

        // Initial highlighting
        highlightTocLink();

        // Handle hash changes
        window.addEventListener('hashchange', highlightTocLink);
    }, 100);
}

// Run the function when the page loads
setupTableOfContentsHighlight();
    """


def footer_link(text: str, href: str):
    return rx.link(
        text,
        class_name="font-small text-slate-9 hover:!text-slate-11 transition-color",
        href=href,
        underline="none",
    )


def footer_link_flex(heading: str, links):
    return rx.box(
        rx.el.h4(
            heading,
            class_name="font-semibold text-slate-12 text-sm tracking-[-0.01313rem]",
        ),
        *links,
        class_name="flex flex-col gap-4",
    )


def thumb_card(score: int, icon: str) -> rx.Component:
    return rx.el.button(
        rx.icon(
            tag=icon,
            color=rx.cond(
                FeedbackState.score == score, c_color("slate", 11), c_color("slate", 9)
            ),
            size=16,
        ),
        background_color=rx.cond(
            FeedbackState.score == score, c_color("slate", 3), c_color("white", 1)
        ),
        on_click=FeedbackState.set_score(score),
        class_name="transition-bg hover:bg-slate-3 shadow-medium border border-slate-4 rounded-lg items-center justify-center cursor-pointer p-2 size-9 flex",
    )


def thumbs_cards() -> rx.Component:
    return rx.hstack(
        thumb_card(1, "thumbs-up"),
        thumb_card(0, "thumbs-down"),
        gap="8px",
    )


def feedback_content() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Send feedback",
                class_name="font-md text-slate-11",
            ),
            rx.form(
                rx.box(
                    rx.el.textarea(
                        name="feedback",
                        placeholder="Write a comment…",
                        type="text",
                        max_length=500,
                        enter_key_submit=True,
                        resize="vertical",
                        required=True,
                        class_name="w-full h-full p-2 text-slate-11 font-small bg-white-1 border border-slate-4 rounded-[10px] max-h-[300px] min-h-[72px] outline-none overflow-y-auto placeholder-slate-9 focus:border-violet-9 focus:border-1",
                    ),
                    thumbs_cards(),
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="Contact email (optional)",
                        max_length=100,
                        class_name="w-full h-full p-2 text-slate-11 font-small bg-white-1 border border-slate-4 rounded-[10px] box-border outline-none placeholder-slate-9 focus:border-violet-9 focus:border-1",
                    ),
                    rx.box(
                        rx.popover.close(
                            button(
                                "Send",
                                type="submit",
                            )
                        ),
                        rx.popover.close(
                            button(
                                "Cancel",
                                variant="secondary",
                            )
                        ),
                        class_name="flex flex-row gap-4 justify-between items-center",
                    ),
                    class_name="w-full gap-4 flex flex-col",
                ),
                class_name="w-full",
                reset_on_submit=True,
                on_submit=FeedbackState.handle_submit,
            ),
            class_name="flex flex-col gap-4 w-full",
        ),
        class_name="rounded-[26px] bg-white-1 w-[341px] max-h-[564px] shadow-large h-auto p-4",
    )


def feedback_button() -> rx.Component:
    thumb_cn = " flex flex-row items-center justify-center gap-2 text-slate-9 whitespace-nowrap border border-slate-5 bg-slate-1 shadow-large cursor-pointer transition-bg hover:bg-slate-3 font-small"
    return rx.popover.root(
        rx.box(
            rx.popover.trigger(
                rx.box(
                    rx.icon(tag="thumbs-up", size=15, class_name="!text-slate-9"),
                    rx.text(
                        "Yes",
                    ),
                    class_name="w-full gap-2 border-r-0 px-3 py-0.5 rounded-[20px_0_0_20px]"
                    + thumb_cn,
                ),
                custom_attrs={"role": "button"},
                aria_label="Yes",
                on_click=FeedbackState.set_score(1),
            ),
            rx.popover.trigger(
                rx.box(
                    rx.icon(tag="thumbs-down", size=15, class_name="!text-slate-9"),
                    rx.text(
                        "No",
                    ),
                    class_name="w-full gap-2 px-3 py-0.5 rounded-[0_20px_20px_0]"
                    + thumb_cn,
                ),
                custom_attrs={"role": "button"},
                aria_label="No",
                on_click=FeedbackState.set_score(0),
            ),
            class_name="w-full lg:w-auto items-center flex flex-row",
        ),
        rx.popover.content(
            feedback_content(),
            align="start",
            class_name="border-none left-0 lg:left-[-255px] origin-bottom lg:origin-bottom-right !p-0 overflow-visible !bg-transparent shadow-none",
            avoid_collisions=True,
        ),
    )


def link_pill(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        underline="none",
        class_name="lg:flex hidden flex-row justify-center items-center gap-2 lg:border-slate-5 bg-slate-3 lg:bg-slate-1 hover:bg-slate-3 shadow-none lg:shadow-large px-3 py-0.5 lg:border lg:border-solid border-none rounded-lg lg:rounded-full w-auto font-small font-small text-slate-9 !hover:text-slate-11 hover:!text-slate-9 truncate whitespace-nowrap transition-bg transition-color cursor-pointer",
    )


@rx.memo
def docpage_footer(path: str):
    from pcweb.constants import FORUM_URL, ROADMAP_URL
    from pcweb.pages.blog import blogs
    from pcweb.pages.docs import getting_started, hosting
    from pcweb.pages.docs.library import library
    from pcweb.pages.errors import errors
    from pcweb.pages.faq import faq
    from pcweb.pages.framework.views.footer_index import dark_mode_toggle
    from pcweb.pages.gallery import gallery
    from pcweb.views.footer import menu_socials, newsletter_form, ph_1

    return rx.el.footer(
        rx.box(
            rx.box(
                rx.text(
                    "Did you find this useful?",
                    class_name="font-small text-slate-11 lg:text-slate-9 whitespace-nowrap",
                ),
                feedback_button(),
                class_name="flex lg:flex-row flex-col items-center gap-3 lg:gap-4 bg-slate-3 lg:bg-transparent p-4 lg:p-0 rounded-lg w-full",
            ),
            rx.box(
                link_pill(
                    "Raise an issue",
                    href=f"https://github.com/reflex-dev/reflex-web/issues/new?title=Issue with reflex.dev documentation&amp;body=Path: {path}",
                ),
                link_pill(
                    "Edit this page",
                    f"https://github.com/reflex-dev/reflex-web/tree/main{path}.md",
                ),
                class_name="lg:flex hidden flex-row items-center gap-2 w-auto",
            ),
            class_name="flex flex-row justify-center lg:justify-between items-center border-slate-4 border-y-0 lg:border-y pt-0 lg:pt-8 pb-6 lg:pb-8 w-full",
        ),
        rx.box(newsletter_form(), class_name="pt-8 pb-10"),
        rx.box(
            rx.box(
                footer_link_flex(
                    "Links",
                    [
                        footer_link("Home", "/"),
                        footer_link("Templates", gallery.path),
                        footer_link("Blog", blogs.path),
                        footer_link(
                            "Changelog", "https://github.com/reflex-dev/reflex/releases"
                        ),
                    ],
                ),
                footer_link_flex(
                    "Documentation",
                    [
                        footer_link("Introduction", getting_started.introduction.path),
                        footer_link("Installation", getting_started.installation.path),
                        footer_link("Components", library.path),
                        footer_link("Hosting", hosting.deploy_quick_start.path),
                    ],
                ),
                footer_link_flex(
                    "Resources",
                    [
                        footer_link("FAQ", faq.path),
                        footer_link("Common Errors", errors.path),
                        footer_link("Roadmap", ROADMAP_URL),
                        footer_link("Forum", FORUM_URL),
                        footer_link("Use Case", "/use-cases"),
                    ],
                ),
                class_name="flex flex-wrap justify-between gap-12 w-full",
            ),
            rx.box(
                rx.box(
                    ph_1(),
                    rx.text(
                        f"Copyright © {datetime.now().year} Pynecone, Inc.",
                        class_name="font-small text-slate-9",
                    ),
                    dark_mode_toggle(),
                    class_name="flex flex-col gap-6",
                ),
                menu_socials(),
                class_name="flex flex-row gap-6 justify-between items-end w-full",
            ),
            class_name="flex flex-col justify-between gap-10 py-6 lg:py-8 w-full",
        ),
        class_name="flex flex-col max-w-full lg:max-w-auto",
    )


def breadcrumb(path: str, nav_sidebar: rx.Component):
    from pcweb.components.docpage.navbar.buttons.sidebar import docs_sidebar_drawer

    # Split the path into segments, removing 'docs' and capitalizing each segment
    segments = [
        segment.capitalize()
        for segment in path.split("/")
        if segment and segment != "docs"
    ]

    # Initialize an empty list to store the breadcrumbs and their separators
    breadcrumbs = []

    # Iteratively build the href for each segment
    current_path = "/docs"
    for i, segment in enumerate(segments):
        current_path += f"/{segment.lower()}"

        # Add the breadcrumb item to the list
        breadcrumbs.append(
            rx.link(
                to_title_case(to_snake_case(segment), sep=" "),
                class_name="font-small text-slate-9 hover:!text-slate-11 transition-color"
                + (" truncate" if i == len(segments) - 1 else ""),
                underline="none",
                href=current_path,
            )
        )

        # If it's not the last segment, add a separator
        if i < len(segments) - 1:
            breadcrumbs.append(
                rx.icon(
                    tag="chevron-right",
                    size=14,
                    class_name="lg:flex hidden !text-slate-8",
                ),
            )
            breadcrumbs.append(
                rx.text(
                    "/",
                    class_name="font-sm text-slate-8 lg:hidden flex",
                )
            )
    from pcweb.components.hosting_banner import HostingBannerState

    # Return the list of breadcrumb items with separators
    return rx.box(
        docs_sidebar_drawer(
            nav_sidebar,
            trigger=rx.box(
                class_name="absolute inset-0 bg-transparent z-[1] lg:hidden flex",
            ),
        ),
        rx.box(
            *breadcrumbs,
            class_name="flex flex-row items-center gap-[5px] lg:gap-4 overflow-hidden",
        ),
        rx.box(
            rx.icon(tag="chevron-down", size=14, class_name="!text-slate-9"),
            class_name="p-[0.563rem] lg:hidden flex",
        ),
        class_name=ui.cn(
            "relative z-10 flex flex-row justify-between items-center gap-4 lg:gap-0 border-slate-4 bg-slate-1 mt-[135px] mb-6 lg:mb-8 p-[0.5rem_1rem_0.5rem_1rem] lg:p-0 border-b lg:border-none w-full",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "lg:mt-[175px]",
                "lg:mt-[145px] mt-[77px]",
            ),
        ),
    )


def get_headings(comp):
    """Get the strings from markdown component."""
    if isinstance(comp, mistletoe.block_token.Heading):
        heading_text = "".join(
            token.content for token in comp.children if hasattr(token, "content")
        )
        return [(comp.level, heading_text)]

    # Recursively get the strings from the children.
    if not hasattr(comp, "children") or comp.children is None:
        return []

    headings = []
    for child in comp.children:
        headings.extend(get_headings(child))
    return headings


def get_toc(source, href, component_list=None):
    from pcweb.flexdown import xd

    component_list = component_list or []
    component_list = component_list[1:]

    # Generate the TOC
    # The environment used for execing and evaling code.
    env = source.metadata
    env["__xd"] = xd

    # Get the content of the document.
    source = source.content

    # Get the blocks in the source code.
    # Note: we must use reflex-web's special flexdown instance xd here - it knows about all custom block types (like DemoBlock)
    blocks = xd.get_blocks(source, href)

    content_pieces = []
    for block in blocks:
        if (
            not isinstance(block, flexdown.blocks.MarkdownBlock)
            or len(block.lines) == 0
            or not block.lines[0].startswith("#")
        ):
            continue
        # Now we should have all the env entries we need
        content = block.get_content(env)
        content_pieces.append(content)

    content = "\n".join(content_pieces)
    doc = mistletoe.Document(content)

    # Parse the markdown headers.
    headings = get_headings(doc)

    if len(component_list):
        headings.append((1, "API Reference"))
    for component_tuple in component_list:
        headings.append((2, component_tuple[1]))
    return headings


def docpage(
    set_path: str | None = None,
    t: str | None = None,
    right_sidebar: bool = True,
    page_title: str | None = None,
    pseudo_right_bar: bool = False,
):
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        t: The title to set for the page.
        right_sidebar: Whether to show the right sidebar.
        page_title: The full title to set for the page. If None, defaults to `{title} · Reflex Docs`.
        pseudo_right_bar: Whether to show a pseudo right sidebar (empty space).

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
        path = get_path(contents) if set_path is None else set_path

        title = contents.__name__.replace("_", " ").title() if t is None else t

        @functools.wraps(contents)
        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            from pcweb.components.docpage.sidebar import get_prev_next
            from pcweb.components.docpage.sidebar import sidebar as sb
            from pcweb.components.hosting_banner import HostingBannerState
            from pcweb.views.docs_navbar import docs_navbar

            sidebar = sb(url=path, width="300px")

            nav_sidebar = sb(url=path, width="100%")

            prev, next = get_prev_next(path)
            links = []

            if prev:
                next_prev_name = (
                    prev.alt_name_for_next_prev
                    if prev.alt_name_for_next_prev
                    else prev.names
                )
                links.append(
                    rx.box(
                        rx.link(
                            rx.box(
                                get_icon(
                                    icon="arrow_right", transform="rotate(180deg)"
                                ),
                                "Back",
                                class_name="flex flex-row justify-center lg:justify-start items-center gap-2 rounded-lg w-full",
                            ),
                            underline="none",
                            href=prev.link,
                            class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
                        ),
                        rx.text(next_prev_name, class_name="font-smbold text-slate-12"),
                        class_name="flex flex-col justify-start gap-1",
                    )
                )
            else:
                links.append(rx.fragment())
            links.append(rx.spacer())

            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.box(
                        rx.link(
                            rx.box(
                                "Next",
                                get_icon(icon="arrow_right"),
                                class_name="flex flex-row lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                            ),
                            underline="none",
                            href=next.link,
                            class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
                        ),
                        rx.text(next_prev_name, class_name="font-smbold text-slate-12"),
                        class_name="flex flex-col justify-start gap-1 items-end",
                    )
                )
            else:
                links.append(rx.fragment())

            toc = []
            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            if isinstance(comp, tuple):
                toc, comp = comp

            show_right_sidebar = right_sidebar and len(toc) >= 2
            return rx.box(
                docs_navbar(),
                rx.el.main(
                    rx.box(
                        sidebar,
                        class_name=(
                            "w-full max-w-[300px] h-screen shrink-0 hidden lg:block z-10 "
                            + rx.cond(
                                HostingBannerState.is_banner_visible,
                                " mt-[146px]",
                                " mt-[90px]",
                            )
                        ),
                    ),
                    rx.box(
                        rx.box(
                            breadcrumb(path=path, nav_sidebar=nav_sidebar),
                            class_name=(
                                "px-0 xl:px-14 pt-0"
                                + rx.cond(
                                    HostingBannerState.is_banner_visible,
                                    " mt-[90px]",
                                    "",
                                )
                            ),
                        ),
                        rx.box(
                            rx.el.article(comp),
                            rx.el.nav(
                                *links,
                                class_name="flex flex-row gap-2 mt-8 lg:mt-10 mb-6 lg:mb-12",
                            ),
                            docpage_footer(path=path.rstrip("/")),
                            class_name="lg:mt-0 mt-6 px-4 xl:px-10 h-auto bg-slate-1",
                        ),
                        class_name="flex-1 bg-slate-1 h-auto mx-auto max-w-4xl overflow-y-auto",
                        # class_name="flex-1 bg-slate-1 h-auto mx-auto overflow-y-auto "
                        #     + "max-w-4xl" if show_right_sidebar and not pseudo_right_bar else "!max-w-7xl",
                    ),
                    rx.box(
                        rx.el.nav(
                            rx.box(
                                rx.el.p(
                                    "On this page",
                                    class_name="font-smbold text-sm text-slate-12 hover:text-violet-9 leading-5 tracking-[-0.01313rem] transition-color",
                                ),
                                rx.el.ul(
                                    *[
                                        (
                                            rx.el.li(
                                                rx.link(
                                                    text,
                                                    class_name="font-small text-slate-9 hover:!text-slate-11 whitespace-normal transition-color break-words",
                                                    underline="none",
                                                    href=path
                                                    + "#"
                                                    + text.lower().replace(" ", "-"),
                                                )
                                            )
                                            if level == 1
                                            else (
                                                rx.list_item(
                                                    rx.link(
                                                        text,
                                                        class_name="font-small text-slate-9 hover:!text-slate-11 whitespace-normal transition-color break-words",
                                                        underline="none",
                                                        href=path
                                                        + "#"
                                                        + text.lower().replace(
                                                            " ", "-"
                                                        ),
                                                    )
                                                )
                                                if level == 2
                                                else rx.el.li(
                                                    rx.link(
                                                        text,
                                                        underline="none",
                                                        class_name="pl-3 block text-sm text-slate-9 hover:!text-slate-11 transition-color break-words",
                                                        href=path
                                                        + "#"
                                                        + text.lower().replace(
                                                            " ", "-"
                                                        ),
                                                    )
                                                )
                                            )
                                        )
                                        for level, text in toc
                                    ],
                                    class_name="flex flex-col gap-y-3 list-none",
                                ),
                                class_name="flex flex-col justify-start gap-y-2 p-[0.875rem_0.5rem_0px_0.5rem] max-h-[80vh] overflow-y-auto sticky top-4",
                            ),
                            class_name=(
                                "w-full h-full"
                                + rx.cond(
                                    HostingBannerState.is_banner_visible,
                                    " mt-[146px]",
                                    " mt-[90px]",
                                )
                            ),
                            id="toc-navigation",
                        ),
                        class_name=(
                            "w-[240px] h-screen sticky top-0 shrink-0 hidden xl:block"
                        ),
                    )
                    if show_right_sidebar and not pseudo_right_bar
                    else rx.box(
                        class_name="w-[180px] h-screen sticky top-0 shrink-0 hidden xl:block"
                    ),
                    class_name="flex justify-center mx-auto mt-0 max-w-[94.5em] h-full min-h-screen w-full lg:px-10",
                ),
                class_name="flex flex-col justify-center bg-slate-1 w-full relative",
                on_mount=rx.call_script(right_sidebar_item_highlight()),
            )

        components = path.split("/")
        category = (
            " ".join(
                word.capitalize() for word in components[2].replace("-", " ").split()
            )
            if len(components) > 2
            else None
        )
        if page_title:
            return Route(
                path=path,
                title=page_title,
                component=wrapper,
            )
        return Route(
            path=path,
            title=f"{title} · Reflex Docs" if category is None else title,
            component=wrapper,
        )

    return docpage


class RadixDocState(rx.State):
    """The app state."""

    color: str = "tomato"

    @rx.event
    def set_color(self, color: str):
        self.color = color


def hover_item(component: rx.Component, component_str: str) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(rx.flex(component)),
        rx.hover_card.content(
            rx.el.button(
                get_icon(icon="copy", class_name="p-[5px]"),
                rx.text(
                    component_str,
                    class_name="flex-1 font-small truncate",
                ),
                on_click=rx.set_clipboard(component_str),
                class_name="flex flex-row items-center gap-1.5 border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small pr-1.5 border rounded-md w-full max-w-[300px] text-slate-11 transition-bg cursor-pointer",
            ),
        ),
    )


def dict_to_formatted_string(input_dict):
    # List to hold formatted string parts
    formatted_parts = []

    # Iterate over dictionary items
    for key, value in input_dict.items():
        # Format each key-value pair
        if isinstance(value, str):
            formatted_part = f'{key}="{value}"'  # Enclose string values in quotes
        else:
            formatted_part = f"{key}={value}"  # Non-string values as is

        # Append the formatted part to the list
        formatted_parts.append(formatted_part)

    # Join all parts with a comma and a space
    return ", ".join(formatted_parts)


def used_component(
    component_used: rx.Component,
    components_passed: rx.Component | str | None,
    color_scheme: str,
    variant: str,
    high_contrast: bool,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    if components_passed is None and disabled is False:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is not None and disabled is False:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            **kwargs,
        )

    elif components_passed is None and disabled is True:
        return component_used(
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )

    else:
        return component_used(
            components_passed,
            color_scheme=color_scheme,
            variant=variant,
            high_contrast=high_contrast,
            disabled=True,
            **kwargs,
        )


def style_grid(
    component_used: rx.Component,
    component_used_str: str,
    variants: list,
    components_passed: rx.Component | str | None = None,
    disabled: bool = False,
    **kwargs,
) -> rx.Component:
    text_cn = "text-nowrap font-md flex items-center"
    return rx.box(
        rx.grid(
            rx.text("", size="5"),
            *[
                rx.text(variant, class_name=text_cn + " text-slate-11")
                for variant in variants
            ],
            rx.text(
                "Accent",
                color=f"var(--{RadixDocState.color}-10)",
                class_name=text_cn,
            ),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme=RadixDocState.color,
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("Gray", class_name=text_cn + " text-slate-11"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=False,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=False, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            rx.text("", size="5"),
            *[
                hover_item(
                    component=used_component(
                        component_used=component_used,
                        components_passed=components_passed,
                        color_scheme="gray",
                        variant=variant,
                        high_contrast=True,
                        **kwargs,
                    ),
                    component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, high_contrast=True, {dict_to_formatted_string(kwargs)})",
                )
                for variant in variants
            ],
            (
                rx.fragment(
                    rx.text("Disabled", class_name=text_cn + " text-slate-11"),
                    *[
                        hover_item(
                            component=used_component(
                                component_used=component_used,
                                components_passed=components_passed,
                                color_scheme="gray",
                                variant=variant,
                                high_contrast=True,
                                disabled=disabled,
                                **kwargs,
                            ),
                            component_str=f"{component_used_str}(color_scheme={RadixDocState.color}, variant={variant}, disabled=True, {dict_to_formatted_string(kwargs)})",
                        )
                        for variant in variants
                    ],
                )
                if disabled
                else ""
            ),
            flow="column",
            columns="5",
            rows=str(len(variants) + 1),
            spacing="3",
        ),
        rx.popover.root(
            rx.popover.trigger(
                rx.box(
                    rx.button(
                        rx.text(RadixDocState.color, class_name="font-small"),
                        # Match the select.trigger svg icon
                        rx.html(
                            """<svg width="9" height="9" viewBox="0 0 9 9" fill="currentcolor" xmlns="http://www.w3.org/2000/svg" class="rt-SelectIcon" aria-hidden="true"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg>"""
                        ),
                        color_scheme=RadixDocState.color,
                        variant="surface",
                        class_name="justify-between w-32",
                    ),
                ),
            ),
            rx.popover.content(
                rx.grid(
                    *[
                        rx.box(
                            rx.icon(
                                "check",
                                size=15,
                                class_name="top-1/2 left-1/2 absolute text-gray-12 transform -translate-x-1/2 -translate-y-1/2"
                                + rx.cond(
                                    RadixDocState.color == color,
                                    " block",
                                    " hidden",
                                ),
                            ),
                            on_click=RadixDocState.set_color(color),
                            background_color=f"var(--{color}-9)",
                            class_name="relative rounded-md cursor-pointer shrink-0 size-[30px]"
                            + rx.cond(
                                RadixDocState.color == color,
                                " border-2 border-gray-12",
                                "",
                            ),
                        )
                        for color in list(map(str, LiteralAccentColor.__args__))
                    ],
                    columns="6",
                    spacing="3",
                ),
            ),
        ),
        class_name="flex flex-col justify-center items-center gap-6 border-slate-4 bg-slate-2 mb-4 p-6 border rounded-xl",
    )
