class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high: 
            x = numbers[low] + numbers[high]
            if x == target:
                return [low+1, high+1]
            if x < target: 
                low += 1
            else:
                high -= 1
