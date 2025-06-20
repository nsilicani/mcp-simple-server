"""Server configuration for mcp-simple-server MCP server"""

import os
from dataclasses import dataclass

@dataclass
class ServerConfig:
    """Configuration for the MCP server"""
    name: str = "mcp-simple-server"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


def load_config() -> ServerConfig:
    """Load server configuration from environment or defaults"""
    return ServerConfig(
        name=os.getenv("MCP_SERVER_NAME", "mcp-simple-server"),
        log_level=os.getenv("LOG_LEVEL", "INFO")
    )
