import reflex as rx
from reflex.experimental.client_state import ClientStateVar
from pcweb.components.tabs import tabs
import reflex_ui as ui

collapsed_calculator_cs = ClientStateVar.create("collapsed_calculator", default=True)

CREDITS_PER_HOUR_CPU = 0.2
CREDITS_PER_HOUR_GB = 0.5

COMPUTE_TABLE = {
    "c1m.5": {"vcpu": 1, "ram": 0.5},
    "c1m1": {"vcpu": 1, "ram": 1},
    "c1m2": {"vcpu": 1, "ram": 2},
    "c2m2": {"vcpu": 2, "ram": 2},
    "c2m4": {"vcpu": 2, "ram": 4},
    "c4m4": {"vcpu": 4, "ram": 4},
    "c4m8": {"vcpu": 4, "ram": 8},
}


def table_header(cost_text: str) -> rx.Component:
    return rx.box(
        rx.text("Machine", class_name="text-sm font-semibold text-slate-12"),
        rx.text("vCPU", class_name="text-sm font-semibold text-slate-12"),
        rx.text("GB RAM", class_name="text-sm font-semibold text-slate-12"),
        rx.el.div(
            ui.icon("TokenCircleIcon", class_name="text-slate-9 size-4"),
            rx.text(
                cost_text, class_name="text-sm font-semibold text-slate-12 text-end"
            ),
            class_name="flex flex-row gap-1 items-center justify-end",
        ),
        class_name="grid grid-cols-4 gap-4 px-6 py-3 border-b border-slate-4",
    )


def table_row(name: str, cpu: str, ram: str, cost: str | rx.Component) -> rx.Component:
    return rx.box(
        rx.box(
            name,
            class_name="px-2 w-fit text-slate-12 border-slate-6 h-5 rounded-md border justify-start items-center gap-0.5 inline-flex bg-slate-1 text-sm font-medium shrink-0",
        ),
        rx.text(cpu, class_name="font-medium text-sm text-slate-9"),
        rx.text(ram, class_name="font-medium text-sm text-slate-9"),
        (
            rx.text(cost, class_name="font-medium text-sm text-slate-9 text-end")
            if isinstance(cost, str)
            else cost
        ),
        class_name="grid grid-cols-4 gap-4 px-6 py-2 border-b border-slate-4 hover:bg-slate-2",
    )


def learn_more():
    return rx.box(
        rx.el.p(
            "Learn more about how we calculate ",
            rx.el.a(
                "compute costs",
                href="/docs/hosting/compute",
                class_name="text-sm font-medium text-slate-10 underline",
            ),
            " only when your app is being used.",
            class_name="text-sm font-medium text-slate-9",
        ),
    )


def min_table(cost_text: str, description: bool = False) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                rx.el.span(
                    rx.el.span(
                        f"{(specs['vcpu'] * CREDITS_PER_HOUR_CPU + specs['ram'] * CREDITS_PER_HOUR_GB) / 60:.3f}",
                        class_name="font-medium text-sm text-slate-9",
                    ),
                    class_name="flex flex-row gap-1 items-center justify-end",
                ),
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        class_name="w-full",
    )


def hour_table(cost_text: str, description: bool = False) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                rx.el.span(
                    rx.el.span(
                        f"{specs['vcpu'] * CREDITS_PER_HOUR_CPU + specs['ram'] * CREDITS_PER_HOUR_GB:.3f}",
                        class_name="font-medium text-sm text-slate-9",
                    ),
                    class_name="flex flex-row gap-1 items-center justify-end",
                ),
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        class_name="w-full",
    )


def month_table(cost_text: str) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                rx.el.span(
                    rx.el.span(
                        f"{specs['vcpu'] * CREDITS_PER_HOUR_CPU + specs['ram'] * CREDITS_PER_HOUR_GB:.3f}",
                        class_name="font-medium text-sm text-slate-9",
                    ),
                    class_name="flex flex-row gap-1 items-center justify-end",
                ),
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        class_name="w-full",
    )


def compute_table() -> rx.Component:
    return rx.box(
        tabs.root(
            rx.box(
                learn_more(),
                tabs.list(
                    tabs.tab(
                        "Per min",
                        value="min",
                    ),
                    tabs.tab(
                        "Per hour",
                        value="hour",
                    ),
                    tabs.indicator(),
                ),
                class_name="flex flex-col lg:flex-row gap-4 items-center justify-center lg:justify-between p-6 border-b border-slate-4",
            ),
            tabs.panel(
                min_table("Credits / min", description=True),
                value="min",
            ),
            tabs.panel(
                hour_table("Credits / hour", description=True),
                value="hour",
            ),
            default_value="min",
        ),
        class_name="flex flex-col w-full relative data-[collapsed=true]:max-h-[11.5rem] data-[collapsed=true]:overflow-hidden transition-all",
        data_collapsed=collapsed_calculator_cs.value,
    )


def compute_table_base() -> rx.Component:
    return rx.box(
        tabs.root(
            rx.box(
                rx.vstack(
                    rx.el.h3(
                        "Machine Sizes",
                        class_name="text-slate-11 text-lg font-semibold",
                    ),
                    align_items="left",
                    justify_content="center`",
                ),
                rx.spacer(),
                tabs.list(
                    tabs.tab(
                        "Per min",
                        value="min",
                    ),
                    tabs.tab(
                        "Per hour",
                        value="hour",
                    ),
                    tabs.indicator(),
                ),
                class_name="flex flex-row gap-2 items-center justify-end pb-6 border-b border-slate-4",
            ),
            tabs.panel(
                min_table("Credits / min"),
                value="min",
            ),
            tabs.panel(
                hour_table("Credits / hour"),
                value="hour",
            ),
            default_value="min",
        ),
        class_name="flex flex-col w-full py-6",
    )


def calculator_section() -> rx.Component:
    return rx.el.section(
        compute_table(),
        rx.el.div(
            rx.cond(
                collapsed_calculator_cs.value,
                rx.el.div(
                    class_name="from-slate-1 to-transparent absolute z-10 transition-opacity pointer-events-none opacity-100 bg-linear-to-t -top-27 left-0 w-full h-29",
                ),
            ),
            ui.button(
                ui.icon(
                    "ArrowDown01Icon",
                    size=16,
                    class_name=(
                        "transition-all",
                        rx.cond(collapsed_calculator_cs.value, "", "rotate-180"),
                    ),
                ),
                rx.cond(
                    collapsed_calculator_cs.value,
                    "Expand Compute Pricing",
                    "Collapse Compute Pricing",
                ),
                on_click=collapsed_calculator_cs.set_value(
                    ~collapsed_calculator_cs.value
                ),
                size="sm",
                variant="outline",
                class_name="w-full",
            ),
            class_name="w-full p-2 relative",
        ),
        class_name="flex flex-col w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem] justify-center items-center",
    )
