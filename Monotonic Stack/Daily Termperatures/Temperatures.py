class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index,val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                result[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            
            stack.append((index,val))
        return result