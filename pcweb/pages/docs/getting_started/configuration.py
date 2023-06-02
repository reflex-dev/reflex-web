import pynecone as pc

from pcweb import constants
from pcweb.templates.docpage import (
    doccode,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)


@docpage()
def configuration():
    return pc.box(
        docheader("Configuration"),
        doctext("There are 3 ways to configure your pynecone application."),
        doctext(""),
        subheader("PCConfig Arguments"),
        doctext(
            "The first place to configure your pynecone application is ",
            "by setting the different options in the",
            pc.code("pcconfig.py"),
            " file.",
        ),
        doctext(
            "Refer to Config API Reference for the details of all options availables."
        ),
        subheader("Environment Arguments"),
        doctext(
            "You can also set option in a .env file in the root directory of your project.",
        ),
        doctext(
            "Any environment options will prevail over the one defined in ",
            pc.code("pcconfig.py"),
        ),
        subheader("Command line Arguments"),
        doctext(
            "Those are the arguments that you pass when using ", pc.code("pc run"), "."
        ),
        doctext(
            "Any command line options will prevail over the one defined in ",
            pc.code("pcconfig.py"),
        ),
    )
