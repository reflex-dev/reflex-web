import reflex as rx
import reflex_ui as ui


def comparison_title(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        ui.icon(icon, stroke_width=1.5, class_name="shrink-0 lg:size-7 size-6"),
        rx.el.span(
            title,
            class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-lg text-base font-[575]",
        ),
        class_name="flex flex-row items-center gap-3 lg:p-12 p-6 border-y border-r border-m-slate-4 dark:border-m-slate-10",
    )


def pros_card(pros: list[str]) -> rx.Component:
    return rx.el.ul(
        *[
            rx.el.li(
                ui.icon(
                    "Tick02Icon",
                    class_name="shrink-0 text-primary-9 dark:text-primary-10 h-[1.5rem]",
                ),
                rx.el.span(
                    pro,
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
                ),
                class_name="flex flex-row items-start gap-2.5",
            )
            for pro in pros
        ],
        class_name="list-inside flex flex-col gap-2 lg:p-12 p-6 [box-shadow:0_0_0_1px_rgba(0,_0,_0,_0.12)_inset,_0_6px_12px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_6px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none rounded-xl bg-white-1 dark:bg-m-slate-11 w-full",
    )


def cons_card(cons: list[str]) -> rx.Component:
    return rx.el.ul(
        *[
            rx.el.li(
                ui.icon(
                    "MultiplicationSignIcon",
                    stroke_width=1.5,
                    class_name="shrink-0 text-m-slate-7 dark:text-m-slate-6 h-[1.5rem]",
                ),
                rx.el.span(
                    con,
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525]",
                ),
                class_name="flex flex-row items-start gap-2.5",
            )
            for con in cons
        ],
        class_name="list-inside flex flex-col gap-2 lg:p-12 p-6 w-full lg:border-x border-l border-m-slate-4 dark:border-m-slate-10",
    )


def pros_cons_cards(pros: list[str], cons: list[str]) -> rx.Component:
    return rx.el.div(
        pros_card(pros),
        cons_card(cons),
        class_name="grid lg:grid-cols-2 grid-cols-1 max-lg:border-r",
    )


def top_title(title: str) -> rx.Component:
    return rx.el.span(
        title,
        class_name="text-m-slate-12 dark:text-m-slate-3 text-xs leading-[1.5rem] font-medium font-mono border-r border-m-slate-4 dark:border-m-slate-10 lg:px-8 lg:py-3 p-6 bg-secondary-1 dark:bg-m-slate-10 border-t",
    )


def comparison_cards() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            top_title("Reflex"),
            top_title("Retool, Streamlit, Plotly Dash, Power BI"),
            class_name="grid grid-cols-2",
        ),
        comparison_title("Full Control Without the Ceiling", "CodesandboxIcon"),
        pros_cons_cards(
            [
                "Write real Python — no ceiling on what you can build",
                "Handle custom logic, complex data flows, and performance optimization natively",
                "Build anything a full-stack app can do",
            ],
            [
                "Get you to v1 fast, then you hit walls",
                "Custom logic and complex data flows require ugly workarounds",
                "Platform limitations dictate what's possible, not your requirements",
            ],
        ),
        comparison_title("You Own Your Code", "SourceCodeSquareIcon"),
        pros_cons_cards(
            [
                "It's your Python code — deploy it anywhere",
                "Full version control with Git",
                "Never hostage to a platform's pricing or shutdown",
            ],
            [
                "Your app lives on their infrastructure in their proprietary format",
                "Vendor lock-in makes migration painful or impossible",
                "Pricing changes or platform shutdowns put your app at risk",
            ],
        ),
        comparison_title("Python Ecosystem Access", "PythonIcon"),
        pros_cons_cards(
            [
                "Use libraries you already know — pandas, scikit-learn, whatever",
                "Build internal tools or customer-facing apps in one language",
                "Leverage the entire Python ecosystem with no restrictions",
            ],
            [
                "Limited to the platform's pre-built integrations",
                "Can't tap into Python's ML, data science, or backend libraries",
                "Forces non-JS developers to learn new tools or work around limitations",
            ],
        ),
        comparison_title("Scales With Complexity", "SquareArrowExpand02Icon"),
        pros_cons_cards(
            [
                "Auth flows, real-time features, complex state management — all native",
                "Handles growing complexity because it's just code",
                "No artificial boundaries on what you can build",
            ],
            [
                "Great for simple CRUD apps and dashboards, then it breaks down",
                "Once you need real complexity, you're fighting the tool instead of building",
                "Workarounds pile up and become unmaintainable",
            ],
        ),
        comparison_title(
            "Team Collaboration & Engineering Practices", "UserSwitchIcon"
        ),
        pros_cons_cards(
            [
                "Fits into normal engineering workflows — Git, PRs, CI/CD",
                "Code review and automated testing work out of the box",
                "Your whole team can collaborate using standard dev practices",
            ],
            [
                "Version control is difficult or impossible",
                "Code review and testing are afterthoughts at best",
                "Engineering best practices don't apply to proprietary drag-and-drop formats",
            ],
        ),
        rx.el.div(
            class_name="absolute -top-24 right-0 w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -top-24 -left-px w-px h-24 bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 max-lg:hidden"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 right-0 w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        rx.el.div(
            class_name="absolute -bottom-24 -left-px w-px h-24 bg-gradient-to-b from-current to-transparent text-m-slate-4 dark:text-m-slate-10"
        ),
        class_name="flex flex-col w-full max-w-[45rem] ml-auto border-l border-m-slate-4 dark:border-m-slate-10 mt-18 border-b mb-24 relative",
    )


def compare() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Compare",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-m-slate-6",
                ),
                rx.el.h1(
                    "How You Benefit ",
                    rx.el.br(class_name="max-lg:hidden"),
                    "With Reflex vs. ",
                    rx.el.br(class_name="max-lg:hidden"),
                    "Other Approaches",
                    class_name="text-m-slate-12 dark:text-m-slate-3 text-3xl font-[575]",
                ),
                rx.el.h2(
                    "No-code tools get you started fast, but Reflex lets you finish. Here's how Reflex compares to platforms like Retool, Streamlit, Plotly Dash, and Power BI.",
                    class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
                ),
                class_name="flex flex-col gap-6 lg:max-w-[18rem] lg:sticky lg:top-[11rem] lg:self-start max-lg:self-center max-lg:items-center max-lg:text-center",
            ),
            comparison_cards(),
            class_name="flex lg:flex-row flex-col max-lg:gap-6 max-w-(--docs-layout-max-width) mx-auto relative py-24 max-lg:px-6",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full relative",
    )
