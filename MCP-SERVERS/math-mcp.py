from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Maths MCP",
    description="MCP Server for mathematical operations",
)

@mcp.tool(name="add", description="Add two numbers")
async def add(a: float, b: float) -> float:
    """
    Add two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of the two numbers.
    Example:
        add(5, 3)
    Example response:
        8.0
    """
    return a + b

@mcp.tool(name="subtract", description="Subtract two numbers")
async def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The result of subtracting b from a.
    Example:
        subtract(5, 3)
    Example response:
        2.0
    """
    return a - b

@mcp.tool(name="multiply", description="Multiply two numbers")
async def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The product of the two numbers.
    Example:
        multiply(5, 3)
    Example response:
        15.0
    """
    return a * b

@mcp.tool(name="divide", description="Divide two numbers")
async def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    Args:
        a (float): The numerator.
        b (float): The denominator.
    Returns:
        float: The result of dividing a by b.
    Example:
        divide(6, 3)
    Example response:
        2.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool(name="power", description="Raise a number to the power of another")
async def power(base: float, exponent: float) -> float:
    """
    Raise a number to the power of another.
    Args:
        base (float): The base number.
        exponent (float): The exponent.
    Returns:
        float: The result of base raised to the power of exponent.
    Example:
        power(2, 3)
    Example response:
        8.0
    """
    return base ** exponent

@mcp.tool(name="sqrt", description="Calculate the square root of a number")
async def sqrt(number: float) -> float:
    """
    Calculate the square root of a number.
    Args:
        number (float): The number to calculate the square root of.
    Returns:
        float: The square root of the number.
    Example:
        sqrt(16)
    Example response:
        4.0
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5

@mcp.tool(name="factorial", description="Calculate the factorial of a number")
async def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    Args:
        n (int): The number to calculate the factorial of.
    Returns:
        int: The factorial of the number.
    Example:
        factorial(5)
    Example response:
        120
    """
    if n < 0:
        raise ValueError("Cannot calculate the factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool(name="modulus", description="Calculate the modulus of two numbers")
async def modulus(a: float, b: float) -> float:
    """
    Calculate the modulus of two numbers.
    Args:
        a (float): The dividend.
        b (float): The divisor.
    Returns:
        float: The remainder of the division of a by b.
    Example:
        modulus(5, 3)
    Example response:
        2.0
    """
    if b == 0:
        raise ValueError("Cannot calculate modulus with a divisor of zero.")
    return a % b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    """
    Run the MCP server.
    This will start the server and make the tools available for use.
    """