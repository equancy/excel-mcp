"""HTTP entry point for Cloud Run deployment."""

import os

from fastmcp.server.auth import StaticTokenVerifier

from .server import mcp

if __name__ == "__main__":
    token = os.environ.get("MCP_BEARER_TOKEN", "")
    if token:
        mcp.auth = StaticTokenVerifier(
            tokens={token: {"client_id": "excel-mcp-client", "scopes": ["read"]}}
        )

    port = int(os.environ.get("PORT", "8000"))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
