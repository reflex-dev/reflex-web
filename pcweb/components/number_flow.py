import reflex as rx


class NumberFlow(rx.Component):
    library = "@number-flow/react"

    tag = "NumberFlow"

    is_default = True

    # The numeric value to display and animate
    # NumberFlow will automatically transition when this prop changes
    value: rx.Var[int | str | float]

    # The locale(s) for number formatting (e.g., "en-US", "de-DE")
    # Accepts Intl.LocalesArgument format
    # Default: "en-US"
    locales: rx.Var[str] = rx.Var.create("en-US")

    # Custom prefix string to display before the number
    # Example: "$" for currency display
    prefix: rx.Var[str]

    # Custom suffix string to display after the number
    # Example: "/mo" for monthly pricing, "%" for percentages
    suffix: rx.Var[str]

    # If true, NumberFlow's transitions are isolated from other layout changes
    # that may occur in the same update. Has no effect when inside NumberFlowGroup.
    # Default: false
    isolate: rx.Var[bool]

    # Controls whether animations are enabled
    # Can be set to false to disable all animations and finish current ones
    # Useful for scenarios like input fields where you want instant updates
    # Default: true
    animated: rx.Var[bool]

    # If true, applies CSS will-change properties to relevant elements
    # Useful if your number changes frequently or you experience unwanted repositioning
    # Note: Excessive use can result in excessive memory usage
    # Default: false
    will_change: rx.Var[bool]

    # Controls the direction of digit animations
    # "+1": digits always go up
    # "0": each digit goes up if increasing, down if decreasing (no overall trend)
    # "-1": digits always go down
    # Can also be a function: (oldValue: number, value: number) => number
    # Default: "+1" (which corresponds to Math.sign(value - oldValue))
    trend: rx.Var[str] = rx.Var.create("+1")


number_flow = NumberFlow.create
