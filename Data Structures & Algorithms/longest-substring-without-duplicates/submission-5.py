class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        rec = {} # char -> number of appearances in substring 
        for i in range(len(s)):
            if s[i] not in rec:
                rec[s[i]] = 0
        low = 0
        high = 1
        rec[s[low]] += 1
        rec[s[high]] += 1
        curr = 1
        while high < len(s): 
            # print(low,high)
            # print(rec)
            if rec[s[low]] < 2 and rec[s[high]] < 2: 
                if high - low + 1 > curr:
                    curr = high - low + 1
                high += 1
                if high >= len(s): 
                    rec[s[low]] -= 1
                    low += 1
                else: 
                    rec[s[high]] += 1
                continue
            else:
                rec[s[low]] -= 1
                low += 1
        return curr


