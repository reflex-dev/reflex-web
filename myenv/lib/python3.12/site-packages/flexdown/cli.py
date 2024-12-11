"""The Flexdown CLI.""" ""
import os

from reflex.reflex import typer
from reflex.utils.processes import new_process

from flexdown import constants


# The command line app.
app = typer.Typer()


@app.command()
def run(path: str):
    # Create a .flexdown directory in the current directory.
    os.makedirs(constants.FLEXDOWN_DIR, exist_ok=True)

    # Create a reflex project.
    new_process(
        ["reflex", "init"], cwd=constants.FLEXDOWN_DIR, show_logs=True, run=True
    )

    # Replace the app file with a template.
    with open(constants.FLEXDOWN_FILE, "w") as f:
        f.write(constants.APP_TEMPLATE.format(path=f"../../{path}"))

    # Run the reflex project.
    new_process(["reflex", "run"], cwd=constants.FLEXDOWN_DIR, show_logs=True, run=True)
