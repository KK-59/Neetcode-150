class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or len(nums) == 0:
            return False
        rec = {}
        for i in range(len(nums)):
            if nums[i] not in rec:
                rec[nums[i]] = 0
        l = 0
        r = 1
        rec[nums[0]] += 1
        rec[nums[1]] += 1
        while l < r and r < len(nums): 
            # print(l,r)
            # print(rec)
            if abs(l-r) > k:
                rec[nums[l]] -= 1
                l += 1
                continue
            if l == r:
                r += 1
                rec[nums[r]] += 1
                continue
            if rec[nums[r]] == 2:
                return True
            r += 1
            if r < len(nums):
                rec[nums[r]] += 1
            
        return False
            
            