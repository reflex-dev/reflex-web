# All Style and Layout Props

```python exec
import reflex as rx

props = {
    "align": {
        "description": "in a flex, it controls the alignment of items on the cross axis and in a grid layout, it controls the alignment of items on the block axis within their grid area (equivalent to align_items)",
        "values": ["brown", "rgb(255, 255, 128)", "#7499ee"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/background-color",
    },
    "background_color": {
        "description": "sets the background color of an element",
        "values": ["brown", "rgb(255, 255, 128)", "#7499ee"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/background-color",
    },
    "border": {
        "description": "sets an element's border, which sets the values of border_width, border_style, and border_color.",
        "values": ["solid", "dashed red", "thick double #32a1ce", "4mm ridge rgba(211, 220, 50, .6)"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/border",
    },
    "border_top / border_bottom / border_right / border_left": {
        "description": "sets an element's top / bottom / right / left border. It sets the values of border-(top / bottom / right / left)-width, border-(top / bottom / right / left)-style and border-(top / bottom / right / left)-color",
        "values": ["solid", "dashed red", "thick double #32a1ce", "4mm ridge rgba(211, 220, 50, .6)"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom",
    },
    "color": {
        "description": "sets the foreground color value of an element's text",
        "values": ["rebeccapurple", "rgb(255, 255, 128)", "#00a400"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/color",
    },
    "display": {
        "description": "sets whether an element is treated as a block or inline box and the layout used for its children, such as flow layout, grid or flex",
        "values": ["block", "inline", "inline-block", "flex", "inline-flex", "grid", "inline-grid", "flow-root"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/display",
    },
    "height": {
        "description": "sets an element's height",
        "values": ["150px", "20em", "75%", "auto"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/height",
    },

    "margin": {
        "description": "sets the margin area (creates extra space around an element) on all four sides of an element",
        "values": ["1em", "5% 0", "10px 50px 20px", "10px 50px 20px 0"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/margin",
    },
    "margin_x / margin_y": {
        "description": "sets the margin area (creates extra space around an element) along the x-axis / y-axis and a positive value places it farther from its neighbors, while a negative value places it closer",
        "values": ["1em", "10%", "10px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/margin",
    },
    "margin_top / margin_right / margin_bottom / margin_left ": {
        "description": "sets the margin area (creates extra space around an element) on the top / right / bottom / left of an element",
        "values": ["1em", "10%", "10px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top",
    },



    "max_height / min_height": {
        "description": "sets the maximum / minimum height of an element and prevents the used value of the height property from becoming larger / smaller than the value specified for max_height / min_height",
        "values": ["150px", "7em", "75%"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/max-height",
    },
    "max_width / min_width": {
        "description": "sets the maximum / minimum width of an element and prevents the used value of the width property from becoming larger / smaller than the value specified for max_width / min_width",
        "values": ["150px", "20em", "75%"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/max-width",
    },
    "padding": {
        "description": "sets the padding area (creates extra space within an element) on all four sides of an element at once",
        "values": ["1em", "10px 50px 30px 0", "0", "10px 50px 20px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/padding",
    },
    "padding_x / padding_y": {
        "description": "creates extra space within an element along the x-axis / y-axis",
        "values": ["1em", "10%", "10px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/padding",
    },
    "padding_top / padding_right / padding_bottom / padding_left ": {
        "description": "sets the height of the padding area on the top / right / bottom / left of an element",
        "values": ["1em", "10%", "20px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top",
    },
    "position": {
        "description": "sets how an element is positioned in a document and the top, right, bottom, and left properties determine the final location of positioned elements",
        "values": ["static", "relative", "absolute", "fixed", "sticky"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/position",
    },
    "text_align": {
        "description": "sets an element's width",
        "values": ["150px", "20em", "75%", "auto"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/width",
    },

    "top / bottom / right / left": {
        "description": "sets the vertical / horizontal position of a positioned element. It does not effect non-positioned elements.",
        "values": ["0", "4em", "10%", "20px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/top",
    },
    "width": {
        "description": "sets an element's width",
        "values": ["150px", "20em", "75%", "auto"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/width",
    },
    

}

# 12. text_align 15. align (align items) 16. justify (justify_content),
# 17. z_index, 18. backdrop_filter, 19. backdrop_blur, 20. border_color, 21. border_radius,  21a. border_width, 22. box_shadow, 23. background_image, 
# 25. flex_grow, 26. background (bg) 27. text_wrap, 28. whitespace, 29. word-break


def show_props(key, props_dict):
    prop_details = props_dict[key]
    return rx.table.row(
        rx.table.cell(rx.code(key)),
        rx.table.cell(prop_details["description"]),
        rx.table.cell(rx.vstack(*[rx.badge(value) for value in prop_details["values"]])),
        rx.table.cell(rx.link("More Info", href=prop_details["link"], is_external=True)),
        align="center",
    )

```


```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell(
                "Prop", justify="start"
            ),
            rx.table.column_header_cell(
                "Description",
                justify="start",
            ),
            rx.table.column_header_cell(
                "Potential Values",
                justify="start",
            ),
            rx.table.column_header_cell(
                "Extra Information",
                justify="start",
            ),
            rx.table.column_header_cell(justify="start"),
        )
    ),
    rx.table.body(
        *[show_props(key, props) for key in props]
    ),
    width="100%",
    padding_x="0",
    size="1",
)
```