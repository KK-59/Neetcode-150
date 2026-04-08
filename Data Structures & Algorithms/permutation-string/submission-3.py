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
        print(record1)
        # print(record2)
        init = record2.copy()
        print(init)

        i = 0
        j = 1
        if s2[i] in record2:
            print("in hereeee")
            record2[s2[i]] += 1
        print(record2)
        while (i < j and j < len(s2)):
            if record2 == record1:
                return True
            print("while start")
            print(s2[i])
            print("j: ",s2[j])
            
            if s2[j] in record2 and record2[s2[j]] < record1[s2[j]]:
                print(s2[j])
                record2[s2[j]] += 1
                j += 1
            elif s2[j] in record2 and record2[s2[j]] >= record1[s2[j]]:
                # advance i until we free up room for s2[j]
                while s2[i] != s2[j]:
                    if s2[i] in record2:  # <-- add this check
                        record2[s2[i]] -= 1
                    i += 1
                i += 1  # skip past the conflicting character itself
                j += 1
            else: 
                record2 = init.copy()
                i += 1
                j = i + 1                             # <-- fix j too (was missing)
                if i < len(s2) and s2[i] in record2:  # <-- add this
                    record2[s2[i]] += 1    
           
            print(record2)
        if record2 == record1:  # <-- add this
            return True
        return False

        