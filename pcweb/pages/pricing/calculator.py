import reflex as rx
from typing import Optional
from reflex.event import EventType, BASE_STATE
from .button import button
from .plan_cards import radial_circle
import enum

MONTH_MINUTES = 60 * 24 * 30


class Tiers(enum.Enum):
    PRO = "Pro"
    TEAM = "Team"


class BillingState(rx.State):
    selected_plan: str = Tiers.PRO.value
    # Rates
    cpu_rate: float = 0.000463
    mem_rate: float = 0.000231

    # Estimated numbers for the widget calculator
    estimated_cpu_number: int = 1
    estimated_ram_gb: int = 1
    estimated_seats: int = 1

    @rx.var(cache=True)
    def seat_rate(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 20
        elif self.selected_plan == Tiers.TEAM.value:
            return 50

    @rx.var(cache=True)
    def max_seats(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 5
        elif self.selected_plan == Tiers.TEAM.value:
            return 25

    @rx.var(cache=True)
    def max_cpu(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 5
        elif self.selected_plan == Tiers.TEAM.value:
            return 32

    @rx.var(cache=True)
    def max_ram(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 10
        elif self.selected_plan == Tiers.TEAM.value:
            return 64

    @rx.event
    def change_plan(self, plan: str | list[str]) -> None:
        self.selected_plan = plan[0] if isinstance(plan, list) else plan
        if plan == Tiers.PRO.value:
            self.included_cpu = 1
            self.included_ram = 0.5
            self.included_seats = 1
            # Enforce Pro tier limits
            self.estimated_cpu_number = min(self.estimated_cpu_number, 5)
            self.estimated_ram_gb = min(self.estimated_ram_gb, 10)
            self.estimated_seats = min(self.estimated_seats, 5)
        else:
            self.included_cpu = 2
            self.included_ram = 3
            self.included_seats = 5
            # Enforce Team tier minimum seats
            self.estimated_seats = max(5, self.estimated_seats)


def calculator(text: str, component: rx.Component, total: str) -> rx.Component:
    return rx.box(
        rx.text(text, class_name="text-sm text-slate-12 font-medium text-nowrap"),
        rx.box(component, class_name="flex justify-center items-center mx-auto"),
        rx.text(total, class_name="text-sm text-slate-9 font-medium text-right"),
        class_name="grid grid-cols-3 items-center gap-4",
    )


def stepper(
    value: rx.Var[int],
    default_value: str,
    min_value: int,
    max_value: int,
    on_click_decrement: Optional[EventType[[], BASE_STATE]],
    on_click_increment: Optional[EventType[[], BASE_STATE]],
) -> rx.Component:
    return rx.box(
        # Number of seats/cpu/tam
        rx.box(
            rx.el.input(
                value=value,
                placeholder="0",
                default_value=default_value,
                min=min_value,
                max=max_value,
                name="token_days",
                on_click=on_click_decrement,
                max_length=1000,
                class_name="flex flex-row flex-1 gap-2 px-2.5 py-1.5 font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 absolute left-0 h-full bg-transparent w-[4rem] pointer-events-none",
                type="number",
                style={
                    "appearance": "textfield",
                    "-webkit-appearance": "textfield",
                    "-moz-appearance": "textfield",
                    "&::-webkit-inner-spin-button": {"-webkit-appearance": "none"},
                    "&::-webkit-outer-spin-button": {"-webkit-appearance": "none"},
                },
            ),
            rx.box(
                button(
                    icon=rx.icon(
                        "minus",
                    ),
                    variant="transparent",
                    size="icon-xs",
                    disabled=rx.cond(
                        value <= min_value,
                        True,
                        False,
                    ),
                    type="button",
                    on_click=on_click_decrement,
                ),
                button(
                    icon=rx.icon(
                        "plus",
                    ),
                    variant="transparent",
                    size="icon-xs",
                    disabled=rx.cond(
                        value >= max_value,
                        True,
                        False,
                    ),
                    type="button",
                    on_click=on_click_increment,
                ),
                class_name="flex flex-row items-center absolute right-0 border-l border-slate-5 h-full px-1 gap-1",
            ),
            class_name="!w-[8.5rem] relative border-slate-5 bg-slate-1 border rounded-[0.625rem] h-[2.25rem] flex items-center",
        ),
        class_name="flex flex-row gap-2.5 h-[2.25rem]",
    )


def pricing_widget() -> rx.Component:
    return rx.box(
        rx.box(
            # Tier
            calculator(
                "Tier",
                rx.box(
                    rx.segmented_control.root(
                        rx.segmented_control.item("Pro", value="Pro"),
                        # rx.segmented_control.item("Team (coming soon)", value="Team"),
                        on_change=BillingState.change_plan,
                        default_value="Pro",
                        width="100%",
                    ),
                    class_name="flex flex-row pt-2 !w-[8.5rem] !h-[2.25rem] mb-2",
                ),
                "",
            ),
            # Team seats
            calculator(
                "Members",
                stepper(
                    BillingState.estimated_seats,
                    default_value="1",
                    min_value=1,
                    max_value=BillingState.max_seats,
                    on_click_decrement=BillingState.setvar(
                        "estimated_seats", (BillingState.estimated_seats - 1)
                    ),
                    on_click_increment=BillingState.setvar(
                        "estimated_seats", (BillingState.estimated_seats + 1)
                    ),
                ),
                f"${BillingState.estimated_seats * BillingState.seat_rate}",
            ),
            # GB RAM
            calculator(
                "GB RAM",
                stepper(
                    BillingState.estimated_ram_gb,
                    default_value="1",
                    min_value=1,
                    max_value=BillingState.max_ram,
                    on_click_decrement=BillingState.setvar(
                        "estimated_ram_gb", (BillingState.estimated_ram_gb - 1)
                    ),
                    on_click_increment=BillingState.setvar(
                        "estimated_ram_gb", (BillingState.estimated_ram_gb + 1)
                    ),
                ),
                f"${round(BillingState.estimated_ram_gb * (BillingState.mem_rate * MONTH_MINUTES))}",
            ),
            # CPU
            calculator(
                "CPU",
                stepper(
                    BillingState.estimated_cpu_number,
                    default_value="0",
                    min_value=1,
                    max_value=BillingState.max_cpu,
                    on_click_decrement=BillingState.setvar(
                        "estimated_cpu_number", (BillingState.estimated_cpu_number - 1)
                    ),
                    on_click_increment=BillingState.setvar(
                        "estimated_cpu_number", (BillingState.estimated_cpu_number + 1)
                    ),
                ),
                f"${round(BillingState.estimated_cpu_number * (BillingState.cpu_rate * MONTH_MINUTES))}",
            ),
            class_name="flex flex-col gap-2",
        ),
        # Total 1 month
        rx.center(
            rx.flex(
                rx.badge(
                    f"Total: ${calculate_total()}- $20 free credits = ",
                    rx.text.strong(f"${calculate_total()-20}/mo"),
                    size="3",
                ),
                class_name="mt-6",
            )
        ),
        class_name="flex-1 flex flex-col relative h-full w-full max-w-[25rem] pb-2.5 z-[2]",
    )


def calculate_total():
    # Base price using rx.cond
    base_price = rx.cond(BillingState.selected_plan == Tiers.PRO.value, 20, 250)

    # Calculate additional seats cost
    additional_seats = rx.cond(
        BillingState.estimated_seats > 1, BillingState.estimated_seats - 1, 0
    )
    seat_cost = additional_seats * BillingState.seat_rate

    compute_cost = (BillingState.estimated_ram_gb) * (
        BillingState.mem_rate * MONTH_MINUTES
    ) + (BillingState.estimated_cpu_number) * (BillingState.cpu_rate * MONTH_MINUTES)

    total = base_price + seat_cost + compute_cost
    return round(total)


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


def filtering_tags():
    return rx.box(
        # Glow
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="216" height="88" viewBox="0 0 216 88" fill="none">
  <path d="M0 44C0 68.3005 48.3532 88 108 88C167.647 88 216 68.3005 216 44C216 19.6995 167.647 0 108 0C48.3532 0 0 19.6995 0 44Z" fill="url(#paint0_radial_13427_11205)"/>
  <defs>
    <radialGradient id="paint0_radial_13427_11205" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(108 44) rotate(90) scale(44 108)">
      <stop stop-color="var(--c-violet-3)"/>
      <stop offset="1" stop-color="var(--c-slate-2)" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>
""",
            class_name="w-[13.5rem] h-[5.5rem] shrink-0 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-[0] pointer-events-none -mt-2",
        ),
        rx.box(
            rx.segmented_control.root(
                rx.segmented_control.item(Tiers.PRO.value, value=Tiers.PRO.value),
                rx.segmented_control.item(Tiers.TEAM.value, value=Tiers.TEAM.value),
                on_change=BillingState.change_plan,
                value=BillingState.selected_plan,
                class_name="shadow-large bg-slate-1 rounded-lg border border-slate-3",
            ),
            class_name="mb-5 relative z-[1] overflow-x-auto",
        ),
        class_name="relative",
    )


def calculator_section() -> rx.Component:
    return rx.el.section(
        header(),
        rx.box(
            radial_circle(),
            rx.box(
                rx.flex(
                    # filtering_tags(),
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
                align_items="center",
                width="100%",
            ),
            rx.box(pricing_widget()),
            class_name="flex flex-col p-8 border border-slate-4 rounded-[1.125rem] shadow-small bg-slate-2 relative z-[1]",
        ),
        class_name="flex flex-col w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem] justify-center items-center",
    )
