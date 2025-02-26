import reflex as rx


def timer():
    remove_negative_sign = rx.vars.function.ArgsFunctionOperation.create(
        args_names=("t",),
        return_expr=rx.vars.sequence.string_replace_operation(
            rx.Var("t").to(str), "-", ""
        ),
    )

    return rx.box(
        rx.text("Launch in", class_name="font-small font-medium text-slate-9"),
        rx.moment(
            date="2024-12-05T00:00:00",
            duration_from_now=True,
            format="DD[d] HH[h] mm[m] ss[s]",
            class_name="text-3xl font-semibold text-slate-12 countdown text-nowrap",
            custom_attrs={"filter": remove_negative_sign},
            interval=1000,
        ),
        class_name="absolute top-[18.25rem] left-1/2 -translate-x-1/2 flex flex-col gap-1 text-center",
    )
