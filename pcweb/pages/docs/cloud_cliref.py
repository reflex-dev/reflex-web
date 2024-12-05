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

# Get the help output
project_subcommands_output = get_command_help_output(path_to_file="reflex_cli.v2.project", name_of_cli_program="reflex cloud project")
secrets_subcommands_output = get_command_help_output(path_to_file="reflex_cli.v2.secrets", name_of_cli_program="reflex cloud secrets")
apps_subcommands_output = get_command_help_output(path_to_file="reflex_cli.v2.apps", name_of_cli_program="reflex cloud apps")
vmtypes_regions_subcommands_output = get_command_help_output(path_to_file="reflex_cli.v2.vmtypes_regions", name_of_cli_program="reflex cloud")

reflexpy_output = get_command_help_output(path_to_file="reflex.reflex")


# Regular expression to capture each section
pattern_project_subcommands = r"## `reflex cloud project (.*?)`\n(.*?)(?=\n## `reflex cloud project|\Z)"
pattern_secrets_subcommands = r"## `reflex cloud secrets (.*?)`\n(.*?)(?=\n## `reflex cloud secrets|\Z)"
pattern_apps_subcommands = r"## `reflex cloud apps (.*?)`\n(.*?)(?=\n## `reflex cloud apps|\Z)"
pattern_vmtypes_regions_subcommands = r"## `reflex cloud (.*?)`\n(.*?)(?=\n## `reflex cloud|\Z)"
pattern_reflexpy = r"## `reflex (.*?)`\n(.*?)(?=\n## `reflex|\Z)"

matches_project_subcommands = re.finditer(pattern_project_subcommands, project_subcommands_output, re.DOTALL)
matches_secrets_subcommands = re.finditer(pattern_secrets_subcommands, secrets_subcommands_output, re.DOTALL)
matches_apps_subcommands = re.finditer(pattern_apps_subcommands, apps_subcommands_output, re.DOTALL)
matches_vmtypes_regions_subcommands = re.finditer(pattern_vmtypes_regions_subcommands, vmtypes_regions_subcommands_output, re.DOTALL)
matches_reflexpy = re.finditer(pattern_reflexpy, reflexpy_output, re.DOTALL)

# Iterate over all matches and populate the dictionary
for match in matches_project_subcommands:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[f"project {command_name}"] = command_doc

# Iterate over all matches and populate the dictionary
for match in matches_secrets_subcommands:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[f"secrets {command_name}"] = command_doc

# Iterate over all matches and populate the dictionary
for match in matches_apps_subcommands:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[f"apps {command_name}"] = command_doc

for match in matches_vmtypes_regions_subcommands:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[f"{command_name}"] = command_doc

for match in matches_reflexpy:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[command_name] = command_doc


# Dictionary to store the categories and their respective commands
categories = {
    "login": ["login", "logout"],
    "deploy": ["deploy"],
    "apps": ["apps status", "apps start", "apps stop", "apps scale", "apps delete", "apps logs", "apps history"],
    "project": ["project list", "project create", "project select", "project invite",
                 "project get-select", "project usage", "project role-permissions", "project users"],
    "secrets": ["secrets list", "secrets delete", "secrets update"],
    "vmtypes": ["vmtypes"],
    "regions": ["regions"],
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