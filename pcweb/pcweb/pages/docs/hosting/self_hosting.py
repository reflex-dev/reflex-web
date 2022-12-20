import pynecone as pc

from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
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
def self_hosting():
    from pcweb.pages.docs.getting_started import installation

    return pc.box(
        docheader("Self Hosting", first=True),
        doctext(
            "We recommend using ",
            pc.code("pc deploy"),
            " but you can also host your apps yourself.",
        ),
        doctext(
            "Clone your code to a server and install the ",
            doclink("requirements", href=installation.path),
            ". ",
        ),
        subheader("Edit Config"),
        doctext(
            "Edit your ",
            pc.code("pcconfig.py"),
            " file to match the ip address of your server. With the port ",
            pc.code(":8000"),
            " at the end.",
        ),
        doctext(
            "For example if your server is at 192.168.1.1, your config would look like this: "
        ),
        doccode(
            """config = pc.Config(
    app_name="your_app_name",
    api_url="192.168.1.1:8000",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)
""",
        ),
        doctext("Then run your app in production mode: "),
        doccode("$ pc run --env prod", language="bash"),
        doctext(
            " Production mode creates an optimized build of your app.",
            " Your app will be available on port ",
            pc.code("3000"),
            " by default.",
        ),
    )
