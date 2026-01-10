from dataclasses import dataclass

import reflex as rx
import reflex_ui as ui
from reflex.experimental.client_state import ClientStateVar
from pcweb.components.demo_form import demo_form_dialog

from pcweb.constants import PRO_TIERS_TABLE, REFLEX_CLOUD_URL
from pcweb.pages.pricing.calculator import (
    COMPUTE_TABLE,
    CREDITS_PER_HOUR_CPU,
    CREDITS_PER_HOUR_GB,
)

_SORTED_TIERS = sorted(
    [{"key": k, **v} for k, v in PRO_TIERS_TABLE.items()], key=lambda x: x["credits"]
)

machine_keys = list(COMPUTE_TABLE.keys())


def format_number(number: int | float) -> str:
    """Format number with locale string, handling non-numeric values."""
    return rx.Var(
        f"(typeof {number} === 'number' ? {number} : 0).toLocaleString('en-US')"
    ).to(str)


@dataclass
class Machine:
    vcpu: int
    ram: float
    index: int
    weekly_credits: float = 0.0

    @classmethod
    def from_index(cls, index: int) -> "Machine":
        """Create Machine from COMPUTE_TABLE index."""
        machine_key = machine_keys[index]
        specs = COMPUTE_TABLE[machine_key]
        weekly_credits = calculate_weekly_credits(specs["vcpu"], specs["ram"])
        return cls(
            vcpu=specs["vcpu"],
            ram=specs["ram"],
            index=index,
            weekly_credits=weekly_credits,
        )


def calculate_weekly_credits(vcpu: int, ram: float) -> float:
    """Calculate weekly credits for a machine."""
    credits_per_hour = vcpu * CREDITS_PER_HOUR_CPU + ram * CREDITS_PER_HOUR_GB
    return round(credits_per_hour * 24 * 7, 2)


message_tooltip_open_cs = ClientStateVar.create("message_tooltip_open", default=False)
pro_tier_keys = list(PRO_TIERS_TABLE.keys())
COMPUTE_TABLE_KEYS = rx.Var.create(machine_keys)
PRO_TIER_KEYS = rx.Var.create(pro_tier_keys)

MESSAGES_VALUES = [0] + [50 * (2**i) for i in range(9)] + [20000, 0]


def get_is_enterprise_tier(messages_tier_index: int) -> bool:
    """Check if slider is at Enterprise position."""
    return messages_tier_index == len(MESSAGES_VALUES) - 1


def get_message_credits(messages_tier_index: int) -> int:
    """Get credits from message tier slider."""
    return MESSAGES_VALUES[messages_tier_index]


class MachineState(rx.State):
    machines: rx.Field[list[Machine]] = rx.field(default_factory=list)
    messages_tier_index: rx.Field[int] = rx.field(default=0)

    machines_weekly_credits: rx.Field[float] = rx.field(default=0.0)
    current_tier: rx.Field[dict] = rx.field(
        default_factory=lambda: {"key": "Pro", "credits": 0, "price": 0}
    )
    total_credits: rx.Field[str] = rx.field(default="0")
    recommended_tier_info: rx.Field[dict] = rx.field(
        default_factory=lambda: {
            "price": "$0/mo",
            "needs_enterprise": False,
            "name": "Pro Plan",
            "credits": 0,
        }
    )

    def _recalculate_all(self):
        """Recalculate all derived values when state changes."""
        # Calculate machines weekly credits using cached values
        machines_credits = sum(m.weekly_credits for m in self.machines)
        self.machines_weekly_credits = machines_credits

        # Calculate current tier based on message credits
        msg_credits = get_message_credits(self.messages_tier_index)
        is_enterprise = get_is_enterprise_tier(self.messages_tier_index)

        # Early return path for enterprise tier
        if is_enterprise:
            self.current_tier = {
                "key": "Enterprise",
                "credits": msg_credits,
                "price": "custom",
            }
            self.total_credits = "Custom"
            self.recommended_tier_info = {
                "price": "Custom",
                "needs_enterprise": True,
                "name": "Enterprise",
                "credits": "Custom",
            }
            return

        # Non-enterprise path - find tiers once
        current_tier = self._find_tier_for_credits(msg_credits)
        total = msg_credits + machines_credits
        total_tier = self._find_tier_for_credits(total)

        # Set current tier
        self.current_tier = {
            "key": current_tier["key"] if current_tier else "Enterprise",
            "credits": msg_credits,
            "price": current_tier["price"] if current_tier else "custom",
        }

        # Set total credits display
        self.total_credits = f"{total:,}" if total_tier else "Custom"

        # Set recommended tier info
        if total_tier:
            self.recommended_tier_info = {
                "price": f"${total_tier['price']}/mo",
                "needs_enterprise": False,
                "name": f"{total_tier['key']} Plan",
                "credits": total_tier["credits"],
            }
        else:
            self.recommended_tier_info = {
                "price": "Custom",
                "needs_enterprise": True,
                "name": "Enterprise",
                "credits": "Custom",
            }

    @rx.event(temporal=True)
    def add_machine(self):
        self.machines.append(Machine.from_index(0))
        self._recalculate_all()

    @rx.event(temporal=True)
    def remove_machine(self, index: int):
        self.machines = self.machines[:index] + self.machines[index + 1 :]
        self._recalculate_all()

    @rx.event(temporal=True)
    def update_machine(self, index: int, new_machine_index: int):
        self.machines[index] = Machine.from_index(new_machine_index)
        yield
        self._recalculate_all()

    @rx.event(temporal=True)
    def update_messages_tier(self, new_tier_index: int):
        if new_tier_index == self.messages_tier_index:
            return
        self.messages_tier_index = new_tier_index
        yield
        self._recalculate_all()

    def _find_tier_for_credits(self, credits: float) -> dict | None:
        """Find Pro tier that fits the given credits using binary search."""
        for tier in _SORTED_TIERS:
            if credits <= tier["credits"]:
                return tier
        return None

    @rx.event(temporal=True)
    def reset_machines(self):
        self.reset()
        self._recalculate_all()


