class Solution:
    def check(self, s: str, target: str) -> bool:
        for i in range(len(target)):
            if s[i] != target[i]:
                # print("false")
                return False
        # print("true")
        return True
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        W = [0]*(len(s)+1)
        W[0] = 1
        length = 0
        for i in range(len(s)):
            # print("current letter: ", s[i])
            k = 1 + i
            flag = False
            for j in range(len(wordDict)):
                # print("current word: ", wordDict[j])

                if k - len(wordDict[j]) >= 0 and W[k - len(wordDict[j])] == 1:
                    # print(s[(i - len(wordDict[j])):i+1])
                    if self.check(s[(k - len(wordDict[j])):k], wordDict[j]):
                        W[k] = 1
                        # print(W)
                        flag = True
                        length += len(wordDict[j])
                        # print(length)
                if flag == False:
                    W[k] = 0
                else:
                    W[k] = 1
        # print(W)
        return W[-1] == 1