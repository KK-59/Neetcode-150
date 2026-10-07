class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        curr = s[0]
        low = 0
        high = 1
        rec = {} # hash map of character -> no. of appearances
        for i in range(len(s)):
            rec[s[i]] = 0
        rec[s[low]] += 1
        rec[s[high]] += 1
        res = 1
        while high < len(s):
            # print(low, high) 
            # print("curr: ", curr)
            # print(rec)
            if (high - low + 1) - rec[curr] <= k:
                if high - low + 1 > res: 
                    # print(s[low:high])
                    res = high - low + 1
                # print("here: ", (high - low + 1) - rec[curr])
                high += 1
                if high < len(s):
                    rec[s[high]] += 1
            else:
                rec[s[low]] -= 1
                low += 1
            # if low == high: 
            #     high += 1
            #     if high < len(s):
            #         rec[s[high]] += 1
            for key in rec: 
                if rec[key] > rec[curr]: 
                    curr = key
            # print("res: ", res)
        return res