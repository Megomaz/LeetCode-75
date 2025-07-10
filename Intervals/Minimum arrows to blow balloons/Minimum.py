class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        stack = []
        count = 0

        for interval in points:
            if stack and stack[-1] >= interval[0]:
                continue
            else:
                stack.append(interval[1])

        return len(stack)

        
        