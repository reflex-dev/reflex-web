"""Enterprise sidebar items."""

from ..state import SideBarItem


def get_sidebar_items_enterprise_usage():
    """Get the enterprise usage sidebar items."""
    return [
        SideBarItem(
            names="Overview",
            children=[
                SideBarItem(
                    names="How to use Enterprise",
                    link="/docs/enterprise/overview/",
                ),
            ],
        ),
        SideBarItem(
            names="Configuration",
            children=[
                SideBarItem(
                    names="Built with Reflex",
                    link="/docs/enterprise/built-with-reflex/",
                ),
                SideBarItem(
                    names="Single Port Proxy",
                    link="/docs/enterprise/single-port-proxy/",
                ),
            ],
        ),
    ]


def get_sidebar_items_enterprise_components():
    """Get the enterprise components sidebar items."""
    return [
        SideBarItem(
            names="AG Grid",
            children=[
                SideBarItem(
                    names="Overview",
                    link="/docs/enterprise/ag_grid/",
                ),
                SideBarItem(
                    names="Column Definitions",
                    link="/docs/enterprise/ag_grid/column-defs/",
                ),
                SideBarItem(
                    names="Aligned Grids",
                    link="/docs/enterprise/ag_grid/aligned-grids/",
                ),
                SideBarItem(
                    names="Model Wrapper",
                    link="/docs/enterprise/ag_grid/model-wrapper/",
                ),
                SideBarItem(
                    names="Pivot Mode",
                    link="/docs/enterprise/ag_grid/pivot-mode/",
                ),
                SideBarItem(
                    names="Theme",
                    link="/docs/enterprise/ag_grid/theme/",
                ),
                SideBarItem(
                    names="Value Transformers",
                    link="/docs/enterprise/ag_grid/value-transformers/",
                ),
            ],
        ),
        SideBarItem(
            names="AG Chart",
            children=[
                SideBarItem(
                    names="Overview",
                    link="/docs/enterprise/ag_chart/",
                ),
            ],
        ),
        SideBarItem(
            names="Interactive Components",
            children=[
                SideBarItem(
                    names="Drag and Drop",
                    link="/docs/enterprise/drag-and-drop/",
                ),
                SideBarItem(
                    names="Mapping",
                    link="/docs/enterprise/map/",
                ),
            ],
        ),
        SideBarItem(
            names="Mantine",
            children=[
                SideBarItem(
                    names="Overview",
                    link="/docs/enterprise/mantine/",
                ),
                SideBarItem(
                    names="Autocomplete",
                    link="/docs/enterprise/mantine/autocomplete/",
                ),
                SideBarItem(
                    names="Collapse",
                    link="/docs/enterprise/mantine/collapse/",
                ),
                SideBarItem(
                    names="JSON Input",
                    link="/docs/enterprise/mantine/json-input/",
                ),
                SideBarItem(
                    names="Loading Overlay",
                    link="/docs/enterprise/mantine/loading-overlay/",
                ),
                SideBarItem(
                    names="Multi Select",
                    link="/docs/enterprise/mantine/multi-select/",
                ),
                SideBarItem(
                    names="Number Formatter",
                    link="/docs/enterprise/mantine/number-formatter/",
                ),
                SideBarItem(
                    names="Pill",
                    link="/docs/enterprise/mantine/pill/",
                ),
                SideBarItem(
                    names="Ring Progress",
                    link="/docs/enterprise/mantine/ring-progress/",
                ),
                SideBarItem(
                    names="Semi Circle Progress",
                    link="/docs/enterprise/mantine/semi-circle-progress/",
                ),
                SideBarItem(
                    names="Spoiler",
                    link="/docs/enterprise/mantine/spoiler/",
                ),
                SideBarItem(
                    names="Tags Input",
                    link="/docs/enterprise/mantine/tags-input/",
                ),
                SideBarItem(
                    names="Timeline",
                    link="/docs/enterprise/mantine/timeline/",
                ),
                SideBarItem(
                    names="Tree",
                    link="/docs/enterprise/mantine/tree/",
                ),
            ],
        ),
    ]


enterprise_usage_items = get_sidebar_items_enterprise_usage()
enterprise_component_items = get_sidebar_items_enterprise_components()
enterprise_items = (
    enterprise_usage_items + enterprise_component_items
)  # Keep for backward compatibility
