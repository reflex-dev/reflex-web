"""Reflex custom component AgGrid."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from types import SimpleNamespace
import reflex as rx

import os
from typing import Any, Callable, Union
from .datasource import Datasource, SSRMDatasource
from reflex.components.props import PropsBase
from typing import Literal
from reflex.components.el import Div


def callback_content(iterable: list[str]) -> str:
    return "; ".join(iterable)


def arrow_callback(js_expr: str | list[str]):
    if isinstance(js_expr, list):
        js_expr = callback_content(js_expr)
    return rx.Var(f"(() => {{{js_expr}}})()")


def exclude_non_serializable_keys(
    event: rx.Var,
    exclude_keys: list[str],
    log_event: bool = False,
) -> list[str]:
    exclude_keys_str = ", ".join(exclude_keys)

    exprs = [
        f"let {{{exclude_keys_str}, ...rest}} = {event}",
        "return rest",
    ]

    if log_event:
        exprs = [f"console.log({event})", *exprs]
    return exprs


def _on_cell_event_spec(event: rx.Var) -> list[rx.Var]:
    # Remove non-serializable keys from the event object
    exclude_keys = [
        "context",
        "api",
        "columnApi",
        "column",
        "node",
        "event",
        "eventPath",
    ]
    return [
        arrow_callback(
            exclude_non_serializable_keys(
                event,
                exclude_keys,
                True,
            )
        ),
    ]


def _on_row_event_spec(event: rx.Var) -> list[rx.Var]:
    exclude_keys = ["context", "api", "source", "node", "event", "eventPath"]
    return [
        arrow_callback(
            exclude_non_serializable_keys(
                event,
                exclude_keys,
                True,
            )
        ),
    ]


def _on_column_event_spec(event: rx.Var) -> list[rx.Var]:
    return [
        arrow_callback(
            [
                f"console.log({event})",
                f"let {{type, column, colDef, api, ...rest}} = {event}",
                "let columnID = column.colId",
                "return {type, columnID}",
            ]
        ),  # ID of the column being clicked
    ]


def _on_row_selected(event: rx.Var) -> list[rx.Var]:
    return [
        arrow_callback(
            [
                f"let {{type, node, data, rowIndex, ...rest}} = {event}",
                "return {type, data, rowIndex}",
            ]
        )
    ]


def _on_cell_value_changed(event: rx.Var) -> list[rx.Var]:
    return [
        rx.Var(
            f"(() => {{let {{rowIndex, ...rest}} = {event}; console.log({event}) ; return rowIndex}})()"
        ),  # index of the row being changed
        rx.Var(
            f"(() => {{let {{colDef, ...rest}} = {event}; return colDef.field}})()"
        ),  # field of the column being changed
        rx.Var(
            f"(() => {{let {{newValue, ...rest}} = {event}; return newValue}})()"
        ),  # new value
    ]


def _on_selection_change_signature(event: rx.Var) -> list[rx.Var]:
    return [
        rx.Var(f"{event}.api.getSelectedRows()"),
        rx.Var(f"{event}.source"),
        rx.Var(f"{event}.type"),
    ]


size_columns_to_fit = rx.Var(
    "(event) => event.api.sizeColumnsToFit()", _var_type=rx.EventChain
)


class AGFilters(SimpleNamespace):
    text = "agTextColumnFilter"
    number = "agNumberColumnFilter"
    date = "agDateColumnFilter"
    set = "agSetColumnFilter"
    multi = "agMultiColumnFilter"


class AGEditors(SimpleNamespace):
    text = "agTextCellEditor"
    large_text = "agLargeTextCellEditor"
    select = "agSelectCellEditor"
    rich_select = "agRichSelectCellEditor"
    number = "agNumberCellEditor"
    date = "agDateCellEditor"
    checkbox = "agCheckboxCellEditor"


class AGRenderers(SimpleNamespace):
    link = rx.vars.function.ArgsFunctionOperation.create(
        ("params",),
        rx.link(
            rx.Var("params.value"),
            href=rx.Var("params.value", _var_type=str),
            target="_blank",
        ),
    ).to(dict)  # TODO: remove cast after reflex 0.6.6


class ColumnDef(PropsBase):
    field: str | rx.Var[str]
    col_id: str | rx.Var[str] | None = None
    type: str | rx.Var[str] | None = None
    cell_data_type: bool | str | rx.Var[bool] | rx.Var[str] | None = None
    hide: bool | rx.Var[bool] = False
    editable: bool | rx.Var[bool] = False
    filter: AGFilters | str | rx.Var[AGFilters] | rx.Var[str] | None = None
    floating_filter: bool | rx.Var[bool] = False
    header_name: str | rx.Var[str] | None = None
    header_tooltip: str | rx.Var[str] | None = None
    checkbox_selection: bool | rx.Var[bool] = False
    cell_editor: AGEditors | str | rx.Var[AGEditors] | rx.Var[str] | None = None
    cell_editor_params: dict[str, list[Any]] | rx.Var[dict[str, list[Any]]] | None = (
        None
    )
    value_setter: rx.EventChain | rx.Var[rx.EventChain] | None = None
    value_formatter: rx.Var | None = None
    wrap_text: bool | None = None
    auto_height: bool | None = None
    auto_header_height: bool | None = None
    enable_cell_change_flash: bool | None = None
    cell_editor_popup: bool | None = None
    cell_editor_popup_position: str | None = None
    resizable: bool | None = None
    suppress_span_header_height: bool | None = None
    cell_renderer: rx.Var | None = None
    flex: int | rx.Var[int] | None = None


class ColumnGroup(PropsBase):
    children: list["ColumnDef | ColumnGroup"] | rx.Var[list["ColumnDef | ColumnGroup"]]
    group_id: str | rx.Var[str]
    marry_children: bool | rx.Var[bool] = False
    open_by_default: bool | rx.Var[bool] = False
    column_group_show: Literal["open", "closed"] | rx.Var[str] = "open"
    header_name: str | rx.Var[str]
    header_tooltip: str | rx.Var[str] | None = None


class AgGridAPI(rx.Base):
    ref: str

    @classmethod
    def create(cls, id: str) -> "AgGridAPI":
        """Create an instance of the AgGridAPI class.

        Args:
            id: The ID of the AgGrid component.

        Returns:
            An instance of the AgGridAPI class.
        """
        return cls(ref=rx.utils.format.format_ref(id))

    @property
    def _api(self) -> rx.Var:
        return f"refs['{self.ref}']?.current?.api"

    def __getattr__(self, name: str) -> Callable[..., rx.event.EventSpec]:
        def _call_api(*args, **kwargs) -> rx.event.EventSpec:
            """Call the ag-grid API method with the given arguments.

            Args:
                *args: Arguments to pass to the API method.
                **kwargs: Keyword arguments to pass to rx.call_script.

            Returns:
                rx.event.EventSpec: The event specification.
            """
            var_args = [str(rx.Var.create(arg)) for arg in args]
            return rx.call_script(
                f"{self._api}.{rx.utils.format.to_camel_case(name)}({', '.join(var_args)})",
                **kwargs,
            )

        return _call_api


class AgGrid(rx.Component):
    """Reflex AgGrid component is a high-performance and highly customizable component that wraps AG Grid, designed for creating rich datagrids."""

    # The library name for the ag-grid-react component
    library: str = "ag-grid-react@32.1.0"

    # The tag name for the AgGridReact component
    tag: str = "AgGridReact"

    # Variable for column definitions
    column_defs: rx.Var[list[dict[str, Any] | ColumnDef | ColumnGroup]]

    # Variable for row data
    row_data: rx.Var[list[dict[str, Any]]]

    # Variable for cell selection
    cell_selection: bool | rx.Var[bool] = False

    # Variable for row selection type
    row_selection: rx.Var[str] = "single"

    # Variable to animate rows
    animate_rows: rx.Var[bool] = False

    # Variable for pagination
    pagination: rx.Var[bool] = False

    # Page size for pagination
    pagination_page_size: rx.Var[int] = rx.Var.create(10)

    # Strategy for auto sizing
    auto_size_strategy: rx.Var[dict] = rx.Var.create({})

    # Selector for pagination page size options
    pagination_page_size_selector: rx.Var[list[int]] = rx.Var.create([10, 25, 50])

    # Variable for the side bar configuration
    side_bar: rx.Var[Union[str, dict[str, Any], bool, list[str]]] = rx.Var.create("")

    # Variable to indicate if tree data is used
    tree_data: rx.Var[bool] = rx.Var.create(False)

    # Default column definition
    default_col_def: rx.Var[dict[str, Any]] = rx.Var.create({})

    # Definition for the auto group column
    auto_group_column_def: rx.Var[Any] = rx.Var.create({})

    # Data for pinned top rows
    pinned_top_row_data: rx.Var[list[dict[str, Any]]] = rx.Var.create([])

    # Data for pinned bottom rows
    pinned_bottom_row_data: rx.Var[list[dict[str, Any]]] = rx.Var.create([])

    # Default expanded group level
    group_default_expanded: rx.Var[int] | None = rx.Var.create(-1)

    # Variable to indicate if group selects children
    group_selects_children: rx.Var[bool] = rx.Var.create(False)

    # Variable to suppress row click selection
    suppress_row_click_selection: rx.Var[bool] = rx.Var.create(False)

    # Event handler for getting the data path
    get_data_path: rx.EventHandler[lambda e0: [e0]]

    # Variable to allow unbalanced groups
    group_allow_unbalanced: rx.Var[bool] = rx.Var.create(False)

    # Variable to show pivot panel
    pivot_panel_show: rx.Var[str] = rx.Var.create("never")

    # Variable to show row group panel
    row_group_panel_show: rx.Var[str] = rx.Var.create("never")

    # Variable to suppress aggregate function in header
    suppress_agg_func_in_header: rx.Var[bool] = rx.Var.create(False)

    # Variable to lock group columns
    group_lock_group_columns: rx.Var[int] = rx.Var.create(0)

    # Variable to maintain column order
    maintain_column_order: rx.Var[bool] = rx.Var.create(False)

    # Row model type for infinite/serverside row model
    row_model_type: rx.Var[str]

    # Cache block size for infinite/serverside row model
    cache_block_size: rx.Var[int]

    # Maximum blocks in cache for infinite/serverside row model
    max_blocks_in_cache: rx.Var[int]

    # Row buffer size for infinite/serverside row model
    row_buffer: rx.Var[int]

    # Cache overflow size for infinite/serverside row model
    cache_overflow_size: rx.Var[int]

    # Maximum concurrent datasource requests for infinite/serverside row model
    max_concurrent_datasource_requests: rx.Var[int]

    # Initial row count for infinite row model
    infinite_initial_row_count: rx.Var[int]

    # Datasource for infinite/serverside row model
    datasource: rx.Var[Datasource]

    # Event handler for getting the row ID
    get_row_id: rx.EventHandler[lambda e0: [e0]]

    # Event handler to check if it is a server-side group
    is_server_side_group: rx.EventHandler[lambda e0: [e0]]

    # Event handler to get the server-side group key
    get_server_side_group_key: rx.EventHandler[lambda e0: [e0]]

    # Server-side datasource for infinite/serverside row model
    server_side_datasource: rx.Var[SSRMDatasource]

    # Event handler to check if server-side group is open by default
    is_server_side_group_open_by_default: rx.EventHandler[lambda e0: [e0]]

    # Variable to enable client-side sort on server-side
    server_side_enable_client_side_sort: rx.Var[bool] = False

    # Event handler to get the child count
    get_child_count: rx.EventHandler[lambda e0: [e0]]

    # Event handler for cell click events
    on_cell_clicked: rx.EventHandler[_on_cell_event_spec]

    # Event handler for cell focused events
    on_cell_focused: rx.EventHandler[_on_cell_event_spec]

    # Event handler for cell mouse over events
    on_cell_mouse_over: rx.EventHandler[_on_cell_event_spec]

    # Event handler for cell mouse out events
    on_cell_mouse_out: rx.EventHandler[_on_cell_event_spec]

    # Event handler for cell double click events
    on_cell_double_clicked: rx.EventHandler[_on_cell_event_spec]

    # Event handler for right click on a cell
    on_cell_context_menu: rx.EventHandler[_on_cell_event_spec]

    # Event handler for row data changed events
    on_cell_value_changed: rx.EventHandler[_on_cell_value_changed]

    # Event handler for row click events
    on_row_clicked: rx.EventHandler[_on_row_event_spec]

    # Event handler for row double click events
    on_row_double_clicked: rx.EventHandler[_on_row_event_spec]

    # Event handler for row selected events
    on_row_selected: rx.EventHandler[_on_row_selected]

    # Event handler for selection change events
    on_selection_changed: rx.EventHandler[_on_selection_change_signature]

    # Event handler for column header clicked events
    on_column_header_clicked: rx.EventHandler[_on_column_event_spec]

    # Event handler for column resized events
    on_column_resized: rx.EventHandler[_on_column_event_spec]

    # Event handler for column moved events
    on_column_moved: rx.EventHandler[_on_column_event_spec]

    # Event handler for column pinned events
    on_column_pinned: rx.EventHandler[_on_column_event_spec]

    # Event handler for column header context menu events
    on_column_header_context_menu: rx.EventHandler[_on_column_event_spec]

    # Event handler for column header focused events
    on_header_focused: rx.EventHandler[_on_column_event_spec]

    # Event handler for first data rendered events
    on_first_data_rendered: rx.EventHandler[_on_cell_event_spec]

    lib_dependencies: list[str] = [
        "ag-grid-community@32.1.0",
        "ag-grid-enterprise@32.1.0",
    ]
    # Change the aesthetic theme of the grid
    theme: rx.Var[Literal["quartz", "balham", "alpine", "material"]]

    # Event handler for when the grid is ready
    on_grid_ready: rx.EventHandler[lambda e0: [e0]]

    @classmethod
    def create(
        cls,
        *children,
        id: str,
        data_path_key: str | None = None,
        is_server_side_group_key: str | None = None,
        get_server_side_group_key: str | None = None,
        server_side_group_open_level: int | None = None,
        child_count_key: str | None = None,
        row_id_key: str | None = None,
        **props,
    ) -> rx.Component:
        props.setdefault("id", id)

        # handle hierarchical data
        if data_path_key is not None:
            props["get_data_path"] = rx.Var(f"(data) => data.{data_path_key}").to(
                rx.EventChain
            )

        if is_server_side_group_key is not None:
            props["is_server_side_group"] = rx.Var(
                f"(data) => data.{is_server_side_group_key}"
            ).to(rx.EventChain)

        if get_server_side_group_key is not None:
            props["get_server_side_group_key"] = rx.Var(
                f"(data) => data.{get_server_side_group_key}",
            ).to(rx.EventChain)

        if server_side_group_open_level is not None:
            props["server_side_group_open_level"] = rx.Var(
                f"(params) => params.rowNode.level < {server_side_group_open_level}"
            ).to(rx.EventChain)

        if child_count_key is not None:
            props["get_child_count"] = rx.Var(
                f"(data) => data ? data.{child_count_key} : undefined"
            ).to(rx.EventChain)

        if row_id_key is not None:
            props["get_row_id"] = rx.Var(f"(params) => params.data.{row_id_key}").to(
                rx.EventChain
            )

        props["class_name"] = rx.match(
            props.get("theme", "quartz"),
            ("quartz", rx.color_mode_cond("ag-theme-quartz", "ag-theme-quartz-dark")),
            ("balham", rx.color_mode_cond("ag-theme-balham", "ag-theme-balham-dark")),
            ("alpine", rx.color_mode_cond("ag-theme-alpine", "ag-theme-alpine-dark")),
            (
                "material",
                rx.color_mode_cond("ag-theme-material", "ag-theme-material-dark"),
            ),
            "",
        )

        if "auto_size_strategy" in props:
            props["on_grid_ready"] = size_columns_to_fit

        return super().create(*children, **props)

    def add_imports(self):
        return {
            "": [
                "ag-grid-community/styles/ag-grid.css",
                "ag-grid-community/styles/ag-theme-quartz.css",
                "ag-grid-community/styles/ag-theme-balham.css",
                "ag-grid-community/styles/ag-theme-material.css",
                "ag-grid-community/styles/ag-theme-alpine.css",
                "ag-grid-enterprise",
            ],
            "d3-format": ["format"],
            "ag-grid-enterprise": [
                "LicenseManager",
            ],
        }

    def add_custom_code(self) -> list[str]:
        ag_grid_license_key = os.getenv("AG_GRID_LICENSE_KEY")
        if ag_grid_license_key is not None:
            return [f"LicenseManager.setLicenseKey('{ag_grid_license_key}');"]
        return ["LicenseManager.setLicenseKey(null);"]

    @property
    def api(self) -> AgGridAPI:
        return AgGridAPI(ref=self.get_ref())

    def get_selected_rows(self, callback: rx.EventHandler) -> rx.event.EventSpec:
        return self.api.getSelectedRows(callback=callback)

    def select_all(self) -> rx.event.EventSpec:
        return self.api.selectAll()

    def deselect_all(self) -> rx.event.EventSpec:
        return self.api.deselectAll()

    def select_rows_by_key(self, keys: list[str]) -> rx.event.EventHandler:
        keys_var = rx.Var.create(keys, _var_is_string=False)
        script = f"""