def total_credits_card() -> rx.Component:
    return rx.el.div(
        rx.el.span(
            "Estimated Credits (Monthly)",
            class_name="text-secondary-12 text-sm font-medium mb-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.cond(
                    get_is_enterprise_tier(MachineState.messages_tier_index),
                    rx.el.span(
                        "Reflex Build Credits (Custom)",
                        class_name="text-secondary-11 text-sm font-medium",
                    ),
                    rx.el.span(
                        f"Reflex Build Credits ({format_number(MachineState.current_tier['credits'])})",
                        class_name="text-secondary-11 text-sm font-medium",
                    ),
                ),
                rx.cond(
                    get_is_enterprise_tier(MachineState.messages_tier_index),
                    rx.el.span(
                        "Custom",
                        class_name="text-secondary-12 text-sm font-medium ml-auto font-mono",
                    ),
                    rx.el.span(
                        format_number(MachineState.current_tier["credits"]),
                        class_name="text-secondary-12 text-sm font-medium font-mono ml-auto",
                    ),
                ),
                class_name="flex flex-row gap-2 items-center justify-between mt-auto",
            ),
            rx.foreach(
                MachineState.machines,
                lambda machine: rx.el.div(
                    rx.el.span(
                        COMPUTE_TABLE_KEYS[machine.index],
                        class_name="text-secondary-11 text-sm font-medium",
                    ),
                    rx.el.span(
                        format_number(machine.weekly_credits),
                        class_name="text-secondary-12 text-sm font-medium font-mono",
                    ),
                    class_name="flex flex-row gap-2 items-center justify-between",
                ),
            ),
            rx.el.div(class_name="h-[0.5px] bg-slate-4 w-full"),
            rx.el.div(
                rx.el.span("Total", class_name="text-secondary-11 text-sm font-medium"),
                rx.el.span(
                    MachineState.total_credits,
                    class_name="text-secondary-12 text-sm font-bold font-mono ml-auto",
                ),
                class_name="flex flex-row gap-2 items-center justify-between",
            ),
            rx.el.div(
                rx.el.span(
                    rx.cond(
                        get_is_enterprise_tier(MachineState.messages_tier_index),
                        rx.el.span(
                            "Get a custom quote for your needs",
                            class_name="text-secondary-12 text-sm font-medium",
                        ),
                        rx.el.div(
                            rx.el.span(
                                f"Pro Plan ({MachineState.recommended_tier_info['price']})",
                                class_name="text-secondary-12 text-sm font-semibold",
                            ),
                            ui.tooltip(
                                trigger=rx.el.span(
                                    ui.icon(
                                        "InformationCircleIcon",
                                        class_name="text-secondary-11 size-4",
                                    ),
                                ),
                                content=f"{format_number(MachineState.recommended_tier_info['credits'])} credits included",
                            ),
                            class_name="flex flex-row gap-2 items-center justify-center",
                        ),
                    ),
                    class_name="text-center",
                ),
                class_name="flex flex-col gap-2 mt-4 pt-2 justify-center",
            ),
            rx.cond(
                get_is_enterprise_tier(MachineState.messages_tier_index),
                demo_form_dialog(
                    trigger=ui.button(
                        "Contact Sales",
                        size="sm",
                        class_name="font-semibold w-full",
                    ),
                ),
                ui.link(
                    render_=ui.button(
                        "Upgrade Now",
                        size="sm",
                        class_name="font-semibold w-full",
                    ),
                    to=f"{REFLEX_CLOUD_URL.rstrip('/')}/?redirect_url={REFLEX_CLOUD_URL.rstrip('/')}/billing/",
                    target="_blank",
                ),
            ),
            class_name="flex flex-col gap-2",
        ),
        class_name="flex flex-col gap-2 lg:min-w-[20rem] lg:border-l border-slate-4 p-6 flex-1 relative",
    )


