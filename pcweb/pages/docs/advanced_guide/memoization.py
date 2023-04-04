import pynecone as pc

from pcweb.templates.docpage import doccode, docdemo, docheader, docpage, doctext


code1 = """
@pc.memo
def fixed_header(text: str) -> pc.Component:
    \"""A fixed header that doesn't change when the state changes.\"""
    return pc.heading(text)
"""
exec(code1)
code2 = """fixed_header(text="This Heading Won't Rerender")"""


@docpage()
def memoization():
    return pc.box(
        docheader("Memoization", first=True),
        doctext(
            "By default, Pynecone will re-render the entire page every time the state changes. "
            "This is fine for small apps, but can be slow for larger apps. "
        ),
        doctext(
            "You can prevent unnecessary rendering by memoizing components, which can greatly improve your apps performance. ",
            "Just add the ",
            pc.code("@pc.memo"),
            " decorator to a component function to make it memoized, ",
            " and list its props as arguments. ",
        ),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.box(
                    pc.alert_title(
                        "Only components that don't depend on the state can be memoized."
                    ),
                    pc.alert_description(
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
