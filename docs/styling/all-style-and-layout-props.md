# All Style and Layout Props

```python exec
import reflex as rx

props = {
    "background_color": {
        "description": "sets the background color of an element",
        "values": ["brown", "rgb(255, 255, 128)", "#7499ee"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/background-color",
    },
    "color": {
        "description": "sets the foreground color value of an element's text",
        "values": ["rebeccapurple", "rgb(255, 255, 128)", "#00a400"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/color",
    },
    "max_height / min_height": {
        "description": "sets the maximum / minimum height of an element and prevents the used value of the height property from becoming larger / smaller than the value specified for max_height / min_height",
        "values": ["7em", "75%", "150px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/max-height",
    },
    "padding_x / padding_y": {
        "description": "creates extra space within an element along the x-axis / y-axis",
        "values": ["1em", "10%", "10px"],
        "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/padding",
    },
    


}

#  4. width, 5. min/max_width, 6. padding_(bottom, top, left, right)
# 7. position, 8. border_(bottom, top, left, right), 9. margin_(bottom, top, left, right), 10. display,
# 11. height, 12. text_align 13. top/bottom/right/left, 15. align (align items) 16. justify (justify_content),
# 17. z_index, 18. backdrop_filter, 19. backdrop_blur, 20. border_color, 21. border_radius, 22. box_shadow, 23. background_image, 
# 24. margin_x/y, 25. flex_grow, 26. background (bg) 27. text_wrap, 28. whitespace, 29. word-break


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