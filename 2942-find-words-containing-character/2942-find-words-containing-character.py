class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i in range(len(words)):
            a = i
            for j in range(len(words[i])):
                list_words = list(words[i])
                if x == list_words[j]:
                    output.append(a)
                    break
        return output