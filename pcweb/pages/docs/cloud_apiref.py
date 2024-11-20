import subprocess
import tempfile
import os
import re
from pcweb.templates.docpage import docpage
import reflex as rx

def get_command_help_output():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_file:
        temp_file_path = temp_file.name

    try:
        # Run the command and save the output to the temporary file
        result = subprocess.run(
            [
                "poetry", "run", "typer", "reflex_cli.v2.deployments", "utils", "docs",
                "--name", "reflex apps", "--output", temp_file_path
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

# Get the help output
help_output = get_command_help_output()

# Dictionary to store the parsed documentation
docs_dict = {}

# Regular expression to capture each section
pattern = r"## `reflex apps (.*?)`\n(.*?)(?=\n## `reflex apps|\Z)"
matches = re.finditer(pattern, help_output, re.DOTALL)

# Iterate over all matches and populate the dictionary
for match in matches:
    command_name = match.group(1).strip()
    command_doc = match.group(2).strip().replace("<", "&lt;").replace(">", "&gt;")
    docs_dict[command_name] = command_doc

# Now you have all the docs in 'docs_dict' with keys being the command names
#print(docs_dict)

apps = ["status", "start", "stop", "scale", "delete", "logs", "history"]
secrets = ["secrets-list", "secrets-delete", "secrets-update"]
projects = ["project-list", "project-create", "project-select", "project-invite", "project-get-select", "project-usage", "project-role-permissions", "project-users"]
vmtypes = ["vmtypes"]
regions = ["regions"]

# Variables to store the extracted documentation
apps_docs = []
secrets_docs = []
projects_docs = []
vmtypes_docs = []
regions_docs = []


# Extract documentation for apps commands
for command in apps:
    if command in docs_dict:
        apps_docs.append(f"# {command}\n\n{docs_dict[command]}")

# Extract documentation for secrets commands
for command in secrets:
    if command in docs_dict:
        secrets_docs.append(f"# {command}\n\n{docs_dict[command]}")

for command in projects:
    if command in docs_dict:
        projects_docs.append(f"# {command}\n\n{docs_dict[command]}")

for command in vmtypes:
    if command in docs_dict:
        vmtypes_docs.append(f"# {command}\n\n{docs_dict[command]}")

for command in regions:
    if command in docs_dict:
        regions_docs.append(f"# {command}\n\n{docs_dict[command]}")

# Combine the extracted documentation into strings
apps_docs = "\n\n".join(apps_docs)
secrets_docs = "\n\n".join(secrets_docs)
projects_docs = "\n\n".join(projects_docs)
vmtypes_docs = "\n\n".join(vmtypes_docs)
regions_docs = "\n\n".join(regions_docs)

modules = {"apps": apps_docs, 
           "secrets": secrets_docs,
           "project": projects_docs,
           "vmtypes": vmtypes_docs,
           "regions": regions_docs
           }


# Now, you have the extracted documentation in separate variables
print("Apps Docs:\n", apps_docs)
print("\nSecrets Docs:\n", secrets_docs)

from pcweb.templates.docpage import h1_comp, h2_comp
from pcweb.flexdown import markdown

def generate_docs(source: str):
    return rx.box(
        markdown(text=source),
    )


pages = []
for module_name, module_value in modules.items():
    #name = module.__name__.lower()
    docs = generate_docs(module_value)
    title = module_name.replace("_", " ").title()
    page_data = docpage(f"/docs/hosting/{module_name}/", title)(docs)
    page_data.title = page_data.title.split('·')[0].strip()
    pages.append(page_data)