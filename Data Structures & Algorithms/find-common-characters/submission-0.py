class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        rec = {} # main hash map. character : frequency

        for i in range(len(words[0])):
            if words[0][i] in rec:
                rec[words[0][i]] += 1
            else:
                rec[words[0][i]] = 1

        for i in range(1, len(words)):
            temp = {} # character : frequency
            temp2 = {}
            for j in range(len(words[i])):
                if words[i][j] in temp:
                    temp[words[i][j]] += 1
                else:
                    temp[words[i][j]] = 1
            for key in temp:
                if key in rec:
                    temp2[key] = min(temp[key], rec[key])
                else:
                    continue 
            rec = temp2
        res = []
        for key in rec:
            for i in range(rec[key]):
                res.append(key)
        return res

