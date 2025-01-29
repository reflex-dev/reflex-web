import reflex as rx

from pcweb.components.tabs import tabs

COMPUTE_TABLE = {
    "c1m.5": {"vcpu": 1, "ram": 0.5, "price_per_min": 0.000073},
    "c1m1": {"vcpu": 1, "ram": 1, "price_per_min": 0.000131},
    "c1m2": {"vcpu": 1, "ram": 2, "price_per_min": 0.000248},
    "c2m2": {"vcpu": 2, "ram": 2, "price_per_min": 0.000263},
    "c4m4": {"vcpu": 4, "ram": 4, "price_per_min": 0.000495},
    "c4m8": {"vcpu": 4, "ram": 8, "price_per_min": 0.00099},
}


def table_header(cost_text: str) -> rx.Component:
    return rx.box(
        rx.text("Machine", class_name="text-sm font-medium text-slate-12"),
        rx.text("vCPU", class_name="text-sm font-medium text-slate-12"),
        rx.text("GB RAM", class_name="text-sm font-medium text-slate-12"),
        rx.text(cost_text, class_name="text-sm font-medium text-slate-12 text-end"),
        class_name="grid grid-cols-4 gap-4 px-6 py-3 border-b border-slate-4",
    )


def table_row(name: str, cpu: str, ram: str, cost: str) -> rx.Component:
    return rx.box(
        rx.box(
            name,
            class_name="px-1.5 w-fit text-slate-12 border-slate-6 h-5 rounded-md border justify-start items-center gap-0.5 inline-flex bg-slate-1 text-xs font-medium shrink-0",
        ),
        rx.text(cpu, class_name="font-medium text-sm text-slate-9"),
        rx.text(ram, class_name="font-medium text-sm text-slate-9"),
        rx.text(cost, class_name="font-medium text-sm text-slate-9 text-end"),
        class_name="grid grid-cols-4 gap-4 px-6 py-2 border-b border-slate-4",
    )


def min_table(cost_text: str) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                f"${specs['price_per_min']:.6f}",
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        class_name="w-full",
    )


def hour_table(cost_text: str) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                f"${(specs['price_per_min'] * 60):.6f}",
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
                f"${specs['price_per_min'] * 60 * 24 * 30:.2f}",
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        class_name="w-full",
    )


def compute_table() -> rx.Component:
    return rx.box(
        tabs.root(
            rx.box(
                tabs.list(
                    tabs.tab(
                        "Per min",
                        value="min",
                    ),
                    tabs.tab(
                        "Per hour",
                        value="hour",
                    ),
                    tabs.tab(
                        "Per month",
                        value="month",
                    ),
                    tabs.indicator(),
                ),
                class_name="flex flex-row gap-2 items-center justify-end p-6 border-b border-slate-4",
            ),
            tabs.panel(
                min_table("Cost / min"),
                value="min",
            ),
            tabs.panel(
                hour_table("Cost / hour"),
                value="hour",
            ),
            tabs.panel(
                month_table("Cost / month (Reserved)"),
                value="month",
            ),
            default_value="min",
        ),
        class_name="flex flex-col w-full mt-5",
    )


def header() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Cost Estimate",
            class_name="text-slate-12 text-3xl font-semibold text-center",
            id="calculator-header",
        ),
        rx.el.p(
            "Get a price estimate for your organization.",
            class_name="text-slate-9 text-2xl font-semibold text-center",
        ),
        class_name="flex items-center mb-5 justify-between text-slate-11 flex-col pt-[5rem] mx-auto w-full",
    )


def calculator_section() -> rx.Component:
    return rx.el.section(
        header(),
        compute_table(),
        class_name="flex flex-col w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem] justify-center items-center",
    )
