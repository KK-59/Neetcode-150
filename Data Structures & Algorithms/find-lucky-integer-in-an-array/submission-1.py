class Solution:
    def findLucky(self, arr: List[int]) -> int:
        rec = {} # value : frequency

        for i in range(len(arr)): 
            if arr[i] in rec:
                rec[arr[i]] += 1
            else:
                rec[arr[i]] = 1
        print(rec)
        res = -1
        for key in rec: 
            if rec[key] == key and key > res:
                res = key
        return res