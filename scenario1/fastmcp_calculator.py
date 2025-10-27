from fastmcp import FastMCP

mcp= FastMCP(name = 'calculator_example')

@mcp.tool( name="multiply",
    description="Multiplies two numbers.",
    tags=("arithmetic", "multiplication"))
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool(
    name="add",
    description="Adds two numbers.",
    tags=("arithmetic", "addition")
)
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b

@mcp.tool(
    name="minus",
    description="Minus two numbers.",
    tags=("arithmetic", "subtraction")
)
def minus(a: float, b: float) -> float:
    """Minus two numbers."""
    return a - b


@mcp.tool(
    name="divide",
    description="Divides two numbers.",
    tags=("arithmetic", "division")
)
def divide(a: float, b: float) -> float:
    """Divides two numbers."""
    return a / b


if __name__ == "__main__":
    mcp.run()