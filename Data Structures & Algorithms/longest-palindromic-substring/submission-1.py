class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 1
        for i in range(len(s)):
            pad = 1
            while i - pad >= 0 and i + pad < len(s):
                if s[i-pad] == s[i+pad]:
                    if 2*pad+1 > right - left:
                        left = i-pad
                        right = i+pad+1
                    pad += 1
                else:
                    break
        left2 = 0
        right2 = 0
        for i in range(0,len(s)):
            if i+1 == len(s):
                break
            if s[i] == s[i+1]:
                pad = 0
                while i - pad >= 0 and i + 1 + pad < len(s):
                    if s[i-pad] == s[i+1+pad]:
                        if i+pad+2 - (i-pad) > right2 - left2:
                            left2 = i-pad
                            right2 = i+pad+2
                        pad += 1
                    else:
                        break
        if len(s[left2:right2]) > len(s[left:right]):
            return s[left2:right2]
        return s[left:right] 
         