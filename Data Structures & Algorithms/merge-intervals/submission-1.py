class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)
        res = []
        low = intervals[0][0]
        high = intervals[0][1]
        print(high)
        for i in range(1,len(intervals)):
            if high >= intervals[i][0] or intervals[i-1][0] == intervals[i][0]:
                high = max(high, intervals[i][1],intervals[i-1][1])
                continue
            res.append([low,high])
            if i+1 < len(intervals):
                # print("in here")
                low = intervals[i][0]
                high = max(high, intervals[i][1])
            else:
                print("in here then")
                res.append(intervals[-1])
            print(i)
                
        if [low,high] not in res:
            res.append([low,high])
        return res