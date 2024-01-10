---
components:
    - rx.Editor
---

An HTML editor component based on [Suneditor](http://suneditor.com/sample/index.html).

```python exec
import reflex as rx

from pcweb import styles
from pcweb.pages.docs.source import Source, generate_docs
from pcweb.templates.docpage import docdemo_from, h2_comp


class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content


def editor_example():
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
        ),
        rx.box(
            rx.html(EditorState.content),
            border="1px dashed #ccc",
            border_radius="4px",
            width="100%",
        ),
    )
```

```python eval
docdemo_from(EditorState, component=editor_example)
```

# EditorOptions

The extended options and toolbar buttons can be customized by passing an instance
of `rx.EditorOptions` for the `set_options` prop.

```python exec
editor_options_source = Source(module=rx.EditorOptions)
```

```python eval
rx.fragment(
    h2_comp(text="Fields"),
    rx.box(rx.table(
        rx.thead(
            rx.tr(
                rx.th("Field"),
                rx.th("Description"),
            )
        ),
        rx.tbody(
            *[
                rx.tr(
                    rx.td(rx.code(field["name"], font_weight=styles.BOLD_WEIGHT)),
                    rx.td(field["description"]),
                )
                for field in editor_options_source.get_fields()
            ],
        ),
    ), style={"overflow": "auto"}),
)
```

```python eval
rx.box(height="2em")
```

The `button_list` prop expects a list of lists, where each sublist contains the
names of buttons forming a group on the toolbar. The character "/" can be used
in place of a sublist to denote a line break in the toolbar.

Some valid `button_list` options are enumerated in `rx.EditorButtonList`, seen below.

```python
class EditorButtonList(list, enum.Enum):

    BASIC = [
        ["font", "fontSize"],
        ["fontColor"],
        ["horizontalRule"],
        ["link", "image"],
    ]
    FORMATTING = [
        ["undo", "redo"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        ["outdent", "indent"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
    ]
    COMPLEX = [
        ["undo", "redo"],
        ["font", "fontSize", "formatBlock"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        "/",
        ["fontColor", "hiliteColor"],
        ["outdent", "indent"],
        ["align", "horizontalRule", "list", "table"],
        ["link", "image", "video"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
        ["save", "template"],
    ]
```

A custom list of toolbar buttons may also be specified using these names as seen
in the following example.

Since this example uses the same state as above, the two editors contents are
shared and can be modified by either one.

```python demo
rx.editor(
    set_contents=EditorState.content,
    set_options=rx.EditorOptions(
        button_list=[
            ["font", "fontSize", "formatBlock"],
            ["fontColor", "hiliteColor"],
            ["bold", "underline", "italic", "strike", "subscript", "superscript"],
            ["removeFormat"],
            "/",
            ["outdent", "indent"],
            ["align", "horizontalRule", "list", "table"],
            ["link"],
            ["fullScreen", "showBlocks", "codeView"],
            ["preview", "print"],
        ]
    ),
    on_change=EditorState.handle_change,
)
```

See the [Suneditor README.md](https://github.com/JiHong88/suneditor/blob/master/README.md) for more
details on buttons and options.

```python eval
rx.box(height="5em")
```