def messages_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                ui.icon("TokenCircleIcon", class_name="text-secondary-11 size-5"),
                rx.cond(
                    get_is_enterprise_tier(MachineState.messages_tier_index),
                    rx.el.span(
                        "Custom Reflex Build Credits / Month",
                        class_name="text-secondary-12 lg:text-lg text-base font-medium",
                    ),
                    rx.el.span(
                        f"{format_number(MachineState.current_tier['credits'])} Reflex Build Credits / Month",
                        class_name="text-secondary-12 lg:text-lg text-base font-medium",
                    ),
                ),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.el.div(
                rx.cond(
                    get_is_enterprise_tier(MachineState.messages_tier_index),
                    rx.el.span(
                        "Custom",
                        class_name="text-secondary-12 lg:text-lg text-base font-medium",
                    ),
                    rx.el.span(
                        format_number(MachineState.current_tier["credits"]),
                        " Credits",
                        class_name="text-secondary-12 lg:text-lg text-base font-medium font-mono",
                    ),
                ),
                class_name="flex flex-row gap-1.5 items-center",
            ),
            class_name="flex flex-row gap-2 items-center justify-between",
        ),
        ui.slider.root(
            ui.slider.control(
                ui.slider.track(
                    ui.slider.indicator(),
                    ui.tooltip(
                        trigger=ui.slider.thumb(),
                        content=rx.cond(
                            get_is_enterprise_tier(MachineState.messages_tier_index),
                            "Custom",
                            f"{format_number(MachineState.current_tier['credits'])} Messages",
                        ),
                        open=message_tooltip_open_cs.value,
                        side="bottom",
                    ),
                ),
            ),
            min=0,
            max=len(MESSAGES_VALUES) - 1,
            step=1,
            on_value_change=lambda new_tier_index: rx.cond(
                MachineState.messages_tier_index != new_tier_index,
                MachineState.update_messages_tier(new_tier_index).throttle(150),
                rx.noop(),
            ),
            on_value_committed=MachineState.update_messages_tier,
            min_steps_between_values=1,
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
def machine_card(machine: Machine, index: int) -> rx.Component:
    machine_tooltip_open_cs = ClientStateVar.create(
        "machine_tooltip_open", default=False, global_ref=False
    )
    machine_name = COMPUTE_TABLE_KEYS[machine.index]

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
                    f"{machine.vcpu}vCPU / {machine.ram}GB",
                    class_name="text-secondary-12 lg:text-lg text-base font-medium",
                ),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.el.div(
                ui.tooltip(
                    trigger=rx.el.span(
                        ui.icon(
                            "InformationCircleIcon",
                            class_name="text-secondary-11 size-4",
                        ),
                    ),
                    hoverable=False,
                    content="Assuming 7 days of serverless compute.",
                ),
                rx.el.div(
                    rx.el.span(
                        f"{machine.weekly_credits}",
                        class_name="text-secondary-12 lg:text-lg text-base font-medium font-mono",
                    ),
                    rx.el.span(
                        " Credits",
                        class_name="text-secondary-11 lg:text-base text-sm font-medium",
                    ),
                    class_name="flex flex-row gap-1 items-baseline",
                ),
                class_name="flex flex-row gap-1.5 items-center",
            ),
            class_name="flex flex-row gap-2 items-center justify-between",
        ),
        ui.slider.root(
            ui.slider.control(
                ui.slider.track(
                    ui.slider.indicator(),
                    ui.tooltip(
                        trigger=ui.slider.thumb(),
                        content=machine_name,
                        open=machine_tooltip_open_cs.value,
                        side="bottom",
                    ),
                ),
            ),
            min=0,
            max=COMPUTE_TABLE_KEYS.length() - 1,
            step=1,
            value=machine.index,
            min_steps_between_values=1,
            on_value_change=lambda new_machine_index: rx.cond(
                machine.index != new_machine_index,
                MachineState.update_machine(index, new_machine_index).throttle(150),
                rx.noop(),
            ),
            on_value_committed=lambda new_machine_index: MachineState.update_machine(
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
                class_name="text-slate-12 lg:text-3xl text-2xl font-semibold text-center",
            ),
            rx.el.h2(
                "Only pay for what you use, nothing more.",
                class_name="text-slate-9 text-2xl font-semibold text-center",
            ),
            class_name="flex flex-col gap-1 justify-center border-b border-slate-4 w-full mx-auto px-6 pb-10",
        ),
        rx.el.div(
            rx.el.div(
                messages_card(),
                rx.foreach(
                    MachineState.machines,
                    lambda machine, index: machine_card(machine=machine, index=index),
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
            total_credits_card(),
            class_name="flex lg:flex-row flex-col lg:gap-10 gap-6 w-full px-6 h-full",
        ),
        class_name="flex flex-col w-full max-w-[64.19rem] border-t-0 2xl:border-x divide-y divide-slate-4 2xl:border-b pt-[6rem] justify-center items-center",
    )
