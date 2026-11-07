class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rec = {} # letter -> frequency
        for i in range(len(magazine)):
            if magazine[i] in rec:
                rec[magazine[i]] += 1
            else:
                rec[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in rec and rec[ransomNote[i]] > 0:
                rec[ransomNote[i]] -= 1
            else:
                return False
        return True