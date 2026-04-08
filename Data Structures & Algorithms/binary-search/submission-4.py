class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        prev = 0
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while low < high:
            print(low)
            print(high)
            mid = (low + high) // 2
            print(mid)
            if nums[low] == target:
                return low
            elif nums[high] == target:
                return high
            else:
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    low = mid
                    if low == prev:
                        return -1
                elif target < nums[mid]:
                    high = mid
                    if high == prev:
                        return -1
                prev = mid
        return -1

        # low = 2 high = 5
        # low = 3 high = 5