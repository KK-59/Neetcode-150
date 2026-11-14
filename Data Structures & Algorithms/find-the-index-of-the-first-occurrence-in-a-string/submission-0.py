class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 0 
                while j < len(needle) and i + j < len(haystack) and needle[j] == haystack[i + j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1