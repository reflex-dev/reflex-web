from __future__ import annotations
from collections.abc import Callable, Sequence
import dataclasses
from importlib.util import find_spec
from typing import Any, TypedDict


import click
from pcweb.templates.docpage import docpage
import reflex as rx
from pcweb.flexdown import markdown
from reflex.reflex import cli


@dataclasses.dataclass(frozen=True)
class Element:
    def into_text(self) -> str:
        """Convert the element into a text representation."""
        raise NotImplementedError("Subclasses must implement this method.")


@dataclasses.dataclass(frozen=True)
class InlineElement(Element): ...


@dataclasses.dataclass(frozen=True)
class InlineTextCollection(InlineElement):
    elements: tuple[InlineElement, ...]

    def into_text(self) -> str:
        return "".join(element.into_text() for element in self.elements)


@dataclasses.dataclass(frozen=True)
class InlineText(InlineElement):
    text: str

    def into_text(self) -> str:
        import html

        return html.escape(self.text)


@dataclasses.dataclass(frozen=True)
class InlineCode(InlineText):
    def into_text(self) -> str:
        return f"`{super().into_text()}`"


@dataclasses.dataclass(frozen=True)
class Paragraph(Element):
    text: InlineElement

    def into_text(self) -> str:
        return f"{self.text.into_text()}\n\n"


@dataclasses.dataclass(frozen=True)
class Header(Element):
    level: int
    text: InlineElement

    def into_text(self) -> str:
        return f"{'#' * self.level} {self.text.into_text()}\n"


@dataclasses.dataclass(frozen=True)
class List(Element):
    items: tuple[InlineElement, ...]
    ordered: bool = False

    def into_text(self) -> str:
        prefix = "1. " if self.ordered else "* "
        return "\n".join(f"{prefix}{item.into_text()}" for item in self.items) + "\n\n"


@dataclasses.dataclass(frozen=True)
class CodeBlock(Element):
    code: str
    language: str | None = None

    def into_text(self) -> str:
        if self.language:
            return f"```{self.language}\n{self.code}\n```\n\n"
        return f"```\n{self.code}\n```\n\n"


@dataclasses.dataclass(frozen=True)
class Empty(Element):
    def into_text(self) -> str:
        return ""


@dataclasses.dataclass(frozen=True)
class Section(Element):
    sub_elements: tuple[Element, ...]

    def into_text(self) -> str:
        return "\n".join(sub_element.into_text() for sub_element in self.sub_elements)


class ParamTypeInfoDict(TypedDict):
    param_type: str
    name: str


class ChoiceParamTypeInfoDict(ParamTypeInfoDict):
    choices: list[str]
    case_sensitive: bool


class ParamsInfoDict(TypedDict):
    name: str | None
    param_type_name: str
    opts: list[str]
    secondary_opts: list[str]
    type: ParamTypeInfoDict | ChoiceParamTypeInfoDict
    required: bool
    nargs: int
    multiple: bool
    default: Any | Callable[[], Any] | None
    envvar: str | Sequence[str] | None


class OptionInfoDict(ParamsInfoDict):
    help: str | None
    prompt: str | None
    is_flag: bool
    flag_value: Any
    count: bool
    hidden: bool


class CommandInfoDict(TypedDict):
    name: str | None
    params: list[ParamsInfoDict | OptionInfoDict]
    help: str | None
    epilog: str | None
    short_help: str | None
    hidden: bool
    deprecated: bool


class MultiCommandInfoDict(CommandInfoDict):
    commands: dict[str, CommandInfoDict | MultiCommandInfoDict]
    chain: bool


class InfoDict(TypedDict):
    command: CommandInfoDict | MultiCommandInfoDict
    info_name: str | None
    allow_extra_args: bool
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    auto_envvar_prefix: str | None


def sort_subcommands(
    commands: dict[str, CommandInfoDict | MultiCommandInfoDict],
) -> dict[str, CommandInfoDict | MultiCommandInfoDict]:
    """Sort subcommands by name."""
    return dict(
        sorted(commands.items(), key=lambda item: len(item[1].get("commands", {})))
    )


# Dictionary to store the parsed documentation
cli_to_doc = {}


