from .item import create_item


def get_sidebar_items_enterprise():
    from pcweb.pages.docs import enterprise

    items = [
        create_item(
            "Overview",
            children=[
                enterprise.index,
            ],
        ),
        create_item(
            "Configuration",
            children=[
                enterprise.built_with_reflex,
                enterprise.single_port_proxy,
            ],
        ),
        create_item(
            "AGGrid and AGChart",
            children=[
                enterprise.ag_grid.index,
                enterprise.ag_grid.column_defs,
                enterprise.ag_grid.value_transformers,
                enterprise.ag_grid.theme,
                enterprise.ag_grid.pivot_mode,
                enterprise.ag_grid.aligned_grids,
                enterprise.ag_grid.model_wrapper,
                enterprise.ag_chart,
            ],
        ),
        create_item(
            "Interactive Components",
            children=[
                enterprise.drag_and_drop,
                enterprise.map.index,
            ],
        ),
        create_item(
            "Mantine",
            children=[
                enterprise.mantine.index,
                enterprise.mantine.autocomplete,
                enterprise.mantine.combobox,
                enterprise.mantine.multi_select,
                enterprise.mantine.tags_input,
                enterprise.mantine.json_input,
                enterprise.mantine.pill,
                enterprise.mantine.tree,
                enterprise.mantine.timeline,
                enterprise.mantine.number_formatter,
                enterprise.mantine.ring_progress,
                enterprise.mantine.semi_circle_progress,
                enterprise.mantine.loading_overlay,
                enterprise.mantine.spoiler,
                enterprise.mantine.collapse,
            ],
        ),
    ]
    return items


enterprise = get_sidebar_items_enterprise()
