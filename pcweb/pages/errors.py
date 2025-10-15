import reflex as rx

from pcweb import constants
from pcweb.components.webpage.comps import h1_title
from pcweb.flexdown import markdown_with_shiki
from pcweb.templates.webpage import webpage


@rx.memo
def h_comp_error(text: rx.Var[str]) -> rx.Component:
    return rx.el.h3(
        text,
        class_name="font-smbold text-slate-12 text-start",
    )


@rx.memo
def h4_comp_error(text: rx.Var[str]) -> rx.Component:
    return rx.el.h4(
        text,
        class_name="font-smbold text-slate-12 text-start",
    )


@rx.memo
def code_block_error(code: str):
    return rx.box(
        rx._x.code_block(
            code,
            language="python",
            class_name="code-block !bg-slate-1",
        ),
        # class_name="!font-code",
    )


@rx.memo
def markdown_error(text: str):
    return markdown_with_shiki(
        text,
        class_name="font-small text-slate-11 text-start markdown-code",
    )


def error_message(
    heading: str, error_code: str, solution: rx.Component, error_type: str = ""
) -> rx.Component:
    return rx.box(
        rx.accordion.root(
            rx.accordion.item(
                rx.accordion.header(
                    rx.accordion.trigger(
                        rx.box(
                            rx.box(
                                h_comp_error(text=heading),
                                rx.code(error_type, class_name="code-error-style")
                                if error_type != ""
                                else rx.fragment(),
                                class_name="flex flex-row gap-2 items-center",
                            ),
                            rx.text(
                                error_code,
                                class_name="font-code text-violet-9 text-pretty font-medium",
                            ),
                            class_name="flex flex-col gap-2.5 text-start",
                        ),
                        rx.spacer(),
                        rx.accordion.icon(color="var(--c-slate-9)"),
                        class_name="!bg-transparent !hover:bg-transparent !p-4 lg:!p-6 gap-4 lg:gap-32",
                    ),
                ),
                rx.accordion.content(
                    rx.box(
                        *solution,
                        class_name="!p-[0rem_1rem_1rem_1rem] lg:!p-[0rem_1.5rem_1.5rem_1.5rem] font-small text-slate-11 text-start flex flex-col gap-3 [&>code]:!font-code",
                    )
                ),
                class_name="border-none",
            ),
            type="multiple",
            collapsible=True,
            class_name="border-slate-4 !bg-slate-2 p-0 border !rounded-xl w-full !shadow-none",
        ),
        class_name="w-full",
    )


def errors_content() -> rx.Component:
    return rx.box(
        error_message(
            heading="Object null is not iterable",
            error_code="TypeError: object null is not iterable (cannot read property Symbol(Symbol.iterator))",
            solution=[
                h4_comp_error(
                    text="This is caused by using an older version of nodejs."
                ),
                rx.el.ul(
                    rx.el.li(
                        markdown_error(
                            text="Ensure the latest version of reflex is being used: `pip install reflex --upgrade`."
                        )
                    ),
                    rx.el.li(
                        markdown_error(
                            text="Remove the .web and ~/.reflex directories and re-run `reflex init`."
                        )
                    ),
                    class_name="list-disc pl-4 space-y-2",
                ),
            ],
            error_type="Server Error",
        ),
        error_message(
            heading="Hydration failed because the initial UI does not match",
            error_code="Error: Hydration failed because the initial UI does not match what was rendered on the server.",
            solution=[
                h4_comp_error(text="Often caused by incorrect nesting of components"),
                rx.el.ul(
                    rx.el.li(
                        markdown_error(
                            text="Particularly `<p>` and `<div>`, but may also occur with tables"
                        )
                    ),
                    rx.el.li(
                        markdown_error(
                            text="Ensure there are no nested rx.text or layout components within `rx.text`"
                        )
                    ),
                    rx.el.li(
                        markdown_error(
                            text="Ensure that all tables are using `rx.table.header` and `rx.table.body` to wrap the `rx.table.row` rows"
                        )
                    ),
                    class_name="space-y-2 list-disc pl-4",
                ),
                rx.text.strong("No", class_name="text-red-10 font-smbold"),
                code_block_error(
                    code="""rx.text(
    rx.text("foo")
)
rx.text(
    rx.box("foo")
)
rx.text(
    rx.center("foo")
)""",
                ),
                code_block_error(
                    code="""rx.table.root(
    rx.table.row(
        rx.table.column_header_cell("Full name"),
    ),
)""",
                ),
                rx.text.strong("Yes", class_name="text-green-10 font-smbold"),
                code_block_error(
                    code="""rx.text("foo")
rx.box(
    rx.text("foo")
)
rx.center(
    rx.text("foo")
)""",
                ),
                code_block_error(
                    code="""rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Full name"),
        ),
    ),
)""",
                ),
                rx.text(
                    "See upstream docs ",
                    rx.link(
                        "here",
                        href="https://nextjs.org/docs/messages/react-hydration-error",
                        underline="always",
                    ),
                    ".",
                ),
            ],
            error_type="Unhandled Runtime Error",
        ),
        error_message(
            heading="Invalid var passed for prop",
            error_code="TypeError: Invalid var passed for prop href, expected type <class 'str'>, got value {state.my_list.at(i)} of type typing.Any.",
            solution=[
                h4_comp_error(text="Add a type annotation for list Vars"),
                rx.text(
                    "For certain props, reflex validates type correctness of the variable. Especially when de-referencing lists and dicts, it is important to supply the correct annotation."
                ),
                code_block_error(
                    code="""class State(rx.State):
    # NO
    my_list = ["a", "b", "c"]

    # YES
    my_indexable_list: list[str] = ["a", "b", "c"]""",
                    language="python",
                ),
                rx.el.ul(
                    rx.el.li("Add type annotations to all state Vars."),
                    class_name="list-disc pl-4",
                ),
            ],
        ),
        error_message(
            heading="TypeError: metaclass conflict (SQLModel)",
            error_code="TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases",
            solution=[
                h4_comp_error(
                    text="This is caused by importing sqlmodel earlier than reflex."
                ),
                rx.el.ul(
                    rx.el.li("Ensure that reflex is imported before sqlmodel."),
                    class_name="list-disc pl-4",
                ),
            ],
            error_type="Python Error",
        ),
        error_message(
            heading="ImportError: couldn't import psycopg",
            error_code="ImportError: couldn't import psycopg 'python' implementation: libpq library not found | couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary' | couldn't import psycopg 'c' implementation: No module named 'psycopg_c'",
            solution=[
                h4_comp_error(
                    text="This is caused by not installing the correct psycopg package. Solution is to add the `psycopg[binary]==3.2.3` package to your requirements.txt file."
                ),
            ],
            error_type="Import Error",
        ),
        class_name="flex flex-col gap-6 w-full",
    )


@webpage(path="/errors", title="Common Errors · Reflex")
def errors() -> rx.Component:
    return rx.el.section(
        rx.box(
            h1_title(title="Common Errors"),
            rx.box(
                rx.el.h2(
                    "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our ",
                    rx.link(
                        "Discord",
                        underline="always",
                        href=constants.DISCORD_URL,
                        class_name="text-violet-9",
                    ),
                    ".",
                ),
                class_name="font-md text-balance text-slate-10",
            ),
            class_name="section-header",
        ),
        errors_content(),
        id="common-errors",
        class_name="section-content",
    )