let api = {self.api};
const selected_nodes = [];
let keys_set = new Set({keys_var});
api.forEachNode(function (node) {{
    if (keys_set.has(node.key)) {{
        selected_nodes.push(node);
    }} 
}});
api.deselectAll()
api.setNodesSelected({{ nodes: selected_nodes, newValue: true }});
"""
        return rx.call_script(script)  # type: ignore

    def log_nodes(self) -> rx.event.EventSpec:
        return rx.call_script(
            f"""
let api = {self.api};
console.log("Logging nodes");
api.forEachNode(function (node) {{
    console.log(node.key);
}});
"""
        )

    def setGridOption(self, key: str, value: rx.Var) -> rx.event.EventSpec:
        return self.api.set_grid_option(key, value)

    def set_datasource(self, datasource: Datasource):
        return self.setGridOption(
            key="datasource",
            value=rx.Var.create(datasource),
        )

    def set_serverside_datasource(self, datasource: SSRMDatasource):
        return self.setGridOption(
            key="serverSideDatasource",
            value=rx.Var.create(datasource, _var_is_string=False),
        )

    def show_loading_overlay(self) -> rx.event.EventSpec:
        return self.api.showLoadingOverlay()

    def show_no_rows_overlay(self) -> rx.event.EventSpec:
        return self.api.showNoRowsOverlay()

    def hide_overlay(self) -> rx.event.EventSpec:
        return self.api.hideOverlay()

    def redraw_rows(self) -> rx.event.EventSpec:
        return self.api.redrawRows()

    def export_data_as_csv(self) -> rx.event.EventSpec:
        """Export the grid data as a CSV file."""
        return self.api.exportDataAsCsv()


class WrappedAgGrid(AgGrid):
    """Reflex AgGrid component is a high-performance and highly customizable component that wraps AG Grid, designed for creating rich datagrids."""

    @classmethod
    def create(cls, *children, **props):
        width = props.pop("width", None)
        height = props.pop("height", None)
        return Div.create(
            super().create(*children, **props),
            width=width or "40vw",
            height=height or "25vh",
        )


class AgGridNamespace(rx.ComponentNamespace):
    api = AgGridAPI.create
    column_def = ColumnDef
    column_group = ColumnGroup
    filters = AGFilters
    editors = AGEditors
    renderers = AGRenderers
    size_columns_to_fit = size_columns_to_fit
    root = AgGrid.create
    __call__ = WrappedAgGrid.create


ag_grid = AgGridNamespace()
