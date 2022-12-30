import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, doctext

code36 = """pc.vstack(
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Error Pynecone version is out of date."),
        status="error",
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Warning Pynecone version is out of date."),
        status="warning",
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status="success",
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is 1.0.0."),
        status="info",
    ),
    width="100%",
)
"""
code37 = """pc.vstack(
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        pc.alert_description("No need to update."),
        status="success",
        variant="subtle",
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status="success",
        variant="solid",
    ),
    pc.alert(
        pc.alert_icon(),
        pc.alert_title("Pynecone version is up to date."),
        status="success",
        variant="top-accent",
    ),
    width="100%",
)
"""

# Feedback
def render_alert():
    return pc.vstack(
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


code38 = """pc.hstack(
    pc.circular_progress(value=0),
    pc.circular_progress(value=25),
    pc.circular_progress(pc.circular_progress_label(50), value=50),
    pc.circular_progress(value=75),
    pc.circular_progress(value=100),
    pc.circular_progress(is_indeterminate=True),
)
"""


def render_circularprogress():
    return pc.vstack(
        doctext(
            "The CircularProgress component is used to indicate the progress for determinate and indeterminate processes. Determinate progress: fills the circular track with color, as the indicator moves from 0 to 360 degrees. Indeterminate progress: grows and shrinks the indicator while moving along the circular track."
        ),
        docdemo(code38),
        align_items="start",
    )


code39 = """pc.vstack(
    pc.progress(value=0, width="100%"),
    pc.progress(value=50, width="100%"),
    pc.progress(value=75, width="100%"),
    pc.progress(value=100, width="100%"),
    pc.progress(is_indeterminate=True, width="100%"),
    spacing="1em",
    min_width=["10em", "20em"],
)"""


def render_progress():
    return pc.vstack(
        doctext(
            "Progress is used to display the progress status for a task that takes a long time or consists of several steps."
        ),
        docdemo(code39),
        align_items="start",
    )


code40 = """pc.stack(
    pc.skeleton(height="10px", speed=1.5),
    pc.skeleton(height="15px", speed=1.5),
    pc.skeleton(height="20px", speed=1.5),
    width="50%",
)
"""
code41 = """pc.stack(
    pc.skeleton_circle(size="30px"),
    pc.skeleton_text(no_of_lines=8),
    width="50%",
)
"""
code42 = """pc.stack(
    pc.skeleton_text(
        no_of_lines=5, start_color="pink.500", end_color="orange.500"
    ),
    width="50%",
)
"""
code43 = """pc.vstack(
    pc.skeleton(pc.text("Text is already loaded."), is_loaded=True),
    pc.skeleton(pc.text("Text is already loaded."), is_loaded=False),
)
"""


def render_skeleton():
    return pc.vstack(
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
            pc.code("is_loaded"),
            " prop.",
        ),
        docdemo(code43),
        align_items="start",
    )


code44 = """pc.hstack(
    pc.spinner(color="red", size="xs"),
    pc.spinner(color="orange", size="sm"),
    pc.spinner(color="green", size="md"),
    pc.spinner(color="blue", size="lg"),
    pc.spinner(color="purple", size="xl"),
)"""
code45 = """pc.hstack(
    pc.spinner(color="lightgreen", thickness=1, speed="1s", size="xl"),
    pc.spinner(color="lightgreen", thickness=5, speed="1.5s", size="xl"),
    pc.spinner(
        color="lightgreen",
        thickness=10,
        speed="2s",
        empty_color="red",
        size="xl",
    ),
)
"""


def render_spinner():
    return pc.vstack(
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
