import flexdown

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
    definition,
)

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
            return rx.chakra.accordion(
                rx.chakra.accordion_item(
                    rx.chakra.accordion_button(
                        rx.hstack(
                            rx.box(
                                rx.match(
                                    status,
                                    ("info", rx.icon(tag="info", size=18, margin_right=".5em")),
                                    ("success", rx.icon(tag="circle_check", size=18, margin_right=".5em")),
                                    ("warning", rx.icon(tag="triangle_alert", size=18, margin_right=".5em")),
                                    ("error", rx.icon(tag="ban", size=18, margin_right=".5em")),
                                )
                            ),
                            rx.markdown(title) if title else self.render_fn(content=content),
                            rx.spacer(),
                            rx.chakra.accordion_icon(color=f"{rx.color(color, 11)}"),
                            align_items="center",
                            justify_content="left",
                            text_align="left",
                            spacing="2",
                            width="100%",
                        ),
                        color=f"{rx.color(color, 11)}", 
                        border_radius="8px",
                        _hover={},
                    ),
                    rx.chakra.accordion_panel(markdown(content)) if title else rx.fragment(),
                    border_radius="8px",
                    background_color=f"{rx.color(color, 3)}",
                    border="none",
                    allow_toggle=True,
                ),
                is_disabled = True,
                allow_toggle=True,
                width="100%",
                margin_y="1em"
            )
        else:
            return rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.match(
                            status,
                            ("info", rx.icon(tag="info", size=18, margin_right=".5em")),
                            ("success", rx.icon(tag="circle_check", size=18, margin_right=".5em")),
                            ("warning", rx.icon(tag="triangle_alert", size=18, margin_right=".5em")),
                            ("error", rx.icon(tag="ban", size=18, margin_right=".5em")),
                        )
                    ),
                    rx.markdown(
                        title,
                        color=f"{rx.color(color, 11)}"
                    ),
                    align_items="center",
                    spacing="1",
                    padding_left = "1em",
                    padding_right = "1em",
                ),
                background_color=f"{rx.color(color, 3)}",
                border_radius="8px",
                margin_y="1em",
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
                            rx.chakra.span(
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
            border_left=f"2.5px {rx.color('mauve', 4)} solid",
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
            rx.mobile_only(rx.chakra.vstack(*defs)),
            rx.tablet_and_desktop(
                rx.chakra.grid(
                    *[
                        rx.chakra.grid_item(d, row_span=1, col_span=1, width="100%")
                        for d in defs
                    ],
                    template_columns="repeat(2, 1fr)",
                    h="10em",
                    width="100%",
                    gap=4,
                    margin_bottom="1em",
                )
            ),
        )
   
 
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
            return rx.box(docdemobox(comp), margin_bottom="1em")
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

        return docdemo(code, comp=comp, demobox_props=demobox_props, theme=self.theme)

class DemoBlockDark(DemoBlock):
    theme = "dark"


component_map = {
    "h1": lambda text: h1_comp_xd(text=text),
    "h2": lambda text: h2_comp_xd(text=text),
    "h3": lambda text: h3_comp_xd(text=text),
    "h4": lambda text: h4_comp_xd(text=text),
    "p": lambda text: text_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block_markdown,
}
comp2 = component_map.copy()
comp2["codeblock"] = code_block_markdown_dark

xd = flexdown.Flexdown(
    block_types=[DemoBlock, AlertBlock, DefinitionBlock, SectionBlock],
    component_map=component_map,
)
xd.clear_modules()
xd2 = flexdown.Flexdown(
    block_types=[DemoBlockDark, AlertBlock, DefinitionBlock, SectionBlock],
    component_map=comp2,
)
xd2.clear_modules()


def markdown(text):
    return xd.get_default_block().render_fn(content=text)
