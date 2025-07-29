# Reflex MCP Integration

```python exec
import reflex as rx
```

## Overview

The Reflex [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) integration provides AI assistants and coding tools with structured access to Reflex framework documentation and component information. This enables intelligent assistance while developing Reflex applications.

The Reflex MCP server is deployed at `https://mcp.reflex.dev/mcp` and provides access to component documentation and Reflex documentation through standardized MCP tools.

## Installation

To use the Reflex MCP integration, you'll need to configure your AI assistant or coding tool to connect to the Reflex MCP server. No additional Python packages are required on your local machine - the server is hosted and ready to use.

### Prerequisites

- An MCP-compatible AI tool (Claude Desktop, Windsurf, Codex, etc.)
- Internet connection to access the hosted MCP server
- Valid Reflex account for OAuth 2.1 authentication

## Authentication

The Reflex MCP server uses OAuth 2.1 protocol for secure authentication. You'll need a valid Reflex account, and authentication is handled automatically through your MCP client configuration when you provide your Reflex credentials.

## IDE and Coding Assistant Integration

### Claude Desktop

Add the Reflex MCP server to your Claude Desktop configuration by editing your configuration file:

```json
{
  "mcpServers": {
    "reflex": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-proxy"],
      "env": {
        "MCP_PROXY_URL": "https://mcp.reflex.dev/mcp"
      }
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
      "serverType": "http",
      "url": "https://mcp.reflex.dev/mcp"
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
env = { "MCP_PROXY_URL" = "https://mcp.reflex.dev/mcp" }
```

Note: Codex requires MCP servers to communicate over stdio. The `@modelcontextprotocol/server-proxy` adapter bridges the connection to the HTTP-based Reflex MCP server.


## Available Tools

The Reflex MCP server provides tools for accessing component documentation and Reflex documentation through standardized MCP capabilities.

## Enterprise Use

For enterprise customers requiring on-premises deployment of the Reflex MCP server, please [book a demo](https://reflex.dev/pricing/) to discuss your requirements.