def process(
    command: CommandInfoDict | MultiCommandInfoDict,
    prefix: str | None,
    override_name: str | None,
) -> Element:
    """Convert a Click command to a Markdown element."""
    actual_name = override_name or command["name"]
    full_name = prefix + " " + actual_name if prefix and actual_name else actual_name
    cli_to_doc[full_name] = Section(
        (
            Paragraph(InlineText(command["help"])) if command["help"] else Empty(),
            Section(
                (
                    Header(3, InlineText("Usage")),
                    CodeBlock(
                        "$"
                        + (" " + prefix.strip() if prefix else "")
                        + " "
                        + actual_name.strip()
                        + (
                            " [OPTIONS]"
                            if command["params"]
                            and any(
                                param.get("param_type_name") != "argument"
                                for param in command["params"]
                            )
                            else ""
                        )
                        + (
                            " " + " ".join(arguments)
                            if (
                                arguments := [
                                    param["name"].upper()
                                    for param in command["params"]
                                    if param.get("param_type_name") == "argument"
                                    and param["name"]
                                ]
                            )
                            else ""
                        ),
                        language="console",
                    ),
                )
            )
            if actual_name
            else Empty(),
            Section(
                (
                    Header(3, InlineText("Options")),
                    List(
                        tuple(
                            InlineTextCollection(
                                (
                                    InlineCode(
                                        ", ".join(param["opts"])
                                        + (
                                            " / " + ", ".join(param["secondary_opts"])
                                            if param["secondary_opts"]
                                            else ""
                                        )
                                        + (
                                            (
                                                " " + param["type"]["name"].upper()
                                                if param["type"]["name"] != "boolean"
                                                else ""
                                            )
                                            if (choices := param["type"].get("choices"))
                                            is None
                                            else " [" + "|".join(choices) + "]"
                                        )
                                    ),
                                    InlineText(": " + option_help),
                                )
                            )
                            for param in command["params"]
                            if (option_help := param.get("help")) is not None
                        ),
                        ordered=False,
                    ),
                )
            )
            if command["params"]
            else Empty(),
        )
    ).into_text()
    for name, sub_command in sort_subcommands(command.get("commands", {})).items():
        process(
            sub_command,
            (prefix + " " + actual_name if prefix and actual_name else actual_name),
            name,
        )


def process_command(command: click.Command, name: str) -> str:
    """Convert a Click command to a Markdown text representation."""
    with click.Context(command) as ctx:
        process(ctx.to_info_dict()["command"], None, name)


if find_spec("typer") is not None and find_spec("typer.main") is not None:
    import typer  # pyright: ignore[reportMissingImports]

    if isinstance(cli, typer.Typer):
        cli = typer.main.get_command(cli)

# Iterate over each command configuration
process_command(cli, "reflex")

from reflex_cli.v2.deployments import hosting_cli
from reflex_cli.v2.apps import apps_cli
from reflex_cli.v2.project import project_cli
from reflex_cli.v2.secrets import secrets_cli
from reflex_cli.v2.vmtypes_regions import vm_types_regions_cli
from reflex_cli.v2.cli import login, logout, deploy

process_command(hosting_cli, "reflex cloud")

@click.command()
@click.option(
    "--loglevel",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    default="INFO",
    help="The log level to use.",
)
def login_cmd(loglevel):
    """Authenticate with experimental Reflex hosting service."""
    pass

@click.command()
@click.option(
    "--loglevel", 
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    default="INFO",
    help="The log level to use.",
)
def logout_cmd(loglevel):
    """Log out of access to Reflex hosting service."""
    pass

@click.command()
@click.option("--app-name", help="The name of the app.")
@click.option("--app-id", help="The ID of the app.")
@click.option("--region", help="The region to deploy to. Use `reflex cloud regions` to see available regions.")
@click.option("--env", "envs", multiple=True, help="The environment variables to set: <key>=<value>.")
@click.option("--vmtype", help="The VM type to allocate. Use `reflex cloud vmtypes` to see available VM types.")
@click.option("--hostname", help="The hostname to use for the frontend.")
@click.option("--interactive/--no-interactive", default=True, help="Whether to use interactive mode.")
@click.option("--envfile", help="The path to an env file to use. Will override any envs set manually.")
@click.option("--project", help="The project to deploy to.")
@click.option("--project-name", help="The name of the project.")
@click.option("--token", help="The authentication token.")
@click.option("--config-path", default="cloud.yml", help="The path to the config file.")
@click.option(
    "--loglevel",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]),
    default="INFO",
    help="The log level to use.",
)
def deploy_cmd(**kwargs):
    """Deploy the app to the Reflex hosting service."""
    pass

# Process core commands
process_command(login_cmd, "reflex login")
process_command(logout_cmd, "reflex logout") 
process_command(deploy_cmd, "reflex deploy")



REFLEX_PREFIX = "reflex"
REFLEX_CLOUD_PREFIX = REFLEX_PREFIX + " cloud"


def prefix(
    prefix: str,
    commands: list[str],
) -> list[str]:
    return [prefix + " " + command for command in commands]


# Dictionary to store the categories and their respective commands
categories = {
    "login": prefix(REFLEX_PREFIX, ["login", "logout"]),
    "deploy": prefix(REFLEX_PREFIX, ["deploy"]),
    "apps": prefix(
        REFLEX_CLOUD_PREFIX + " apps",
        [
            "scale",
            "status",
            "start",
            "stop",
            "delete",
            "logs",
            "history",
            "build-logs",
            "list",
        ],
    ),
    "projects": prefix(
        REFLEX_CLOUD_PREFIX + " project",
        [
            "list",
            "create",
            "select",
            "invite",
            "get-select",
            "usage",
            "role-permissions",
            "users",
        ],
    ),
    "secrets": prefix(
        REFLEX_CLOUD_PREFIX + " secrets",
        ["list", "delete", "update"],
    ),
    "vmtypes": prefix(REFLEX_CLOUD_PREFIX, ["vmtypes"]),
    "regions": prefix(REFLEX_CLOUD_PREFIX, ["regions"]),
    "config": prefix(REFLEX_CLOUD_PREFIX, ["config"]),
}

# Dictionary to store the combined documentation for each category
modules: dict[str, str] = {}

# Extract and combine documentation for each category
for category, commands in categories.items():
    docs_list = [
        f"## {command}\n\n{cli_to_doc[command]}"
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
