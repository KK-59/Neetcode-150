class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 1 * min(heights[0],heights[1])
        print(currMax)

        i = 0 
        j = len(heights) - 1
        while (i < j):
            curr = (j - i) * min(heights[i], heights[j])
            if curr >= currMax:
                currMax = curr
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return currMax
        