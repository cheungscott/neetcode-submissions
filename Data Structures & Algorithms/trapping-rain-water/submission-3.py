class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        area = 0
        
        while l < r:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[l+1])
                area += maxLeft - height[l+1] 
                l += 1
            else:
                maxRight = max(maxRight, height[r-1])
                area += maxRight - height[r-1]
                r -= 1
        return area      