from langchain_core.tools import tool
from typing import List

@tool
def multiplication_tool(numbers: List[float]) -> float:
    """Multiply a list of numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result