import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar
from pcweb.pages.pricing.calculator import COMPUTE_TABLE

MESSAGE_COST = 0.2
PRO_PLAN_COST = 50

messages_cs = ClientStateVar.create("messages_value", default=0)
message_tooltip_open_cs = ClientStateVar.create("message_tooltip_open", default=False)
machine_keys = list(COMPUTE_TABLE.keys())
COMPUTE_TABLE_VAR = rx.Var.create(COMPUTE_TABLE)
COMPUTE_TABLE_KEYS = rx.Var.create(machine_keys)


class MachineState(rx.State):
    machines: rx.Field[list[int]] = rx.field(default_factory=list)

    @rx.event(temporal=True)
    def add_machine(self):
        self.machines.append(0)

    @rx.event(temporal=True)
    def remove_machine(self, index: int):
        self.machines = self.machines[:index] + self.machines[index + 1 :]

    @rx.event(temporal=True)
    def update_machine(self, index: int, new_machine_index: int):
        self.machines[index] = new_machine_index

    @rx.var
    def total_cost(self) -> float:
        return (
            sum(
                COMPUTE_TABLE[machine_keys[machine_index]]["pph"] * 24 * 30
                for machine_index in self.machines
            )
            + PRO_PLAN_COST
        )

    @rx.event
    def reset_machines(self):
        self.reset()


def total_cost_card() -> rx.Component:
    return rx.el.div(
        rx.el.span(
            "Estimated Cost (Monthly)",
            class_name="text-secondary-12 text-sm font-medium mb-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Pro Plan", class_name="text-secondary-11 text-sm font-medium"
                ),
                rx.el.span(
                    f"${PRO_PLAN_COST}",
                    class_name="text-secondary-12 text-sm font-medium font-mono ml-auto",
                ),
                class_name="flex flex-row gap-2 items-center justify-between mt-auto",
            ),
            rx.el.div(
                rx.el.span(
                    "Extra Credits", class_name="text-secondary-11 text-sm font-medium"
                ),
                rx.el.span(
                    f"${round(messages_cs.value * MESSAGE_COST, 2)}",
                    class_name="text-secondary-12 text-sm font-medium font-mono ml-auto",
                ),
                class_name="flex flex-row gap-2 items-center justify-between mt-auto",
            ),
            rx.foreach(
                MachineState.machines,
                lambda machine_index: rx.el.div(
                    rx.el.span(
                        COMPUTE_TABLE_KEYS[machine_index],
                        class_name="text-secondary-11 text-sm font-medium",
                    ),
                    rx.el.span(
                        f"${round(COMPUTE_TABLE_VAR[COMPUTE_TABLE_KEYS[machine_index]]['pph'] * 24 * 30, 2)}",
                        class_name="text-secondary-12 text-sm font-medium font-mono ml-auto",
                    ),
                    class_name="flex flex-row gap-2 items-center justify-between",
                ),
            ),
            rx.el.div(class_name="h-[0.5px] bg-slate-4 w-full"),
            rx.el.div(
                rx.el.span("Total", class_name="text-secondary-11 text-sm font-medium"),
                rx.el.span(
                    f"${round(MachineState.total_cost + (messages_cs.value * MESSAGE_COST), 2)}",
                    class_name="text-secondary-12 text-sm font-bold font-mono ml-auto",
                ),
                class_name="flex flex-row gap-2 items-center justify-between",
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="flex flex-col gap-2 lg:min-w-[20rem] lg:border-l border-slate-4 p-6 flex-1 relative",
    )


def messages_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                ui.icon("StarCircleIcon", class_name="text-secondary-11 size-5"),
                rx.el.span(
                    "Credits (Messages)",
                    class_name="text-secondary-12 lg:text-lg text-base font-medium",
                ),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.el.span(
                f"${round(messages_cs.value * MESSAGE_COST, 2)}",
                class_name="text-secondary-12 lg:text-lg text-base font-medium font-mono",
            ),
            class_name="flex flex-row gap-2 items-center justify-between",
        ),
        ui.slider.root(
            ui.slider.control(
                ui.slider.control(
                    ui.slider.track(
                        ui.slider.indicator(),
                        ui.tooltip(
                            trigger=ui.slider.thumb(),
                            content=f"{messages_cs.value} Credits",
                            open=message_tooltip_open_cs.value,
                            side="bottom",
                        ),
                    ),
                ),
            ),
            min=0,
            max=10000,
            step=1,
            value=messages_cs.value,
            on_value_change=messages_cs.set_value,
            class_name="w-full max-w-full",
        ),
        on_mouse_enter=message_tooltip_open_cs.set_value(True),
        on_mouse_leave=message_tooltip_open_cs.set_value(False),
        class_name=ui.cn(
            ui.card.class_names.ROOT,
            "w-full lg:p-6 p-4 flex flex-col gap-4 bg-secondary-1",
        ),
    )


@rx.memo
def machine_card(machine_index: rx.Var[int], index: int) -> rx.Component:
    machine_tooltip_open_cs = ClientStateVar.create(
        "machine_tooltip_open", default=False, global_ref=False
    )

    return rx.el.div(
        rx.el.button(
            ui.icon("MultiplicationSignIcon", class_name="text-secondary-1 size-4"),
            on_click=MachineState.remove_machine(index),
            class_name="absolute -top-1 -right-1 z-10 size-5 flex items-center justify-center rounded-full bg-secondary-12 hover:bg-secondary-11 transition-colors lg:opacity-0 group-hover:opacity-100",
        ),
        rx.el.div(
            rx.el.div(
                ui.icon("ComputerIcon", class_name="text-secondary-11 size-5"),
                rx.el.span(
                    f"{COMPUTE_TABLE_VAR[COMPUTE_TABLE_KEYS[machine_index]]['vcpu']}vCPU / {COMPUTE_TABLE_VAR[COMPUTE_TABLE_KEYS[machine_index]]['ram']}GB",
                    class_name="text-secondary-12 lg:text-lg text-base font-medium",
                ),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.el.span(
                f"${round(COMPUTE_TABLE_VAR[COMPUTE_TABLE_KEYS[machine_index]]['pph'] * 24 * 30, 2)}",
                class_name="text-secondary-12 lg:text-lg text-base font-medium font-mono",
            ),
            class_name="flex flex-row gap-2 items-center justify-between",
        ),
        ui.slider.root(
            ui.slider.control(
                ui.slider.control(
                    ui.slider.track(
                        ui.slider.indicator(),
                        ui.tooltip(
                            trigger=ui.slider.thumb(),
                            content=COMPUTE_TABLE_KEYS[machine_index],
                            open=machine_tooltip_open_cs.value,
                            side="bottom",
                        ),
                    ),
                ),
            ),
            min=0,
            max=COMPUTE_TABLE_KEYS.length() - 1,
            step=1,
            value=machine_index,
            on_value_change=lambda new_machine_index: MachineState.update_machine(
                index, new_machine_index
            ),
            class_name="w-full max-w-full",
        ),
        on_mouse_enter=machine_tooltip_open_cs.set_value(True),
        on_mouse_leave=machine_tooltip_open_cs.set_value(False),
        class_name=ui.cn(
            ui.card.class_names.ROOT,
            "w-full lg:p-6 p-4 flex flex-col gap-4 bg-secondary-1 relative group",
        ),
    )


def slider_calculator() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "Pricing Calculator",
                class_name="text-slate-12 lg:text-3xl text-2xl font-semibold text-start",
            ),
            rx.el.h2(
                "Only pay for what you use, nothing more.",
                class_name="text-slate-9 text-lg font-semibold text-start",
            ),
            class_name="flex flex-col gap-2 justify-start border-b border-slate-4 w-full mx-auto px-6 pb-10",
        ),
        rx.el.div(
            rx.el.div(
                messages_card(),
                rx.foreach(
                    MachineState.machines,
                    lambda machine_index, index: machine_card(
                        machine_index=machine_index, index=index
                    ),
                ),
                ui.button(
                    ui.icon("PlusSignIcon"),
                    "Add App",
                    variant="secondary",
                    size="sm",
                    class_name="w-full",
                    on_click=MachineState.add_machine,
                ),
                class_name="flex flex-col gap-4 w-full py-6",
            ),
            total_cost_card(),
            class_name="flex lg:flex-row flex-col lg:gap-10 gap-6 w-full px-6 h-full",
        ),
        on_mount=MachineState.reset_machines,
        class_name="flex flex-col w-full max-w-[64.19rem] border-t-0 2xl:border-x divide-y divide-slate-4 2xl:border-b pt-[4rem] justify-center items-center",
    )
