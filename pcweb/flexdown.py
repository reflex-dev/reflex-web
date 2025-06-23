import flexdown
from pcweb.styles.colors import c_color

import reflex as rx
from pcweb.templates.docpage import (
    code_block_markdown,
    code_block_markdown_dark,
    code_comp,
    docdemo,
    docdemobox,
    docgraphing,
    doclink2,
    h1_comp_xd,
    h2_comp_xd,
    h3_comp_xd,
    h4_comp_xd,
    text_comp,
    list_comp,
    definition,
    unordered_list_comp,
    ordered_list_comp,
)

from pcweb.styles.fonts import base, code


def get_code_style(color: str):
    return {
        "p": {"margin_y": "0px"},
        "code": {
            "color": rx.color(color, 11),
            "border_radius": "4px",
            "border": f"1px solid {rx.color(color, 5)}",
            "background": rx.color(color, 4),
            **code,
        },
        **base,
    }


class AlertBlock(flexdown.blocks.MarkdownBlock):
    """A block that displays a component along with its code."""

    starting_indicator = "```md alert"
    ending_indicator = "```"

    include_indicators = True

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        args = lines[0].removeprefix(self.starting_indicator).split()

        if len(args) == 0:
            args = ["info"]
        status = args[0]

        if lines[1].startswith("#"):
            title = lines[1].strip("#").strip()
            content = "\n".join(lines[2:-1])
        else:
            title = ""
            content = "\n".join(lines[1:-1])

        colors = {
            "info": "accent",
            "success": "grass",
            "warning": "amber",
            "error": "red",
        }

        color = colors.get(status, "blue")

        has_content = bool(content.strip())

        if has_content:
            return rx.accordion.root(
                rx.accordion.item(
                    rx.accordion.header(
                        rx.accordion.trigger(
                            rx.hstack(
                                rx.box(
                                    rx.match(
                                        status,
                                        (
                                            "info",
                                            rx.icon(
                                                tag="info", size=18, margin_right=".5em"
                                            ),
                                        ),
                                        (
                                            "success",
                                            rx.icon(
                                                tag="circle_check",
                                                size=18,
                                                margin_right=".5em",
                                            ),
                                        ),
                                        (
                                            "warning",
                                            rx.icon(
                                                tag="triangle_alert",
                                                size=18,
                                                margin_right=".5em",
                                            ),
                                        ),
                                        (
                                            "error",
                                            rx.icon(
                                                tag="ban", size=18, margin_right=".5em"
                                            ),
                                        ),
                                    ),
                                    color=f"{rx.color(color, 11)}",
                                ),
                                (
                                    markdown_with_shiki(
                                        title,
                                        margin_y="0px",
                                        style=get_code_style(color),
                                    )
                                    if title
                                    else self.render_fn(content=content)
                                ),
                                rx.spacer(),
                                rx.accordion.icon(color=f"{rx.color(color, 11)}"),
                                align_items="center",
                                justify_content="left",
                                text_align="left",
                                spacing="2",
                                width="100%",
                            ),
                            padding="0px",
                            color=f"{rx.color(color, 11)} !important",
                            background_color="transparent !important",
                            border_radius="12px",
                            _hover={},
                        ),
                    ),
                    (
                        rx.accordion.content(
                            markdown(content), padding="0px", margin_top="16px"
                        )
                        if title
                        else rx.fragment()
                    ),
                    border_radius="12px",
                    padding=["16px", "24px"],
                    background_color=f"{rx.color(color, 3)}",
                    border=f"1px solid {rx.color(color, 4)}",
                ),
                background="none !important",
                border_radius="0px",
                box_shadow="unset !important",
                collapsible=True,
                width="100%",
                margin_bottom="16px",
            )
        else:
            return rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.match(
                            status,
                            ("info", rx.icon(tag="info", size=18, margin_right=".5em")),
                            (
                                "success",
                                rx.icon(
                                    tag="circle_check", size=18, margin_right=".5em"
                                ),
                            ),
                            (
                                "warning",
                                rx.icon(
                                    tag="triangle_alert", size=18, margin_right=".5em"
                                ),
                            ),
                            ("error", rx.icon(tag="ban", size=18, margin_right=".5em")),
                        ),
                        color=f"{rx.color(color, 11)}",
                    ),
                    markdown_with_shiki(
                        title,
                        color=f"{rx.color(color, 11)}",
                        margin_y="0px",
                        style=get_code_style(color),
                    ),
                    align_items="center",
                    width="100%",
                    spacing="1",
                    padding=["16px", "24px"],
                ),
                border=f"1px solid {rx.color(color, 4)}",
                background_color=f"{rx.color(color, 3)}",
                border_radius="12px",
                margin_bottom="16px",
            )


class SectionBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```md section"
    ending_indicator = "```"

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        # Split up content into sections based on markdown headers.
        header_indices = [i for i, line in enumerate(lines) if line.startswith("#")]
        header_indices.append(len(lines))
        sections = [
            (
                lines[header_indices[i]].strip("#"),
                "\n".join(lines[header_indices[i] + 1 : header_indices[i + 1]]),
            )
            for i in range(len(header_indices) - 1)
        ]

        return rx.box(
            rx.vstack(
                *[
                    rx.fragment(
                        rx.text(
                            rx.text.span(
                                header,
                                font_weight="bold",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            markdown(section),
                            width="100%",
                        ),
                    )
                    for header, section in sections
                ],
                text_align="left",
                margin_y="1em",
                width="100%",
            ),
            border_left=f"1.5px {c_color('slate', 4)} solid",
            padding_left="1em",
            width="100%",
            align_items="center",
        )


class DefinitionBlock(flexdown.blocks.Block):
    starting_indicator = "```md definition"
    ending_indicator = "```"

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        # Split up content into sections based on markdown headers.
        header_indices = [i for i, line in enumerate(lines) if line.startswith("#")]
        header_indices.append(len(lines))
        sections = [
            (
                lines[header_indices[i]].removeprefix("#"),
                "\n".join(lines[header_indices[i] + 1 : header_indices[i + 1]]),
            )
            for i in range(len(header_indices) - 1)
        ]

        defs = [definition(title, content) for title, content in sections]

        return rx.fragment(
            rx.mobile_only(rx.vstack(*defs)),
            rx.tablet_and_desktop(
                rx.grid(
                    *[rx.box(d) for d in defs],
                    columns="2",
                    width="100%",
                    gap="1rem",
                    margin_bottom="1em",
                )
            ),
        )


class DemoOnly(flexdown.blocks.Block):
    """A block that displays only a component demo without showing the code."""

    starting_indicator = "```python demo-only"
    ending_indicator = "```"
    include_indicators = True
    theme: str = None

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        exec_mode = env.get("__exec", False)
        comp = ""

        for arg in args:
            if arg.startswith("id="):
                comp_id = arg.rsplit("id=")[-1]
                break
        else:
            comp_id = None

        if "exec" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
        elif "graphing" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
                # Get all the code before the final "def".
                parts = code.rpartition("def")
                data, code = parts[0], parts[1] + parts[2]
                comp = docgraphing(code, comp=comp, data=data)
                return comp
        elif exec_mode:
            return comp
        elif "box" in args:
            comp = eval(code, env, env)
            return rx.box(comp, margin_bottom="1em", id=comp_id)
        else:
            comp = eval(code, env, env)

        # Return only the component without any code display
        return rx.box(comp, margin_bottom="1em", id=comp_id)


class DemoBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```python demo"
    ending_indicator = "```"
    include_indicators = True
    theme: str = None

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        exec_mode = env.get("__exec", False)
        comp = ""

        for arg in args:
            if arg.startswith("id="):
                comp_id = arg.rsplit("id=")[-1]
                break
        else:
            comp_id = None

        if "exec" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
        elif "graphing" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
                # Get all the code before the final "def".
                parts = code.rpartition("def")
                data, code = parts[0], parts[1] + parts[2]
                comp = docgraphing(code, comp=comp, data=data)
                return comp
        elif exec_mode:
            return comp
        elif "box" in args:
            comp = eval(code, env, env)
            return rx.box(docdemobox(comp), margin_bottom="1em", id=comp_id)
        else:
            comp = eval(code, env, env)

        # Sweep up additional CSS-like props to apply to the demobox itself
        demobox_props = {}
        for arg in args:
            prop, equals, value = arg.partition("=")
            if equals:
                demobox_props[prop] = value

        if "toggle" in args:
            demobox_props["toggle"] = True

        return docdemo(
            code, comp=comp, demobox_props=demobox_props, theme=self.theme, id=comp_id
        )


class DemoBlockDark(DemoBlock):
    theme = "dark"


class VideoBlock(flexdown.blocks.MarkdownBlock):
    """A block that displays a video."""

    starting_indicator = "```md video"
    ending_indicator = "```"

    include_indicators = True

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        args = lines[0].removeprefix(self.starting_indicator).split()

        if len(args) == 0:
            args = ["info"]
        url = args[0]

        if lines[1].startswith("#"):
            title = lines[1].strip("#").strip()
        else:
            title = ""

        color = "blue"

        return rx.accordion.root(
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.hstack(
                            (
                                markdown_with_shiki(
                                    title,
                                    margin_y="0px",
                                    style=get_code_style(color),
                                )
                                if title
                                else markdown_with_shiki("Video Description")
                            ),
                            rx.spacer(),
                            rx.accordion.icon(color=f"{rx.color(color, 11)}"),
                            align_items="center",
                            justify_content="left",
                            text_align="left",
                            spacing="2",
                            width="100%",
                        ),
                        padding="0px",
                        color=f"{rx.color(color, 11)} !important",
                        background_color="transparent !important",
                        border_radius="12px",
                        _hover={},
                    ),
                ),
                rx.accordion.content(
                    rx.video(
                        url=url,
                        width="100%",
                        height="500px",
                        border_radius="10px",
                        overflow="hidden",
                    ),
                    margin_top="16px",
                    padding="0px",
                ),
                border_radius="12px",
                border=f"1px solid {rx.color(color, 4)}",
                background_color=f"{rx.color(color, 3)}",
                padding=["16px", "24px"],
            ),
            margin_bottom="16px",
            background="none !important",
            border_radius="0px",
            box_shadow="unset !important",
            collapsible=True,
            width="100%",
        )


