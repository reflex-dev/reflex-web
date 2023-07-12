import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    docheader,
    docpage,
    doctext,
    subheader,
    doclink,
    docalert,
)

code_state_gc = """
class CookieState(State):
    cookie_val: str = "Hello"
    
    def set_cookie(self):
        yield rx.set_cookie("hello", "world")
        self.cookie_val = self.get_cookies().get("hello","")
"""
exec(code_state_gc)
code_gc = """
rx.heading(CookieState.cookie_val)
"""
code_sc = """
rx.button(CookieState.cookie_val, on_click=CookieState.set_cookie)
"""

code_gls = """
rx.button("Copy Local Storage to clipboard", on_click=rx.set_clipboard(rx.get_local_storage("key")))
"""
code_sls = """
rx.button(
    "Set Local Storage", on_click=rx.set_local_storage("key", "value1")
)
"""


@docpage()
def browser():
    return rx.box(
        docheader("Browser Storage"),
        # subheader("Cookies"),
        # doctext(
        #     "If you want to manipulate cookies in your Reflex app, we provide some getters and setters to ",
        #     "manipulate them.",
        # ),
        # doctext(
        #     "To read the value of a cookie, inside an event handler, you can use",
        #     rx.code("self.get_cookies()"),
        # ),
        # # docdemo(code_gc, state=code_state_gc2, comp=eval(code_gc)),
        # doctext(
        #     "To write a cookie, you can use the ",
        #     doclink("special event", href="/docs/api-reference/special-event"),
        #     " ",
        #     rx.code("set_cookie(key , value)"),
        # ),
        # docdemo(code_sc, state=code_state_gc, comp=eval(code_sc)),
        subheader("Local Storage"),
        doctext(
            "Aside from cookies, if for some reason you need to use the Local Storage on your Reflex app, you can do so with:"
        ),
        doctext(
            "To read a local storage variable and pass it to an event handler, you can use"
        ),
        docdemo(code_gls),
        doctext(
            "To write a variable inside the local storage, you can use the ",
            doclink("special event", href="/docs/api-reference/special-events"),
            " ",
            rx.code("rx.set_local_storage(key,value)"),
        ),
        docdemo(code_sls),
        docalert(
            rx.text(
                rx.code("get_local_storage()"),
                " cannot be used for direct rendering",
            ),
            status="warning",
        ),
    )
