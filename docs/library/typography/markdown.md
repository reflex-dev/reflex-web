---
components:
    - rx.Markdown
---

```python exec
import reflex as rx
```

# Markdown

The markdown component renders a Markdown string as formatted text.

```python demo
rx.vstack(
    rx.markdown("# Hello World!"),
    rx.markdown("## Hello World!"),
    rx.markdown("### Hello World!")
)
```

A more complicated example can be seen below.

```python demo
rx.markdown('''
Support us at **[Reflex](https://pynecone.io)**.
Format your `inline_code` easily.
'''
)
```

Render math equations using LaTeX.

```python demo
rx.markdown(r'$ \\int_a^b x^2 dx $')
```
