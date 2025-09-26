from fastmcp import FastMCP

# 1. Instantiate the server
mcp = FastMCP(name="JupyterToolServer")

# 2. Define a tool (function)
@mcp.tool()
def get_weather_forecast(city: str) -> str:
    """Returns the current weather forecast for the specified city. Use this for weather-related questions."""
    # In a real app, this would call a weather API.
    # For testing, we'll return a simulated result.
    return f"The weather in {city} is currently sunny with a high of 25°C."

# 3. The server entry point, crucial for the subprocess to execute
if __name__ == "__main__":
    # The default run() uses the stdio transport, reading from stdin and writing to stdout
    mcp.run()