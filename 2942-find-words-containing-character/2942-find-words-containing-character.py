class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for (idx, ele) in enumerate(words) if x in ele]