class QuoteBlock(flexdown.blocks.MarkdownBlock):
    """A block that displays a quote."""

    starting_indicator = "```md quote"
    ending_indicator = "```"

    include_indicators = True

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        quote_content = []
        name = ""
        role = ""
        for line in lines[1:-1]:  # Skip the first and last lines (indicators)
            if line.startswith("- name:"):
                name = line.split(":", 1)[1].strip()
            elif line.startswith("- role:"):
                role = line.split(":", 1)[1].strip()
            else:
                quote_content.append(line)

        quote_text = "\n".join(quote_content).strip()

        return rx.box(
            rx.text(f'"{quote_text}"', class_name="text-slate-11 font-base italic"),
            rx.box(
                rx.text(name, class_name="text-slate-11 font-base"),
                rx.text(role, class_name="text-slate-10 font-base"),
                class_name="flex flex-col gap-0.5",
            ),
            class_name="flex flex-col gap-4 border-l-[3px] border-slate-4 pl-6 mt-2 mb-6",
        )


class TabsBlock(flexdown.blocks.Block):
    """A block that displays content in tabs."""

    starting_indicator = "---md tabs"
    ending_indicator = "---"

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)

        tab_sections = []
        current_section = []
        current_title = ""

        for line in lines[1:-1]:  # Skip the first and last lines (indicators)
            stripped_line = line.strip()

            if stripped_line.startswith("--tab "):
                if current_title:
                    tab_sections.append((current_title, "\n".join(current_section)))
                current_title = stripped_line[6:].strip()
                current_section = []
            elif stripped_line == "--":
                if current_title:
                    tab_sections.append((current_title, "\n".join(current_section)))
                    current_title = ""
                    current_section = []
            else:
                current_section.append(line)

        # Add the last section if there's content
        if current_title and current_section:
            tab_sections.append((current_title, "\n".join(current_section)))

        # Create tab components
        triggers = []
        contents = []

        for i, (title, content) in enumerate(tab_sections):
            value = f"tab{i + 1}"
            triggers.append(
                rx.tabs.trigger(
                    title,
                    value=value,
                    class_name="tab-style font-base font-semibold text-[1.25rem]",
                )
            )

            # Render the tab content
            tab_content = []
            for block in env["__xd"].get_blocks(content, self.filename):
                if isinstance(block, flexdown.blocks.MarkdownBlock):
                    block.render_fn = env["__xd"].flexdown_memo
                try:
                    tab_content.append(block.render(env=env))
                except Exception as e:
                    print(
                        f"Error while rendering {type(block)} on line {block.start_line_number}. "
                        f"\n{block.get_content(env)}"
                    )
                    raise e

            contents.append(rx.tabs.content(rx.fragment(*tab_content), value=value))

        return rx.tabs.root(
            rx.tabs.list(*triggers, class_name="mt-4"), *contents, default_value="tab1"
        )


component_map = {
    "h1": lambda text: h1_comp_xd(text=text),
    "h2": lambda text: h2_comp_xd(text=text),
    "h3": lambda text: h3_comp_xd(text=text),
    "h4": lambda text: h4_comp_xd(text=text),
    "p": lambda text: text_comp(text=text),
    "li": lambda text: list_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block_markdown,
}
comp2 = component_map.copy()
comp2["codeblock"] = code_block_markdown_dark
comp2["ul"] = lambda items: unordered_list_comp(items=items)
comp2["ol"] = lambda items: ordered_list_comp(items=items)


xd = flexdown.Flexdown(
    block_types=[
        DemoOnly,
        DemoBlock,
        AlertBlock,
        DefinitionBlock,
        SectionBlock,
        VideoBlock,
        TabsBlock,
        QuoteBlock,
    ],
    component_map=component_map,
)
xd.clear_modules()
xd2 = flexdown.Flexdown(
    block_types=[
        DemoBlockDark,
        AlertBlock,
        DefinitionBlock,
        SectionBlock,
        VideoBlock,
        TabsBlock,
        QuoteBlock,
    ],
    component_map=comp2,
)
xd2.clear_modules()


def markdown(text):
    return xd.get_default_block().render_fn(content=text)


def markdown_with_shiki(*args, **kwargs):
    """
    Wrapper for the markdown component with a customized component map.
    Uses the experimental Shiki-based code block (rx._x.code_block)
    instead of the default CodeBlock component for code blocks.

    Note: This wrapper should be removed once the default codeblock
    in rx.markdown component map is updated to the Shiki-based code block.
    """
    return rx.markdown(
        *args,
        component_map={
            "codeblock": lambda value, **props: rx._x.code_block(value, **props)
        },
        **kwargs,
    )
