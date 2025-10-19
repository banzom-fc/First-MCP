from fastmcp import FastMCP

mcp = FastMCP(
    name="Fast MCP Calculator",
    instructions="A calculator that can perform basic arithmetic operations quickly.",
)

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The product of the two numbers.
    Example:
        multiply(4, 5)
    Example response:
        20.0
    """
    return a * b

@mcp.tool(
    name="add",
    description="Add two numbers",
    tags=["arithmetic", "addition", "math"],
)
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of the two numbers.
    Example:
        add(4, 5)
    Example response:
        9.0
    """
    return a + b


if __name__ == "__main__":
    # mcp.run() # STDIO by default
    
    # OR
    
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8006) # HTTP server