from typing import List

class MultiplicationTool:
    def multiply(self, numbers: List[int]) -> int:
        result = 1
        for num in numbers:
            result *= num
        return result
