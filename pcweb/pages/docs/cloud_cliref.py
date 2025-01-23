import subprocess
import tempfile
import os
import re
from pcweb.templates.docpage import docpage
import reflex as rx

def get_command_help_output(path_to_file: str = None, name_of_cli_program: str = "reflex") -> str:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_file:
        temp_file_path = temp_file.name

    try:
        # Run the command and save the output to the temporary file
        result = subprocess.run(
            [
                "typer", path_to_file, "utils", "docs",
                "--name", name_of_cli_program, "--output", temp_file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the command ran successfully
        if result.returncode != 0:
            print("Error running command:", result.stderr)
            return None

        # Read the content from the temporary file
        with open(temp_file_path, 'r') as file:
            output = file.read()

    finally:
        # Clean up and delete the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    # Return the content of the temporary file
    return output

# Dictionary to store the parsed documentation
docs_dict = {}

def process_command(prefix, path_to_file, dict_prefix=""):
    # Get the help output
    if " " in prefix:
        output = get_command_help_output(
            path_to_file=path_to_file, name_of_cli_program=prefix
        )
    else:
        output = get_command_help_output(path_to_file=path_to_file)

    # Construct the regular expression pattern
    escaped_prefix = re.escape(prefix)
    pattern = rf"## `{escaped_prefix} (.*?)`\n(.*?)(?=\n## `{escaped_prefix}|\Z)"
    
    # Find all matches using the pattern
    matches = re.finditer(pattern, output, re.DOTALL)
    
    # Populate the dictionary with command names and documentation
    for match in matches:
        command_name = match.group(1).strip()
        command_doc = (
            match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
        )
        docs_dict[f"{dict_prefix}{command_name}"] = command_doc


# List of command prefixes and their corresponding file paths
commands_info = [
    ("reflex cloud project", "reflex_cli.v2.project", "project "),
    ("reflex cloud secrets", "reflex_cli.v2.secrets", "secrets "),
    ("reflex cloud apps", "reflex_cli.v2.apps", "apps "),
    ("reflex cloud", "reflex_cli.v2.vmtypes_regions", ""),
    ("reflex", "reflex.reflex", ""),
]

# Iterate over each command configuration
for prefix, path_to_file, dict_prefix in commands_info:
    process_command(prefix, path_to_file, dict_prefix)


# Dictionary to store the categories and their respective commands
categories = {
    "login": ["login", "logout"],
    "deploy": ["deploy"],
    "apps": ["apps scale", "apps status", "apps start", "apps stop", "apps delete", "apps logs", "apps history", "apps build-logs", "apps list"],
    "projects": ["project list", "project create", "project select", "project invite",
                 "project get-select", "project usage", "project role-permissions", "project users"],
    "secrets": ["secrets list", "secrets delete", "secrets update"],
    "vmtypes": ["vmtypes"],
    "regions": ["regions"],
    "config": ["config"]
}

# Dictionary to store the combined documentation for each category
modules = {}

# Extract and combine documentation for each category
for category, commands in categories.items():
    docs_list = [
        f"# {command}\n\n{docs_dict[command]}"
        for command in commands if command in docs_dict
    ]
    modules[category] = "\n\n".join(docs_list)

from pcweb.flexdown import markdown

def generate_docs(source: str):
    return rx.box(
        markdown(text=source),
    )


pages = []
for module_name, module_value in modules.items():
    docs = generate_docs(module_value)
    title = module_name.replace("_", " ").title()
    page_data = docpage(f"/docs/hosting/{module_name}/", title)(docs)
    page_data.title = page_data.title.split('·')[0].strip()
    pages.append(page_data)