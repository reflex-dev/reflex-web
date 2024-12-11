import reflex as rx

from reflex.base import Base
from reflex.config import get_config
from reflex.utils import format
from reflex.utils.imports import ImportVar
from reflex.utils.serializers import serialize


class Datasource(Base):
    uri: str | None = None
    endpoint_uri: str | None = None
    rowCount: rx.Var[int] | int | None = None
    getRows: rx.Var | None = None

    def get_uri(self) -> str:
        return self.uri or (
            f"{self.endpoint_uri}?"
            "start=${params.startRow}"
            "&end=${params.endRow}"
            "&sort_model=${encodeURIComponent(JSON.stringify(params.sortModel))}"
            "&filter_model=${encodeURIComponent(JSON.stringify(params.filterModel))}"
        )

    def _get_rows_function(self) -> str | rx.Var:
        uri = f"getBackendURL(`{get_config().api_url}{self.get_uri()}`)"
        js_func = (
            """
(params) => {
    fetch(%s, {
        headers: {"X-Reflex-Client-Token": token},
    })
    .then((response) => response.json()
        .then((data) => params.successCallback(
            data,
            data.length < params.endRow - params.startRow ? params.startRow + data.length : -1,
        ))
    )
    .catch((error) => params.failCallback())
}
"""
            % uri
        )
        return rx.Var.create_safe(
            js_func.replace("\n", ""),
            _var_is_local=False,
            _var_is_string=False,
            _var_data=rx.vars.VarData(
                imports={
                    "/utils/state": [
                        ImportVar(tag="getBackendURL"),
                        ImportVar(tag="token"),
                    ],
                }
            ),
        )

    def dict(self, **kwargs):
        d = super().dict(**kwargs)
        d.pop("uri", None)
        if self.getRows is None:
            d["getRows"] = self._get_rows_function()
        return d

    def json(self) -> str:
        """Convert the object to a json-like string.

        Vars will be unwrapped so they can represent actual JS var names and functions.

        Keys will be converted to camelCase.

        Returns:
            The object as a Javascript Object literal.
        """
        d = self.dict(exclude={"uri"})
        if self.getRows is None:
            d["getRows"] = self._get_rows_function()
        return format.unwrap_vars(
            self.__config__.json_dumps(
                {format.to_camel_case(key): value for key, value in d.items()},
                default=serialize,
            )
        )


class SSRMDatasource(Base):
    uri: str | None = None
    endpoint_uri: str | None = None
    getRows: rx.Var | None = None

    def get_uri(self) -> str:
        return self.uri or (
            f"{self.endpoint_uri}?"
            "start=${params.request.startRow}"
            "&end=${params.request.endRow}"
            "&rowGroupCols=${encodeURIComponent(JSON.stringify(params.request.rowGroupCols))}"
            "&groupKeys=${encodeURIComponent(JSON.stringify(params.request.groupKeys))}"
            "&valueCols=${encodeURIComponent(JSON.stringify(params.request.valueCols))}"
            "&pivotMode=${params.request.pivotMode}"
            "&sortModel=${encodeURIComponent(JSON.stringify(params.request.sortModel))}"
            "&filterModel=${encodeURIComponent(JSON.stringify(params.request.filterModel))}"
            "&pivotCols=${encodeURIComponent(JSON.stringify(params.request.pivotCols))}"
        )

    def _get_rows_function(self) -> str | rx.Var:
        uri = f"getBackendURL(`{get_config().api_url}{self.get_uri()}`)"
        js_func = (
            """
(params) => {
    fetch(%s, {
        headers: {"X-Reflex-Client-Token": token},
    })
    .then((response) => response.json()
        .then((data) => {
            params.success(data)
        })
    )
    .catch((error) => params.fail())
}
"""
            % uri
        )
        return rx.Var.create_safe(
            js_func.replace("\n", ""),
            _var_is_local=False,
            _var_is_string=False,
            _var_data=rx.vars.VarData(
                imports={
                    "/utils/state": [
                        ImportVar(tag="getBackendURL"),
                        ImportVar(tag="token"),
                    ],
                }
            ),
        )

    def json(self) -> str:
        """Convert the object to a json-like string.

        Vars will be unwrapped so they can represent actual JS var names and functions.

        Keys will be converted to camelCase.

        Returns:
            The object as a Javascript Object literal.
        """
        d = self.dict(exclude={"uri"})
        if self.getRows is None:
            d["getRows"] = self._get_rows_function()
        return format.unwrap_vars(
            self.__config__.json_dumps(
                {format.to_camel_case(key): value for key, value in d.items()},
                default=serialize,
            )
        )
