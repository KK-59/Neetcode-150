class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0
        if s == "":
            return 0
        record = {} # character -> indices where it appears
        for i in range(len(s)):
            if s[i] in record:
                record[s[i]].append(i)
            else:
                record[s[i]] = [i]
        print(record) # s="abcabcbb"
        currMax = 1
        i = 0
        j = 1
        while i < j and j < len(s):
            #print(s[i:j])
            state = False 
            x = record[s[j]]
            # print("j: ",j)
            # print(s[j])
            # print("x: ",x)
            for r in range(len(x)):
                if x[r] < j and x[r] >= i:
                    # print("in here")
                    # print(x[r])
                    # print("j-i: ", j - i + 1)
                    state = True
                    break
            if state == True:
                i += 1
            else:
                if j - i + 1 > currMax:
                    # print("in here? ")
                    currMax = j - i + 1
                    # print(currMax)
                if j != len(s)-1:
                    j += 1
                else:
                    i += 1
            if i == j:
                j += 1
        return currMax      
