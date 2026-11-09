class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0]*len(nums1)
        for i in range(len(nums1)): 
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    break
            k = j + 1
            while k < len(nums2) and nums2[k] <= nums2[j]:
                k += 1
            if k >= len(nums2):
                res[i] = -1
            else:
                res[i] = nums2[k]
        return res