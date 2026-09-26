class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            pad = 0
            while i - pad >= 0 and i + pad < len(s):
                if s[i-pad] == s[i+pad]:
                    counter += 1
                    pad += 1
                    continue
                else:
                    break
        for i in range(len(s)): 
            if i+1 == len(s):
                break
            if s[i] == s[i+1]:
                pad = 0
                while i - pad >= 0 and i + pad + 1 < len(s):
                    if s[i-pad] == s[i+1+pad]:
                        counter += 1
                        pad += 1
                        continue
                    else:
                        break
        return counter
