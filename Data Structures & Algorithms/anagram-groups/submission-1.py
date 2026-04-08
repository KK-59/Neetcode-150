class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {} # word -> frequency array
        output = []
        for i in range(len(strs)):
            temp = [0] * 26
            if strs[i] in record:
                record[strs[i]][1] += 1
            else:
                for j in range(len(strs[i])):
                    x = ord(strs[i][j]) - ord('a')
                    temp[x] += 1
                record[strs[i]] = [temp, 1]
        print(record)
        
        for i in record:
            check = False
            for k in range(len(output)):
                if i in output[k]:
                    check = True
                    break
            print(check, i)
            if check == False: 
                print(check)
                temp = []
                for j in record:
                    if record[i][0] == record[j][0]:
                        print("this: ",record[j][1])
                        if record[j][1] > 1:
                            for r in range(record[j][1]):
                                temp.append(j)
                                record[j][1] = 0
                                print("temp", temp)
                        elif record[j][1] != 0:
                            temp.append(j)
                output.append(temp)
            
        print("here")
        print(output)
        return output
            

        