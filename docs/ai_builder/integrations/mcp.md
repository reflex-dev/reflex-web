# Reflex MCP Integration

```python exec
import reflex as rx
```

The Reflex Model Context Protocol (MCP) integration provides AI assistants and coding tools with structured access to Reflex framework documentation and component information. This enables intelligent assistance while developing Reflex applications.

## What is Model Context Protocol (MCP)?

Model Context Protocol (MCP) is a standardized way for AI tools to access external data sources and services. The Reflex MCP server provides real-time access to:

- **Component Documentation**: Complete documentation for all Reflex components with source code
- **Documentation Sections**: Hierarchical access to all Reflex documentation
- **Resource Discovery**: Browse available components and documentation as MCP resources
- **Tool-based Access**: Retrieve specific documentation through standardized MCP tools

The Reflex MCP server is deployed at `https://reflex-mcp-server.fly.dev` and provides both SSE (Server-Sent Events) and HTTP transport options for maximum compatibility with different AI tools.

## Installation

To use the Reflex MCP integration, you'll need to configure your AI assistant or coding tool to connect to the Reflex MCP server. No additional Python packages are required on your local machine - the server is hosted and ready to use.

### Prerequisites

- An MCP-compatible AI tool (Claude Desktop, Windsurf, Codex, etc.)
- Internet connection to access the hosted MCP server

## Authentication

```python eval
rx.box(height="1rem")
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header="Authentication Details",
        content=rx.box(
            rx.text("The Reflex MCP server is currently in ", rx.el.span("alpha", font_weight="bold"), " and is completely free to use during this period."),
            rx.box(height="0.5rem"),
            rx.text("• ", rx.el.span("No API keys required", font_weight="bold")),
            rx.text("• ", rx.el.span("No registration needed", font_weight="bold")),
            rx.text("• ", rx.el.span("No usage limits", font_weight="bold")),
            rx.box(height="0.5rem"),
            rx.text("Future versions will integrate with Reflex Pro+ subscription plans, but a free tier will remain available with reasonable usage limits."),
        ),
    ),
    variant="surface",
)
```

```python eval
rx.box(height="1rem")
```

## IDE and Coding Assistant Integration

### Claude Desktop

Add the Reflex MCP server to your Claude Desktop configuration:

```bash
claude mcp add --transport sse reflex https://reflex-mcp-server.fly.dev/sse
```

Alternatively, you can manually edit your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "reflex": {
      "command": "python",
      "args": ["-m", "reflex_mcp.reflex_mcp_server"],
      "cwd": "/path/to/reflex-mcp"
    }
  }
}
```

### Windsurf/Cascade

Create a `.vscode/mcp.json` file in your project root:

```json
{
  "mcpServers": {
    "reflex": {
      "serverType": "sse",
      "url": "https://reflex-mcp-server.fly.dev/sse"
    }
  }
}
```

### Codex

Add this configuration to your `~/.codex/config.toml` file:

```toml
[mcp_servers.reflex]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-proxy"]
env = { "MCP_PROXY_URL" = "https://reflex-mcp-server.fly.dev/sse" }
```

Note: Codex requires MCP servers to communicate over stdio. Since the Reflex server uses SSE, you'll need the `@modelcontextprotocol/server-proxy` adapter to bridge the connection.

### Other MCP Clients

For other MCP-compatible tools, use these endpoints:

```python eval
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Transport"),
            rx.table.column_header_cell("URL"),
            rx.table.column_header_cell("Use Case"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell(rx.code("SSE")),
            rx.table.cell(rx.code("https://reflex-mcp-server.fly.dev/sse")),
            rx.table.cell("Real-time communication, preferred for most clients"),
        ),
        rx.table.row(
            rx.table.row_header_cell(rx.code("HTTP")),
            rx.table.cell(rx.code("https://reflex-mcp-server.fly.dev/mcp")),
            rx.table.cell("Traditional REST API access"),
        ),
    ),
    width="100%",
)
```

## Available Tools

The Reflex MCP server provides several tools for accessing documentation and component information:

### Component Documentation

**`get_component_doc`** - Retrieve comprehensive documentation for any Reflex component, including markdown documentation, Python source code, and related component sources.

Example usage: "Show me the Button component documentation"

**`list_components`** - Browse all available Reflex components organized by category.

Example usage: "What form components are available in Reflex?"

### Documentation Access

**`list_doc_sections`** - Explore the complete Reflex documentation structure hierarchically.

Example usage: "What documentation sections are available?"

**`get_doc`** - Read any specific documentation file from the Reflex documentation.

Example usage: "Show me the getting started guide"

## Best Practices

### Effective Usage

1. **Be Specific**: When asking for component documentation, specify the exact component name for best results.

2. **Explore Categories**: Use `list_components` to discover components by category before diving into specific documentation.

3. **Leverage Context**: The MCP server provides rich context including source code, which helps AI assistants give more accurate advice.

4. **Documentation Structure**: Use `list_doc_sections` to understand the full scope of available documentation before asking specific questions.

### Optimization Tips

- **Component Discovery**: Start with category-based searches to find the right components for your use case
- **Source Code Access**: The server provides both documentation and source code, enabling deeper understanding of component behavior
- **Related Components**: Component documentation includes information about related components through YAML frontmatter parsing

## Troubleshooting

### Connection Issues

**Problem**: AI assistant cannot connect to the MCP server

**Solutions**:
- Verify your internet connection
- Check that the server is running by visiting `https://reflex-mcp-server.fly.dev`
- Ensure your MCP client configuration uses the correct URL format
- For SSE connections, make sure your client supports Server-Sent Events

### Configuration Problems

**Problem**: MCP server not appearing in your AI tool

**Solutions**:
- Double-check the configuration file syntax (JSON/TOML formatting)
- Restart your AI assistant after adding the configuration
- Verify the configuration file is in the correct location for your tool
- Check your AI tool's documentation for MCP setup requirements

### Limited Functionality

**Problem**: Some tools or documentation not accessible

**Solutions**:
- The server is in alpha - some features may be temporarily unavailable
- Check the server status at `https://reflex-mcp-server.fly.dev`
- Try alternative transport methods (SSE vs HTTP) if one isn't working
- Report issues to the Reflex team for investigation

### Performance Issues

**Problem**: Slow responses from the MCP server

**Solutions**:
- The server is hosted and may experience occasional latency
- Large documentation requests may take longer to process
- Consider breaking complex queries into smaller, specific requests
- Check your network connection stability

## Server Status

You can check if the Reflex MCP server is running by visiting: `https://reflex-mcp-server.fly.dev`

The status page will show server information and the count of available tools.

```python eval
rx.box(height="1rem")
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header="Alpha Service Notice",
        content=rx.box(
            rx.text("⚠️ ", rx.el.span("ALPHA VERSION", font_weight="bold"), ": This MCP server is currently in alpha and under active development."),
            rx.box(height="0.5rem"),
            rx.text("• Features may change without notice"),
            rx.text("• Occasional downtime for updates and improvements"),
            rx.text("• Your feedback helps improve the service"),
            rx.box(height="0.5rem"),
            rx.text("We appreciate your patience as we continue to enhance the Reflex MCP integration."),
        ),
    ),
    variant="surface",
)
```
