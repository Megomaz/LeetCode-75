class Solution:
    def tribonacci(self, n: int) -> int:
        t1, t2, t3 = 0,1,1

        if n == 0:
            return t1
        elif n == 1:
            return t2

        for i in range(n-2):
            temp = t3
            t3 = t3 + t2 + t1
            t1 = t2
            t2 = temp

        return t3

# Dp solution
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]