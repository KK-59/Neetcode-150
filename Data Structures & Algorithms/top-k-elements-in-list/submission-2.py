class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {} # number -> frequency
        output = []
        for i in nums:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1
        print(record)
        for j in range(k):
            max = -1001
            index = -1
            for p in record:
                if record[p] > max:
                    max = record[p]
                    print(p)
                    index = p
            record[index] = -1
            print(record)
            output.append(index)
           
        return output

        