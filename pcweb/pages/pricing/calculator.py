import reflex as rx

from pcweb.components.tabs import tabs

COMPUTE_TABLE = {
    "c1m.5": {"vcpu": 1, "ram": 0.5, "pph": 0.046},
    "c1m1": {"vcpu": 1, "ram": 1, "pph": 0.083},
    "c1m2": {"vcpu": 1, "ram": 2, "pph": 0.157},
    "c2m2": {"vcpu": 2, "ram": 2, "pph": 0.166},
    "c2m4": {"vcpu": 2, "ram": 4, "pph": 0.312},
    "c4m4": {"vcpu": 4, "ram": 4, "pph": 0.332},
    "c4m8": {"vcpu": 4, "ram": 8, "pph": 0.625},
}


def table_header(cost_text: str) -> rx.Component:
    return rx.box(
        rx.text("Machine", class_name="text-sm font-semibold text-slate-12"),
        rx.text("vCPU", class_name="text-sm font-semibold text-slate-12"),
        rx.text("GB RAM", class_name="text-sm font-semibold text-slate-12"),
        rx.text(cost_text, class_name="text-sm font-semibold text-slate-12 text-end"),
        class_name="grid grid-cols-4 gap-4 px-6 py-3 border-b border-slate-4",
    )


def table_row(name: str, cpu: str, ram: str, cost: str) -> rx.Component:
    return rx.box(
        rx.box(
            name,
            class_name="px-2 w-fit text-slate-12 border-slate-6 h-5 rounded-md border justify-start items-center gap-0.5 inline-flex bg-slate-1 text-sm font-medium shrink-0",
        ),
        rx.text(cpu, class_name="font-medium text-sm text-slate-9"),
        rx.text(ram, class_name="font-medium text-sm text-slate-9"),
        rx.text(cost, class_name="font-medium text-sm text-slate-9 text-end"),
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
        class_name="px-6 py-4 border-b border-slate-4 hover:bg-slate-2",
    )


def min_table(cost_text: str, description: bool = False) -> rx.Component:
    return rx.box(
        table_header(cost_text),
        *[
            table_row(
                name,
                str(specs["vcpu"]),
                str(specs["ram"]),
                f"${specs['pph'] / 60:.6f}",
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        learn_more() if description else rx.fragment(),
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
                f"${specs['pph']:.3f}",
            )
            for name, specs in COMPUTE_TABLE.items()
        ],
        learn_more() if description else rx.fragment(),
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
                rx.vstack(
                    rx.el.h3(
                        "Compute Pricing",
                        class_name="text-slate-12 text-3xl font-semibold",
                    ),
                    rx.el.p(
                        "Only pay when your app is being used, nothing more.",
                        class_name="text-slate-9 text-lg font-semibold",
                    ),
                    align_items="left",
                    justify_content="center`",
                    class_name="flex flex-col gap-1",
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
                class_name="flex flex-row gap-2 items-center justify-end p-6 border-b border-slate-4",
            ),
            tabs.panel(
                min_table("Cost / min", description=True),
                value="min",
            ),
            tabs.panel(
                hour_table("Cost / hour", description=True),
                value="hour",
            ),
            default_value="min",
        ),
        class_name="flex flex-col w-full mt-5 py-24",
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
                min_table("Cost / min"),
                value="min",
            ),
            tabs.panel(
                hour_table("Cost / hour"),
                value="hour",
            ),
            default_value="min",
        ),
        class_name="flex flex-col w-full py-6",
    )


def calculator_section() -> rx.Component:
    return rx.el.section(
        compute_table(),
        class_name="flex flex-col w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem] justify-center items-center",
    )
