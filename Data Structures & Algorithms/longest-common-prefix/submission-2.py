class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            tempCount = 0
            for j in range(len(strs[i])):
                if j < len(com) and strs[i][j] == com[j]:
                    temp += strs[i][j]
                else:
                    break
            com = temp
            res = tempCount
        return com 


