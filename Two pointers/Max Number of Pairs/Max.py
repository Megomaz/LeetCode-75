class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l, r = 0 ,len(nums) - 1

        while (l < r):
            if nums[l] + nums[r] == k:
                total += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1

        return total