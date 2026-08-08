class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # make a hash table with the characters and their counts. update as the sliding window goes on. keep the max character and if it's different change until k = 0
        chars = {} # character -> count
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 0
        chars[s[0]] += 1
        print(chars)
        l = 0 
        r = 1
        maxVal = s[0]
        maxLen = 1
        tempK = k
        while r < len(s):
            chars[s[r]] += 1
            maxVal = max(chars, key=chars.get)
            reps = r - l + 1 - chars[maxVal]
            if reps <= k:
                temp = r - l + 1
                if temp > maxLen:
                    maxLen = temp
            else:
                while reps > k:
                    chars[s[l]] -= 1
                    l += 1
                    maxVal = max(chars, key=chars.get)
                    reps = r - l + 1 - chars[maxVal]
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
                

                


