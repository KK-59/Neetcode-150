class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        R = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            i2 = i + 1
            for j in range(len(text2)):
                j2 = j + 1
                if text1[i] == text2[j]:
                    R[i2][j2] = R[i2-1][j2-1] + 1
                else:
                    R[i2][j2] = max(R[i2][j2-1],R[i2-1][j2])
        return R[-1][-1]
