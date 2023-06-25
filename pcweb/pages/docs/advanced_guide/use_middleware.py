import reflex as rx

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader


@docpage()
def use_middleware():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.styling.overview import styling_overview

    return rx.box(
        docheader("Middleware", first=True),
        doctext(
            "Middleware allows you to run custom code during the handling of events in your app. "
        ),
        subheader("Example: Logging"),
        doctext(
            "Reflex includes a built in middleware that logs all events to the console. "
            "Let's see how it works. "
        ),
        doccode(
            """class LoggingMiddleware(rx.Middleware):

    def preprocess(self, app, state, event):
        print(f"Event {event}")

    def postprocess(self, app, state, event, update):
        print(f"Update {update}")"""
        ),
        doctext(
            "Middleware classes must inherit from ",
            rx.code("rx.Middleware"),
            ". ",
            "They have two functions that can be overridden: ",
            rx.code("preprocess"),
            " and ",
            rx.code("postprocess"),
            ". ",
        ),
        doctext(
            "The logging middleware just logs the incoming event before it is processed, and the delta after the state is updated. "
            "More complicated middleware can modify the actual event or state along the way. "
        ),
        doctext("You can add middleware during app creation. "),
        doccode(
            """app = rx.App(
                middleware=[LoggingMiddleware()]
            )"""
        ),
    )
