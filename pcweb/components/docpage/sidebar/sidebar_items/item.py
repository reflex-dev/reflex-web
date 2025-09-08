from pcweb.route import Route
from ..state import SideBarItem


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title
        url = route.path
        if name.endswith("Overview"):
            # For "Overview", we want to keep the qualifier prefix ("Components overview")
            alt_name_for_next_prev = name
        else:
            alt_name_for_next_prev = ""
        name = (
            name.replace("Api", "API")
            .replace("Cli", "CLI")
            .replace("Ai", "AI")
            .replace("Ide", "IDE")
            .replace("Mcp", "MCP")

        )
        return SideBarItem(
            names=name, alt_name_for_next_prev=alt_name_for_next_prev, link=url
        )
    return SideBarItem(
        names=route,
        children=list(map(create_item, children)),
    )
