# mcp-simple-server

**MCP Server**

## Overview

A simple project to get familiar with MCP

## Features

TODO

## Installation

### From PyPI (if published)

There are two main ways to use the server if it's published on PyPI:

**Option 1: Install and then Run (Recommended for regular use)**

First, install the package into your Python environment using UV:
```bash
# Install using UV
uv pip install mcp_simple_server

# If you don't have UV, you can use pip:
# pip install mcp_simple_server
```

Once installed, you can run the server from your terminal:
```bash
mcp_simple_server-server
```

**Option 2: Run Directly with `uvx` (For quick use without permanent installation)**

If you want to run the server without installing it into your current environment (or to run a specific version easily), you can use `uvx`. This is handy for one-off tasks or testing.

```bash
# Run the latest version of the server directly from PyPI
uvx mcp_simple_server mcp_simple_server-server

# You can also specify a version:
# uvx mcp_simple_server==1.2.3 mcp_simple_server-server
```
This command tells `uvx` to fetch the `mcp_simple_server` package and execute its `mcp_simple_server-server` command.

### From Source

```bash
# Clone the repository
git clone <your-repository-url>
cd mcp_simple_server

# Create and activate a virtual environment using UV
uv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode using UV
uv pip install -e .
```

## Available Tools

### tool_name

TODO

Example:
```bash
# Using stdio transport (default)
mcp_simple_server-client "your command here"

# Using SSE transport
mcp_simple_server-server --transport sse
curl http://localhost:3001/sse
```

## Usage

This MCP server provides two entry points:

1. `mcp_simple_server-server`: The MCP server that handles tool requests
   ```bash
   # Run with stdio transport (default)
   mcp_simple_server-server

   # Run with SSE transport
   mcp_simple_server-server --transport sse
   ```
   When running with SSE transport, you can ping server also with curl. Please see [this script](mcp_simple_server\scripts\send_requests.py).

## Logging

The server logs all activity to both stderr and a rotating log file. Log files are stored in OS-specific locations:

- **macOS**: `~/Library/Logs/mcp-servers/mcp_simple_server.log`
- **Linux**: 
  - Root user: `/var/log/mcp-servers/mcp_simple_server.log`
  - Non-root: `~/.local/state/mcp-servers/logs/mcp_simple_server.log`
- **Windows**: `%USERPROFILE%\AppData\Local\mcp-servers\logs\mcp_simple_server.log`

Log files are automatically rotated when they reach 10MB, with up to 5 backup files kept.

You can configure the log level using the `LOG_LEVEL` environment variable:
```bash
# Set log level to DEBUG for more detailed logging
LOG_LEVEL=DEBUG mcp_simple_server-server
```

Valid log levels are: DEBUG, INFO (default), WARNING, ERROR, CRITICAL

2. `mcp_simple_server-client`: A convenience client for testing
   ```bash
   mcp_simple_server-client "your command here"
   ```

## Requirements

- Python 3.11 or later (< 3.13)
- Operating Systems: Linux, macOS, Windows

## Configuration

TODO

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed development instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- Niccolò Silicani

---
