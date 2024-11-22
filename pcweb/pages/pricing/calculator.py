import reflex as rx
from typing import Optional
from reflex.event import EventType, BASE_STATE
from .button import button
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
    estimated_cpu_number: int = 0
    estimated_ram_gb: int = 0
    estimated_seats: int = 1

    @rx.var(cache=True)
    def seat_rate(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 19
        elif self.selected_plan == Tiers.TEAM.value:
            return 29

    @rx.var(cache=True)
    def max_seats(self) -> int:
        if self.selected_plan == Tiers.PRO.value:
            return 5
        elif self.selected_plan == Tiers.TEAM.value:
            return 15

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
    def change_plan(self, plan: str) -> None:
        self.selected_plan = plan
        if plan == Tiers.PRO.value:
            if self.estimated_cpu_number > 5:
                self.estimated_cpu_number = 5
            if self.estimated_ram_gb > 10:
                self.estimated_ram_gb = 10
            if self.estimated_seats > 5:
                self.estimated_seats = 5


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
                    min_value=0,
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
                    min_value=0,
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
        rx.text(
            f"Total: ${round(BillingState.estimated_seats * BillingState.seat_rate + BillingState.estimated_ram_gb * (BillingState.mem_rate * MONTH_MINUTES) + BillingState.estimated_cpu_number * (BillingState.cpu_rate * MONTH_MINUTES))}/month",
            class_name="text-base font-medium text-slate-12 text-center mt-6",
        ),
        class_name="flex-1 flex flex-col relative h-full w-full max-w-[25rem] pb-2.5 z-[2]",
    )


def header() -> rx.Component:
    return rx.box(
        rx.el.h3(
            "Calculate costs.",
            class_name="text-slate-12 text-3xl font-semibold text-center",
        ),
        rx.el.p(
            "Simply usage based pricing.",
            class_name="text-slate-9 text-3xl font-semibold text-center",
        ),
        class_name="flex items-center justify-between text-slate-11 flex-col pt-[5rem] 2xl:border-x border-slate-4 max-w-[64.125rem] mx-auto w-full",
    )


def tag_item(tag: str):
    return rx.el.button(
        rx.text(
            tag,
            class_name="font-small shrink-0",
            color=rx.cond(
                BillingState.selected_plan == tag,
                "var(--c-white-1)",
                "var(--c-slate-9)",
            ),
        ),
        class_name="flex items-center justify-center px-3 py-1.5 cursor-pointer transition-bg shrink-0",
        background_=rx.cond(
            BillingState.selected_plan == tag,
            "var(--c-violet-9)",
            "var(--c-slate-2)",
        ),
        _hover={
            "background": rx.cond(
                BillingState.selected_plan == tag,
                "var(--c-violet-9)",
                "var(--c-slate-3)",
            )
        },
        on_click=BillingState.change_plan(tag),
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
            tag_item(Tiers.PRO.value),
            tag_item(Tiers.TEAM.value),
            class_name="shadow-large bg-slate-1 rounded-lg border border-slate-3 flex items-center divide-x divide-slate-3 mt-8 mb-12 relative overflow-hidden z-[1] overflow-x-auto",
        ),
        class_name="relative",
    )


def calculator_section() -> rx.Component:
    return rx.el.section(
        header(),
        filtering_tags(),
        pricing_widget(),
        class_name="flex flex-col w-full max-w-[64.19rem] 2xl:border-x border-slate-4 2xl:border-b pb-[6rem] justify-center items-center",
    )
