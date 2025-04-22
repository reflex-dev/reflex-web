from functools import lru_cache
import subprocess
import tempfile
import os
import re
from pcweb.templates.docpage import docpage
import reflex as rx
from pcweb.flexdown import markdown


@lru_cache
def get_command_help_output(path_to_file: str, name_of_cli_program: str) -> str:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_file:
        temp_file_path = temp_file.name

    try:
        # Run the command and save the output to the temporary file
        result = subprocess.run(
            [
                "typer",
                path_to_file,
                "utils",
                "docs",
                "--name",
                name_of_cli_program,
                "--output",
                temp_file_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Check if the command ran successfully
        if result.returncode != 0:
            print("Error running command:", result.stderr)
            return None

        # Read the content from the temporary file
        with open(temp_file_path, "r") as file:
            output = file.read()

    finally:
        # Clean up and delete the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    # Return the content of the temporary file
    return output


# Dictionary to store the parsed documentation
cli_to_doc = {}


def process_command(
    prefix: str,
    cli_module: str,
    subcommand: str | tuple[str, ...],
    contains_nested_subcommand: bool,
):
    # Get the help output
    output = get_command_help_output(
        path_to_file=cli_module, name_of_cli_program=prefix
    )

    if output is None:
        raise ValueError(f"Failed to get help output for {prefix}")

    subcommands = subcommand if isinstance(subcommand, tuple) else (subcommand,)

    # Construct the regular expression pattern
    escaped_prefix = re.escape(prefix + (" " + subcommands[0]))
    # This matches against the command name then until the next command (## `) or the end of the string
    pattern = rf"# `{escaped_prefix}`\n(.*?)(?=\n## `|\Z)"

    # Find all matches using the pattern
    matches = re.findall(pattern, output, re.DOTALL)

    if len(matches) > 1:
        raise ValueError(
            f"Multiple matches found for `{escaped_prefix}` in the output. Please check the regex pattern."
        )

    if len(matches) == 0:
        if len(subcommands) > 1:
            return process_command(
                prefix, cli_module, subcommands[1:], contains_nested_subcommand
            )
        print(output)
        raise ValueError(
            f"No matches found for `{escaped_prefix}` in the output. Please check the regex pattern."
        )

    first_match: str = matches[0]

    if not contains_nested_subcommand:
        cli_to_doc[subcommands[0]] = (
            first_match.strip().replace("<", "&lt;").replace(">", "&gt;")
        )
        return

    subcommands_pattern = rf"### `{escaped_prefix} ([a-zA-Z -]*)`\n(.*?)(?=\n### `|\Z)"
    subcommands_matches = re.finditer(subcommands_pattern, first_match, re.DOTALL)

    # Populate the dictionary with command names and documentation
    for match in subcommands_matches:
        nested_subcommand_name = match.group(1).strip()
        command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
        cli_to_doc[subcommands[0] + " " + nested_subcommand_name] = command_doc


# List of command prefixes and their corresponding file paths
commands_info = (
    (
        "reflex cloud",
        "reflex_cli.v2.deployments",
        ("project", "project-cli"),
        True,
    ),
    (
        "reflex cloud",
        "reflex_cli.v2.deployments",
        ("secrets", "secrets-cli"),
        True,
    ),
    ("reflex cloud", "reflex_cli.v2.deployments", ("apps", "apps-cli"), True),
    ("reflex cloud", "reflex_cli.v2.deployments", "vmtypes", False),
    ("reflex cloud", "reflex_cli.v2.deployments", "regions", False),
    ("reflex cloud", "reflex_cli.v2.deployments", "config", False),
    ("reflex", "reflex.reflex", "deploy", False),
    ("reflex", "reflex.reflex", "login", False),
    ("reflex", "reflex.reflex", "logout", False),
)

# Iterate over each command configuration
for (
    prefix,
    path_to_file,
    dict_prefix,
    contains_subcommands,
) in commands_info:
    process_command(prefix, path_to_file, dict_prefix, contains_subcommands)


# Dictionary to store the categories and their respective commands
categories = {
    "login": ["login", "logout"],
    "deploy": ["deploy"],
    "apps": [
        "apps scale",
        "apps status",
        "apps start",
        "apps stop",
        "apps delete",
        "apps logs",
        "apps history",
        "apps build-logs",
        "apps list",
    ],
    "projects": [
        "project list",
        "project create",
        "project select",
        "project invite",
        "project get-select",
        "project usage",
        "project role-permissions",
        "project users",
    ],
    "secrets": ["secrets list", "secrets delete", "secrets update"],
    "vmtypes": ["vmtypes"],
    "regions": ["regions"],
    "config": ["config"],
}

# Dictionary to store the combined documentation for each category
modules = {}

# Extract and combine documentation for each category
for category, commands in categories.items():
    docs_list = [
        f"# {command}\n\n{cli_to_doc[command]}"
        for command in commands
        if command in cli_to_doc
    ]
    modules[category] = "\n\n".join(docs_list)


def generate_docs(source: str):
    return rx.box(
        markdown(text=source),
    )


pages = []
for module_name, module_value in modules.items():
    docs = generate_docs(module_value)
    title = module_name.replace("_", " ").title()
    page_data = docpage(f"/docs/hosting/cli/{module_name}/", title)(docs)
    page_data.title = page_data.title.split("·")[0].strip()
    pages.append(page_data)
