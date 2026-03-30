"""Pipeline for rendering reflex-shipped docs via reflex_docgen.markdown."""

import importlib
import importlib.util
import shutil
import sys
from pathlib import Path

import reflex as rx
from reflex_docgen.markdown import (
    CodeBlock,
    DirectiveBlock,
    Document,
    HeadingBlock,
    ListBlock,
    QuoteBlock,
    TableBlock,
    TextBlock,
    ThematicBreakBlock,
    parse_document,
)
from reflex_docgen.markdown._types import (
    BoldSpan,
    CodeSpan,
    FrontMatter,
    ImageSpan,
    ItalicSpan,
    LineBreakSpan,
    LinkSpan,
    ListItem,
    Span,
    StrikethroughSpan,
    TableCell,
    TableRow,
    TextSpan,
)
from reflex_docgen.markdown.transformer import DocumentTransformer

from pcweb.constants import REFLEX_ASSETS_CDN
from pcweb.templates.docpage.blocks.code import code_block
from pcweb.templates.docpage.blocks.demo import docdemo, docdemobox, docgraphing
from pcweb.templates.docpage.blocks.headings import (
    h1_comp_xd,
    h2_comp_xd,
    h3_comp_xd,
    h4_comp_xd,
    img_comp_xd,
)
from pcweb.templates.docpage.blocks.typography import (
    code_comp,
    doclink2,
    list_comp,
    text_comp,
)

# ---------------------------------------------------------------------------
# Exec environment — mirrors flexdown's module-based exec mechanism
# ---------------------------------------------------------------------------

_MODULE_DIR = Path(__file__).resolve().parent / "_docgen_modules"
_files: dict[str, list[str]] = {}


def _get_id(content: str) -> str:
    import hashlib

    return "m_" + hashlib.sha256(content.encode()).hexdigest()[:16]


def _exec_code(content: str, env: dict, filename: str) -> None:
    """Execute a ``python exec`` code block, updating *env* in place."""
    _MODULE_DIR.mkdir(parents=True, exist_ok=True)

    per_file = _files.setdefault(filename, [])
    mod_name_base = _get_id(content + filename + str(len(per_file)))
    mod_path = _MODULE_DIR / f"{mod_name_base}.py"

    if per_file:
        prev = f"pcweb._docgen_modules.{per_file[-1]}"
        content = f"from {prev} import *\n\n" + content
    mod_path.write_text(content + "\n")
    per_file.append(mod_name_base)

    mod_full = f"pcweb._docgen_modules.{mod_name_base}"
    if mod_full in sys.modules:
        raise RuntimeError(f"{mod_full} already imported from {filename}")

    spec = importlib.util.spec_from_file_location(mod_full, str(mod_path))
    if not spec or not spec.loader:
        return
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_full] = module
    spec.loader.exec_module(module)
    env.update(vars(module))


def _clear_modules(filename: str | None = None) -> None:
    if filename is not None:
        _files.pop(filename, None)
    if _MODULE_DIR.exists():
        shutil.rmtree(_MODULE_DIR)


# ---------------------------------------------------------------------------
# Span → rx.Component helpers
# ---------------------------------------------------------------------------


def _render_spans(spans: tuple[Span, ...]) -> list[rx.Component | str]:
    """Convert a sequence of spans into a list of Reflex children."""
    out: list[rx.Component | str] = []
    for span in spans:
        match span:
            case TextSpan(text=text):
                out.append(text)
            case BoldSpan(children=children):
                out.append(rx.text(rx.text.strong(*_render_spans(children)), as_="span"))
            case ItalicSpan(children=children):
                out.append(rx.text(rx.text.em(*_render_spans(children)), as_="span"))
            case StrikethroughSpan(children=children):
                inner = "".join(
                    c if isinstance(c, str) else "" for c in _render_spans(children)
                )
                out.append(rx.text("~" + inner + "~", as_="span"))
            case CodeSpan(code=code):
                out.append(code_comp(text=code))
            case LinkSpan(children=children, target=target):
                inner = "".join(
                    c if isinstance(c, str) else "" for c in _render_spans(children)
                )
                out.append(doclink2(text=inner, href=target))
            case ImageSpan(src=src):
                out.append(img_comp_xd(src=src))
            case LineBreakSpan(soft=soft):
                out.append("\n" if soft else rx.el.br())
    return out


