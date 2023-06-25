import reflex as rx

from pcweb.templates.docpage import doccode, docdemo, docheader, docpage, doctext


code1 = """
@rx.memo
def fixed_header(text: str) -> rx.Component:
    \"""A fixed header that doesn't change when the state changes.\"""
    return rx.heading(text)
"""
exec(code1)
code2 = """fixed_header(text="This Heading Won't Rerender")"""


@docpage()
def memoization():
    return rx.box(
        docheader("Memoization", first=True),
        doctext(
            "By default, Reflex will re-render the entire page every time the state changes. "
            "This is fine for small apps, but can be slow for larger apps. "
        ),
        doctext(
            "You can prevent unnecessary rendering by memoizing components, which can greatly improve your app's performance. ",
            "Just add the ",
            rx.code("@rx.memo"),
            " decorator to a component function to make it memoized, ",
            " and list its props as arguments. ",
        ),
        doctext(
            rx.alert(
                rx.alert_icon(),
                rx.box(
                    rx.alert_title(
                        "Only components that don't depend on the state can be memoized."
                    ),
                    rx.alert_description(
                        "Memoized components aren't re-rendered when the state changes. "
                    ),
                ),
                status="warning",
            ),
        ),
        doctext(
            "The memoized component can be used like any other component. ",
            "Use keyword arguments to pass in the component's props. ",
        ),
        docdemo(code2, state=code1, comp=eval(code2), context=True),
    )
