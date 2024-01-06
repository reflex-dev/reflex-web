import reflex as rx

from pcweb.templates.docpage import docdemo, doctext

code36 = """rx.vstack(
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Error Reflex version is out of date."),
        status="error",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Warning Reflex version is out of date."),
        status="warning",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is 0.1.32."),
        status="info",
    ),
    width="100%",
)
"""
code37 = """rx.vstack(
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        rx.alert_description("No need to update."),
        status="success",
        variant="subtle",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
        variant="solid",
    ),
    rx.alert(
        rx.alert_icon(),
        rx.alert_title("Reflex version is up to date."),
        status="success",
        variant="top-accent",
    ),
    width="100%",
)
"""


# Feedback
def render_alert():
    return rx.vstack(
        doctext(
            "Alerts are used to communicate a state that affects a system, feature or page. An example of the different alert statuses is shown below."
        ),
        docdemo(code36),
        doctext(
            "Along with different status types, alerts can also have different style variants and an optional description. By default the variant is 'subtle'."
        ),
        docdemo(code37),
        align_items="start",
    )


code38 = """rx.hstack(
    rx.circular_progress(value=0),
    rx.circular_progress(value=25),
    rx.circular_progress(rx.circular_progress_label(50), value=50),
    rx.circular_progress(value=75),
    rx.circular_progress(value=100),
    rx.circular_progress(is_indeterminate=True),
)
"""


def render_circularprogress():
    return rx.vstack(
        doctext(
            "The CircularProgress component is used to indicate the progress for determinate and indeterminate processes. Determinate progress: fills the circular track with color, as the indicator moves from 0 to 360 degrees. Indeterminate progress: grows and shrinks the indicator while moving along the circular track."
        ),
        docdemo(code38),
        align_items="start",
    )


code39 = """rx.vstack(
    rx.progress(value=0, width="100%"),
    rx.progress(value=50, width="100%"),
    rx.progress(value=75, width="100%"),
    rx.progress(value=100, width="100%"),
    rx.progress(is_indeterminate=True, width="100%"),
    spacing="1em",
    min_width=["10em", "20em"],
)"""


def render_progress():
    return rx.vstack(
        doctext(
            "Progress is used to display the progress status for a task that takes a long time or consists of several steps."
        ),
        docdemo(code39),
        align_items="start",
    )


code40 = """rx.stack(
    rx.skeleton(height="10px", speed=1.5),
    rx.skeleton(height="15px", speed=1.5),
    rx.skeleton(height="20px", speed=1.5),
    width="50%",
)
"""
code41 = """rx.stack(
    rx.skeleton_circle(size="30px"),
    rx.skeleton_text(no_of_lines=8),
    width="50%",
)
"""
code42 = """rx.stack(
    rx.skeleton_text(
        no_of_lines=5, start_color="pink.500", end_color="orange.500"
    ),
    width="50%",
)
"""
code43 = """rx.vstack(
    rx.skeleton(rx.text("Text is already loaded."), is_loaded=True),
    rx.skeleton(rx.text("Text is already loaded."), is_loaded=False),
)
"""


def render_skeleton():
    return rx.vstack(
        doctext("Skeleton is used to display the loading state of some components."),
        docdemo(code40),
        doctext(
            "Along with the basic skeleton box there are also a skeleton circle and text for ease of use."
        ),
        docdemo(code41),
        doctext(
            "Another feature of skeleton is the ability to animate colors. We provide the args start_color and end_color to animate the color of the skeleton component(s)."
        ),
        docdemo(code42),
        doctext(
            "You can prevent the skeleton from loading by using the ",
            rx.code("is_loaded"),
            " prop.",
        ),
        docdemo(code43),
        align_items="start",
    )


code44 = """rx.hstack(
    rx.spinner(color="red", size="xs"),
    rx.spinner(color="orange", size="sm"),
    rx.spinner(color="green", size="md"),
    rx.spinner(color="blue", size="lg"),
    rx.spinner(color="purple", size="xl"),
)"""
code45 = """rx.hstack(
    rx.spinner(color="lightgreen", thickness=1, speed="1s", size="xl"),
    rx.spinner(color="lightgreen", thickness=5, speed="1.5s", size="xl"),
    rx.spinner(
        color="lightgreen",
        thickness=10,
        speed="2s",
        empty_color="red",
        size="xl",
    ),
)
"""


def render_spinner():
    return rx.vstack(
        doctext(
            "Spinners provide a visual cue that an event is either processing, awaiting a course of change or a result."
        ),
        docdemo(code44),
        doctext(
            "Along with the color you can style further with props such as speed, empty color, and thickness."
        ),
        docdemo(code45),
        align_items="start",
    )
