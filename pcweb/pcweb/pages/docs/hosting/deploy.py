import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """pc.text('hello world', color='blue')"""
code_example2 = """
pc.hstack(
    pc.circular_progress(
        pc.circular_progress_label("50", color="green"),
        value=50,
    ),
    pc.circular_progress(
        pc.circular_progress_label("∞", color="rgb(107,99,246)"),
        is_indeterminate=True,
    ),
)
"""


@docpage()
def deploy():
    return pc.box(
        docheader("Deploy", first=True, coming_soon=True),
        doctext(
            "So far, we've been running our apps locally on our own machines.",
            "But what if we want to share our apps with the world?",
            "This is where deployment comes in.",
        ),
        subheader("PC Deploy"),
        doctext(
            "Pynecone makes it easy to deploy your apps with a single command.",
            "In your terminal, add your ",
            pc.code("PC_TOKEN"),
            " to your environment variables: ",
        ),
        doccode(
            "$ export PC_TOKEN=your_token",
            language="bash",
        ),
        doctext(
            "Then run the deploy command:",
        ),
        doccode(
            "$ pc deploy",
            language="bash",
        ),
        doctext(
            "This will build your app and deploy it to Pynecone's servers.",
            "You will get back a URL at ",
            pc.code("https://myapp.pynecone.app"),
            " that you can share with anyone. "
            "You can log into your Pynecone dashboard to monitor your app.",
        ),
        doctext(
            "This feature is coming soon! ",
        ),
        doctext(
            "In the meantime, you can create a production build and ",
            " deploy with an existing cloud provider ",
            " as we will see in the next section.",
        ),
    )
