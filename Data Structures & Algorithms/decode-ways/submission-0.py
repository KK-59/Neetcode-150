class Solution:
    def numDecodings(self, s: str) -> int:
        A = {} # letter -> number
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(alphabet)):
            A[alphabet[i]] = i+1
        
        res = [0] * len(s)

        if int(s[0]) >= 1 and int(s[0]) <= 26:
            res[0] = 1

        for i in range(1,len(res)):
            if int(s[i]) >= 1 and int(s[i]) <= 26 and int(s[i-1] + s[i]) >= 1 and int(s[i-1] + s[i]) <= 26 and int(s[i-1]) != 0:
                if i - 2 >= 0:
                    res[i] = res[i-1] + res[i-2]
                else:
                    res[i] = 2
            elif int(s[i-1] + s[i]) >= 1 and int(s[i-1] + s[i]) <= 26 and int(s[i-1]) != 0:
                if res[i-2] > 0:
                    res[i] = res[i-2]
                else:
                    res[i] = 1
            elif int(s[i]) >= 1 and int(s[i]) <= 26:
                res[i] = res[i-1]
        # print(res)
        return res[-1]


        # 1, 1, 1, 1