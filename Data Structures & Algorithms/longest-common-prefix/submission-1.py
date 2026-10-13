class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            tempCount = 0
            # print(strs[i])
            # print("com: ", com)
            for j in range(len(strs[i])):
                # print(j) 
                # print(temp)
                if j < len(com) and strs[i][j] == com[j]:
                    # print("in here") 
                    temp += strs[i][j]
                else:
                    break
            com = temp
            res = tempCount
        return com 


