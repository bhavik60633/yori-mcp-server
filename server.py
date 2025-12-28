from mcp.server.fastmcp import FastMCP
from mcp.servers.airbnb import AirbnbServer
from mcp.servers.google_maps import GoogleMapsServer

mcp = FastMCP("Yori MCP Server")

# Airbnb MCP (no API key required)
mcp.add_server(AirbnbServer())

# Google Maps MCP (API key comes from environment)
mcp.add_server(GoogleMapsServer())

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=3333
    )
