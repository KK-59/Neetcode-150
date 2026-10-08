class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = min(len(word1), len(word2))
        print(x)
        i = 0
        res = ""
        while i < x: 
            res += word1[i]
            res += word2[i]
            i += 1
        if i < len(word1): 
            res += word1[i:]
        elif i < len(word2):
            res += word2[i:]
        return res
