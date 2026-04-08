class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        record1 = {} #s1 character -> frequency
        record2 = {}
        for i in s1:
            if i in record1:
                record1[i] += 1
            else:
                record1[i] = 1
                record2[i] = 0

        # print(record2)
        init = record2.copy()


        i = 0
        j = 1
        if s2[i] in record2:
            record2[s2[i]] += 1

        while (i < j and j < len(s2)):
            if record2 == record1:
                return True

            if s2[j] in record2 and record2[s2[j]] < record1[s2[j]]:
                record2[s2[j]] += 1
                j += 1
            elif s2[j] in record2 and record2[s2[j]] >= record1[s2[j]]:
                
                while s2[i] != s2[j]:
                    if s2[i] in record2:  
                        record2[s2[i]] -= 1
                    i += 1
                i += 1  
                j += 1
            else: 
                record2 = init.copy()
                i += 1
                j = i + 1                            
                if i < len(s2) and s2[i] in record2:  
                    record2[s2[i]] += 1    

        if record2 == record1:
            return True
        return False

        