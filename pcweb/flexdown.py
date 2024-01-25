import flexdown

import reflex as rx
from pcweb import styles
from pcweb.templates.docpage import (
    code_block_markdown,
    code_comp,
    docdemo,
    docdemobox,
    docgraphing,
    doclink2,
    h1_comp,
    h2_comp,
    h3_comp,
    h4_comp,
    text_comp,
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

        return rx.alert(
            rx.alert_icon(),
            rx.box(
                rx.alert_title(markdown(title)) if title else "",
                rx.alert_description(markdown(content)),
            ),
            status=status,
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
                            rx.span(
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
                margin_bottom="2em",
                width="100%",
            ),
            margin_top="1em",
            margin_left=".5em",
            border_left="1px #F4F3F6 solid",
            padding_left="1em",
            width="100%",
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

        def single_def(title, content):
            return rx.box(
                rx.heading(
                    title, font_size="1em", margin_bottom="0.5em", font_weight="bold"
                ),
                markdown(content),
                padding="1em",
                border=styles.DOC_BORDER,
                border_radius=styles.DOC_BORDER_RADIUS,
                _hover={
                    "box_shadow": styles.DOC_SHADOW_LIGHT,
                    "border": f"2px solid {styles.colors['violet'][200]}",
                },
            )

        defs = [single_def(title, content) for title, content in sections]

        return rx.fragment(
            rx.mobile_only(rx.vstack(*defs)),
            rx.tablet_and_desktop(
                rx.grid(
                    *[
                        rx.grid_item(d, row_span=1, col_span=1, width="100%")
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

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        if "exec" in args:
            env["__xd"].exec(code, env, self.filename)
            comp = env[list(env.keys())[-1]]()
        elif "graphing" in args:
            env["__xd"].exec(code, env, self.filename)
            comp = env[list(env.keys())[-1]]()
            # Get all the code before the final "def".
            parts = code.rpartition("def")
            data, code = parts[0], parts[1] + parts[2]
            comp = docgraphing(code, comp=comp, data=data)
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

        return docdemo(code, comp=comp, demobox_props=demobox_props)


component_map = {
    "h1": lambda text: h1_comp(text=text),
    "h2": lambda text: h2_comp(text=text),
    "h3": lambda text: h3_comp(text=text),
    "h4": lambda text: h4_comp(text=text),
    "p": lambda text: text_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block_markdown,
}

xd = flexdown.Flexdown(
    block_types=[DemoBlock, AlertBlock, DefinitionBlock, SectionBlock],
    component_map=component_map,
)
xd.clear_modules()


def markdown(text):
    return xd.default_block_type().render_fn(content=text)