def _spans_to_plaintext(spans: tuple[Span, ...]) -> str:
    """Extract plain text from spans (for headings, etc.)."""
    parts: list[str] = []
    for span in spans:
        match span:
            case TextSpan(text=text):
                parts.append(text)
            case BoldSpan(children=children) | ItalicSpan(children=children) | StrikethroughSpan(children=children) | LinkSpan(children=children):
                parts.append(_spans_to_plaintext(children))
            case CodeSpan(code=code):
                parts.append(code)
            case _:
                pass
    return "".join(parts)


# ---------------------------------------------------------------------------
# ReflexDocTransformer
# ---------------------------------------------------------------------------


class ReflexDocTransformer(DocumentTransformer[rx.Component]):
    """Transforms a reflex_docgen Document into Reflex components.

    Mirrors the rendering that the flexdown pipeline produces, so docs from
    the reflex package look identical to the locally-authored ones.
    """

    def __init__(self, filename: str = "") -> None:
        self.filename = filename
        self.env: dict = {}

    # ------------------------------------------------------------------
    # Top-level
    # ------------------------------------------------------------------

    def transform(self, document: Document) -> rx.Component:
        _clear_modules(self.filename)

        if document.frontmatter is not None:
            # Populate env with component preview metadata.
            for preview in document.frontmatter.component_previews:
                self.env[preview.name] = preview.source
            self.env["REFLEX_ASSETS_CDN"] = REFLEX_ASSETS_CDN

        children: list[rx.Component] = []
        for block in document.blocks:
            comp = self.transform_block(block)
            if comp is not None:
                children.append(comp)

        return rx.fragment(*children)

    # ------------------------------------------------------------------
    # Blocks
    # ------------------------------------------------------------------

    def frontmatter(self, block: FrontMatter) -> rx.Component:
        return rx.fragment()

    def heading(self, block: HeadingBlock) -> rx.Component:
        text = _spans_to_plaintext(block.children)
        match block.level:
            case 1:
                return h1_comp_xd(text=text)
            case 2:
                return h2_comp_xd(text=text)
            case 3:
                return h3_comp_xd(text=text)
            case _:
                return h4_comp_xd(text=text)

    def text_block(self, block: TextBlock) -> rx.Component:
        children = _render_spans(block.children)
        if len(children) == 1 and isinstance(children[0], str):
            return text_comp(text=children[0])
        return rx.text(
            *children,
            class_name="font-[475] text-m-slate-8 dark:text-m-slate-6 mb-4 leading-7",
        )

    def code_block(self, block: CodeBlock) -> rx.Component:
        flags = set(block.flags)
        language = block.language or "plain"

        # ``python exec`` — execute code, produce nothing visible.
        if language == "python" and "exec" in flags:
            _exec_code(block.content, self.env, self.filename)
            return rx.fragment()

        # ``python demo`` — execute or eval, then show code + component.
        if language == "python" and "demo" in flags:
            return self._render_demo(block.content, flags)

        # ``python demo-only`` — like demo but no code display.
        if language == "python" and "demo-only" in flags:
            return self._render_demo_only(block.content, flags)

        # Regular code block.
        return code_block(code=block.content, language=language)

    def directive(self, block: DirectiveBlock) -> rx.Component:
        """Handle ```md <directive>``` blocks (alert, video, etc.)."""
        match block.name:
            case "alert":
                return self._render_alert(block)
            case "video":
                return self._render_video(block)
            case "quote":
                return self._render_quote_directive(block)
            case _:
                # Fallback: render content as text.
                return text_comp(text=block.content)

    def list_block(self, block: ListBlock) -> rx.Component:
        items = [self.transform_list_item(item) for item in block.items]
        if block.ordered:
            return rx.list.ordered(*items, class_name="mb-6")
        return rx.list.unordered(*items, class_name="mb-6")

    def transform_list_item(self, item: ListItem) -> rx.Component:
        children: list[rx.Component] = []
        for child_block in item.children:
            match child_block:
                case TextBlock(children=spans):
                    text = _spans_to_plaintext(spans)
                    children.append(list_comp(text=text))
                case _:
                    children.append(self.transform_block(child_block))
        if len(children) == 1:
            return children[0]
        return rx.fragment(*children)

    def quote(self, block: QuoteBlock) -> rx.Component:
        children = [self.transform_block(b) for b in block.children]
        return rx.box(
            *children,
            class_name="border-l-[3px] border-slate-4 pl-6 mt-2 mb-6",
        )

    def table(self, block: TableBlock) -> rx.Component:
        header_cells = [
            rx.table.column_header_cell(
                *_render_spans(cell.children),
                class_name="font-small text-slate-12 font-bold",
            )
            for cell in block.header.cells
        ]
        rows = []
        for row in block.rows:
            cells = [
                rx.table.cell(
                    *_render_spans(cell.children),
                    class_name="font-small text-slate-11",
                )
                for cell in row.cells
            ]
            rows.append(rx.table.row(*cells))

        return rx.table.root(
            rx.table.header(rx.table.row(*header_cells)),
            rx.table.body(*rows),
            variant="surface",
            size="1",
            class_name="w-full border border-slate-4 mb-4",
        )

    def transform_table_row(self, row: TableRow) -> rx.Component:
        cells = [self.transform_table_cell(cell) for cell in row.cells]
        return rx.table.row(*cells)

    def transform_table_cell(self, cell: TableCell) -> rx.Component:
        return rx.table.cell(*_render_spans(cell.children))

    def thematic_break(self, block: ThematicBreakBlock) -> rx.Component:
        return rx.separator(class_name="my-6")

    # ------------------------------------------------------------------
    # Spans (not used directly by DocumentTransformer dispatch, but
    # kept for completeness if someone calls transform_span)
    # ------------------------------------------------------------------

    def text_span(self, span: TextSpan) -> rx.Component:
        return rx.text(span.text, as_="span")

    def bold(self, span: BoldSpan) -> rx.Component:
        return rx.text(rx.text.strong(*self.transform_spans(span.children)), as_="span")

    def italic(self, span: ItalicSpan) -> rx.Component:
        return rx.text(rx.text.em(*self.transform_spans(span.children)), as_="span")

    def strikethrough(self, span: StrikethroughSpan) -> rx.Component:
        return rx.text("~", *self.transform_spans(span.children), "~", as_="span")

    def code_span(self, span: CodeSpan) -> rx.Component:
        return code_comp(text=span.code)

    def link(self, span: LinkSpan) -> rx.Component:
        inner = _spans_to_plaintext(span.children)
        return doclink2(text=inner, href=span.target)

    def image(self, span: ImageSpan) -> rx.Component:
        return img_comp_xd(src=span.src)

    def line_break(self, span: LineBreakSpan) -> rx.Component:
        return rx.fragment()

    # ------------------------------------------------------------------
    # Demo / exec helpers
    # ------------------------------------------------------------------

    def _render_demo(self, content: str, flags: set[str]) -> rx.Component:
        """Render a ``python demo`` block — code + live component."""
        comp_id = None
        for flag in flags:
            if flag.startswith("id="):
                comp_id = flag.split("=", 1)[1]

        if "exec" in flags:
            _exec_code(content, self.env, self.filename)
            comp = self.env[list(self.env.keys())[-1]]()
        elif "graphing" in flags:
            _exec_code(content, self.env, self.filename)
            comp = self.env[list(self.env.keys())[-1]]()
            parts = content.rpartition("def")
            data, code = parts[0], parts[1] + parts[2]
            return docgraphing(code, comp=comp, data=data)
        elif "box" in flags:
            comp = eval(content, self.env, self.env)  # noqa: S307
            return rx.box(docdemobox(comp), margin_bottom="1em", id=comp_id)
        else:
            comp = eval(content, self.env, self.env)  # noqa: S307

        demobox_props: dict = {}
        for flag in flags:
            k, sep, v = flag.partition("=")
            if sep and k not in ("id",):
                demobox_props[k] = v
        if "toggle" in flags:
            demobox_props["toggle"] = True

        return docdemo(content, comp=comp, demobox_props=demobox_props, id=comp_id)

    def _render_demo_only(self, content: str, flags: set[str]) -> rx.Component:
        """Render a ``python demo-only`` block — component only, no code."""
        comp_id = None
        for flag in flags:
            if flag.startswith("id="):
                comp_id = flag.split("=", 1)[1]

        if "exec" in flags:
            _exec_code(content, self.env, self.filename)
            comp = self.env[list(self.env.keys())[-1]]()
        elif "graphing" in flags:
            _exec_code(content, self.env, self.filename)
            comp = self.env[list(self.env.keys())[-1]]()
            parts = content.rpartition("def")
            data, code = parts[0], parts[1] + parts[2]
            return docgraphing(code, comp=comp, data=data)
        elif "box" in flags:
            comp = eval(content, self.env, self.env)  # noqa: S307
        else:
            comp = eval(content, self.env, self.env)  # noqa: S307

        return rx.box(comp, margin_bottom="1em", id=comp_id)

    def _render_alert(self, block: DirectiveBlock) -> rx.Component:
        """Render a ``md alert`` directive."""
        status = block.args[0] if block.args else "info"
        colors = {
            "info": "accent",
            "success": "grass",
            "warning": "amber",
            "error": "red",
        }
        color = colors.get(status, "blue")

        lines = block.content.splitlines()
        if lines and lines[0].startswith("#"):
            title = lines[0].lstrip("#").strip()
            content = "\n".join(lines[1:])
        else:
            title = ""
            content = block.content

        icon_map = {
            "info": "info",
            "success": "circle_check",
            "warning": "triangle_alert",
            "error": "ban",
        }
        icon_tag = icon_map.get(status, "info")

        return rx.box(
            rx.hstack(
                rx.icon(tag=icon_tag, size=18, color=rx.color(color, 11)),
                rx.text(
                    title or content.strip(),
                    class_name="font-[475]",
                    color=rx.color(color, 11),
                ),
                align_items="center",
                spacing="2",
                padding=["16px", "24px"],
                width="100%",
            ),
            border=f"1px solid {rx.color(color, 4)}",
            background_color=rx.color(color, 3),
            border_radius="12px",
            margin_bottom="16px",
            margin_top="16px",
            width="100%",
        )

    def _render_video(self, block: DirectiveBlock) -> rx.Component:
        """Render a ``md video`` directive."""
        url = block.args[0] if block.args else ""
        lines = block.content.splitlines()
        title = lines[0].lstrip("#").strip() if lines and lines[0].startswith("#") else "Video"
        return rx.box(
            rx.text(title, class_name="font-[475] text-slate-11 mb-2"),
            rx.video(
                src=url,
                width="100%",
                height="500px",
                border_radius="10px",
                overflow="hidden",
            ),
            class_name="my-4",
        )

    def _render_quote_directive(self, block: DirectiveBlock) -> rx.Component:
        """Render a ``md quote`` directive."""
        lines = block.content.splitlines()
        quote_text: list[str] = []
        name = ""
        role = ""
        for line in lines:
            if line.startswith("- name:"):
                name = line.split(":", 1)[1].strip()
            elif line.startswith("- role:"):
                role = line.split(":", 1)[1].strip()
            else:
                quote_text.append(line)

        return rx.box(
            rx.text(
                f'"{" ".join(quote_text).strip()}"',
                class_name="text-slate-11 font-base italic",
            ),
            rx.box(
                rx.text(name, class_name="text-slate-11 font-base"),
                rx.text(role, class_name="text-slate-10 font-base"),
                class_name="flex flex-col gap-0.5",
            ),
            class_name="flex flex-col gap-4 border-l-[3px] border-slate-4 pl-6 mt-2 mb-6",
        )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def render_docgen_document(filepath: str | Path) -> rx.Component:
    """Parse and render a doc file from the reflex package using reflex_docgen.

    Args:
        filepath: Absolute path to the .md file.

    Returns:
        A Reflex component tree for the document content.
    """
    source = Path(filepath).read_text(encoding="utf-8")
    doc = parse_document(source)
    transformer = ReflexDocTransformer(filename=str(filepath))
    return transformer.transform(doc)


def get_docgen_toc(filepath: str | Path) -> list[dict]:
    """Extract table-of-contents headings from a reflex-package doc.

    Args:
        filepath: Absolute path to the .md file.

    Returns:
        A list of dicts with 'text' and 'level' keys.
    """
    source = Path(filepath).read_text(encoding="utf-8")
    doc = parse_document(source)
    return [
        {"text": _spans_to_plaintext(h.children), "level": h.level}
        for h in doc.headings
    ]


def get_docgen_frontmatter(filepath: str | Path) -> FrontMatter | None:
    """Extract frontmatter from a reflex-package doc.

    Args:
        filepath: Absolute path to the .md file.

    Returns:
        The FrontMatter, or None.
    """
    source = Path(filepath).read_text(encoding="utf-8")
    doc = parse_document(source)
    return doc.frontmatter
