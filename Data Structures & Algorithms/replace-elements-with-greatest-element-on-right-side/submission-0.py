class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = arr.copy()
        cur = arr[-1]
        res[-1] = -1
        j = len(arr) - 2
        while j >= 0: 
            res[j] = cur
            if arr[j] > cur:
                cur = arr[j]
            j -= 1
        return res

