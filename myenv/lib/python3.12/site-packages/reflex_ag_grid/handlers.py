"""Handlers for the reflex_ag_grid component."""

import datetime
from typing import Any, Type, TypeVar

from sqlmodel import not_, and_, or_
from sqlmodel.sql.expression import SelectOfScalar
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.roles import WhereHavingRole

import reflex as rx

M = TypeVar("M", bound=rx.Model)


def handle_text_filter(value, filter_def) -> bool:
    type = filter_def.get("type", "contains")
    filter = filter_def.get("filter", "")
    if type == "contains":
        return filter in value
    if type == "notContains":
        return filter not in value
    if type == "equals":
        return value == filter
    if type == "notEqual":
        return value != filter
    if type == "startsWith":
        return value.startswith(filter)
    if type == "endsWith":
        return value.endswith(filter)
    if type == "blank":
        return not value
    if type == "notBlank":
        return bool(value)
    assert False, f"type {type} does not exist"


def handle_number_filter(value, filter_def) -> bool:
    type = filter_def.get("type", "equals")
    filter = filter_def.get("filter")
    if type == "equals":
        return value == filter
    if type == "notEqual":
        return value != filter
    if type == "greaterThan":
        return value > filter
    if type == "greaterThanOrEqual":
        return value >= filter
    if type == "lessThan":
        return value < filter
    if type == "lessThanOrEqual":
        return value <= filter
    if type == "inRange":
        return filter <= value <= filter_def.get("filterTo")
    if type == "blank":
        return not value
    if type == "notBlank":
        return bool(value)

    assert False, f"type {type} does not exist"


def handle_filter_def(value, filter_def) -> bool:
    if not filter_def:
        return True
    operator = filter_def.get("operator", "").lower()
    if operator == "and":
        return all(
            handle_filter_def(value, sub_filter)
            for sub_filter in filter_def.get("conditions", [])
        )
    elif operator == "or":
        return any(
            handle_filter_def(value, sub_filter)
            for sub_filter in filter_def.get("conditions", [])
        )
    filter_type = filter_def.get("filterType", "text")
    if filter_type == "text":
        return handle_text_filter(value, filter_def)
    if filter_type == "number":
        return handle_number_filter(value, filter_def)
    return False


def handle_filter_model(row, filter_model) -> bool:
    if not filter_model:
        return True
    for field, filter_def in filter_model.items():
        try:
            if not handle_filter_def(row[field], filter_def):
                return False
        except Exception as e:
            print(f"Error filtering {field} of {row}: {e}")
            return False
    return True


_sql_operations = {
    "and": and_,
    "or": or_,
}


def where_text_filter(
    value: InstrumentedAttribute, filter_def: dict[str, str]
) -> WhereHavingRole:
    type = filter_def.get("type", "contains")
    filter = filter_def.get("filter", "")
    if type == "contains":
        return value.contains(filter)
    if type == "notContains":
        return not_(value.contains(filter))
    if type == "equals":
        return value == filter
    if type == "notEqual":
        return value != filter
    if type == "startsWith":
        return value.startswith(filter)
    if type == "endsWith":
        return value.endswith(filter)
    if type == "blank":
        return or_(value == None, value == "")  # noqa: E711
    if type == "notBlank":
        return and_(value != None, value != "")  # noqa: E711
    assert False, f"type {type} does not exist"


def where_number_filter(
    value: InstrumentedAttribute, filter_def: dict[str, str | int | float]
) -> WhereHavingRole:
    type = filter_def.get("type", "equals")
    to_filter = None
    if filter_def.get("filterType") == "date":
        filter = datetime.datetime.fromisoformat(filter_def.get("dateFrom"))
        if filter_def.get("dateTo"):
            to_filter = datetime.datetime.fromisoformat(filter_def.get("dateTo"))
    else:
        filter = filter_def.get("filter", 0)
        if filter_def.get("filterTo"):
            to_filter = filter_def.get("filterTo")
    if type == "equals":
        return value == filter
    if type == "notEqual":
        return value != filter
    if type == "greaterThan":
        return value > filter
    if type == "greaterThanOrEqual":
        return value >= filter
    if type == "lessThan":
        return value < filter
    if type == "lessThanOrEqual":
        return value <= filter
    if type == "inRange":
        return and_(
            value >= filter,
            value <= to_filter,
        )
    if type == "blank":
        return value == None  # noqa: E711
    if type == "notBlank":
        return value != None  # noqa: E711

    assert False, f"type {type} does not exist"


def where_filter_def(
    value: InstrumentedAttribute, filter_def: dict[str, Any]
) -> WhereHavingRole | None:
    if not filter_def:
        return
    operator = _sql_operations.get(
        filter_def.get("operator", "").lower(),
    )
    if operator:
        return operator(
            *(
                where_filter_def(value, sub_filter)
                for sub_filter in filter_def.get("conditions", [])
            )
        )
    filter_type = filter_def.get("filterType", "text")
    if filter_type == "text":
        return where_text_filter(value, filter_def)
    if filter_type in ("number", "date"):
        return where_number_filter(value, filter_def)


def apply_filter_model(
    model: Type[M], filter_model: dict[str, dict[str, Any]]
) -> SelectOfScalar[M]:
    query = model.select()
    for field, filter_def in filter_model.items():
        filter_applies = where_filter_def(
            value=getattr(model, field),
            filter_def=filter_def,
        )
        if filter_applies is not None:
            query = query.where(filter_applies)
    return query


def apply_sort_model(
    model: Type[M], query: SelectOfScalar[M], sort_model: list[dict[str, str]]
) -> SelectOfScalar[M]:
    for sort_spec in sort_model:
        field = getattr(model, sort_spec["colId"], None)
        if field is None:
            continue
        query = query.order_by(
            field.desc() if sort_spec["sort"] == "desc" else field.asc()
        )
    return query
