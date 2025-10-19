# HTTP MCP Server 
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(
    title="Calculator MCP Server (HTTP Based)",
)

@app.post("/multiply")
def multiply(a: float, b: float) -> dict:
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
    return {"result": a * b}

@app.post("/add")
def add(a: float, b: float) -> dict:
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
    return {"result": a + b}

@app.post("/divide")
def divide(a: float, b: float) -> dict:
    """
    Divide two numbers.
    Args:
        a (float): The numerator.
        b (float): The denominator.
    Returns:
        float: The result of dividing a by b.
    Example:
        divide(10, 2)
    Example response:
        5.0
    """
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}

mcp = FastApiMCP(app, name="Calculator MCP")
mcp.mount_http(mount_path="/mcp")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)