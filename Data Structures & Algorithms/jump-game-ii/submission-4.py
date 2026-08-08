class Solution:
    def jump(self, nums: List[int]) -> int:
        # out of the possible places to jump to, find the highest number you can jump to and go there 
        if len(nums) == 1:
            return 0
        i = 0
        res = 0
        while i < len(nums):
            l = i + 1
            r = i + nums[i]
            currMax = i
            while l <= r:
                # print("i: ",i)
                # print("l: ",l)
                # print("r: ",r)
                # print("currmax: ",currMax)
                if l == len(nums) - 1:
                    print("in here: ",res)
                    return res + 1
                if l < len(nums) and l + nums[l] >= currMax + nums[currMax]:
                    currMax = l
                l += 1
            i = currMax
            res += 1
            # print("res")
        return res
        
