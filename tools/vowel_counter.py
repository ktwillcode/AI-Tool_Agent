from langchain_core.tools import tool

@tool
def vowel_counter(text: str) -> int:
    """Count the number of vowels in the given text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)