class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        i = 0
        j = len(heights) - 1
        maxarea = 0
        while i<j:
            curarea = min(heights[i], heights[j]) * (j-i)
            if curarea > maxarea:
                maxarea = curarea
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxarea