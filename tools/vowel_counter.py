class VowelCounter:
    def count(self, text: str) -> int:
        vowels = set('aeiouAEIOU')
        return sum(1 for char in text if char in vowels)
