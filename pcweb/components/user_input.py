from typing import List, Optional, Union

import reflex as rx
from reflex.event import EventHandler, EventSpec
from reflex.vars.base import get_unique_variable_name

from pcweb.components.icons import get_icon
from pcweb.components.utils.twmerge import cn
from pcweb.components.icons.hugeicons import hi


def user_input(
    placeholder: str = "",
    name: str = "",
    input_id: str = "",
    input_cn: str = "",
    type_: str = "text",
    clear_button_event: list[EventHandler | EventSpec] | None = None,
    class_name: str = "",
    **props,
) -> rx.Component:
    """Create a basic input component.

    Args:
        placeholder: Placeholder text for the input.
        name: Name of the input.
        input_id: ID of the input.
        input_cn: Additional Tailwind CSS class for input.
        type_: Type of the input.
        clear_button_event: Event to trigger when clear button is clicked.
        class_name: Additional CSS classes to apply to the input component.
        **props: Additional props to pass to the input element.

    Returns:
        rx.Component: A basic input component.

    """
    if not input_id:
        input_id = get_unique_variable_name()
    return rx.box(
        rx.el.input(
            placeholder=placeholder,
            name=name,
            id=input_id,
            class_name=cn(
                "box-border flex flex-row flex-1 gap-2 border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
                input_cn,
            ),
            type=type_,
            custom_attrs={
                "autoComplete": "off",
                "autoCorrect": "off",
                "data-vaul-no-drag": "",
            },
            **props,
        ),
        rx.el.button(
            get_icon("cancel-circle"),
            class_name="right-0 z-10 absolute inset-y-0 flex items-center opacity-100 peer-placeholder-shown:opacity-0 pr-2.5 text-slate-9 hover:text-slate-12 transition-bg peer-placeholder-shown:pointer-events-none peer-disabled:pointer-events-none peer-disabled:hidden",
            content_editable=False,
            on_click=[
                rx.set_value(input_id, ""),
                *([clear_button_event] if clear_button_event is not None else []),
            ],
            on_mouse_down=rx.prevent_default,
            type="button",
            tab_index=-1,
        ),
        class_name=cn("relative flex", class_name),
    )


def input(
    placeholder: str = "",
    name: str = "",
    id: str = "",
    input_cn: str = "",
    form_cn: str = "",
    icon: str = "",
    type_: str = "text",
    clear_button_event: Optional[List[Union[EventHandler, EventSpec]]] = None,
    class_name: str = "",
    **props,
) -> rx.Component:
    """Create an input component with clear functionality.

    Args:
        placeholder (str): Placeholder text for the input. Defaults to "".
        name (str): Name of the input. Defaults to "".
        id (str): ID of the input. Defaults to "".
        input_cn (str): Additional Tailwind CSS class for input. Defaults to "".
        form_cn (str): Additional Tailwind CSS class for form. Defaults to "".
        icon (str): Icon to display in the input. Defaults to "".
        type_ (str): Type of the input. Defaults to "text".
        clear_button_event (Optional[EventType[[]]]): Event to trigger when clear button is clicked. Defaults to None.
        **props: Additional properties to pass to the form element.

    Returns:
        rx.Component: A form component containing the input and clear button.

    """
    padding_left_cn = "pl-8" if icon else "pl-2.5"
    icon_component = (
        rx.box(
            hi(
                icon,
                class_name="!text-slate-9 pointer-events-none",
            ),
            class_name="left-0 z-10 absolute inset-y-0 flex items-center pl-2.5",
        )
        if icon
        else rx.fragment()
    )
    id = get_unique_variable_name()
    return rx.box(
        icon_component,
        rx.el.input(
            placeholder=placeholder,
            name=name,
            id=id,
            class_name=f"box-border flex flex-row flex-1 gap-2 border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer {padding_left_cn} {input_cn}",
            type=type_,
            custom_attrs={"autoComplete": "off", "autoCorrect": "off"},
            **props,
        ),
        rx.el.button(
            get_icon("cancel-circle"),
            class_name="right-0 z-10 absolute inset-y-0 flex items-center opacity-100 peer-placeholder-shown:opacity-0 pr-2.5 text-slate-9 hover:text-slate-12 transition-bg peer-placeholder-shown:pointer-events-none",
            content_editable=False,
            on_click=[
                rx.set_value(id, ""),
                *([clear_button_event] if clear_button_event is not None else []),
            ],
            on_mouse_down=rx.prevent_default,
            type="button",
            tab_index=-1,
        ),
        class_name=f"relative flex w-full {form_cn} {class_name}",
    )
