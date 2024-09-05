import flexdown
from pcweb.styles.colors import c_color
import reflex_chakra as rc

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

        icons = {
            "info": "info",
            "success": "circle_check",
            "warning": "triangle_alert",
            "error": "ban",
        }

        color = colors.get(status, "blue")
        icon_tag = icons.get("status", "info")

        has_content = bool(content.strip())

        if has_content:
            return rc.accordion(
                rc.accordion_item(
                    rc.accordion_button(
                        rx.icon(
                            tag=icon_tag,
                            size=18,
                            color=rx.color(color, 11),
                            class_name="shrink-0",
                        ),
                        (
                            rx.markdown(
                                title, class_name="!my-0 font-base markdown-code"
                            )
                            if title
                            else self.render_fn(content=content)
                        ),
                        rx.spacer(),
                        rc.accordion_icon(color=rx.color(color, 11)),
                        class_name="flex items-center gap-4 !bg-transparent hover:!bg-transparent !p-4 lg:!p-6 justify-start",
                    ),
                    (
                        rc.accordion_panel(
                            markdown(content),
                            class_name="!p-[0rem_1rem_1rem_1rem] lg:!p-[0rem_1.5rem_1.5rem_1.5rem] font-small text-slate-11 text-start [&>code]:!font-code",
                        )
                        if title
                        else rx.fragment()
                    ),
                    color=rx.color(color, 11),
                    class_name="border-none",
                ),
                is_disabled=True,
                allow_toggle=True,
                background_color=rx.color(color, 3),
                border=f"1px solid {rx.color(color, 4)}",
                class_name="mb-4 rounded-xl w-full",
            )
        else:
            return rx.box(
                rx.box(
                    rx.icon(
                        tag=icon_tag,
                        size=18,
                        color=rx.color(color, 11),
                        class_name="shrink-0",
                    ),
                    rx.markdown(
                        title,
                        color=rx.color(color, 11),
                        class_name="!my-0 font-base markdown-code",
                    ),
                    class_name="flex items-center gap-4 !p-4 lg:!p-6",
                ),
                border=f"1px solid {rx.color(color, 4)}",
                background_color=f"{rx.color(color, 3)}",
                class_name="mb-4 rounded-xl w-full",
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
            *[
                rx.fragment(
                    rx.text(
                        rx.text(
                            header,
                            class_name="font-bold font-md text-slate-12 tracking-[-0.0225rem]",
                        ),
                        width="100%",
                    ),
                    markdown(section),
                )
                for header, section in sections
            ],
            class_name="border-l border-slate-4 w-full pl-6 mb-10 text-left flex flex-col gap-4 [&>p]:mb-0",
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
            rx.mobile_only(rc.vstack(*defs)),
            rx.tablet_and_desktop(
                rc.grid(
                    *[
                        rc.grid_item(d, row_span=1, col_span=1, width="100%")
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

        return rc.accordion(
            rc.accordion_item(
                rc.accordion_button(
                    (
                        rx.markdown(
                            title,
                            class_name="!my-0 font-base markdown-code text-blue-11",
                        )
                        if title
                        else rx.markdown("Video Description")
                    ),
                    rx.spacer(),
                    rc.accordion_icon(color=rx.color(color, 11)),
                    class_name="flex items-center gap-4 !bg-transparent hover:!bg-transparent !p-4 lg:!p-6 justify-start",
                ),
                rc.accordion_panel(
                    rx.video(
                        url=url,
                        height="500px",
                        width="100%",
                        class_name="rounded-xl overflow-hidden",
                    ),
                    class_name="!p-[0rem_1rem_1rem_1rem] lg:!p-[0rem_1.5rem_1.5rem_1.5rem]",
                ),
                class_name="border-none",
            ),
            is_disabled=True,
            allow_toggle=True,
            background_color=rx.color(color, 3),
            border=f"1px solid {rx.color(color, 4)}",
            class_name="mb-4 rounded-xl w-full",
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

xd = flexdown.Flexdown(
    block_types=[DemoBlock, AlertBlock, DefinitionBlock, SectionBlock, VideoBlock],
    component_map=component_map,
)
xd.clear_modules()
xd2 = flexdown.Flexdown(
    block_types=[DemoBlockDark, AlertBlock, DefinitionBlock, SectionBlock, VideoBlock],
    component_map=comp2,
)
xd2.clear_modules()


def markdown(text):
    return xd.get_default_block().render_fn(content=text)
