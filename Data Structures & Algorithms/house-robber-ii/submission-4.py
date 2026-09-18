class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        R = [0] * (len(nums)-1)
        R[0] = nums[0]
        R[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            R[i] = max(R[i-1], R[i-2] + nums[i])
        
        
        nums = nums[1:]
        K = [0] * (len(nums))
        K[0] = nums[0]
        K[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            K[i] = max(K[i-1], K[i-2] + nums[i])
    
        print(R)
        print(K)
        return max(R[-1], K[-1])
        
        