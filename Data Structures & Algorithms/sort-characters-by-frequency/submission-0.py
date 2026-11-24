class Solution:
    def frequencySort(self, s: str) -> str:
        rec = {} # char -> frequency
        for i in range(len(s)):
            if s[i] in rec:
                rec[s[i]] += 1
            else: 
                rec[s[i]] = 1

        res = ""
        sortRec = []

        for key in rec: 
            sortRec.append((rec[key], key))

        sortRec = sorted(sortRec, reverse=True)
        
        for i in range(len(sortRec)):
            res += sortRec[i][1] * sortRec[i][0]

        return res