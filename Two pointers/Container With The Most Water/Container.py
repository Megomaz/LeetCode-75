class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1

        area = 0

        while l < r:
            minA = height[l] if height[l] < height[r] else height[r]
            area = max(area, (r - l ) * minA)
            if minA == height[l]:
                l += 1
            else:
                r -= 1

        return area